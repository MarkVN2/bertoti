package github.markvn2;

class Main {
    public static void main (String[] args){
        WeatherStation station = new WeatherStation("A");
        Viewer viewer1 = new Viewer("Viewer 1");
        Viewer viewer2 = new Viewer("Viewer 2");
        station.addSubscriber(viewer1);
        station.addSubscriber(viewer2);
        station.setMeasurements(10, 20);
        station.setMeasurements(20, 30);
        station.notifyObservers();

        WeatherStation b = new WeatherStation("B");
        Viewer viewer3 = new Viewer("Viewer 3");
        Viewer viewer4 = new Viewer("Viewer 4");
        b.addSubscriber(viewer3);
        b.addSubscriber(viewer4);
        b.setMeasurements(10, 20);
        b.notifyObservers();
        b.setMeasurements(20, 30);
        b.notifyObservers();

    }
}