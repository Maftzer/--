input_string = input()
digits = tuple(char for char in input_string if char.isdigit())
letters = tuple(char for char in input_string if char.isalpha())
others = tuple(char for char in input_string if not char.isdigit() and not char.isalpha())

print("".join(digits))
print("".join(letters))
print("".join(others))

