package github.markvn2;

public class Viewer implements Subscriber {
    private String name;
    public Viewer(String name) {
        this.name = name;
    }

    @Override
    public void stationUpdated(String station) {
        System.out.println( name +" recieved update on " + station);
    }
}

