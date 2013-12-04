package oop_patterns_lab1;

import java.util.ArrayList;
import java.util.List;

/* Main Doctor class */

interface IHealing {
    void Operation();
}

abstract class Doctor implements IHealing {
    protected void WashHands() {
        System.out.println("Hands have been washed");
    }
    
    protected void Diagnostic() {
        System.out.println("Doctor is diagnosting you");
    }
    
    @Override
    public void Operation() {
        this.WashHands();
        this.Diagnostic();
        System.out.println("Operation has been done");
    }
}

/* Abstract decorator that just have doctor in it */
abstract class Decorator extends Doctor {
    protected Doctor doctor;
    
    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }
}

/* Some implementation of decorator 
 * With overrided method
 */
class Stomatologist extends Decorator {
    protected void removeTooth() {
        System.out.println("Tooth has been removed");
    }
    
    @Override
    public void Operation() {
        super.Operation();
        removeTooth();
    }
}

/* Another decorator */
class Surgeon extends Decorator {
    protected void removeArm() {
        System.out.println("Arm has been removed");
    }
    
    @Override
    public void Operation() {
        super.Operation();
        removeArm();
    }
}

/* Last decorator */
class Podiatrist extends Decorator {
    protected void removeToy() {
        System.out.println("Toy has been removed");
    }
    
    @Override
    public void Operation() {
        super.Operation();
        removeToy();
    }
}

class ConcreteDoctorA extends Doctor {
    @Override
    public void Operation() {
        System.out.println("ConcreteDoctorA");
    }
}

class ConcreteDoctorB extends Doctor {
    @Override
    public void Operation() {
        System.out.println("ConcreteDoctorB");
    }
}

/* Class that has Doctors in it
 * Also it overrides method from Doctor's class
 */
class CompositeDoctor extends Doctor {
    protected List<Doctor> doctors = new ArrayList<>();
    
    public void add(Doctor doctor) {
        doctors.add(doctor);
    }
    
    public void remove(Doctor doctor) {
        doctors.remove(doctor);
    }
    
    @Override
    public void Operation() {
        for (Doctor doctor : doctors) {
            doctor.Operation();
        }
    }
}

public class Oop_patterns_lab1 {
    public static void main(String[] args) {
        /*
        Doctor doctor = new Doctor();
        
        Stomatologist st = new Stomatologist();
        st.setDoctor(doctor);
        
        Surgeon sr = new Surgeon();
        sr.setDoctor(doctor);
        
        Podiatrist pd = new Podiatrist();
        pd.setDoctor(doctor);
        */
        ConcreteDoctorA st = new ConcreteDoctorA();
        ConcreteDoctorB sr = new ConcreteDoctorB();
        
        CompositeDoctor cd = new CompositeDoctor();
        cd.add(st);
        cd.add(sr);
        
        cd.Operation();
    }
}
