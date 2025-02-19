from pathlib import Path

file_path = Path("access_log.txt")
updated_file_path = Path("access_log_updated.txt")

lines = file_path.read_text().splitlines()

user_input = input("Enter your username: ")

user_in_list = False

updated_list = []

for line in lines:
    parts = line.split(';')
    if parts[0] == user_input:
        updated_total = int(parts[1]) + 1
        updated_list.append(f"{parts[0]};{int(updated_total)}")
        user_in_list = True
    else:
        updated_list.append(line)

if not user_in_list:
    updated_list.append(f"{user_input};{int(1)}")

updated_file_path.write_text("\n".join(updated_list))