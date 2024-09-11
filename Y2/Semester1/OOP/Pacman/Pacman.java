package Y2.Semester1.OOP.Pacman;

public class Pacman {

  // Define ANSI escape codes for True Color using RGB values
  public static final String ANSI_RESET = "\033[0m";

  // Ghosts' colors (RGB)
  public static final String PINK = "\033[38;2;234;130;229m"; // Pink
  public static final String LIGHT_BLUE = "\033[38;2;70;191;238m"; // Light blue
  public static final String RED = "\033[38;2;255;62;25m"; // Red
  public static final String ORANGE = "\033[38;2;219;133;28m"; // Orange

  // Pacman and Walls' colors (RGB)
  public static final String YELLOW = "\033[38;2;253;255;0m"; // Yellow
  public static final String BLUE = "\033[38;2;33;33;222m"; // Blue

  public static void main(String[] args) {
    // Example usage of the defined colors
    System.out.println(PINK + "This is pink (Ghost : ᑎ)." + ANSI_RESET);
    System.out.println(
      LIGHT_BLUE + "This is light blue (Ghost : ᑎ)." + ANSI_RESET
    );
    System.out.println(RED + "This is red (Ghost : ᑎ)." + ANSI_RESET);
    System.out.println(ORANGE + "This is orange (Ghost : ᑎ)." + ANSI_RESET);
    System.out.println(
      YELLOW + "This is yellow (Pacman : ᗤ, ᗣ, ᗧ, ᗨ)." + ANSI_RESET
    );
    System.out.println(BLUE + "This is blue (Walls : □)." + ANSI_RESET);
    System.out.println("This is food : •••");
    System.err.println("These are the cherries and pills : 🍒 💊");
  }
}
