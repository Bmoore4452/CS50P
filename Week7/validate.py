import re

email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

if re.search(
    r"^[\w_]+@(\w+\.)?[\w]+\.(edu|com|net)$", email, re.IGNORECASE
):  # r =raw string
    print("Valid")
else:
    print("Invalid")
