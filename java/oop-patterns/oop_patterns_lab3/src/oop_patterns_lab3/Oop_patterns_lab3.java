package oop_patterns_lab3;

public class Oop_patterns_lab3 {
    public static void main(String[] args) {
       
       Operator life = new Operator("Life :)");
       life.setDefaultTariff(new Tariff("Default", 25, 2, 1));
       
       life.addTariff(new Tariff("Free", 100, 0, 0));
       life.addTariff(new Tariff("Business", 50, 1.5, 0.5));
       
       Abonent kramar = new Abonent("0935970146");
       kramar.setPUKcode(1234);
       
       life.addAbonent(kramar);
       
       AbonentProxy Proxy = new AbonentProxy();
       Proxy.setAbonent(kramar);
       
       Proxy.changeTariff();
       kramar.printTariff();
    }
}
