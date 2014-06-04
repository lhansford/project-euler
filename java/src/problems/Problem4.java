package problems;

import utilities.Palindrome;

public class Problem4 {
	
	public static void main(String[] args) {
		System.out.println(findPalindrome(3));
	}
	
	/** Finds the longest palindromic nubmer that is the product of two numbers
	n-digits long.
	 * @param productLength
	 * @return
	 */
	private static int findPalindrome(int productLength){
		int biggest = 0;
		int minProduct = (int) Math.pow(10, productLength-1);
		int maxProduct = (int) Math.pow(10, productLength) - 1;
		for(int i = maxProduct; i > minProduct; i--){
			for(int j = maxProduct; j > minProduct; j--){
				int product = i*j;
				if (product > biggest && Palindrome.isPalindrome(product)){
					biggest = product;
				}
			}
		}
		return biggest;
	}

}
