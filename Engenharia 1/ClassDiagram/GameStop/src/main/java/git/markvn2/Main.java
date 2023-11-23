package git.markvn2;

import git.markvn2.models.Game;
import git.markvn2.models.GameSpecifics;
import git.markvn2.models.GameStop;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        GameStop gameStop1 = new GameStop();
        ArrayList<String>  zeldaplats = new ArrayList<>();
        zeldaplats.add("Nintendo Switch");

        ArrayList<String> theforestplats = new ArrayList<>();
        theforestplats.add("PC");
        theforestplats.add("PS4");
        theforestplats.add("XBOX");

        GameSpecifics zeldaspec = new GameSpecifics("Nintendo","Zelda:Breath of the Wild","12", zeldaplats );
        GameSpecifics tforestspecs = new GameSpecifics("ENDNIGHT","The Forest", "16", theforestplats);
        Game zeldabotw = new Game(10,zeldaspec,20);
        Game theforest = new Game(10,tforestspecs,1);

        gameStop1.AddGame(zeldabotw);
        gameStop1.AddGame(theforest);
        List<Game> list = gameStop1.getGames();

        System.out.println(list.toString());
        System.out.println();
        System.out.println(zeldaspec.toString());
        System.out.println(tforestspecs.toString());
    }
}