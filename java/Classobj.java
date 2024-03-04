class Calculator {
    int a;

    public int add(int n1, int n2) {

        int e = n1 + n2;
        System.out.println("in add");
        return e;
    }
}

public class Classobj {
    public static void main(String[] args) {
        int num1 = 4;
        int num2 = 5;

        Calculator calc = new Calculator(); // object

        int res = calc.add(num1, num2);

        System.out.println(res);
    }

}

// JDk - java development kit - to convert into byte code
// jvm = java virtual machine
// JRE = java runtime environment