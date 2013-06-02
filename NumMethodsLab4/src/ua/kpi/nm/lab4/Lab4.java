package ua.kpi.nm.lab4;

import javafx.util.Pair;

/**
 * Laboratory work #4 main task.
 */
public class Lab4 {
    public static void main(String []args) {
        FunctionXy function = new FunctionXy() {
            @Override
            public double f(double x, double y) {
                return 2 * y - x * x;
            }
        };

        // TODO: some output
        for (Pair<Double, Double> p : new KuttaMerson(function, 0, 1).valuesAt(2, 100)) {
            System.out.printf("{%f,%f},", p.getKey(), p.getValue());
        }

        for (Pair<Double, Double> p : new Euler(function, 0, 1).valuesAt(2, 100)) {
            System.out.printf("{%f,%f},", p.getKey(), p.getValue());
        };

        for (Pair<Double, Double> p : new Khoin(function, 0, 1).valuesAt(2, 100)) {
            System.out.printf("{%f,%f},", p.getKey(), p.getValue());
        }
    }
}