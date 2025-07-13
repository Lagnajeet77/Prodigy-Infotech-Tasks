import re

def check_password_strength(password):
    strength_score = 0
    feedback = []

    # Criteria
    length_ok = len(password) >= 8
    upper_ok = bool(re.search(r"[A-Z]", password))
    lower_ok = bool(re.search(r"[a-z]", password))
    digit_ok = bool(re.search(r"[0-9]", password))
    special_ok = bool(re.search(r"[\W_]", password))  # Non-alphanumeric

    # Scoring
    if length_ok:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if upper_ok:
        strength_score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if lower_ok:
        strength_score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if digit_ok:
        strength_score += 1
    else:
        feedback.append("Include at least one number.")

    if special_ok:
        strength_score += 1
    else:
        feedback.append("Include at least one special character (e.g., @, #, $, !).")

    # Rating
    if strength_score <= 2:
        rating = "Weak"
    elif strength_score == 3 or strength_score == 4:
        rating = "Moderate"
    else:
        rating = "Strong"

    return strength_score, rating, feedback

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ").strip()

    score, rating, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {rating} ({score}/5)")
    if feedback:
        print("Suggestions:")
        for item in feedback:
            print(f" - {item}")
    else:
        print("Your password meets all recommended criteria!")

if __name__ == "__main__":
    main()
