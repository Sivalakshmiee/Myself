class Student {

    int rollno;
    java.lang.String name;
    int marks;

}

public class Foreach {
    public static void main(String[] args) {
        // int nums[] = new int[4];
        // nums[0] = 4;
        // nums[1] = 9;
        // nums[2] = 7;
        // nums[3] = 5;
        // // nums[4] = 6;

        // for (int n : nums) {
        // System.out.println(n);
        // }

        Student s1 = new Student();
        s1.rollno = 1;
        s1.name = "Siva";
        s1.marks = 99;

        Student s2 = new Student();
        s2.rollno = 2;
        s2.name = "park";
        s2.marks = 98;

        Student s3 = new Student();
        s3.rollno = 3;
        s3.name = "Min";
        s3.marks = 97;

        System.out.println(s1.name + " : " + s1.marks);

        Student students[] = new Student[3];
        // array of objects
        students[0] = s1;
        students[1] = s2;
        students[2] = s3;

        // for (int i = 0; i < students.length; i++) {
        // System.out.println(students[i].name + i);

        // }
        for (Student st : students) {
            System.out.println(st.name + " : " + st.marks);
        }
    }
}
