package oop_patterns_lab4;

public class Desk {
    FigureFactory factory = new FigureFactory();
    
    public void addFigure(String name, byte [] data) {
        factory.addFigure(name, data);
    }
    
    public String getFigureForPrint(String name) {
        return factory.getFigure(name).name;
    }
    
    public void printFigure(String n, int x, int y) {
        factory.getFigure(n).printFigure(x, y);
    }
}
