##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""
print("Enter Username and Password")
correct_user = "admin"
correct_pass = "12345"

user = ""
password = ""
attempt = 0

while attempt < 3:
    user = input("username:")
    password = input("password:")

    if user == correct_user and password == correct_pass:
        print("access granted")
        break
    else:
        print("access denied")
        attempt += 1
if attempt == 3:
    print("too many failed attemtps. Access denied")