package utilities;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

/**
 * @author luke
 *
 */
public class Basic {
	
	/** Get all multiples of a number under the limit.
	 * @param n
	 * @param limit
	 * @return
	 */
	public static ArrayList<Integer> getMultiplesOfN(int n, int limit) {
		ArrayList<Integer> multiples = new ArrayList<Integer>();
		for (int i = n; i < limit; i += n) {
			multiples.add(i);
		}
		return multiples;
	}
	
	/** Takes a list of ints and finds all multiples of those ints under the limit
	 * @param n
	 * @param limit
	 * @return
	 */
	public static ArrayList<Integer> getMultiplesOfIntegers(int[] n, int limit) {
		Set<Integer> multiples = new HashSet<Integer>();
		for (int i = 0; i < n.length; i++) {
			multiples.addAll(getMultiplesOfN(n[i],limit));
		}
		ArrayList<Integer> multiplesArray = new ArrayList<Integer>();
		multiplesArray.addAll(multiples);
		return multiplesArray;
	}
	
	/** Sum all numbers in array
	 * @param array
	 * @return
	 */
	public static int sum(ArrayList<Integer> array) {
		int sum = 0;
		for (int i = 0; i < array.size(); i++){
			sum += array.get(i);
		}
		return sum;
	}

	/** Sum all even numbers in array
	 * @param array
	 * @return
	 */
	public static int sumEven(ArrayList<Integer> array) {
		int sum = 0;
		for (int i = 0; i < array.size(); i++){
			if (array.get(i) % 2 == 0){
				sum += array.get(i);
			}
		}
		return sum;
	}

}
