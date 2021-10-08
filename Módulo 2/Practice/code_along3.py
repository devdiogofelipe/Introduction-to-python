
password = ''

while password != "secret":
    
    user = input("Enter your username: ")
    password = input("Enter the password: ")

    if password == 'secret':
        print("Welcome, ", user)
    else:
        print('Sorry, the password you entered is incorrect. Please try again.')

