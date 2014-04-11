package utilities;

import java.util.ArrayList;

public class Fibonacci {
	
	/** Get all Fibonacci numbers under the limit.
	 * @param limit
	 * @return
	 */
	public static ArrayList<Integer> getFibonacciNums(int limit){
		ArrayList<Integer> fibNums = new ArrayList<Integer>();
		int f1 = 0;
		int f2 = 1;
		while (f1+f2 < limit) {
			fibNums.add(f1+f2);
			int x = f1 +f2;
			f1 = f2;
			f2 = x;
		}
		return fibNums;
	}
}
