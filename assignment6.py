correct_pass = "password123"
user_pass = input("Please enter your password: ")
if user_pass == correct_pass:
    print("Correct! Password accepted.")
else:
    while user_pass != correct_pass:
        print("Incorrect.")
        user_pass == input("Please enter your password: ")
