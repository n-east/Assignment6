attempt_number = 0
correct_pass = "password123"
user_pass = input("Please enter your password: ")
if user_pass == correct_pass:
    print("Correct! Password accepted.")
else:
    while user_pass != correct_pass:
        print("Incorrect.")
        attempt_number += 1
        print("Password attempt number: ", attempt_number)
        user_pass = input("Please enter your password: ")
print("Correct! Password accepted.")
