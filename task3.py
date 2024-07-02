
def password_strength(password):
    # Criteria flags
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Strength score
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])

    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character.")

    # Strength levels
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Medium"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

def main():
    password = input("Enter a password to assess: ")
    strength, feedback = password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")

if __name__ == "__main__":
    main()
