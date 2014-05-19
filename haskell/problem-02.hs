fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

getFibonaccis :: Integer -> [a]
getFibonaccis limit = [f1+f2 | f]

sumEvens nums = sum [x | x <- nums, mod x 2 == 0]