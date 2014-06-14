--Returns True if a list contains a multiple of the given Int, False otherwise.
listContainsMultiples :: Int -> [Int] -> Bool
listContainsMultiples n [] = False
listContainsMultiples n (x:xs)
	| n `mod` x == 0 = True
	| otherwise = listContainsMultiples n xs

--Returns True if a given Int is prime, False otherwise
isPrime :: Int -> Bool
isPrime n
	| n < 2 = False
	| n == 2 = True
	| n `mod` 2 == 0 = False
	| listContainsMultiples n [3,5.. ceiling(sqrt (fromIntegral  n))] = False
	| otherwise = True

--Get the Nth prime number
getNthPrime :: Int -> Int
getNthPrime n = [x | x <- 2:[3,5..], isPrime x] !! (n - 1)