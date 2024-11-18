public class SingletonClass {
    private static SingletonClass instance;
    public int value;
    private SingletonClass(int val){
        this.value = val;
    }
    public static SingletonClass getInstance(int val){
        if (instance == null) {
            instance = new SingletonClass(val);
        }
        return instance;
    }
    public void incrementValue(int val){
        value += val;
    }
    public void showValue(){
        System.out.println("Singleton value: "+value);
    }

}
