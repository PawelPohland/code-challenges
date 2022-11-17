def hide_password():
    password = input("Enter password: ")
    password_hidden = "*" * len(password)

    print(
        f"Your password {password_hidden} is {len(password)} characters long.")


if __name__ == "__main__":
    hide_password()
