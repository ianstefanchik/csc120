from pathlib import Path

file_path = Path("integer_log.txt")
new_file_path = Path("integers_sorted.txt")

lines = file_path.read_text().splitlines()

integers = [int(line) for line in lines]

sorted_integers = sorted(integers)

new_file_path.write_text("\n".join(str(number) for number in sorted_integers))
