package main

func getRange(min int, max int, step int) []int {
	var nums []int
	for i := min; i < max; i += step {
		nums = append(nums, i)
	}
	return nums
}
