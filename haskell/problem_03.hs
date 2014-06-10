--Returns True if a list contains a multiple of the given Int, False otherwise.
listContainsMultiples :: Int -> [Int] -> Bool
listContainsMultiples n [] = False
listContainsMultiples n (x:xs)
	| n `mod` x == 0 = True
	| otherwise = listContainsMultiples n xs

--Returns the ceiling of the square root of the given integer
ceilingSqrt :: Int -> Int
ceilingSqrt n = ceiling(sqrt (fromIntegral  n))

--Returns all prime multiples of a given Int
getPrimeMultiples :: Int -> [Int]
getPrimeMultiples n = 
	[x | x <- [1,2..ceilingSqrt n], n `mod` x == 0 && isPrime x]

--Returns True if a given Int is prime, False otherwise
isPrime :: Int -> Bool
isPrime n
	| n < 2 = False
	| n == 2 = True
	| n `mod` 2 == 0 = False
	| listContainsMultiples n [3,5.. ceiling(sqrt (fromIntegral  n))] = False
	| otherwise = True

--Run the following line to get the answer to the problem
--last (getPrimeMultiples 600851475143)