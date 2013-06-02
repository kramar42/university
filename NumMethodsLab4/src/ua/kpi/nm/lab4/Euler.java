package ua.kpi.nm.lab4;

import javafx.util.Pair;

import java.util.ArrayList;
import java.util.List;

public class Euler {
    private final FunctionXy f;
    private final double y0;
    private final double x0;

    public Euler(FunctionXy f, double x0, double y0) {
        this.f = f;
        this.x0 = x0;
        this.y0 = y0;
    }

    public List<Pair<Double, Double>> valuesAt(double right, int steps) {
        List<Pair<Double, Double>> result = new ArrayList<>(steps);
        final double h = (right - x0) / steps;
        double xi = x0;
        double yi = y0;
        while (xi < right + h / 8) {
            result.add(new Pair<>(xi, yi));
            yi += h * f.f(xi, yi);
            xi += h;
        }
        return result;
    }
}
