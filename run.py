#!/usr/bin/env python3.8
from credential import Credential
from user import User
import random


def create_user(fname, lname, uname, pwd):
    new_user = User(fname, lname, uname, pwd)
    return new_user


def create_credential(title, url, uname, pwd):
    new_credential = Credential(title, url, uname, pwd)
    return new_credential
