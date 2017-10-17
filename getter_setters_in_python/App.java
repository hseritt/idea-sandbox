public class App {
	public static void main(String[] args) {
		Thing thing = new Thing(42);
		
		// Incorrect
		System.out.println(thing.x);
		thing.x = 25;
		System.out.println(thing.x);

		// Correct
		// System.out.println(thing.getX());
		// thing.setX(25);
		// System.out.println(thing.getX());
	}
}