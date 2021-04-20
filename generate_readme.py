#!/usr/bin/env python3


import pathlib
import json
from pprint import pprint as pp


title = 'Eris\' Cogs'
desc = 'Welcome to my cogs!'

readme = f"# {title}\n{desc}\n\nIf you're on windows, " \
         f"you'll need to delete the symlinked `eris_event_lib.py` " \
         f"files in the directories of the cogs you wish to install " \
         f"and replace it with a copy of the root-level file.\n"

meta_keys = [
    'short',
    'description',
    'author',
]

all_dirs = [
    d for d in
    pathlib.Path().glob('*')
    if not d.name.startswith('.')
    and d.is_dir()
]
all_dirs = sorted(all_dirs)

for d in all_dirs:
    name = d.name
    meta = json.loads((d / 'info.json').read_text())
    new_entry = f"## {name.capitalize()}\n"

    meta_entries = []
    for k in meta_keys:
        val = meta.get(k)
        if k == 'author':
            val = ', '.join(val)
        if val:
            val = val.replace('\n', '\n\n')
        meta_entries.append(f'{k.capitalize()}: {val}')
    new_entry += '\n\n'.join(meta_entries)

    readme += new_entry
    readme += '\n'

readmefile = pathlib.Path() / 'README.md'
readmefile.write_text(readme)

