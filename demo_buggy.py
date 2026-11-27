import os
import sqlite3


def get_user(user_id):
    conn = sqlite3.connect("example.db")
    # Bug 1 fixed: parameterized query instead of string concatenation
    cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


def process_items(items=None):
    # Bug 2 fixed: mutable default argument replaced with None
    if items is None:
        items = []
    items.append("processed")
    return items


def read_file(path):
    # Bug 3 fixed: catch specific exception instead of bare except
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


def connect_db():
    # Bug 4 fixed: hardcoded password replaced with environment variable
    password = os.getenv("DB_PASSWORD")
    if not password:
        raise ValueError("DB_PASSWORD environment variable not set")
    return password


def divide(a, b):
    # Bug 5 fixed: check for zero divisor
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
