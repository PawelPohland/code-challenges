def user_name(email: str) -> str:
    at = email.find("@")
    if at != -1:
        return email[0:at:1]

    return ""


def user_name2(email: str) -> str:
    try:
        return email[0:email.index("@"):1]
    except ValueError:
        return ""


def user_name3(email: str) -> str:
    return email.split("@")[0]


if __name__ == "__main__":
    emails = ["john.doe@gmail.com", "not-a-valid-email.com",
              "no-reply@test.io", "the_one_and_two_and_three@acme.co"]

    for email in emails:
        print(
            f"{email} => {user_name(email)} | {user_name2(email)} | {user_name3(email)}")
