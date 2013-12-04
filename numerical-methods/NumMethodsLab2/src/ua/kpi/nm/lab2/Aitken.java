package ua.kpi.nm.lab2;

import java.util.Arrays;
import java.util.Comparator;

/**
 * Calculates function interpolation using Aitken Scheme.
 */
public class Aitken {
    private Point[] nodePoints;
    private Double[][] polinomValues;

    public Aitken(Point[] nodePoints) {
        this.nodePoints = nodePoints;
        polinomValues = new Double[nodePoints.length][nodePoints.length];
    }

    public double [] valuesAt(double[] xVector) {
        double [] yVector = new double[xVector.length];
        for (int i = 0; i < xVector.length; i++) {
            yVector[i] = valueAt(xVector[i]);
        }
        return yVector;
    }

    private double valueAt(double x) {
        orderNodePoints(x);
        double y = polinom(x, 0, 1);
        double yPrev = polinom(x, 0, 2);
        for (int k = 3; k < nodePoints.length; k++) {
            yPrev = y;
            y = polinom(x, 0, k);
        }
        polinomValues = new Double[nodePoints.length][nodePoints.length];
        return y;
    }

    private void orderNodePoints(final double x) {
        Arrays.sort(nodePoints, new Comparator<Point>() {
            @Override
            public int compare(Point o1, Point o2) {
                return Double.valueOf(Math.abs(o1.x() - x)).compareTo(Math.abs(o2.x() - x));
            }
        });
    }

    private double polinom(double x, int i, int k) {
        if (i == k) {
            polinomValues[i][k] = nodePoints[i].y();
        }
        if (polinomValues[i][k] == null) {
            polinomValues[i][k] = ((x - nodePoints[i].x()) * polinom(x, i + 1, k)
                    - (x - nodePoints[k].x()) * polinom(x, i, k - 1))
                    / (nodePoints[k].x() - nodePoints[i].x());
        }
        return polinomValues[i][k];
    }
}
