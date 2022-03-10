import java.util StringTokonizer;
class Name
{
public static void main(String args[])
{
StringTokenizer St = new StringTokenizer("My name is Achal "," ");
while(St.hasMoreTokens())
{
System.out.println(St.nextToken());
}
}
}