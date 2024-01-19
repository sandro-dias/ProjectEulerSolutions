public class SumSquareDifference
{
    static void Main(string[] args)
    {
        var sumOfTheSquares = CalculateSumOfTheSquares();
        var squareofTheSums = CalculateSquareOfTheSum();
        var difference = squareofTheSums - sumOfTheSquares;
        Console.WriteLine($"{difference}");
    }


    private int CalculateSumOfTheSquares()
    {
        var sum;
        for (int i = 1; i <= 100; i++)
        {
            sum = sum + i * i;
        }
        return sum;
    }

    private int CalculateSquareOfTheSum()
    {
        var sum;
        for (int i = 1; int <= 100; i++)
        {
            sum = sum + i;
        }

        sum = sum * sum;
        return sum;
    }
}