package git.markvn2.models;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class GameStop {

    private List<Game> games;

    public GameStop(){
        games = new ArrayList<Game>();
    }

    public void AddGame(Game game){
        games.add(game);
    }
    public List<Game> getGames(){
        return  games;
    }
    public List<Game> getGamesByAuthor(String author){
        List<Game> authorgames = new ArrayList<>();
        for (Game games:games){
            if(Objects.equals(games.getSpecs().getAuthor(), author)){
                authorgames.add(games);
            }
        }
        return authorgames;
    }
    public List<Game> getGamesByPrice(float price){
        List<Game> samepricedgames = new ArrayList<>();
        for (Game games:games){
            if(games.getSpecs().getPrice() == price){
                samepricedgames.add(games);
            }
        }
        return samepricedgames;
    }

}
