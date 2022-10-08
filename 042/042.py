def get_user_input():
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))

    return width, length


def calc_area(width, length):
    return width * length


def calc_area_diag(width_or_length, diagonal):
    side_squared = width_or_length * width_or_length
    diag_squared = diagonal * diagonal

    return width_or_length * ((diag_squared - side_squared) ** 0.5)


def calc_perimeter(width, length):
    return 2 * (width + length)


def calc_diagonal(width, length):
    # math.sqrt(width * width + length * length)
    return (width * width + length * length) ** 0.5


if __name__ == "__main__":
    width, length = get_user_input()

    area = calc_area(width, length)
    perimeter = calc_perimeter(width, length)
    diagonal = calc_diagonal(width, length)

    area_by_diag = calc_area_diag(width, diagonal)

    print(f"Area = {area} ({area_by_diag})")
    print(f"Perimeter = {perimeter}")
    print(f"Diagonal = {diagonal}")
