package oop_patterns_lab3;

import java.util.ArrayList;
import java.util.List;

class Operator {
    private String name;
    private List<Tariff> tariffs = new ArrayList<>();
    private List<Abonent> abonents = new ArrayList<>();
    private Tariff defaultTariff;
    
    Operator(String n) {
        name = n;
    }
    
    public void setDefaultTariff(Tariff d) {
        if (defaultTariff != null) {
            tariffs.remove(defaultTariff);
        }
        defaultTariff = d;
        tariffs.add(defaultTariff);
    }
    
    public void printTarrifs() {
        System.out.println("[" + name + "] tariffs:");
        for (Tariff tarrif : tariffs) {
            System.out.println(tarrif);
        }
    }
    
    public void printAbonents() {
        for (Abonent abonent : abonents) {
            System.out.println(abonent);
        }
    }
    
    public void addAbonent(Abonent abonent) {
        abonents.add(abonent);
        abonent.setOperator(this);
        abonent.setTariff(defaultTariff);
    }
    
    public Abonent getAbonent(String number) {
        for (Abonent abonent : abonents) {
            if (abonent.hasNumber(number)) {
                return abonent;
            }
        }
        
        return null;
    }
    
    public void addTariff(Tariff tariff) {
        tariffs.add(tariff);
    }
    
    public Tariff getTariff(String name) {
        for (Tariff t : tariffs) {
            if (t.getName().equals(name)) {
                return t;
            }
        }
        
        return null;
    }
    
    @Override
    public String toString() {
        String str = "Operator:\n";
        str = str.concat("\tName: " + name + "\n");
        str = str.concat("\tNumber of tariffs: " + tariffs.size() + "\n");
        str = str.concat("\tNumber of abonents: " + abonents.size() + "\n");
        
        return str;
    }
}
