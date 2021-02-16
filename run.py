#!/usr/bin/env python3.8
from credential import Credential
from user import User
import random


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


def find_credentials(title):
    return Credential.find_by_title(title)


def copy_passwords(title):
    return Credential.copy_password(title)


def generate_password(length):
    return Credential.generatePassword(length)


def verify_users(username, password):
    return User.verify_user(username, password)


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
                length = input(
                    "please enter the lenght of the password you want generated...")
                int_length = int(length)
                password = generate_password(int_length)
                break
            else:
                print("Invalid password option Please try again")
        save_users(create_user(first_name, last_name, user_name, password))
        print("*="*42)
        print(
            f"Hi {user_name}, welcome to password Locker!! your password is {password}")
    elif short_code == "li":
        print("*="*25)
        print("Enter username and password to log in")
        print("*="*25)
        uname = input("Username: ")
        pwd = input("Password: ")
        login = verify_users(uname, pwd)
        if verify_users == login:
            print(f"Hello {uname}. Welcome to Password Locker\n")
            while True:
                print("Use these short codes: \n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
                s_code = input().lower().strip()
                if s_code == "cc":
                    print("Create credential")
                    print("*="*10)
                    print("Enter Title eg ... Facebook")
                    title = input().lower().strip()
                    print("Enter URL eg ... https://www.facebook.com/login")
                    url = input().lower().strip()
                    print("Enter username...")
                    user_name = input()
                    print(user_name)
                    while True:
                        print(
                            "Enter: \n TP --- To type your password or \n GP --- To generate password")
                        pwd_choice = input().lower().strip()
                        if pwd_choice == "tp":
                            pwd = input("Type in your password...\n")
                            break
                        elif pwd_choice == "gp":
                            length = int(input(
                                "please enter the lenght of the password you want generated..."))
                            int_length = int(length)
                            pwd = generate_password(int_length)
                            break
                        else:
                            print("Invalid choice Please try again")
                    save_credentials(create_credential(
                        title, url, user_name, pwd))
                    print(
                        f"credential for {title}: \n URL: {url} \n Username: {user_name}\n Password: {pwd}\n")
                elif s_code == "dc":
                    if display_credentials():
                        print("Displaying crredentials")
                        print("*="*15)
                        print("*="*15)
                        for credential in display_credentials():
                            print(
                                f"Title:{credential.title}\n URL: {credential.url}\n Username: {credential.user_name}\n password: {credential.password}")
                            print("*="*15)
                        print("*="*15)
                    else:
                        print("No saved credentials yet...")
                elif s_code == "fc":
                    search_name = input(
                        "Enter account title to search for ").lower().strip()
                    if find_credentials(search_name):
                        search_credential = find_credentials(search_name)
                        copy_passwords(search_name)
                        print("*="*25)
                        print(
                            f"Title: {search_credential.title}\n URL: {search_credential.url}\n Username: {search_credential.user_name} \n Password: {search_credential.password}")
                        print("NOTE: PASSWORD HAS BEEN COPIED TO CLIPBOARD!!!!")
                        print("*="*25)
                    else:
                        print("Credential does not exist\n")
                elif s_code == "d":
                    search_name = input(
                        "Enter title of credential you want to delete")
                    if find_credentials(search_name):
                        print("*_"*25)
                        print(
                            f"credentials for {search_credential.title} heve been deleted successfully")
                    else:
                        print("Credential does not exist \n")

                elif s_code == "gp":
                    length = int(
                        input("please enter the lenght of the password you want generated..."))
                    int_length = int(length)
                    pwd = generate_password(int_length)
                    print(f"generated password: {pwd}")
                elif s_code == "ex":
                    print("Thanks for using Password Locker....")
                    break
                else:
                    print(
                        "Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")


if __name__ == '__main__':

    main()
