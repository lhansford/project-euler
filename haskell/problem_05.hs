--Find the smallest number that can be evenly diveded from 1 to the given Int
smallestMultiple :: Int -> Int
smallestMultiple range = head [x | x <- [range*(range-1),2*(range*(range-1))..],
 divisibleRange x range]

--Return True if the fisrt given Int can be evenly divided by each number from 
--1 to the second Int, False otherwise
divisibleRange :: Int -> Int -> Bool
divisibleRange n 1 = True
divisibleRange n range
	| n `mod` range == 0 = divisibleRange n (range-1)
	| otherwise = False