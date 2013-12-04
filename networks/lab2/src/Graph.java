public class Graph {

    private double[][] matrix;
    private double[] probability;
    private final int N;
    private final int STEP = 1;
    private final double e = 0.00001;
    private int k;
    private double t;
    private double[] times;

    public Graph(final double[][] matrix) {
        this.matrix = matrix;
        N = matrix.length;
        probability = new double[N];
        probability[0] = 1;
    }

    public Graph(final double[][] matrix, final double[] times) {
        this(matrix);
        this.times = times;
    }

    public double[] getProbability(int t)
    {
        double[] newprobability = new double[N];
        double s;
        for (int k = 0; k < t; ++k)
        {
            for(int i = 0; i < N; ++i)
            {
                s = 0;
                for(int j = 0; j < N; ++j)
                {
                    s += probability[j] * matrix[j][i];
                }
                newprobability[i] = s;
            }
            probability = newprobability.clone();
        }
        return probability.clone();
    }

    public int runGraphForLastNode()
    {
        for(k = 0; 1 - getProbability(STEP)[N - 1] > e; ++k)
        {
            for(int i = 0; i < N; ++i)
                t += probability[i] * times[i];
        }
        return k;
    }

    public int getTime()
    {
        return (int)t;
    }
}
