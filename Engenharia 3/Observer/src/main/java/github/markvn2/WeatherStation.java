package github.markvn2;

import java.util.List;

public class WeatherStation {
    private String name;
    private double temp = 0;
    private double pres = 0;
    private List<Subscriber> subcribers;

    public WeatherStation(String name){
        this.name = name;
    }

    public void addSubscriber(Subscriber sub){
        subcribers.add(sub);
    }

    public void notifyObservers(){
        for(Subscriber subscriber : subcribers){
            subscriber.stationUpdated(this.name);
        }
    }  
    
    public void setMeasurements(double temp ,double pres){
        this.temp = temp;
        this.pres = pres;
    }

}

