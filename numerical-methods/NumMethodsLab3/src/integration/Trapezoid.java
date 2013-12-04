package integration;

public class Trapezoid {


    static double trapz(Function f, double a, double b, int N) {
        double sum = 0;
        for (int k = 1; k < N; k++) {
            sum += f.f(a + k * (b - a) / N);
        }
        sum += (f.f(a) + f.f(b)) / 2;
        return (b - a) / N * sum;
    }

    public static double integrate(Function function, double a, double b, int n) {
        double h = (b - a) / n;
        double result = 0;
        for (double x = a + h; x < b; x += h) {
            result += function.f(x);
        }
        result = h * ((function.f(a) + function.f(b)) / 2 + result);
        return result;
    }
}
