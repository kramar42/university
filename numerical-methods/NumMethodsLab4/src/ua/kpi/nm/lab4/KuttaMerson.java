package ua.kpi.nm.lab4;
import javafx.util.Pair;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class KuttaMerson {
    private static final double EPSILON = 0.005;
    private final FunctionXy f;
    private final double y0;
    private final double x0;
    private Double[] kVals;
    private Function3[] k;

    public KuttaMerson(FunctionXy f, double x0, double y0) {
        this.f = f;
        this.x0 = x0;
        this.y0 = y0;
    }

    private double getK(int i, double x, double y, double h) {
        if (kVals[i] == null) {
            kVals[i] = k[i].f(x, y, h);
        }
        return kVals[i];
    }

    public List<Pair<Double, Double>> valuesAt(double right, int steps) {
        final double h = (right - x0) / steps;
        kVals = new Double[5];
        k = new Function3[5];
        k[0] = new Function3() {
            @Override
            public double f(double x, double y, double h) {
                return f.f(x, y);
            }
        };
        k[1] = new

                Function3() {
                    @Override
                    public double f(double x, double y, double h) {
                        return f.f(x + h / 3, y + h / 3 * getK(0, x, y, h));
                    }
                };
        k[2] = new

                Function3() {
                    @Override
                    public double f(double x, double y, double h) {return f.f(x + h / 3, y + h / 6 * getK(0, x, y, h) + h / 6 * getK(1, x, y, h));
                    }
                };
        k[3] = new

                Function3() {

                    @Override
                    public double f(double x, double y, double h) {return f.f(x + h / 2, y + h / 8 * getK(0, x, y, h) + 3 * h / 8 * getK(1, x, y, h));
                    }
                };
        k[4] = new
                Function3() {
                    @Override
                    public double f(double x, double y, double h) { return f.f(x + h, y + h / 2 * getK(0, x, y, h) - 3 * h / 2 * getK(2, x, y, h) + 2 * h * getK(3, x, y, h));
                    }
                };
        double xi = x0;
        double yi = y0;
        double yD;
        double yN;
        double hi;
        List<Pair<Double, Double>> result = new ArrayList<>(steps);
        while (xi < right + h / 8) {
            hi = h;
            do {
                yD = yi + hi / 2 * (getK(0, xi, yi, hi) - 3 * getK(2, xi, yi, hi) + 4 * getK(3, xi, yi, hi));
                yN = yi + hi / 6 * (getK(0, xi, yi, hi) + 4 * getK(3, xi, yi, hi) + getK(4, xi, xi, hi));
                Arrays.fill(kVals, null);
                hi /= 2;
            } while (0.2 * Math.abs(yi - yD) > EPSILON);
            result.add(new Pair<>(xi, yi));
            xi += hi;
            yi = yN;
        }
        return result;
    }
}
