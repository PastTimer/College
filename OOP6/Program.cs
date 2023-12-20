using System;
using System.Diagnostics.Eventing.Reader;

namespace OOP6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter number: ");
            int num = Convert.ToInt32(Console.ReadLine());

            if (num % 2 == 0) {Console.WriteLine(num + " is even");}
            else if (num % 2 >= 1) {Console.WriteLine(num + " is odd");}
            else {Console.WriteLine("A irrational number has been entered");}

            Console.ReadKey();
        }
    }
}
