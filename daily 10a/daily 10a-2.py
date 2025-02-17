from pathlib import Path

path = Path('names.txt')

all_names = path.read_text()

names = all_names.splitlines()

three_or_four_letter_names = [name for name in names if len(name) == 3 or len(name) == 4]

name_start_with_rea = [name for name in names if name[:3] == 'Rea']

name_contains_rea = [name for name in names if 'rea' in name.lower()]
