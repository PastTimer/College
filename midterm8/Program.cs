using System;

namespace midterm8
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter number: ");
            int num = Convert.ToInt32(Console.ReadLine());

            if (num == 0 )
            {
                Console.WriteLine("The number " + num + " is zero.");
            }
            else if (num > 0 ) 
            {
                Console.WriteLine("The number " + num + " is positive.");
            }
            else if (num < 0)
            {
                Console.WriteLine("The number " + num + " is negative.");
            }
        }
    }
}
