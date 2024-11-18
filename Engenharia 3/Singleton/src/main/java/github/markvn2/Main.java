class Singleton {
    public static void main (String[] args){
        System.out.println("Instancing one with value 5, and adding 5 :");
        SingletonClass sing1 = SingletonClass.getInstance(5);
        sing1.showValue();
        sing1.addValue(5);
        sing1.showValue();

        System.out.println("\n another with value 3600, and adding 5, and decreasing by 1000:");
        SingletonClass sing2 = SingletonClass.getInstance(3600);
        sing2.showValue();
        sing2.addValue(5);
        sing2.showValue();
        sing2.decreaseValue(1000);
        sing2.showValue();

    }
}