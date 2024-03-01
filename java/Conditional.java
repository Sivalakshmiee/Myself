public class Conditional {
    public static void main(String[] args) {

        int x = 10;
        int y = 13;
        int z = 17;

        if (x > y && x <= z) {
            System.out.println(x);
        } else if (y > x && y > z) {
            System.out.println(y);
        } else {
            System.out.println(z);
        }

    }
}
