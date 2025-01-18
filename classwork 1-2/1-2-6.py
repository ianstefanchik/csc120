import statistics

list_of_numbers = [1.0,5.0,8.0,20.0,30.0,50.0]
#a
average = statistics.mean(list_of_numbers)

print(average)
#b
med = statistics.median(list_of_numbers)

print(med)
#c
std_deviation = statistics.stdev(list_of_numbers)

print(round(std_deviation))