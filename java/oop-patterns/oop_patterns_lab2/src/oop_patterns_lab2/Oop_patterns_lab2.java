package oop_patterns_lab2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

/* Abstract class with fields in it */
class Vacancy {
    String name;
    String company;
    int category;
    String region;
    
    Vacancy(String name, String company, int category,
            String region) {
        this.name = name;
        this.company = company;
        this.category = category;
        this.region = region;
    }
    
    @Override
    public String toString() {
        String str = "";
        str = str.concat("Name: " + this.name + "\n");
        str = str.concat("Company: " + this.company + "\n");
        str = str.concat("Category: " + this.category + "\n");
        str = str.concat("Region: " + this.region + "\n");
        return str;
    }
}


class Vacancies implements Iterable {
    private List<Vacancy> vacancies = new ArrayList<>();
    
    public void add(Vacancy vacancy) {
        this.vacancies.add(vacancy);
    }
    public void remove(Vacancy vacancy) {
        this.vacancies.remove(vacancy);
    }
    
    public void sortByCompany() {
        Collections.sort(this.vacancies, new byCompany());
    }
    
    public void sortByName() {
        Collections.sort(this.vacancies, new byName());
    }
    
    public void sortByCategory() {
        Collections.sort(this.vacancies, new byCategory());
    }
    
    public void sortByRegion() {
        Collections.sort(this.vacancies, new byRegion());
    }

    @Override
    public Iterator iterator() {
        return this.vacancies.iterator();
    }
    
    @Override
    public String toString() {
        String str = "";
        for (Object vacancy : this.vacancies) {
            str = str.concat(((Vacancy)vacancy).toString() + "\n");
        }
        
        return str;
    }
}

/* Sorting classes */
class byCompany implements java.util.Comparator {
    @Override
    public int compare(Object a, Object b) {
        return ((Vacancy)a).company.compareTo(((Vacancy)b).company);
    }
}

class byName implements java.util.Comparator {
    @Override
    public int compare(Object a, Object b) {
        return ((Vacancy)a).name.compareTo(((Vacancy)b).name);
    }
}

class byCategory implements java.util.Comparator {
    @Override
    public int compare(Object a, Object b) {
        return ((Vacancy)b).category - ((Vacancy)a).category;
    }
}

class byRegion implements java.util.Comparator {
    @Override
    public int compare(Object a, Object b) {
        return ((Vacancy)a).region.compareTo(((Vacancy)b).region);
    }
}

/* Abstract implementation */
abstract class PrintVacancy {
    abstract void print(Vacancies vacancies);
    abstract void printByName(Vacancies vacancies);
    abstract void printByCompany(Vacancies vacancies);
    abstract void printByCategory(Vacancies vacancies);
    abstract void printByRegion(Vacancies vacancies);
}

class SimplePrintVacancy extends PrintVacancy {

    @Override
    public void print(Vacancies vacancies) {
        System.out.println(vacancies);
    }

    @Override
    public void printByName(Vacancies vacancies) {
        vacancies.sortByName();
        System.out.println(vacancies);
    }

    @Override
    public void printByCompany(Vacancies vacancies) {
        vacancies.sortByCompany();
        System.out.println(vacancies);
    }

    @Override
    public void printByCategory(Vacancies vacancies) {
        vacancies.sortByCategory();
        System.out.println(vacancies);
    }

    @Override
    public void printByRegion(Vacancies vacancies) {
        vacancies.sortByRegion();
        System.out.println(vacancies);
    }
}


class AdvancedPrintVacancy extends PrintVacancy {

    @Override
    void print(Vacancies vacancies) {
        System.out.println("Some another realization");
    }

    @Override
    void printByName(Vacancies vacancies) {
        System.out.println("Some another realization");
    }

    @Override
    void printByCompany(Vacancies vacancies) {
        System.out.println("Some another realization");
    }

    @Override
    void printByCategory(Vacancies vacancies) {
        System.out.println("Some another realization");
    }

    @Override
    void printByRegion(Vacancies vacancies) {
        System.out.println("Some another realization");
    }
    
}

class VacancyBank {
    private Vacancies vacancies = new Vacancies();
    PrintVacancy realization;
    
    public void addVacancy(Vacancy vacancy) {
        this.vacancies.add(vacancy);
    }
    
    public void print() {
        this.realization.print(vacancies);
    }
    public void printByName() {
        this.realization.printByName(this.vacancies);
    }
    public void printByCompany() {
        this.realization.printByCompany(this.vacancies);
    }
    public void printByRegion() {
        this.realization.printByRegion(this.vacancies);
    }
    public void printByCategory() {
        this.realization.printByCategory(this.vacancies);
    }
}

public class Oop_patterns_lab2 {
    public static void main(String[] args) {
        VacancyBank bank = new VacancyBank();
        bank.addVacancy(new Vacancy("Programmer", "Google", 10, "UA"));
        bank.addVacancy(new Vacancy("Sys admin", "Google", 7, "UK"));
        bank.addVacancy(new Vacancy("Programmer", "Yandex", 7, "FR"));
        bank.addVacancy(new Vacancy("Chief", "Yandex", 8, "UA"));
        
        
        bank.realization = new SimplePrintVacancy();
        bank.printByCompany();
        bank.printByName();
        bank.printByCategory();
        
        bank.realization = new AdvancedPrintVacancy();
        bank.print();
        bank.printByName();
    }
}
