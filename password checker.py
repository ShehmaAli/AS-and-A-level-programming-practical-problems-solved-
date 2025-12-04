# enter the password
pass1 = input("Enter the password: ")

# initialising attempts
attempts = 0

# starting the while loop to compare the passwords of the user
while True:
    pass2 = input("Please re enter the password: ")
    if pass2 != pass1:
        print("Please enter the correct password")
        attempts += 1
    if pass1 == pass2 and attempts == 3 or pass1 == pass2 and attempts < 3:
        print("Password matched")
        break
    if attempts == 3:
        print("Sorry all attempts used")
        break
