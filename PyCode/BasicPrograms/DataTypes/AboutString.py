# About String data structure

first_string = 'This is first string'
second_string = "This is second string"

print(first_string.upper())
print(second_string.lower())

# String split[Slicing]
temp_list = first_string.split()
print(temp_list)
temp_list = second_string.split("i")
print(temp_list)

# String Searching
temp_char = first_string[0]
print(temp_char)

temp_char = second_string[-2]
print(temp_char)

# More on string
print(f" Count of 'is' within '{first_string}' => {first_string.count('is')}")
print(f"Number of occur of 'is' in {second_string} => {second_string.find('is')}")
print(f"Get index of first 'is' in string {first_string} => {first_string.index('is')}")

# Char list utilize in string
print(f"Print everything '{first_string[::]}'")
print(f"Print from index 1 to index -2 step jump 1 '{first_string[1:-2:1]}'")
print(f"Print from index 1 to index -2 step jump 2 '{first_string[1:-2:2]}'")
print(f"Print from index 0 to index -1 step jump 3 '{first_string[:-1:3]}'")
print(f"Print first half of string '{first_string[:len(first_string) // 2]}'")
print(f"Print second half of string '{first_string[len(first_string) // 2:]}'")

# Bonus Reverse string direct
print(f"Print from index -1 to index 0 step jump -1 '{first_string[::-1]}'")
