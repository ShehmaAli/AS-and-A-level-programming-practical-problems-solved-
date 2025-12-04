# enter the password
pass1 = input("Enter the password: ")

# initialising attempts
attempts = 0

# starting the while loop to compare the passwords of the user
while True:
    # asking the user again for the password
    pass2 = input("Please re enter the password: ")

    # comparing the passwords using the if statement
    if pass2 != pass1:
        print("Please enter the correct password")
        # incrementing the attempts variable
        attempts += 1
    # setting the if condition to see weather the password
    if pass1 == pass2 and attempts == 3 or pass1 == pass2 and attempts < 3:
        print("Congrats password matched")
        break
    # seeing if all the attempts are used
    if attempts == 3:
        print("Sorry all attempts used")
        break
