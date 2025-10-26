what_to_do = input("What do you want to do? (encode/decode): ").strip().lower()
shift = int(input("Enter the shift value (integer): ")) % 26  # Ensure shift is within 0-25
text = input("Enter the message: ")
result = ""
if what_to_do == "encode":
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char  # Non-alphabetic characters remain unchanged
elif what_to_do == "decode":
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
        else:
            result += char  # Non-alphabetic characters remain unchanged
else:
    result = "Invalid operation. Please choose 'encode' or 'decode'."
print(f"Result: {result}")
