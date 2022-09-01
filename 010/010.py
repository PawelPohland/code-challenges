def card_hash(card_number):
    return "#" * (len(card_number) - 4) + card_number[-4:]


def card_hash2(card_number):
    hashed = ""

    for _ in card_number[:-4]:
        hashed += "#"

    hashed += card_number[-4:]

    return hashed


if __name__ == "__main__":
    card_numbers = ["5435782486540786", "5235682486420687"]

    for card_number in card_numbers:
        print(f"{card_number} => {card_hash(card_number)}")
        print(f"{card_number} => {card_hash2(card_number)}")
