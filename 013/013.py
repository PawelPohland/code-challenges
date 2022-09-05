def is_pallindrome(text):
    return text == text[::-1]


def is_pallindrome2(text):
    for i in range(0, int(len(text) / 2), 1):
        if text[i] != text[len(text) - 1 - i]:
            return False

    return True


def is_pallindrome3(text, front_index, back_index):
    if len(text) < 2:
        return False

    if text[front_index] != text[back_index]:
        return False

    if front_index == back_index:
        return True

    return is_pallindrome3(text, front_index + 1, back_index - 1)


if __name__ == "__main__":
    words = ["radar", "not a palindrome",
             "kayak", "rotor", "abcdefghijkjihgfedcba"]

    for word in words:
        print(f"is_pallindrome('{word}') = {is_pallindrome(word)}")
        print(f"is_pallindrome('{word}') = {is_pallindrome2(word)}")
        print(
            f"is_pallindrome('{word}') = {is_pallindrome3(word, 0, len(word) - 1)}")
