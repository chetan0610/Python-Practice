def reverse_string(text):

    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text


user_input = input("Enter a string to reverse: ")

result = reverse_string(user_input)

print(f"Reversed string: {result}")