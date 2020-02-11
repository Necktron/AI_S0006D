import pygame;
from pygame.locals import *;

pG = pygame;

class GameLoop():

    gScr = 0;
    cellSize = 40;
    gridSizeX = 0;
    gridSizeY = 0;
    walkedPath = [ ];

    class Algorithms():
        # A Star
        # Breath First
        # ETC
        pass;

    class Maps():
        MAP1 = 'Map1.txt';
        MAP2 = 'Map2.txt';
        MAP3 = 'Map3.txt';

    class Colors():
        BLACK = (0, 0, 0);
        BLUE = (0, 0, 255);
        BROWN = (153, 76, 0);
        CYAN = (0, 255, 255);
        GRAY =(128, 128, 128);
        GREEN = (0, 255, 0);
        LIME_GREEN = (128, 255, 0);
        LIGHT_BLUE = (0, 128, 255);
        MAGENTA = (255, 0, 255);
        ORANGE = (255, 128, 0);
        PINK = (255, 0, 127);
        PURPLE = (127, 0, 255);
        RED = (255, 0, 0);
        TURKOSE = (0, 255, 128);
        WHITE = (255, 255, 255);
        YELLOW = (255, 255, 0);

        POLICE_SIREN = [ RED, BLUE ];
        RAINBOW = [ RED,
                    ORANGE,
                    YELLOW,
                    LIME_GREEN,
                    GREEN,
                    TURKOSE,
                    CYAN,
                    LIGHT_BLUE,
                    BLUE,
                    PURPLE,
                    MAGENTA,
                    PINK ];

    def getMap(mapInput):
        fileToRead = mapInput;

        mapFile = open(fileToRead, "r");

        print ("CURRENT MAP: " +fileToRead);

        GameLoop.gMap = mapFile.read().replace("\n", "");

        mapFile.close();

        #Each line in map ends with \n, remove one sign heren and extend Y with one for proper calculations
        mapFile = open(fileToRead, "r");
        GameLoop.gridSizeX = len(mapFile.readline()) - 1;
        print ("MAP SIZE X: " +str(GameLoop.gridSizeX));

        GameLoop.gridSizeY = len(mapFile.readlines()) + 1;
        print ("MAP SIZE Y: " +str(GameLoop.gridSizeY));
        mapFile.close();

    def drawMap():
        drawIndex = 0;

        for y in range(0, GameLoop.gridSizeY):
            for x in range(0, GameLoop.gridSizeX):

                if GameLoop.gMap[drawIndex] == "X":
                    pG.draw.rect(GameLoop.gScr, GameLoop.Colors().BLACK, (GameLoop.cellSize * x, GameLoop.cellSize * y, GameLoop.cellSize, GameLoop.cellSize));

                if GameLoop.gMap[drawIndex] == "0":
                    pG.draw.rect(GameLoop.gScr, GameLoop.Colors().BLACK, (GameLoop.cellSize * x, GameLoop.cellSize * y, GameLoop.cellSize, GameLoop.cellSize), 1);

                if GameLoop.gMap[drawIndex] == "S":
                    pG.draw.rect(GameLoop.gScr, GameLoop.Colors().BLUE, (GameLoop.cellSize * x, GameLoop.cellSize * y, GameLoop.cellSize, GameLoop.cellSize));

                if GameLoop.gMap[drawIndex] == "G":
                    pG.draw.rect(GameLoop.gScr, GameLoop.Colors().GREEN, (GameLoop.cellSize * x, GameLoop.cellSize * y, GameLoop.cellSize, GameLoop.cellSize));

                if GameLoop.gMap[drawIndex] == "\n":
                    pass;

                drawIndex += 1;

    def cycleMap(Map):
        getMap(Map);
        GameLoop.gScr = pG.display.set_mode((GameLoop.cellSize * GameLoop.gridSizeX, GameLoop.cellSize * GameLoop.gridSizeY));
        GameLoop.gScr.fill(background);

    def drawPath():
        pG.draw.line(GameLoop.gScr, GameLoop.Colors().ORANGE, (60, 80), (150, 20));

    def main():

        pG.init();
        pG.display.set_caption("Nackens Algorithmer");
        
        gameRunning = True;
        background = GameLoop.Colors().WHITE;
        keyDict = { K_w: "UP", K_s: "DOWN", K_a: "LEFT", K_d: "RIGHT", K_SPACE: "SPACE" };

        GameLoop.getMap(GameLoop.Maps.MAP1);

        GameLoop.gScr = pG.display.set_mode((GameLoop.cellSize * GameLoop.gridSizeX, GameLoop.cellSize * GameLoop.gridSizeY));
        GameLoop.gScr.fill(background);

        while gameRunning:

            for event in pG.event.get():
                if event.type == KEYDOWN:
                    if event.key in keyDict:
                        print (keyDict[event.key]);

            #ALGORITHM CALCULATION

            GameLoop.gScr.fill(background);
            GameLoop.drawMap();
            GameLoop.drawPath();
            pG.display.flip();
            pG.display.update();
        pG.quit();

        return;

GameLoop.main();