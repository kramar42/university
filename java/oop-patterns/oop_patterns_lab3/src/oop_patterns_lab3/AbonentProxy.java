package oop_patterns_lab3;
import java.util.Scanner;

class AbonentProxy {
    private Abonent abonent;
    
    public void setAbonent(Abonent a) {
        abonent = a;
    }
    
    public void changeTariff() {
        System.out.println("Please, enter your PUK-code: ");
        Scanner in = new Scanner(System.in);
        int PUKcode = in.nextInt();
        
        if (!abonent.hasPUKcode(PUKcode)) {
            System.out.println("Wrong PUK-code");
            return;
        }
        
        abonent.printTariffs();
        System.out.println("Choose tariff: ");
        String tariff = in.next();
        
        abonent.setTariff(tariff);
    }
}
