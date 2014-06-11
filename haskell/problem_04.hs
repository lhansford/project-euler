--Returns True if given String is palindrome, False otherwise.
isPalindrome :: String -> Bool
isPalindrome [] = True
isPalindrome [x] = True
isPalindrome (x:xs)
	| x /= last xs = False
	| otherwise = isPalindrome (init xs)

--Return the length of the given Int
intLength :: Int -> Int
intLength n = length (show n)

--Returns True if the given Int is a product of two 3-digit Ints
has3DigitFactors :: Int -> Bool
has3DigitFactors x
	| [a | a <- [100,101..1000], x `mod` a == 0 &&
	 	intLength (x `div` a) == 3] /= [] = True
	| otherwise = False

-- Returns the largest Palindrome, less than the given Int, that is a product 
-- of 3 digit nums
largestPalindromeProduct :: Int -> Int
largestPalindromeProduct x
	| isPalindrome (show x) == False = largestPalindromeProduct (x-1)
	| has3DigitFactors x == False = largestPalindromeProduct (x-1)
	| otherwise = x

--To get answer run the following
--largestPalindromeProduct 998001