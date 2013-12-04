package oop_patterns_lab4;

public class Figure {
    String name;
    byte [] data;
    
    Figure(String name, byte data []) {
        this.name = name;
        this.data = data;
    }
    
    public void printFigure(int x, int y) {
        System.out.println("Figure " + name + " was putted on " + x + "." + y);
    }
}