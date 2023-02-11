import java.util.Scanner;

public class Login {
  public static void main(String[] args) {
    // Define the username and password
    String username = "admin";
    String password = "password";

    // Prompt the user to enter their username and password
    Scanner input = new Scanner(System.in);
    System.out.print("Enter your username: ");
    String inputUsername = input.nextLine();
    System.out.print("Enter your password: ");
    String inputPassword = input.nextLine();

    // Check if the entered username and password match the predefined credentials
    if (inputUsername.equals(username) && inputPassword.equals(password)) {
      System.out.println("Login successful!");
    } else {
      System.out.println("Login failed. Incorrect username or password.");
    }
  }
}
