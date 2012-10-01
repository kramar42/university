package oop_patterns_lab5;

public class Oop_patterns_lab5 {
    
    enum Company {Google, Yandex, MailRu};
    
    public static void main(String[] args) {
        Company myCompany = Company.MailRu;
        Creator factory = null;
        
        switch (myCompany) {
            case Google:
                factory = new PassCreator("Google");
                factory.setType("permanent");
                break;
            case Yandex:
                factory = new PassCreator("Yandex");
                factory.setType("temporary");
                break;
            case MailRu:
                factory = new OrderCreator("Mail.ru");
                factory.setType("input");
                break;
            default:
                System.out.println("Wrong Company Type.");
                break;
        }
        
        Document document = factory.createDocument();
        document.print();
    }
}