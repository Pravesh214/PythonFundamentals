from PyCode.BasicPrograms.Programs.ReverseString import reverse_string

user_str = input("Enter String: ")


def check_palindrome(input_str):
    if input_str == reverse_string(input_str):
        return "String is Palindrome"
    return "String is not Palindrome"


print(check_palindrome(user_str))
