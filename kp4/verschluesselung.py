# Autor:                Elia Ressl
# Place:                Homeoffice
# Date:                 08.02.2025
# Filename:             verschluesselung.py
# Short description:    verschlüsselt einen beliebigen string. mein code funktioniert nicht und ich weiss nicht wie ich ihn zum funktionieren bringen soll. irgend etwas mit str und int beisst sich.



# MY CODE

# def replacenumber(number):
#     key = "9276815340"
#     if number == 0:
#         number = key.index("0")
#     elif number == 1:
#         number = key.index("1")
#     elif number == 2:
#         number = key.index("2")
#     elif number == 3:
#         number = key.index("3")
#     elif number == 4:
#         number = key.index("4")
#     elif number == 5:
#         number = key.index("5")
#     elif number == 6:
#         number = key.index("6")
#     elif number == 7:
#         number = key.index("7")
#     elif number == 8:
#         number = key.index("8")
#     elif number == 9:
#         number = key.index("9")
#     return number


# def encrypt(code):
#     for i in range(len(code)):
#         replacenumber(code.index(str(i)))
#     return code

# encryptedcode = encrypt(str(7834291578159))

# print(encryptedcode)





# code from CHATGPT
# def replacenumber(number):
#     key = "1234567890"  # Key as a string
#     return key.index(str(number))  # Convert number to string before using index()


# def encrypt(code):
#     encrypted_code = ""  # Use a string to store encrypted result
#     for digit in code:  # Loop through each character in code
#         encrypted_code += str(replacenumber(digit))  # Convert back to string
#     return encrypted_code  # Return the encrypted string

# # Example usage
# encrypted_code = encrypt("0")
# print(encrypted_code)






# code from DEEPSEEK
# def encrypt(code):
#     # Define the key
#     key = "9450387126"
  
#     # Create a mapping from each digit to its corresponding index in the key
#     mapping = {str(digit): str(key.index(str(digit))) for digit in range(10)}
  
#     # Encrypt the code by replacing each digit with its mapped value
#     encrypted_code = ""
#     for char in code:
#         if char in mapping:  # Check if the character is a digit
#             encrypted_code += mapping[char]
#         else:
#             encrypted_code += char  # Keep non-digit characters as they are
  
#     return encrypted_code
# # Example usage
# encryptedcode = encrypt("j6438643j6438")
# print(encryptedcode)  # Output will be the encrypted code