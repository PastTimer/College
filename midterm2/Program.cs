using System;
using System.Runtime.ExceptionServices;

namespace midterm
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter first number: ");
            float num1 = Convert.ToSingle(Console.ReadLine());
            Console.Write("Enter second number: ");
            float num2 = Convert.ToSingle(Console.ReadLine());

            float product = num1 * num2;
            Console.WriteLine("The product is " + product);
            Console.ReadKey();
        }
    }
}
