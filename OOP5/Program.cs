using System;

namespace OOP5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double debt, rate, time;
            Console.Write("Enter principal: ");
            debt = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter interest rate: ");
            rate = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter year/s: ");
            time = Convert.ToDouble(Console.ReadLine());

            double x = (debt * rate * time)/100;
            Console.WriteLine("Interest is: " + x);
            Console.ReadKey();
        }
    }
}
