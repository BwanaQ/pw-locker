#!/usr/bin/env python3.8
from credential import Credential
from user import User
import random


def verify_user(user_name, password):
    pass


def create_user(fname, lname, uname, pwd):
    new_user = User(fname, lname, uname, pwd)
    return new_user


def save_users(user):
    user.save_user()


def delete_users(user):
    user.delete_user()


def display_users():
    return User.display_users()


def create_credential(title, url, uname, pwd):
    new_credential = Credential(title, url, uname, pwd)
    return new_credential


def save_credentials(credential):
    credential.save_credential()


def delete_credentials(credential):
    credential.delete_credential()


def display_credentials():
    return Credential.display_credentials()


def generate_password():
    return Credential.generatePassword()


def main():
    print("Welcome to Password Locker... \n Please enter one to continue\n SU --- Sign Up\n LI --- Log in")
    short_code = input("").lower().strip()
    if short_code == "su":
        print("Sign Up")
        print('=*'*25)
        first_name = input("First name: ")
        last_name = input("Last name: ")
        user_name = input("Username: ")
        while True:
            print("TP --- To Type Password:\n GP --- To generate Password")
            password_option = input().lower().strip()
            if password_option == 'tp':
                password = input("Enter your password\n")
                break
            elif password_option == 'gp':
                password = generate_password()
                break
            else:
                print("Invalid password option Please try again")
        save_users(create_user(first_name, last_name, user_name, password))
        print("*="*42)
        print(f"Hi {user_name}, welcome to password Locker!!")
    elif short_code == "li":
        print("*="*25)
        print("Enter username and password to log in")
        print("*="*25)
        uname = input("Username: ")
        pwd = input("Password: ")
        login = verify_user(uname, pwd)
        if verify_user == login:
            print(f"Hello {uname}. Welcome to Password Locker\n")
    while True:
        print("Use these short codes: \n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")


if __name__ == '__main__':

    main()
