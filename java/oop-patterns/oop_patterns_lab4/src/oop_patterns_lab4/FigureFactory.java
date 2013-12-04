package oop_patterns_lab4;

import java.util.ArrayList;

public class FigureFactory {
    ArrayList<Figure> figures = new ArrayList<>();
    
    public void addFigure(String name, byte [] data) {
        for (Figure f : figures) {
            if (f.name.equals(name)) {
                return;
            }
        }
        
        figures.add(new Figure(name, data));
    }
    
    public Figure getFigure(String name) {
        for (Figure f : figures) {
            if (f.name.equals(name)) {
                return f;
            }
        }
        return null;
    }
}
