arr = input("Enter array with values comma separated ").split(",")
print(f"User input array {arr}")


def bubble_sort_arr(input_arr):
    length = len(input_arr)
    for i in range(length):
        for j in range(0, length - i - 1):
            if input_arr[j] > input_arr[j + 1]:
                input_arr[j], input_arr[j + 1] = input_arr[j + 1], input_arr[j]
    return input_arr


print(f"Sorted array {bubble_sort_arr(arr)}")
