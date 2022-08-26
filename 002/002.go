package main

import "fmt"

func factorial1(number int) int {
	var result int = 1

	for num := 1; num <= number; num++ {
		result *= num
	}

	return result
}

func factorial2(number int) int {
	if number <= 1 {
		return 1
	}

	return factorial2(number-1) * number
}

func main() {
	fmt.Print("Enter a number: ")

	var number int = 0
	fmt.Scanf("%d", &number)

	factorial := factorial1(number)
	fmt.Printf("%d! = %d\n", number, factorial)

	factorial = factorial2(number)
	fmt.Printf("%d! = %d\n", number, factorial)
}
