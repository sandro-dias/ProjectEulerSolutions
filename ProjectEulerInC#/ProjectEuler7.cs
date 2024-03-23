namespace ProjectEulerInC_
{
    public static class ProjectEuler7
    {
        /*
         * Criar um método para dividir um número pelos primos anteriores, validando se tem resto
         * Criar um contador para contar os números que são divididos por 1 e ele mesmo sem resto
         * Parar quando atingir 10001
         * 
         * 23.03: A depender da forma como se busca o número, pode demorar uma eternidade ou alguns segundos.
         * Duas melhorias de performance foram: incrementar de 2 em 2 e colocar como limite máximo a raiz do candidato a primo
         * */

        public static List<int> PrimeNumbers = [1];

        public static void Main()
        {
            IsPrimeNumber();
            Console.WriteLine(PrimeNumbers[10000]);
        }

        public static void IsPrimeNumber()
        {
            PrimeNumbers[0] = 2;
            var number = 3;
            var counting = 1;

            for (var count = 1; count <= 10000; count++) 
            {
                PrimeNumbers.Add(0);
            }

            while (counting <= 10000)
            {
                foreach (var primeNumber in PrimeNumbers)
                {
                    if (primeNumber == 0 || Math.Sqrt(number) < primeNumber)
                    {
                        PrimeNumbers[counting] = number;
                        counting++;
                        number += 2;
                        break;
                    }

                    var rest = number % primeNumber;
                    if (rest == 0 )
                    {
                        number += 2;
                        break;
                    }
                }
            }
        }
    }
}
