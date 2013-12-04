package oop_patterns_lab3;

class Tariff {
    private String name;
    private double price;
    private double pricePerHour;
    private double smsPrice;
    
    Tariff(String n, double p, double h, double s) {
        name = n;
        price = p;
        pricePerHour = h;
        smsPrice = s;
    }
    
    public String getName() {
        return name;
    } 
    
    @Override
    public String toString() {
        String str = "\tName: " + name + "\n";
        str = str.concat("\tPrice: " + price + "\n");
        str = str.concat("\tPrice per hour: " + pricePerHour + "\n");
        str = str.concat("\tSms price: " + smsPrice + "\n");
        
        return str;
    }
}
