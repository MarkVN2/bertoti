class Singleton {
    public static void main (String[] args){
        System.out.println("Instancing a singleton with value 10, and incrementing 5:");
        SingletonClass sing1 = SingletonClass.getInstance(10);
        sing1.showValue();
        sing1.incrementValue(5);
        sing1.showValue();

        System.out.println("\nTrying to instance another singleton with value 2000, and incrementing 5:");
        SingletonClass sing2 = SingletonClass.getInstance(2000);
        sing2.showValue();
        sing2.incrementValue(5);
        sing2.showValue();
    }
}