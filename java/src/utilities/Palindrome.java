package utilities;

public class Palindrome {
	
	/** Checks if a String is a palindrome
	 * @param string
	 * @return
	 * 		True if is a palindrome, false otherwise
	 */
	public static boolean isPalindrome(String string){
		if(string.length() < 2){
			return true;
		}
		if(string.charAt(0) == string.charAt(string.length() - 1)){
			if(string.length() == 2){
				return true;
			}else{
				return isPalindrome(string.substring(1, string.length() - 1));
			}
		}else{
			return false;
		}
	}
	
	/** Checks if an integer is a palindrome
	 * @param int
	 * @return
	 * 		True if is a palindrome, false otherwise
	 */
	public static boolean isPalindrome(int number){
		return isPalindrome(String.valueOf(number));
	}
}
