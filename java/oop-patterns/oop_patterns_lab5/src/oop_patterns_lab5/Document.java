package oop_patterns_lab5;

    abstract class Document {
        protected String _text;
        abstract public void print();
    }

    // concrete document (1)
    class Pass extends Document {
        
        Pass(String name) {
            _text = name;
        }
        
        @Override
        public void print() {
            System.out.println("Pass: " + _text);
        }
    }

    // concrete document (2)
    class Order extends Document {
        
        Order(String name) {
            _text = name;
        }
        
        @Override
        public void print() {
            System.out.println("Order: " + _text);
        }
    }
