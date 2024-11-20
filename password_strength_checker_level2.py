import re

def evaluate_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\'\\:"|,.<>\/?]', password))

    # Password strength score
    score = 0
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    # Return the results
    return {
        "length_criteria": length_criteria,
        "uppercase_criteria": uppercase_criteria,
        "lowercase_criteria": lowercase_criteria,
        "digit_criteria": digit_criteria,
        "special_char_criteria": special_char_criteria,
        
    }
    
# Example usage
password = input("Enter your password: ")
result = evaluate_password_strength(password)

# Print the password evaluation
print("\nPassword Strength Evaluation:")
print(f"Length is sufficient: {result['length_criteria']}")
print(f"Contains uppercase letters: {result['uppercase_criteria']}")
print(f"Contains lowercase letters: {result['lowercase_criteria']}")
print(f"Contains digits: {result['digit_criteria']}")
print(f"Contains special characters: {result['special_char_criteria']}")
