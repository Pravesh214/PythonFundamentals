# Lists basics and initial methods
string_list = ["second item", 'first item', "third item"]
number_list = [10, 2, 13, 5, 9]
mix_list = ["first", 2, "third", 9.0]
list_of_list = [[1, 2, 3], ["one", "three", "two"]]

# Sorting
string_list.sort()  # This will sort original list itself
print(string_list)
print(sorted(number_list))  # This with return sorted copy of list


# Slicing / appending / inserting
string_list.pop()
print(string_list)
number_list.append(6)
print(number_list)
string_list.insert(1, "name")
print(string_list)

mix_list.insert(1, string_list)
print(mix_list)
mix_list.append(number_list)
print(mix_list)


# Access item in list
print(mix_list[1][2])
print((mix_list[-1][-1]))



