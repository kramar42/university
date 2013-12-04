package ua.kpi.nm.lab4;

import javafx.util.Pair;

import java.util.ArrayList;
import java.util.List;

public class Khoin {
    private final FunctionXy f;
    private final double x0;
    private final double y0;

    public Khoin(FunctionXy f, double x0, double y0) {
        this.f = f;
        this.x0 = x0;
        this.y0 = y0;
    }

    public List<Pair<Double, Double>> valuesAt(double right, int steps) {
        double h = (right - x0) / steps;
        double xi = x0;
        double yi = y0;
        List<Pair<Double, Double>> result = new ArrayList<>(steps);
        result.add(new Pair<>(xi, yi));
        while (xi < right + h / 8) {
            xi += h;
            yi = yi + h / 2 * (f.f(xi, yi) + f.f(xi + h, yi + h * f.f(xi, yi)));
            result.add(new Pair<>(xi, yi));
        }
        return result;
    }
}
