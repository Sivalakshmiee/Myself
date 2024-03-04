public class While {
    public static void main(String[] args) {

        int i = 1;

        while (i < 6) {
            System.out.println("Hi" + i);

            int j = 1;

            while (j < 4) {
                System.out.println("Hello");

                j++;
            }
            i++;
        }
        System.out.println("Bye" + i);
    }
}
