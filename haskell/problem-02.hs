--Takes a list of integers (supposedly a fibonacci sequence) and adds the next
--integer in the sequence to the front of the list
nextFibonacci :: [Int] -> [Int]
nextFibonacci [] = [1]
nextFibonacci [1] = [2,1]
nextFibonacci (x:y:xs) = x+y:x:y:xs

--Takes an empty list and limit and returns a list of all fibonnaci numbers
--with a value less than limit
getFibonaccis :: [Int] -> Int -> [Int]
getFibonaccis [] limit = getFibonaccis (nextFibonacci []) limit
getFibonaccis nums limit
	| head nums < limit = getFibonaccis (nextFibonacci nums) limit
	| otherwise = nums

--Returns the sum of all even numbers in a given list of integers
sumEvens :: [Int] -> Int
sumEvens [] = 0
sumEvens (x:xs)
	| x `mod` 2 == 0 = x + sumEvens xs
	| otherwise = 0 + sumEvens xs

--Run the following to get the answer
--sumEvens (getFibonaccis [] 40000000)