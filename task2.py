#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
print("Enter Username and Password")
correct_user = "admin"
correct_pass = "12345"

user = ""
password = ""

while user != correct_user or correct_pass != password:
    user = input("username:")
    password = input("password:")

    if user == correct_user and password == correct_pass:
        print("access granted")
    else:
        print("access denied")