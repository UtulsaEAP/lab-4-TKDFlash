"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Sean Killian
Lab Time: Thursday @ 2pm
"""

def password_mod():
    word = input()
    password = ''
    # Type your code here.

    for letter in word:
        if letter == "i":
            password += "1"
        elif letter == "a":
            password += "@"
        elif letter == "m":
            password += "M"
        elif letter == "B":
            password += "8"
        elif letter == "s":
            password += "$"
        else:
            password += letter

    print(password + "!")

if __name__ == "__main__":
    password_mod()