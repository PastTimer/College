using System;

namespace OOP3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter grade of 1st subject: ");
            double fir = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter grade of 2nd subject: ");
            double sec = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter grade of 3rd subject: ");
            double thi = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter grade of 4th subject: ");
            double fou = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter grade of 5th subject: ");
            double fif = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter grade of 6th subject: ");
            double six = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter grade of 7th subject: ");
            double sev = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter grade of 8th subject: ");
            double eig = Convert.ToDouble(Console.ReadLine());

            double ave = (fir + sec + thi + fou + fif + six + sev + eig) / 8;
            Console.WriteLine("The average is: " + ave);
        }
    }
}
