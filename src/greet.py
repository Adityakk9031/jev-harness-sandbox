def greeting(user, default="friend"):
    if user is None:
        return f"Hello, {default}!"
    return f"Hello, {user.name}!"
