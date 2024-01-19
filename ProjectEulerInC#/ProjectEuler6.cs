public static class ProjectEuler6
{
    public static void Main()
    {
        var sumOfTheSquares = CalculateSumOfTheSquares();
        var squareofTheSums = CalculateSquareOfTheSum();
        var difference = squareofTheSums - sumOfTheSquares;
        Console.WriteLine($"{difference}");
    }


    private static int CalculateSumOfTheSquares()
    {
        var sum = 0;
        for (int i = 1; i <= 100; i++)
        {
            sum += i * i;
        }
        return sum;
    }

    private static int CalculateSquareOfTheSum()
    {
        var sum = 0;
        for (int i = 1; i <= 100; i++)
        {
            sum += i;
        }

        sum *= sum;
        return sum;
    }
}