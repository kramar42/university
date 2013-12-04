package oop_patterns_lab6;

class DedMoroz extends ToyFactory {
    @Override
    public InsideToy createInsideToy() {
        return new InsideForBoys();
    }

    @Override
    public PackToy createPackToy() {
        return new PackForBoy();
    }
    
    private DedMoroz(){}
    public static ToyFactory getInstance() {
        if (_this == null) {
            _this = new DedMoroz();
        }
        return _this;
    }
}

class Snegurochka extends ToyFactory {

    @Override
    public InsideToy createInsideToy() {
        return new InsideForGirls();
    }

    @Override
    public PackToy createPackToy() {
        return new PackForGirl();
    }
    
    private Snegurochka(){}
    public static ToyFactory getInstance() {
        if (_this == null) {
            _this = new Snegurochka();
        }
        return _this;
    }
}

abstract class ToyFactory {
    public abstract InsideToy createInsideToy();
    public abstract PackToy createPackToy();
    
    protected static ToyFactory _this;
}