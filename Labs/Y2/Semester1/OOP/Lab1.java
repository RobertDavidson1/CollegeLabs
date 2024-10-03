package Y2.Semester1.OOP;

public class Lab1 {

  public static void main(String[] args) {
    arithmeticOperations();
    circleAreaCalculator();
    stringConcatenation();
  }

  /**
   * Java program that performs the following basic arithmetic operations on two predefined integers.
   */
  public static void arithmeticOperations() {
    System.out.println("\nExercise 1: Basic Arithmetic Operations");

    // 1. Declare two integer variables a and b
    int a;
    int b;

    // 2. Initialize a with the value 10 and b with the value 5
    a = 10;
    b = 5;

    // 3(i). Calculate and print the sum of a and b
    int sum = a + b;
    System.out.println("a + b = " + sum);

    // 3(ii). Calculate and print the difference of a and b
    int difference = a - b;
    System.out.println("a - b = " + difference);

    // 3(iii). Calculate and print the product of a and b
    int product = a * b;
    System.out.println("a * b = " + product);

    // 3(iv). Calculate and print the quotient of a divided by b
    int quotient = a / b;
    System.out.println("a / b = " + quotient);

    // 3(Challenge). Calculate and print the remainder of a divided by b
    int remainder = a % b;
    System.out.println("a mod b = " + remainder);
  }

  /**
   * Java program that calculates the area of a circle with a predefined radius.
   */
  public static void circleAreaCalculator() {
    System.out.println("\nExercise 2: Simple Circle Area Calculation");

    // 1. Declare a double variable for the radius and initialize it with the value 7.0.
    double radius = 7.0;

    // 2. Use the constant PI (which can be approximated as 3.14159 ) in your calculation.
    double PI = 3.14159;

    // 3. Calculate the area of the circle using the formula: Area = PI * radius * radius.
    double area = PI * radius * radius;

    // 4. Print the result
    System.out.println(
      "The area of a circle with radius " + radius + " is " + area
    );
  }

  /**
   * Java program that combines text (strings) with numbers and prints a sentence.
   */
  public static void stringConcatenation() {
    System.out.println("\nExercise 3: String Concatenation and Output");

    // 1.Declare String variables firstName and lastName , and initialize them with your first and last name
    String firstName = "Robert";
    String lastName = "Davidson";

    // 2. Declare an int variable age and initialize it with your age
    int age = 22;

    // 3. Concatenate these values into a full sentence like: "John Doe is 20 years old."
    String outputString =
      firstName + " " + lastName + " is " + age + " years old.";

    // 4. Print the sentence
    System.out.println(outputString);
  }
}
