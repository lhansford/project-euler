-- Square the sum of the Ints in the given list
squareSum :: [Int] -> Int
squareSum x = (sum x)^2

-- Return the sum of the squares of each Int in the given list
sumSquares :: [Int] -> Int
sumSquares [] = 0
sumSquares (x:xs) = x^2 + sumSquares xs

-- Find the difference between the sum of squares and the square of the sum for 
-- a given list of Ints
sumSquareDifference :: [Int] -> Int
sumSquareDifference x = squareSum x - sumSquares x

-- Run the following to get the answer
-- sumSquareDifference [1,2..100]