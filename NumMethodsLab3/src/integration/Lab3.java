package integration;

public class Lab3 {
    public static void main(String[] args) {
        Function function = new Function() {
            @Override
            public double f(double x) {
                return 1 / (Math.sin(x) * Math.cos(x));
            }
        };
        System.out.println(Trapezoid.integrate(function, 0.5, 1.0, 100));
        System.out.println(Romberg.integrate(function, 0.5, 1.0, 100));
    }
}
