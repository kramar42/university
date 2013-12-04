package oop_patterns_lab6;

//=========================================
abstract class InsideToy {
    abstract void workWithToy(Toy toy);
}
class InsideForBoys extends InsideToy {
    @Override
    void workWithToy(Toy toy) {
        toy.setInside("Car");
    } 
}
class InsideForGirls extends InsideToy {
    @Override
    void workWithToy(Toy toy) {
        toy.setInside("Doll");
    } 
}
//=========================================
abstract class PackToy {
    abstract void workWithToy(Toy toy);
}
class PackForBoy extends PackToy {
    @Override
    void workWithToy(Toy toy) {
        toy.setPack("Red");
    }
}
class PackForGirl extends PackToy {
    @Override
    void workWithToy(Toy toy) {
        toy.setPack("Blue");
    }
}
//=========================================


class Toy {
    protected String _inside;
    protected String _pack;

    public void setInside(String inside) {
        _inside = inside;
    }
    public void setPack(String pack) {
        _pack = pack;
    }    
    
    public void print() {
        System.out.println("Toy with " + _inside + " and with " + _pack + " pack");
    }
}

class ToyCreator {
    public InsideToy insideToy;
    public PackToy packToy;
    
    ToyCreator(ToyFactory factory) {
        insideToy = factory.createInsideToy();
        packToy = factory.createPackToy();
    }
    
    public void workWithToy(Toy toy) {
        insideToy.workWithToy(toy);
        packToy.workWithToy(toy);
    }
}