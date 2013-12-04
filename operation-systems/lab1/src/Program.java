import java.lang.Math;

public class Program
{
    static int n;
    static double l, l1, l2, l3, l4;
    static double[]   B;
    static double[][] S;
    static double[][] P;
    static double[][] P1;
    static double[][] P2;
    static double[][] P3;
    static double[][] P4;
    static double[][] P5;
    static double[][] P6;
    static double[][] P7;
    static double[][] P8;
    static double[][] P9;
    static double[][] P10;
    static double[][] P11;
    static double[][] P12;
    static double[][] P13;
    static double[][] P14;
    static double[][] P15;
    static double[][] P16;

    public static void main(String[] args)
    {
        n = 16;
        l = 2; l1 = 2; l2 = 2; l3 = 3; l4 = 3;
        S = new double[][] {
                {0 ,l4,l3,0 ,l2,0 ,0 ,0 ,l1,0 ,0 ,0 ,0 ,0 ,0 ,0 },
                {l ,0 ,0 ,l3,0 ,l2,0 ,0 ,0 ,l1,0 ,0 ,0 ,0 ,0 ,0 },
                {l ,0 ,0 ,l4,0 ,0 ,l2,0 ,0 ,0 ,l1,0 ,0 ,0 ,0 ,0 },
                {0 ,l ,l ,0 ,0 ,0 ,0 ,l2,0 ,0 ,0 ,l1,0 ,0 ,0 ,0 },
                {l ,0 ,0 ,0 ,0 ,l4,l3,0 ,0 ,0 ,0 ,0 ,l1,0 ,0 ,0 },
                {0 ,l ,0 ,0 ,l ,0 ,0 ,l3,0 ,0 ,0 ,0 ,0 ,l1,0 ,0 },
                {0 ,0 ,l ,0 ,l ,0 ,0 ,l4,0 ,0 ,0 ,0 ,0 ,0 ,l1,0 },
                {0 ,0 ,0 ,l ,0 ,l ,l ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,l1},
                {l ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,l4,l3,0 ,l2,0 ,0 ,0 },
                {0 ,l ,0 ,0 ,0 ,0 ,0 ,0 ,l ,0 ,0 ,l3,0 ,l2,0 ,0 },
                {0 ,0 ,l ,0 ,0 ,0 ,0 ,0 ,l ,0 ,0 ,l4,0 ,0 ,l2,0 },
                {0 ,0 ,0 ,l ,0 ,0 ,0 ,0 ,0 ,l ,l ,0 ,0 ,0 ,0 ,l2},
                {0 ,0 ,0 ,0 ,l ,0 ,0 ,0 ,l ,0 ,0 ,0 ,0 ,0 ,0 ,0 },
                {0 ,0 ,0 ,0 ,0 ,l ,0 ,0 ,0 ,l ,0 ,0 ,0 ,0 ,0 ,0 },
                {0 ,0 ,0 ,0 ,0 ,0 ,l ,0 ,0 ,0 ,l ,0 ,0 ,0 ,0 ,0 },
                {0 ,0 ,0 ,0 ,0 ,0 ,0 ,l ,0 ,0 ,0 ,l ,0 ,0 ,0 ,0 }};

        P = new double[n][n];
        for (int i = 0; i < n - 1; i++)
        {
            double s = 0;
            for (int j = 0; j < n; j++)
            {
                s += S[i][j];
            }
            P[i][i] = -s;
            for (int j = 0; j < n; j++)
            {
                if(i != j)
                    P[i][j] = S[j][i];
            }
        }

        for (int i = 0; i < n; i++)
        {
            P[n - 1][i] = 1;
        }

        B   = new double[] {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1};
        P1  = new double[n][n]; P2  = new double[n][n];
        P3  = new double[n][n]; P4  = new double[n][n];
        P5  = new double[n][n]; P6  = new double[n][n];
        P7  = new double[n][n]; P8  = new double[n][n];
        P9  = new double[n][n]; P10 = new double[n][n];
        P11 = new double[n][n]; P12 = new double[n][n];
        P13 = new double[n][n]; P14 = new double[n][n];
        P15 = new double[n][n]; P16 = new double[n][n];

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                P1[i][j]   = P[i][j];
                P1[i][0]   = B[i];
                P2[i][j]   = P[i][j];
                P2[i][1]   = B[i];
                P3[i][j]   = P[i][j];
                P3[i][2]   = B[i];
                P4[i][j]   = P[i][j];
                P4[i][3]   = B[i];
                P5[i][j]   = P[i][j];
                P5[i][4]   = B[i];
                P6[i][j]   = P[i][j];
                P6[i][5]   = B[i];
                P7[i][j]   = P[i][j];
                P7[i][6]   = B[i];
                P8[i][j]   = P[i][j];
                P8[i][7]   = B[i];
                P9[i][j]   = P[i][j];
                P9[i][8]   = B[i];
                P10[i][j]  = P[i][j];
                P10[i][9]  = B[i];
                P11[i][j]  = P[i][j];
                P11[i][10] = B[i];
                P12[i][j]  = P[i][j];
                P12[i][11] = B[i];
                P13[i][j]  = P[i][j];
                P13[i][12] = B[i];
                P14[i][j]  = P[i][j];
                P14[i][13] = B[i];
                P15[i][j]  = P[i][j];
                P15[i][14] = B[i];
                P16[i][j]  = P[i][j];
                P16[i][15] = B[i];
            }
        }

        double p1, p2, p3, p4, p5, p6, p7, p8;
        double p9, p10, p11, p12, p13, p14, p15, p16;
        double P0 = Determinant(P);

        p1  = Determinant(P1)  / Determinant(P);
        p2  = Determinant(P2)  / Determinant(P);
        p3  = Determinant(P3)  / Determinant(P);
        p4  = Determinant(P4)  / Determinant(P);
        p5  = Determinant(P5)  / Determinant(P);
        p6  = Determinant(P6)  / Determinant(P);
        p7  = Determinant(P7)  / Determinant(P);
        p8  = Determinant(P8)  / Determinant(P);
        p9  = Determinant(P9)  / Determinant(P);
        p10 = Determinant(P10) / Determinant(P);
        p11 = Determinant(P11) / Determinant(P);
        p12 = Determinant(P12) / Determinant(P);
        p13 = Determinant(P13) / Determinant(P);
        p14 = Determinant(P14) / Determinant(P);
        p15 = Determinant(P15) / Determinant(P);
        p16 = Determinant(P16) / Determinant(P);


        for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                System.out.print(S[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("Предельные вероятности состояний:");
        System.out.println("P1:  " + p1);
        System.out.println("P2:  " + p2);
        System.out.println("P3:  " + p3);
        System.out.println("P4:  " + p4);
        System.out.println("P5:  " + p5);
        System.out.println("P6:  " + p6);
        System.out.println("P7:  " + p7);
        System.out.println("P8:  " + p8);
        System.out.println("P9:  " + p9);
        System.out.println("P10: " + p10);
        System.out.println("P11: " + p11);
        System.out.println("P12: " + p12);
        System.out.println("P13: " + p13);
        System.out.println("P14: " + p14);
        System.out.println("P15: " + p15);
        System.out.println("P16: " + p16);
    }

    static private int SignOfElement(int i, int j)
    {
        if ((i + j) % 2 == 0)
        {
            return 1;
        }
        else
        {
            return -1;
        }
    }
    static private double[][] CreateSmallerMatrix(double[][] input, int i, int j)
    {
        int order = (int) Math.sqrt(input.length);
        double[][] output = new double[order - 1][order - 1];
        int x = 0, y;
        for (int m = 0; m < order; m++, x++)
        {
            if (m != i)
            {
                y = 0;
                for (int n = 0; n < order; n++)
                {
                    if (n != j)
                    {
                        output[x][y] = input[m][n];
                        y++;
                    }
                }
            }
            else
            {
                x--;
            }
        }
        return output;
    }

    static private double Determinant(double[][] input)
    {
        long order = (long) Math.sqrt(input.length);
        if (order > 2)
        {
            double value = 0;
            for (int j = 0; j < order; j++)
            {
                double[][] Temp = CreateSmallerMatrix(input, 0, j);
                value = value + input[0][j] * (SignOfElement(0, j) * Determinant(Temp));
            }
            return value;
        }
        else if (order == 2)
        {
            return ((input[0][0] * input[1][1]) - (input[1][0] * input[0][1]));
        }
        else
        {
            return (input[0][0]);
        }
    }
}

