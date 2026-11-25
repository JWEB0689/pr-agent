"""Demo file with deliberate bugs for an autofix engine proof."""
import os
import sqlite3


def add_user(name, users=[]):
    users.append(name)
    return users


def get_ratio(a, b):
    return a / b


def run_command(name):
    return os.system("echo " + name)


def find_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '%s'" % username)
    return cur.fetchall()


def load_settings(path):
    password = "supersecret123"
    try:
        with open(path) as f:
            return f.read(), password
    except:
        return None, password


def calculate(expression):
    return eval(expression)
