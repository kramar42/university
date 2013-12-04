package oop_patterns_lab4;

import java.util.WeakHashMap;

public class Oop_patterns_lab4 {  
    public static void main(String[] args) {
        Desk chessDesk = new Desk();
        
        chessDesk.addFigure("Pawn", new byte [100000]);
        chessDesk.addFigure("King", new byte [1000000]);
        chessDesk.addFigure("Rook", new byte [100000]);
        chessDesk.addFigure("Queen", new byte [1000000]);
        
        chessDesk.printFigure("Pawn", 1, 1);
        WeakHashMap w;
    }
}
