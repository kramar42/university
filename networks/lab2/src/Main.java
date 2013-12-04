import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
        int n, m;

        File dir = new File("");
        Scanner scanner = new Scanner(new File(dir.getAbsolutePath() + File.separator + "data.txt"));

        n = scanner.nextInt();
        m = scanner.nextInt();

        double[] times = getTime(scanner, n);
        Graph graph = new Graph(getProbabilityMatrix(scanner, n, m), times);

        int steps = graph.runGraphForLastNode();
        int time = graph.getTime();

        System.out.println("STEPS = " + steps + "\nTIME = " + time);
    }

    public static double[] getTime(Scanner scanner, int n)
    {
        double[] time = new double[n];
        double p;

        for (int i = 0; i < n; ++i)
        {
            p = scanner.nextDouble();
            time[i] = p;
        }
        return time;
    }

    public static double[][] getProbabilityMatrix(Scanner scanner, int n, int m)
    {
        double[][] matrix = new double[n][n];

        int x, y;
        double p;

        for (int i = 0; i < m; ++i)
        {
            x = scanner.nextInt();
            y = scanner.nextInt();
            p = scanner.nextDouble();
            matrix[x - 1][y - 1] = p;
        }
        return setDiagonalProbabilityMatrix(matrix);
    }

    private static double[][] setDiagonalProbabilityMatrix(double[][] matrix)
    {
        int n = matrix.length;
        double sum;
        for(int i = 0; i < n; ++i)
        {
            sum = 0;
            for(int j = 0; j < n; ++j)
            {
                if(j != i)
                    sum += matrix[i][j];
            }
            matrix[i][i] = 1 - sum;
        }
        return matrix;
    }
}
