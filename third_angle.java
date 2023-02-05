import java.util.Scanner;
class Test
{
public static void main(String args[])
{
    int a, b, c;
    Scanner op=new Scanner(System.in);

    System.out.print("Enter First angles of triangle: ");
    a=op.nextInt();
    System.out.print("Enter Second angles of triangle: ");
    b=op.nextInt();;


    c = 180 - (a + b);


    System.out.println("Third angle of the triangle = "+c);
}
}
