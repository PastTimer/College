
using System;

namespace midterm4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter P: ");
            float p = Convert.ToSingle(Console.ReadLine());
            Console.Write("Enter R: ");
            float r = Convert.ToSingle(Console.ReadLine());
            Console.Write("Enter T: ");
            float t = Convert.ToSingle(Console.ReadLine());

            float si = (p * r * t) / 100;
            Console.WriteLine("The result is: " + si);
        }
    }
}
