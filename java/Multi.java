//multi-dimensional array

public class Multi {
    public static void main(Str[] args) {

        int nums[][] = new int[3][4];
        // int random = 0;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 4; j++) {
                nums[i][j] = (int) (Math.random() * 10);
            }
        }

        for (int i = 0; i < 3; i++) {

            for (int j = 0; j < 4; j++) {

                System.out.println(nums[i][j] + "");
            }
            System.out.println();
        }

    }

}
