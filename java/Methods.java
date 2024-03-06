class Computer {
    public void playMusic() {
        System.out.println("Music playing");
    }

    public String getMePen(int cost) {
        return "pen";
    }
}

public class Methods {
    public static void main(Str[] args) { // main method
        Computer obj = new Computer();
        obj.playMusic();
        String str = obj.getMePen(10);
        System.out.println(str);

    }

}
