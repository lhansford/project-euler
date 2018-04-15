package main

import "fmt"

func sumEvenFibs(max int) int {
	var a int = 1
	var b int = 2
	var sum int = 0
	var next int
	for b < max {
		if b % 2 == 0 {
			sum = sum + b
		}
		next = a + b
		a = b
		b = next
	}
	return sum
}
	
func main() {
	fmt.Println(sumEvenFibs(4000000))
}
