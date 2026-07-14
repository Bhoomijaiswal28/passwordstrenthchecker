print("=================================")
print("   PASSWORD STRENGTH CHECKER")
print("=================================")

password = input("Enter your password: ")

score = 0

# Length Check
if len(password) >= 8:
    print("✔ Password length is good")
    score += 1
else:
    print("✘ Password should be at least 8 characters")

# Uppercase Check
if any(ch.isupper() for ch in password):
    print("✔ Contains uppercase letter")
    score += 1
else:
    print("✘ Add at least one uppercase letter")

# Lowercase Check
if any(ch.islower() for ch in password):
    print("✔ Contains lowercase letter")
    score += 1
else:
    print("✘ Add at least one lowercase letter")

# Number Check
if any(ch.isdigit() for ch in password):
    print("✔ Contains a number")
    score += 1
else:
    print("✘ Add at least one number")

# Special Character Check
special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if any(ch in special for ch in password):
    print("✔ Contains special character")
    score += 1
else:
    print("✘ Add at least one special character")

print("\n---------------------------")
print("Score:", score, "/5")

if score == 5:
    print("Password Strength : Very Strong ")
elif score == 4:
    print("Password Strength : Strong ")
elif score == 3:
    print("Password Strength : Medium ")
elif score == 2:
    print("Password Strength : Weak ")
else:
    print("Password Strength : Very Weak ")

print("   PASSWORD STRENGTH CHECKER")
print("=================================")

password = input("Enter your password: ")

score = 0

# Length Check
if len(password) >= 8:
    print("✔ Password length is good")
    score += 1
else:
    print("✘ Password should be at least 8 characters")

# Uppercase Check
if any(ch.isupper() for ch in password):
    print("✔ Contains uppercase letter")
    score += 1
else:
    print("✘ Add at least one uppercase letter")

# Lowercase Check
if any(ch.islower() for ch in password):
    print("✔ Contains lowercase letter")
    score += 1
else:
    print("✘ Add at least one lowercase letter")

# Number Check
if any(ch.isdigit() for ch in password):
    print("✔ Contains a number")
    score += 1
else:
    print("✘ Add at least one number")

# Special Character Check
special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if any(ch in special for ch in password):
    print("✔ Contains special character")
    score += 1
else:
    print("✘ Add at least one special character")

print("\n---------------------------")
print("Score:", score, "/5")

if score == 5;

    print("Password Strength : Very Strong ")
elif score == 4:
    print("Password Strength : Strong ")
elif score == 3:
    print("Password Strength : Medium ")
elif score == 2:
    print("Password Strength : Weak ")
else:
    print("Password Strength : Very Weak ")
