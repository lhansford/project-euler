package problems;

public class Problem6 {
	public static void main(String[] args) {
		int limit = 101;
		int sumOfSquares = 0;
		int squareOfSum = 0;
		for (int i = 1; i < limit; i++){
			sumOfSquares += Math.pow(i, 2);
			squareOfSum += i;		
		}
		squareOfSum = (int) Math.pow(squareOfSum, 2);
		System.out.println(squareOfSum - sumOfSquares);
	}
}
