from pathlib import Path

path = Path('words.txt')

contents = path.read_text()

words = contents.splitlines()

for word in words:
    if len(word) > 7:
        print(f"{word} has more than 7 letters")
    else:
        print(f"{word} has 7 or fewer letters.")
        