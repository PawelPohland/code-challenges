package main

import "fmt"

func getNumbers(startNum int, endNum int) []int {
	var numbers []int

	for number := startNum; number <= endNum; number++ {
		if number%7 == 0 && number%5 != 0 {
			numbers = append(numbers, number)
		}
	}

	return numbers
}

func main() {
	numbers := getNumbers(2000, 3200)

	for index, value := range numbers {
		if index > 0 {
			fmt.Print(", ")
		}
		fmt.Print(value)
	}

	fmt.Println()
}
