package git.markvn2.models;

public class Game {
    private GameSpecifics specs;
    private int quantity;
    public Game(float price, GameSpecifics specs, int quantity) {
        this.specs = specs;
        this.quantity = quantity;
    }
    @Override
    public String toString(){
        return specs.getName();
    }
    public GameSpecifics getSpecs() {
        return specs;
    }
    public void setSpecs(GameSpecifics specs) {
        this.specs = specs;
    }
    public int getQuantity() {
        return quantity;
    }
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public float totalPrice(){
        return quantity * specs.getPrice();
    }
}
