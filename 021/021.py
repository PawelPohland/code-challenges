def sum_of_homologous(a, b):
    max_index = len(a)

    if len(b) > max_index:
        max_index = len(b)

    for index in range(max_index):
        total = 0

        if len(a) - 1 >= index:
            total += a[index]

        if len(b) - 1 >= index:
            total += b[index]

        print(total)


def sum_of_homologous2(a, b):
    for a_num, b_num in zip(a, b):
        print(a_num + b_num)


if __name__ == "__main__":
    sum_of_homologous([1, 2, 3], (4, 5, 6))
    sum_of_homologous([1, 2, 3], (4, 5, 6, 100))
    sum_of_homologous2([1, 2, 3], (4, 5, 6, 100))
