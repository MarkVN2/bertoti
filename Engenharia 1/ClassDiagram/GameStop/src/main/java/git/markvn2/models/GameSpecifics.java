package git.markvn2.models;

import java.util.LinkedList;
import java.util.List;
import java.util.Objects;

public class GameSpecifics {
    private String author;
    private String name;
    private String pgrating;
    private float price;
    private List<String> platforms;

    public GameSpecifics(String author, String name, String pgrating, List<String> platforms) {
        this.author = author;
        this.name = name;
        this.pgrating = pgrating;
        this.platforms = platforms;
    }

    @Override
    public String toString(){
        return String.format(" Name: '%s' \n Author:  '%s' \n PGrating: '%s' \n Platforms : '%s' \n",name,author,pgrating,platforms.toString());
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public float getPrice(){
        return price;
    }
    public void setPrice(float price){
        this.price = price;
    }
    public String getPGrating() {
        return pgrating;
    }

    public void setPGrating(String pgrating) {
        this.pgrating = pgrating;
    }

    public List<String> getPlatforms() {
        return platforms;
    }

    public void setPlatforms(List<String> platforms) {
        this.platforms = platforms;
    }

    public boolean compareWithSelf(GameSpecifics gameSpecifics){
        return Objects.equals(gameSpecifics.pgrating, this.pgrating) && Objects.equals(gameSpecifics.author, this.author) && Objects.equals(gameSpecifics.name, this.name) && Objects.equals(gameSpecifics.platforms, this.platforms);
    }

}
