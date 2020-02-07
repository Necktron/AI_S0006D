import pygame;
from pygame.locals import *;

pG = pygame;

class GameLoop():

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

        #POLICE_SIREN = [ RED, BLUE ];
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

    def getMap():
        fileToRead = "Map1.txt";

        mapFile = open(fileToRead, "r");
        print (mapFile.read());

        #return the map translated from ASCII to actual coords

    def main():

        pG.init();
        
        gameRunning = True;
        background = GameLoop.Colors().WHITE;
        keyDict = { K_w: "UP", K_s: "DOWN", K_a: "LEFT", K_d: "RIGHT", K_SPACE: "SPACE" };

        gMap = GameLoop.getMap();

        gScr = pG.display.set_mode((1024, 768));
        gScr.fill(background);

        while gameRunning:

            for event in pG.event.get():

                #LISTEN FOR INPUT
                if event.type == KEYDOWN:
                    if event.key in keyDict:
                        print (keyDict[event.key]);

                #LISTEN FOR SHUT DOWN
                #if event.type == pG.quit():
                    #gameRunning = False;

            gScr.fill(background);
            pG.display.update();
            #END OF LOOP

        pG.quit();

        return;

GameLoop.main();