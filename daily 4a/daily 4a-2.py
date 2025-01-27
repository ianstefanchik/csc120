squares = []
sum_of_squares = 0

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

    sum_of_squares += square
    

print(squares)
print(sum_of_squares)