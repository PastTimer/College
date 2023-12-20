using System;

namespace OOP1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter number: ");
            int x = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter number: ");
            int y = Convert.ToInt32(Console.ReadLine());

            int addi = x + y;
            Console.WriteLine("Sum: " + addi);
            int subt = x - y;
            Console.WriteLine("Difference: " + subt);
            int mult = x * y;
            Console.WriteLine("Product: " + mult);
            int divi = x / y;
            Console.WriteLine("Quotient: " + divi);
            Console.ReadKey();
        }
    }
}
