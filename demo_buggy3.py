"""Demo file with deliberate bugs for an autofix engine proof."""


def add_user(name, users=[]):
    users.append(name)
    return users


def get_ratio(a, b):
    return a / b


def load_settings(path):
    password = "supersecret123"
    try:
        with open(path) as f:
            return f.read(), password
    except:
        return None, password
