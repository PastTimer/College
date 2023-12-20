using System;

namespace OOP7
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter number: ");
            int num = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter table length: ");
            int p = Convert.ToInt32(Console.ReadLine());
            for (int i = 1; i <= p; i++) 
            {
                Console.WriteLine(num + " x " + i + " = " + num * i);
            }
            Console.ReadLine();
        }
    }
}
