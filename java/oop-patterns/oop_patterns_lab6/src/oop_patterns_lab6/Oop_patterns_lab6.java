package oop_patterns_lab6;

public class Oop_patterns_lab6 {
    
    public static void main(String[] args) {
        Toy toy = new Toy();
        
        ToyFactory factory = Snegurochka.getInstance();
        
        ToyCreator creator = new ToyCreator(factory);
        creator.workWithToy(toy);
        toy.print();
    }
}
