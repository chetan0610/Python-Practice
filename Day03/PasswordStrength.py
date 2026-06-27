def check_password(password):
    if len(password) < 8:
        return "Weak Password"
    else:
        return "Strong Password"


user_password = input("Enter a password to test: ")

strength = check_password(user_password)

print(f"Password Strength: {strength}")