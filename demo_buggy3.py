"""Demo file with deliberate bugs for an autofix engine proof."""
import os
import sqlite3
def add_user(name, users=None):
    if users is None:
        users = []
    users.append(name)
    return users


def get_ratio(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def run_command(name):
    import subprocess
    return subprocess.run(["echo", name], check=True)


def find_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = ?", (username,))
    return cur.fetchall()


def load_settings(path):
    password = os.getenv("APP_PASSWORD", "") # Load from environment variable or other secure source
    try:
        with open(path) as f:
            return f.read(), password
    except FileNotFoundError: # Catch specific exceptions like FileNotFoundError
        return None, password


def calculate(expression):
    # eval(expression) is a security risk. Do not use with untrusted input.
    raise ValueError("Unsafe expression evaluation attempted.")
