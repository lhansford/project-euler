package problems;

import java.util.ArrayList;

import utilities.Basic;

public class Problem1 {

	public static void main(String[] args) {
		int[] n = {3,5};
		ArrayList<Integer> multiples = Basic.getMultiplesOfIntegers(n, 1000);
		System.out.println(Basic.sum(multiples));
	}
	
}
