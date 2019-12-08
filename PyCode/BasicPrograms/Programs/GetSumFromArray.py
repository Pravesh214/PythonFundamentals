my_list = [10, 15, 6, 12, 4, 3]

def get_sum_of_list(list):
    sum = 0
    for item in list:
        sum = sum + item
    return sum

print(get_sum_of_list(my_list))
print(max(my_list))
