import pygame;
from pygame.locals import *;

pG = pygame;

class GameLoop():

    gScr = 0;
    cellSize = 50;
    cellCore = cellSize / 2;
    gridSizeX = 0;
    gridSizeY = 0;
    gMap = "";
    mapStart = (0, 0);
    mapGoal = (0, 0);

    class Algorithms():
        class ASTAR():
            class node():
                def __init__(self, parent = None, position = None):
                    self.parent = parent;
                    self.position = position;
                    self.g = 0;
                    self.h = 0;
                    self.f = 0;

                def __eq__(self, other):
                    return self.position == other.position;

            def search(gameMap, sPos, gPos):
                sNode = GameLoop.Algorithms.ASTAR.node(None, sPos);
                sNode.g = sNode.h = sNode.f = 0;
                gNode = GameLoop.Algorithms.ASTAR.node(None, gPos);
                gNode.g = gNode.h = gNode.f = 0;

                visitedNodes = [];
                undiscoveredNodes = [];

                visitedNodes.append(sNode);

                while len(visitedNodes) > 0:
                    
                    cNode = visitedNodes[0];
                    cIndex = 0;

                    for index, item in enumerate(visitedNodes):
                        if item.f < cNode.f:
                            cNode = item;
                            cIndex = index;

                    visitedNodes.pop(cIndex)
                    undiscoveredNodes.append(cNode);

                    if cNode == gNode:
                        path = [];
                        current = cNode;
                        print ("WE FOUND THE GOAL!");
                        while current is not None:
                            path.append(current.position);
                            current = current.parent;
                        return path[::-1];

                    children = [];
                    for newPos in [ (0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1) ]:
                        nodePos = (cNode.position[0] + newPos[0], cNode.position[1] + newPos[1]);

                        if nodePos[0] > (len(gameMap) - 1) or nodePos[0] < 0 or nodePos[1] > (len(gameMap[len(gameMap)-1]) -1) or nodePos[1] < 0:
                            continue;

                        if gameMap[nodePos[0]][nodePos[1]] != 0:
                            continue;

                        newNode = GameLoop.Algorithms.ASTAR.node(cNode, nodePos);

                        children.append(newNode);

                    for child in children:

                        for cChild in undiscoveredNodes:
                            if child == cChild:
                                continue;

                        child.g = cNode.g + 1;
                        child.h = ((child.position[0] - gNode.position[0]) ** 2) + ((child.position[1] - gNode.position[1]) ** 2)
                        child.f = child.g + child.h

                        for oNode in visitedNodes:
                            if child == oNode and child.g > oNode.g:
                                continue;

                        visitedNodes.append(child);

        class BRUTE_B:
            pass;

        class BRUTE_D:
            pass;

        class ASTAR_NN:
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
                    GameLoop.mapStart = (x, y);

                if GameLoop.gMap[drawIndex] == "G":
                    pG.draw.rect(GameLoop.gScr, GameLoop.Colors().GREEN, (GameLoop.cellSize * x, GameLoop.cellSize * y, GameLoop.cellSize, GameLoop.cellSize));
                    GameLoop.mapGoal = (x, y);

                if GameLoop.gMap[drawIndex] == "\n":
                    pass;

                drawIndex += 1;

    def cycleMap(Map):
        pG.quit();
        pG.init();
        pG.display.set_caption("Nackens Algorithmer");
        getMap(Map);
        GameLoop.gScr = pG.display.set_mode((GameLoop.cellSize * GameLoop.gridSizeX, GameLoop.cellSize * GameLoop.gridSizeY));
        pass;

    def drawPath():
        #pG.draw.line(GameLoop.gScr, GameLoop.Colors().BLACK, (GameLoop.cellCore, GameLoop.cellCore), (60, 180));
        pass;

    def main():

        pG.init();
        pG.display.set_caption("Nackens Algorithmer");
        
        gameRunning = True;
        background = GameLoop.Colors().WHITE;
        keyDict = { K_w: "UP", K_s: "DOWN", K_a: "LEFT", K_d: "RIGHT", K_SPACE: "SPACE" };

        GameLoop.getMap(GameLoop.Maps.MAP1);
        GameLoop.translateMap(GameLoop.gMap);

        GameLoop.gScr = pG.display.set_mode((GameLoop.cellSize * GameLoop.gridSizeX, GameLoop.cellSize * GameLoop.gridSizeY));
        GameLoop.gScr.fill(background);

        algExe = GameLoop.Algorithms.ASTAR;

        while gameRunning:

            for event in pG.event.get():
                if event.type == KEYDOWN:
                    if event.key in keyDict:
                        print(keyDict[event.key]);

            GameLoop.gScr.fill(background);
            GameLoop.drawMap(); #Draw the map itself
            algExe.search(GameLoop.gMap, GameLoop.mapStart, GameLoop.mapGoal);
            GameLoop.drawPath(); #Draw the path calculated by the algorithm
            pG.display.flip();
            pG.display.update();
        pG.quit();

        return;

GameLoop.main();