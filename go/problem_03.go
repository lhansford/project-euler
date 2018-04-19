package main

import "fmt"
import "math"

func main() {
	fmt.Printf("%v", getPrimeFactors(600851475143))
}

func getPrimeFactors(number int) []int {
	var primeFactors []int
	for number % 2 == 0 {
		primeFactors = append(primeFactors, 2)
		number = number / 2
	}

	for _, e := range getRange(3, int(math.Sqrt(float64(number))) + 1, 2) {
		for number % e == 0 {
			primeFactors = append(primeFactors, e)
			number = number / e
		}
	}
	if number > 2 {
		primeFactors = append(primeFactors, number)
	}
	return primeFactors
}
