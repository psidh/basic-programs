import java.util.Scanner;

public class Marks {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter marks in Maths: ");
    float maths = sc.nextFloat();

    System.out.print("Enter marks in Science: ");
    float science = sc.nextFloat();

    System.out.print("Enter marks in English: ");
    float english = sc.nextFloat();

    float total = maths + science + english;
    float average = total / 3;
    float percentage = (total / 300) * 100;

    System.out.println("Total marks: " + total);
    System.out.println("Average marks: " + average);
    System.out.println("Percentage: " + percentage);
  }
}
