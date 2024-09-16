package Y2.Semester1.OOP;

import java.util.Scanner;

public class Lab2 {

  // Shared scanner for all methods
  private static Scanner scanner = new Scanner(System.in);

  // 1. Set up your Java program with a main method.
  public static void main(String[] args) {
    tempConverter();
    sumAndAvgCalc();
    initialsExtractor();

    // Close the shared scanner
    scanner.close();
  }

  /*
   * Java program that prompts the user to input three numbers.
   * Calculates the sum and average, and displays the results
   */
  public static void tempConverter() {
    System.out.print("Exercise 1: Temperature Converter\n");

    System.out.print("Enter temperature in Fahrenheit: ");

    // 2. Use a Scanner to prompt the user for a temperature in Fahrenheit
    double f_temp = scanner.nextDouble();

    // 3. Convert the temperature to Celsius using the formula
    double c_temp = (5.0 / 9.0) * (f_temp - 32);

    // 4. Display the converted temperature
    System.out.printf("Temperature in Celsius: %.2f\n", c_temp);
  }

  /*
   * Java program that prompts the user to input three numbers.
   * Calculates the sum and average, and displays the results.
   */
  public static void sumAndAvgCalc() {
    System.out.println("\nExercise 2: Sum and Average Calculator");

    //2.  Use a Scanner to prompt the user for three numbers.
    System.out.print("Enter first number: ");
    double num_one = scanner.nextDouble();

    System.out.print("Enter second number: ");
    double num_two = scanner.nextDouble();

    System.out.print("Enter third number: ");
    double num_three = scanner.nextDouble();

    // Consume the leftover newline
    scanner.nextLine();

    // 3. Calculate the sum of the three numbers.
    double sum = num_one + num_two + num_three;

    // 4. Calculate the average by dividing the sum by 3.
    double average = sum / 3.0;

    // 5. Display both the sum and the average
    System.out.printf("Sum: %.2f\n", sum);
    System.out.printf("Average: %.2f\n", average);
  }

  /*
   * Java program that prompts the user to input their first and last name separately
   * Then displays their initials.
   */
  public static void initialsExtractor() {
    System.out.println("\nExercise 3: Initials Extractor");

    // 2. Use a Scanner to prompt the user to enter their first name
    System.out.print("Enter your first name: ");
    String firstName = scanner.nextLine();

    // 3. Prompt the user to enter their last name.
    System.out.print("Enter your last name: ");
    String lastName = scanner.nextLine();

    // 4. Store the first character of each name in separate variables.
    char firstInitial = Character.toUpperCase(firstName.charAt(0));
    char lastInitial = Character.toUpperCase(lastName.charAt(0));

    // 5. Display the initials by printing both characters together.
    System.out.println("Your initials are " + firstInitial + lastInitial);
  }
}
