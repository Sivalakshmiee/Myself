//method overloading - two methods in a  class with the same name but different parameters
//access modifiers - private, protected and public. Private is default if no access modifier specified.

class Calc {
    public int add(int n1, int n2, int n3) {
        return n1 + n2 + n3;
    }

    public int add(int n1, int n2) {
        return n1 + n2;
    }
}

public class Calculator {
    public static void main(String[] args) {
        Calc obj = new Calc();

        int r1 = obj.add(8, 5);

        System.out.println(r1);

    }
}
