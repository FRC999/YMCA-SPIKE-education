#!/usr/bin/env python3
"""Detect drift in reviewed exports. This does not regenerate or certify content."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'scripts/reading_copies.json'
TEXT_SUFFIXES = {'.md', '.html', '.py', '.json'}


def digest(path: Path) -> str:
    data = path.read_bytes()
    if path.suffix.lower() in TEXT_SUFFIXES:
        data = data.replace(b'\r\n', b'\n')
    return hashlib.sha256(data).hexdigest()


def local_path(root: Path, name: str) -> Path:
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f'Path outside repository: {name}')
    return path


def check(root: Path, entries: list[dict]) -> list[str]:
    errors = []
    seen = set()
    for entry in entries:
        output = entry['output']
        if output in seen:
            errors.append(f'Duplicate output: {output}')
        seen.add(output)
        files = {output: entry['sha256'], **entry['sources']}
        if not entry['sources']:
            errors.append(f'No editorial source: {output}')
        for name, expected in files.items():
            path = local_path(root, name)
            if not path.is_file():
                errors.append(f'Missing {name} (export: {output})')
            elif digest(path) != expected:
                errors.append(f'Changed {name} (review/re-export: {output})')
    return errors


def record(root: Path, entries: list[dict], selected: list[str]) -> None:
    known = {e['output'] for e in entries}
    unknown = set(selected) - known
    if unknown:
        raise ValueError('Unknown output(s): ' + ', '.join(sorted(unknown)))
    for entry in entries:
        if entry['output'] in selected:
            entry['sha256'] = digest(local_path(root, entry['output']))
            entry['sources'] = {name: digest(local_path(root, name)) for name in entry['sources']}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true', help='Read-only drift check (default)')
    mode.add_argument('--record', nargs='+', metavar='OUTPUT', help='Record named outputs ONLY after regeneration and visual/content review')
    args = parser.parse_args()
    try:
        path = ROOT / MANIFEST
        manifest = json.loads(path.read_text(encoding='utf-8'))
        if manifest['version'] != 1:
            raise ValueError('Unsupported manifest version')
        entries = manifest['copies']
        if args.record:
            record(ROOT, entries, args.record)
            path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
            print(f'Recorded {len(args.record)} reviewed output(s). No files were regenerated.')
        errors = check(ROOT, entries)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'Reading-copy check failed: {exc}', file=sys.stderr)
        return 1
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'All {len(entries)} reviewed reading copies match their recorded sources and outputs.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
