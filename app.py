def check_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in '!@#$%^&*()-_=+[{]};:\'",<.>/?\\|`~' for char in password):
        strength += 1

    if strength <= 1:
        return "Weak"
    elif strength == 2 or strength == 3:
        return "Medium"
    else:
        return "Strong"

password=input("Enter password,or 'exit' to quit: ")
while password.lower() != 'exit':
    print("Password strength:", check_strength(password))
    password = input("Enter password,or 'exit' to quit: ")