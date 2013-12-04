
package integration;

import static java.lang.Math.abs;
import static java.lang.Math.pow;

public class Romberg {

    public static double integrate(Function f, double a, double b, int max) {
        max += 1;
        double[] s = new double[max];
        double var = 0;
        double lastVal = Double.NEGATIVE_INFINITY;
        for (int k = 1; k < max; k++) {
            for (int i = 1; i <= k; i++) {
                if (i == 1) {
                    var = s[i];
                    s[i] = Trapezoid.trapz(f, a, b, (int) pow(2, k - 1));
                } else {
                    s[k] = (pow(4, i - 1) * s[i - 1] - var) / (pow(4, i - 1) - 1);
                    var = s[i];
                    s[i] = s[k];
                }
            }
            if (abs(lastVal - s[k]) < 1e-9) {
                return s[k];
            } else {
                lastVal = s[k];
            }
        }
        return s[max - 1];
    }
}