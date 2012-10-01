package oop_patterns_lab5;

// abstract creator
abstract class Creator {        
    abstract public Document createDocument();  
    abstract public void setType(String type);

    protected String _type;
    protected String _name;
}

// concrete creator (1)
class PassCreator extends Creator {
    PassCreator(String name) {
        _name = name;
    }
    
    @Override
    public Document createDocument() {
        System.out.println("Pass-" + _type + " creator");
        return new Pass(_name);
    }

    @Override
    public void setType(String type) {
        _type = type;
    }
}

// concrete creator (2)
class OrderCreator extends Creator {
    
    OrderCreator(String name) {
        _name = name;
    }
    
    @Override
    public Document createDocument() {
        System.out.println("Order-" + _type + " creator");
        return new Order(_name);
    }

    @Override
    public void setType(String type) {
        _type = type;
    }
}