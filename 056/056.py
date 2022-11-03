def my_discount():
    price = float(input("Enter price: "))
    discount_percentage = float(input("Enter discount (%): "))

    return price - (price * discount_percentage / 100)


if __name__ == "__main__":
    price_after_discount = my_discount()
    print(f"Price after dicount: {price_after_discount}")
