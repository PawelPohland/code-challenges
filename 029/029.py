def odd_even(number):
    odd_nums = []
    even_nums = []

    for num in range(1, number + 1):
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)

    return (odd_nums, even_nums)


def odd_even2(number):
    odd_nums = [num for num in range(1, number + 1) if num % 2 != 0]
    even_nums = [num for num in range(1, number + 1) if num % 2 == 0]

    return odd_nums, even_nums


if __name__ == "__main__":
    max_num = 100

    odd_even_nums = odd_even(max_num)

    print(f"Odd numbers [1, {max_num}] = {odd_even_nums[0]}")
    print(f"Even numbers [1, {max_num}] = {odd_even_nums[1]}")

    odd_even_nums = odd_even2(max_num)

    print(f"Odd numbers [1, {max_num}] = {odd_even_nums[0]}")
    print(f"Even numbers [1, {max_num}] = {odd_even_nums[1]}")
