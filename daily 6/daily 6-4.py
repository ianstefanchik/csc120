from pathlib import Path

path = Path('demographics.txt')

families = []

lines = path.read_text().splitlines()

for line in lines[1:]: 
    parts = line.split(',')

    last_name = parts[0]
    hometown = parts[1]
    salary = int(parts[2])
    family_names = parts[3:]

    family = {
        "last_name": last_name,
        "hometown": hometown,
        "salary": salary,
        "first_names": family_names,
    }

    families.append(family)

for family in families:
    print(family)