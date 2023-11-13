package git.markvn2;

import git.markvn2.models.Game;
import git.markvn2.models.GameSpecifics;
import git.markvn2.models.GameStop;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        GameStop gameStop1 = new GameStop();


        GameSpecifics zeldaspec = new GameSpecifics("Nintendo","Zelda:Breath of the Wild","12", new ArrayList<>());
        Game zeldabotw = new Game(10,zeldaspec,20);

        gameStop1.AddGame(zeldabotw);
        System.out.println(gameStop1.getGames());
        System.out.println(zeldaspec.toString());
    }
}