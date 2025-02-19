from pathlib import Path
import random

integers = []

for integer in range(10000):
    random_ints = str(random.randint(1000, 50000))
    integers.append(random_ints)

single_string = "\n".join(integers)

path = Path("integer_log.txt")

path.write_text(single_string)