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


def delete_credentials(user):
    user.delete_credential()


def display_credentials():
    return Credential.display_credentials()


def main():
    pass


if __name__ == '__main__':

    main()
