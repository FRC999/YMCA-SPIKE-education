/* Shared parsing logic: only checkbox marks may change in the source file. */
(function (root) {
  'use strict';
  function parse(text) {
    const tasks = []; let heading = 'Preparation'; let offset = 0;
    for (const line of text.split(/(?<=\n)/)) {
      const h = line.match(/^#{1,6}\s+(.+?)\r?\n?$/);
      if (h) heading = h[1];
      const m = line.match(/^([ \t]*- \[)([ xX])(\][ \t]+)([^\r\n]*)/);
      if (m) tasks.push({offset: offset + m[1].length, checked: m[2].toLowerCase() === 'x', label: m[4], heading});
      offset += line.length;
    }
    return tasks;
  }
  function update(text, offset, checked) {
    if (!parse(text).some(t => t.offset === offset)) throw new Error('The checkbox no longer matches the loaded file. Reopen it.');
    return text.slice(0, offset) + (checked ? 'x' : ' ') + text.slice(offset + 1);
  }
  const api = {parse, update};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.PrepChecklist = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
