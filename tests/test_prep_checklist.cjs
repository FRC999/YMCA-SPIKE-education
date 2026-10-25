'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const {parse,update}=require('../scripts/prep_checklist.js');
test('preserves headings, duplicate labels, Unicode, BOM and CRLF',()=>{
  const input='\uFEFF# Prep\r\n## Motors\r\n- [ ] Check café 🤖\r\nKeep these notes.\r\n## Sensors\r\n- [X] Check café 🤖\r\n';
  const tasks=parse(input);assert.equal(tasks.length,2);assert.equal(tasks[0].heading,'Motors');assert.equal(tasks[1].heading,'Sensors');assert.equal(tasks[1].checked,true);
  const changed=update(input,tasks[0].offset,true);
  assert.equal(changed,input.replace('- [ ]','- [x]'));
  assert.equal(update(changed,tasks[0].offset,false),input);
});
test('toggling each actual prep task changes exactly one character',()=>{
  const input=fs.readFileSync(path.join(__dirname,'../SESSION_PREP.md'),'utf8');
  const tasks=parse(input);assert.ok(tasks.length>30);
  for(const task of tasks){
    const output=update(input,task.offset,!task.checked);
    assert.equal(output.length,input.length);
    assert.equal(output.slice(0,task.offset),input.slice(0,task.offset));
    assert.equal(output.slice(task.offset+1),input.slice(task.offset+1));
    assert.equal(parse(output).find(t=>t.offset===task.offset).checked,!task.checked);
  }
});
test('rejects stale offsets and leaves non-checkbox text alone',()=>{
  const input='# Prep\n- [ ] Test\nNot a checkbox [ ]\n';
  assert.throws(()=>update(input,1,true));assert.equal(parse(input).length,1);
  assert.equal(parse('No tasks here').length,0);
});
test('browser scripts have valid JavaScript syntax',()=>{
  const html=fs.readFileSync(path.join(__dirname,'../SESSION_PREP_CHECKLIST.html'),'utf8');
  for(const script of html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g))new vm.Script(script[1]);
});
async function pageHarness(){
  // Unit-test the save handlers with an in-memory file and minimal DOM objects.
  // This does not substitute for a real browser permission/picker check.
  const nodes=[];
  const node=()=>{const n={events:{},children:[],addEventListener(k,f){this.events[k]=f;},append(...xs){this.children.push(...xs);},replaceChildren(){this.children=[];}};nodes.push(n);return n;};
  const ids=Object.fromEntries(['open','save','download','upload','file','status','progress','tasks','context','source'].map(id=>[id,node()]));
  const state={disk:'# Prep\n## Kits\n- [ ] Test motor\nKeep this note.\n',writes:0};
  const handle={async getFile(){const bytes=new TextEncoder().encode(state.disk);return {name:'SESSION_PREP.md',async arrayBuffer(){return bytes.buffer;}};},async createWritable(){let pending;return {async write(text){pending=text;},async close(){state.disk=pending;state.writes++;}};}};
  const picker=async()=>[handle];
  const ctx={document:{getElementById:id=>ids[id],createElement:()=>node(),querySelectorAll:()=>nodes.filter(n=>n.type==='checkbox')},window:{showOpenFilePicker:picker,addEventListener(){}},showOpenFilePicker:picker,TextDecoder,PrepChecklist:{parse,update},confirm:()=>true};
  vm.createContext(ctx);
  const html=fs.readFileSync(path.join(__dirname,'../SESSION_PREP_CHECKLIST.html'),'utf8');
  for(const script of html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g))vm.runInContext(script[1],ctx);
  await ids.open.events.click();const box=nodes.find(n=>n.type==='checkbox');box.checked=true;box.events.change();
  return {state,ids};
}
test('save writes only the checked marker and clears unsaved state',async()=>{
  const {state,ids}=await pageHarness();assert.equal(ids.save.disabled,false);
  await ids.save.events.click();assert.equal(state.disk,'# Prep\n## Kits\n- [x] Test motor\nKeep this note.\n');assert.equal(state.writes,1);assert.equal(ids.save.disabled,true);assert.match(ids.status.textContent,/Saved to SESSION_PREP/);
});
test('save refuses an outside edit without overwriting it',async()=>{
  const {state,ids}=await pageHarness();state.disk+='A newer observation.\n';const external=state.disk;
  await ids.save.events.click();assert.equal(state.disk,external);assert.equal(state.writes,0);assert.match(ids.status.textContent,/changed outside/);
});
