import statistics

#1

numbers = [9910, 5323, 6241, 3170, 3728, 4362, 3480, 5026, 7412, 4951, 2590, 3779, 9264, 9599, 363, 392, 6825, 2896, 6037, 8854, 6141, 382, 6195, 5498, 1256, 3607, 3465, 2100, 5064, 2018, 4001, 8292, 712, 7407, 6212, 2194, 4401, 8006, 8996, 504, 7005, 7488, 3921, 3623, 3400, 9165, 1755, 4661, 8178, 4790, 2571, 2855, 3017, 9807, 206, 243, 3694, 1591, 4347, 4842, 6588, 1197, 2422, 8566, 186, 1823, 7628, 2931, 8958, 356, 422, 1842, 9139, 612, 1960, 3267, 3622, 466, 8645, 2370, 9360, 1387, 8757, 5249, 5109, 2383, 1285, 9913, 2685, 2533, 3978, 3014, 3320, 9666, 3804, 2138, 267, 6402, 1730, 9201, 521]
#a
print(max(numbers))
sorted_numbers = sorted(numbers)
print(sorted_numbers)

#b
print(min(numbers))
print(sorted_numbers[0])

#c
print(sum(numbers))

#d
print(statistics.mean(numbers))
print(statistics.median(numbers))

#2
word_lists = [ ['carrot', 'banana'], ['apricot', 'banana', 'cherry'], ['zebra', 'antelope'], ['melon', 'lettuce', 'aardvark'] ]

#a
print(word_lists[0])

#b
print(word_lists[0][0])

#c
print(word_lists[2][1].upper())

#d
print(len(word_lists))

#e 
print(sorted(word_lists))

#3
new_list = ['carrot', 'banana', 'apricot', 'banana', 'cherry', 'zebra', 'antelope', 'melon', 'lettuce', 'aardvark']
new_list_two = ['strawberry', 'blueberry', 'raspberry', 'blackberry', 'kiwi', 'mango', 'pineapple', 'peach', 'pear']
print(new_list.count('zebra'))
print(new_list.index('melon'))
print(new_list.extend(new_list_two))
new_list.clear()

print(2+2)
print("Hello" + "World")
combined_list = new_list + new_list_two

print(combined_list)