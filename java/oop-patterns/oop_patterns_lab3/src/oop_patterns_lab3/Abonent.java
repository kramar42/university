package oop_patterns_lab3;

interface IAbonent {
    public void printTariff();
    public void printTariffs();
    
    public void setTariff(String name);
    public void setTariff(Tariff tariff);
    public void setOperator(Operator operator);
    public void setPUKcode(int PUKcode);
    
    public boolean hasNumber(String number);
    public boolean hasPUKcode(int PUKcode);
}

class Abonent implements IAbonent {
    private String number;
    private Tariff tariff;
    private Operator operator;
    private int PUKcode;
    
    Abonent(String number) {
        this.number = number;
    }
    
    @Override
    public void printTariff() {
        System.out.println("[" + number + "] tariff:");
        System.out.println(tariff);
    }

    @Override
    public void setTariff(String name) {
        tariff = operator.getTariff(name);
    }
    
    @Override
    public void setTariff(Tariff tariff) {
        this.tariff = tariff;
    }
    
    @Override
    public void setOperator(Operator operator) {
        this.operator = operator;
    }

    @Override
    public void printTariffs() {
        operator.printTarrifs();
    }   
    
    @Override
    public boolean hasNumber(String number) {
        return this.number.equals(number);
    }
    
    @Override
    public String toString() {
        String str = "Abonent:\n";
        str = str.concat("\tNumber: " + number + "\n");
        str = str.concat("\tTariff: " + tariff + "\n");
        str = str.concat(operator + "\n");
        
        return str;
    }

    @Override
    public boolean hasPUKcode(int PUKcode) {
        return this.PUKcode == PUKcode;
    }

    @Override
    public void setPUKcode(int PUKcode) {
        this.PUKcode = PUKcode;
    }
}