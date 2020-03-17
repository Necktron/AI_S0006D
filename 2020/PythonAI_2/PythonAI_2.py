import time;
import pygame;
import queue;
import math;
from pygame.locals import *;

pG = pygame;

class GameLoop():

    gScr = 0;
    cellSize = 20;
    cellCore = cellSize / 2;
    gridSizeX = 0;
    gridSizeY = 0;
    gMap = "";
    vMap = [];
    walkedPath = [];
    mapStart = (0, 0);
    mapGoal = (0, 0);
    gameRunning = True;

    class Algorithms:

        class node():
            def __init__(self, parent = None, position = None):
                self.parent = parent;
                self.position = position;
                self.g = 0;
                self.h = 0;
                self.f = 0;

            def __eq__(self, other):
                return self.position == other.position;

            def __hash__(self):
                return hash(self.position);

            def setG(self, gVal):
                self.g = gVal

            def setH(self, hVal):
                self.h = hVal

            def setF(self, fVal):
                self.f = fVal

        class ASTAR:
            def search(gameMap, sPos, gPos):
                sNode = GameLoop.Algorithms.node(None, sPos);
                sNode.g = sNode.h = sNode.f = 0;
                gNode = GameLoop.Algorithms.node(None, gPos);
                gNode.g = gNode.h = gNode.f = 0;

                openNodes = [];
                closedNodes = set();

                openNodes.append(sNode);
                start = time.time();

                while len(openNodes) > 0:
                    cNode = openNodes[0];
                    cIndex = 0;

                    for index, item in enumerate(openNodes):
                        if item.f < cNode.f:
                            #if item.h < cNode.h:
                            cNode = item;
                            cIndex = index;

                            print ("OPEN NODE VALUES: " +str(cNode.g)+ ", " +str(cNode.h)+ ", " +str(cNode.f)+ ".");

                    openNodes.pop(cIndex);
                    closedNodes.add(cNode);

                    #pG.draw.rect(GameLoop.gScr, GameLoop.Colors.ORANGE , (GameLoop.cellSize * cNode.position[0], GameLoop.cellSize * cNode.position[1], GameLoop.cellSize, GameLoop.cellSize), 3);
                    #curFont = pG.font.Font('freesansbold.ttf', int(GameLoop.cellSize / 4)) 
                    #curText = curFont.render(str("NODE"), True, GameLoop.Colors.BLACK, GameLoop.Colors.WHITE) ;
                    #curTextTrans = curText.get_rect();
                    #curTextTrans.center = (GameLoop.cellSize * cNode.position[0] + GameLoop.cellSize / 2, GameLoop.cellSize * cNode.position[1] + GameLoop.cellSize / 2); 
                    #GameLoop.gScr.blit(curText, curTextTrans);
                    #pG.display.flip();
                    #pG.display.update();

                    # If we reach the goal, render a path from start to goal
                    if cNode == gNode:
                        path = [];
                        current = cNode;
                        print ("WE FOUND THE GOAL!");
                        while current is not None:
                            path.append(current.position);
                            pG.draw.rect(GameLoop.gScr, GameLoop.Colors.LIME_GREEN , (GameLoop.cellSize * current.position[0], GameLoop.cellSize * current.position[1], GameLoop.cellSize, GameLoop.cellSize));
                            current = current.parent;

                        end = time.time();
                        print("Algorithm Completed in " +str(end - start)+ "!");
                        return path[::-1];

                    #Investigate
                    for newPos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        nodePos = (cNode.position[0] + newPos[0], cNode.position[1] + newPos[1]);

                        # Within range?
                        if nodePos[0] > (len(gameMap) - 1) or nodePos[0] < 0 or nodePos[1] > (len(gameMap[len(gameMap)-1]) -1) or nodePos[1] < 0:
                            continue;

                        # Walkable?
                        if gameMap[nodePos[1]][nodePos[0]] != 0:
                            continue;

                        # DOWN LEFT
                        if newPos == (-1, 1):
                            if gameMap[nodePos[1] - 1][nodePos[0]] != 0 or gameMap[nodePos[1]][nodePos[0] + 1] != 0:
                                #print ("The node itself is walkable, but it cuts a corner, therefor it's invalid as child traversal");
                                continue;

                        # UP LEFT
                        if newPos == (-1, -1):
                            if gameMap[nodePos[1]][nodePos[0] + 1] != 0 or gameMap[nodePos[1]][nodePos[0]  + 1 ] != 0:
                                #print ("The node itself is walkable, but it cuts a corner, therefor it's invalid as child traversal");
                                continue;

                        # UP RIGHT
                        if newPos == (1, -1):
                            if gameMap[nodePos[1] + 1][nodePos[0]] != 0 or gameMap[nodePos[1]][nodePos[0] - 1] != 0:
                                #print ("The node itself is walkable, but it cuts a corner, therefor it's invalid as child traversal");
                                continue;

                        # DOWN RIGHT
                        if newPos == (1, 1):
                            if gameMap[nodePos[1] - 1][nodePos[0]] != 0 or gameMap[nodePos[1]][nodePos[0] - 1] != 0:
                                #print ("The node itself is walkable, but it cuts a corner, therefor it's invalid as child traversal");
                                continue;

                        neighborNode = GameLoop.Algorithms.node(cNode, nodePos);

                        # Set G value
                        #if newPos == ((1, 1) or (-1, -1) or (-1, 1) or (1, -1)):
                            #neighborCost = 14;

                        #else:
                            #neighborCost = 10;

                        newNeighborCost = GameLoop.Algorithms.ASTAR.getCost(sNode, cNode) + GameLoop.Algorithms.ASTAR.getCost(cNode, neighborNode);
                      

                        #or neighborNode in closedNodes
                        #newNeighborCost < neighborNode.g
                        if neighborNode in closedNodes:
                            continue

                        #cost = cNode.g + GameLoop.Algorithms.ASTAR.getCost(neighborNode, cNode)

                        if neighborNode in openNodes:
                            if neighborNode.g > newNeighborCost:
                                neighborNode.setG(newNeighborCost)

                        else:
                            neighborNode.setG(newNeighborCost)
                            openNodes.append(neighborNode)

                        neighborNode.setH(GameLoop.Algorithms.ASTAR.heuristic(neighborNode, gNode))
                        neighborNode.setF(neighborNode.g + neighborNode.h);

                        #Only for render
                        pG.draw.rect(GameLoop.gScr, GameLoop.Colors.PURPLE , (GameLoop.cellSize * neighborNode.position[0], GameLoop.cellSize * neighborNode.position[1], GameLoop.cellSize, GameLoop.cellSize), 2);
                        pG.display.flip();
                        pG.display.update();
                        
                        nodeGFont = pG.font.Font('freesansbold.ttf', int(GameLoop.cellSize / 4)) 
                        nodeGText = nodeGFont.render(str(neighborNode.g), True, GameLoop.Colors.BLACK, GameLoop.Colors.GREEN) ;
                        nodeGTextTrans = nodeGText.get_rect()
                        nodeHFont = pG.font.Font('freesansbold.ttf', int(GameLoop.cellSize / 4)) 
                        nodeHText = nodeHFont.render(str(neighborNode.h), True, GameLoop.Colors.BLACK, GameLoop.Colors.RED) ;
                        nodeHTextTrans = nodeHText.get_rect()
                        nodeFFont = pG.font.Font('freesansbold.ttf', int(GameLoop.cellSize / 3)) 
                        nodeFText = nodeFFont.render(str(neighborNode.f), True, GameLoop.Colors.BLACK, GameLoop.Colors.YELLOW) ;
                        nodeFTextTrans = nodeFText.get_rect()
                        
                        nodeGTextTrans.center = (GameLoop.cellSize * neighborNode.position[0] + GameLoop.cellSize / 4, GameLoop.cellSize * neighborNode.position[1] + GameLoop.cellSize / 4); 
                        nodeHTextTrans.center = (GameLoop.cellSize * neighborNode.position[0] + (GameLoop.cellSize / 4) * 3 , GameLoop.cellSize * neighborNode.position[1] + GameLoop.cellSize / 4);
                        nodeFTextTrans.center = (GameLoop.cellSize * neighborNode.position[0] + GameLoop.cellSize / 2, GameLoop.cellSize * neighborNode.position[1] + GameLoop.cellSize / 2); 
                        GameLoop.gScr.blit(nodeGText, nodeGTextTrans);
                        GameLoop.gScr.blit(nodeHText, nodeHTextTrans);
                        GameLoop.gScr.blit(nodeFText, nodeFTextTrans);
                        pG.display.flip();
                        pG.display.update();

            def heuristic(node1, node2):
                dx = abs(node1.position[0] - node2.position[0])
                dy = abs(node1.position[1] - node2.position[1])
                D = 1
                D2 = math.sqrt(2)
                return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

            def getCost(node1, node2):
                if int(node2.position[0] - node1.position[0]) == 0 or int(node2.position[1] - node1.position[1]) == 0:
                    cost = 1  # horizontal/vertical cost
                else:
                    cost = 2  # diagonal cost
                return node1.g + cost

            #def getDist(nodeAPos, nodeBPos):
                #Set H value
                #xDist = abs(nodeAPos[0] - nodeBPos[0]);
                #yDist = abs(nodeAPos[1] - nodeBPos[1]);

                #if xDist > yDist:
                    #return 14 * yDist + 10 * (xDist - yDist);

                #return 14 * xDist + 10 * (yDist - xDist);


        class BFS():
            def search(gameMap, sPos, gPos):
                sNode = GameLoop.Algorithms.node(None, sPos);
                sNode.g = sNode.h = sNode.f = 0;
                gNode = GameLoop.Algorithms.node(None, gPos);
                gNode.g = gNode.h = gNode.f = 0;

                openNodes = [];
                closedNodes = set();

                openNodes.append(sNode);
                start = time.time();

                while len(openNodes) > 0:
                    cNode = openNodes[0];
                    cIndex = 0;

                    for index, item in enumerate(openNodes):
                        if item.f < cNode.f:
                            #if item.h < cNode.h:
                            cNode = item;
                            cIndex = index;

                            #print ("OPEN NODE VALUES: " +str(cNode.g)+ ", " +str(cNode.h)+ ", " +str(cNode.f)+ ".");

                    openNodes.pop(cIndex);
                    closedNodes.add(cNode);

                    #pG.draw.rect(GameLoop.gScr, GameLoop.Colors.ORANGE , (GameLoop.cellSize * cNode.position[0], GameLoop.cellSize * cNode.position[1], GameLoop.cellSize, GameLoop.cellSize), 3);
                    #curFont = pG.font.Font('freesansbold.ttf', int(GameLoop.cellSize / 4)) 
                    #curText = curFont.render(str("NODE"), True, GameLoop.Colors.BLACK, GameLoop.Colors.WHITE) ;
                    #curTextTrans = curText.get_rect();
                    #curTextTrans.center = (GameLoop.cellSize * cNode.position[0] + GameLoop.cellSize / 2, GameLoop.cellSize * cNode.position[1] + GameLoop.cellSize / 2); 
                    #GameLoop.gScr.blit(curText, curTextTrans);
                    #pG.display.flip();
                    #pG.display.update();

                    # If we reach the goal, render a path from start to goal
                    if cNode == gNode:
                        path = [];
                        current = cNode;
                        print ("WE FOUND THE GOAL!");
                        while current is not None:
                            path.append(current.position);
                            pG.draw.rect(GameLoop.gScr, GameLoop.Colors.LIME_GREEN , (GameLoop.cellSize * current.position[0], GameLoop.cellSize * current.position[1], GameLoop.cellSize, GameLoop.cellSize));
                            current = current.parent;

                        end = time.time();
                        print("Algorithm Completed in " +str(end - start)+ "!");
                        return path[::-1];

                    #Investigate
                    for newPos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        nodePos = (cNode.position[0] + newPos[0], cNode.position[1] + newPos[1]);

                        # Within range?
                        if nodePos[0] > (len(gameMap) - 1) or nodePos[0] < 0 or nodePos[1] > (len(gameMap[len(gameMap)-1]) -1) or nodePos[1] < 0:
                            continue;

                        # Walkable?
                        if gameMap[nodePos[1]][nodePos[0]] != 0:
                            continue;

                        # DOWN LEFT
                        if newPos == (-1, 1):
                            if gameMap[nodePos[1] - 1][nodePos[0]] != 0 or gameMap[nodePos[1]][nodePos[0] + 1] != 0:
                                #print ("The node itself is walkable, but it cuts a corner, therefor it's invalid as child traversal");
                                continue;

                        # UP LEFT
                        if newPos == (-1, -1):
                            if gameMap[nodePos[1]][nodePos[0] + 1] != 0 or gameMap[nodePos[1]][nodePos[0]  + 1 ] != 0:
                                #print ("The node itself is walkable, but it cuts a corner, therefor it's invalid as child traversal");
                                continue;

                        # UP RIGHT
                        if newPos == (1, -1):
                            if gameMap[nodePos[1] + 1][nodePos[0]] != 0 or gameMap[nodePos[1]][nodePos[0] - 1] != 0:
                                #print ("The node itself is walkable, but it cuts a corner, therefor it's invalid as child traversal");
                                continue;

                        # DOWN RIGHT
                        if newPos == (1, 1):
                            if gameMap[nodePos[1] - 1][nodePos[0]] != 0 or gameMap[nodePos[1]][nodePos[0] - 1] != 0:
                                #print ("The node itself is walkable, but it cuts a corner, therefor it's invalid as child traversal");
                                continue;

                        neighborNode = GameLoop.Algorithms.node(cNode, nodePos);

                        # Set G value
                        #if newPos == ((1, 1) or (-1, -1) or (-1, 1) or (1, -1)):
                            #neighborCost = 14;

                        #else:
                            #neighborCost = 10;

                        newNeighborCost = GameLoop.Algorithms.BFS.getCost(sNode, cNode) + GameLoop.Algorithms.BFS.getCost(cNode, neighborNode);
                      

                        #or neighborNode in closedNodes
                        #newNeighborCost < neighborNode.g
                        if neighborNode in closedNodes:
                            continue

                        #cost = cNode.g + GameLoop.Algorithms.ASTAR.getCost(neighborNode, cNode)

                        if neighborNode in openNodes:
                            if neighborNode.g > newNeighborCost:
                                neighborNode.setG(newNeighborCost)

                        else:
                            neighborNode.setG(newNeighborCost)
                            openNodes.append(neighborNode)

                        neighborNode.setH(GameLoop.Algorithms.BFS.heuristic(neighborNode, gNode))
                        neighborNode.setF(neighborNode.g + neighborNode.h);

                        #Only for render
                        #pG.draw.rect(GameLoop.gScr, GameLoop.Colors.PURPLE , (GameLoop.cellSize * neighborNode.position[0], GameLoop.cellSize * neighborNode.position[1], GameLoop.cellSize, GameLoop.cellSize), 2);
                        #pG.display.flip();
                        #pG.display.update();
                        #nodeGFont = pG.font.Font('freesansbold.ttf', int(GameLoop.cellSize / 4)) 
                        #nodeGText = nodeGFont.render(str(neighborNode.g), True, GameLoop.Colors.BLACK, GameLoop.Colors.GREEN) ;
                        #nodeGTextTrans = nodeGText.get_rect()
                        #nodeHFont = pG.font.Font('freesansbold.ttf', int(GameLoop.cellSize / 4)) 
                        #nodeHText = nodeHFont.render(str(neighborNode.h), True, GameLoop.Colors.BLACK, GameLoop.Colors.RED) ;
                        #nodeHTextTrans = nodeHText.get_rect()
                        #nodeFFont = pG.font.Font('freesansbold.ttf', int(GameLoop.cellSize / 3)) 
                        #nodeFText = nodeFFont.render(str(neighborNode.f), True, GameLoop.Colors.BLACK, GameLoop.Colors.YELLOW) ;
                        #nodeFTextTrans = nodeFText.get_rect()
                        #nodeGTextTrans.center = (GameLoop.cellSize * neighborNode.position[0] + GameLoop.cellSize / 4, GameLoop.cellSize * neighborNode.position[1] + GameLoop.cellSize / 4); 
                        #nodeHTextTrans.center = (GameLoop.cellSize * neighborNode.position[0] + (GameLoop.cellSize / 4) * 3 , GameLoop.cellSize * neighborNode.position[1] + GameLoop.cellSize / 4);
                        #nodeFTextTrans.center = (GameLoop.cellSize * neighborNode.position[0] + GameLoop.cellSize / 2, GameLoop.cellSize * neighborNode.position[1] + GameLoop.cellSize / 2); 
                        #GameLoop.gScr.blit(nodeGText, nodeGTextTrans);
                        #GameLoop.gScr.blit(nodeHText, nodeHTextTrans);
                        #GameLoop.gScr.blit(nodeFText, nodeFTextTrans);
                        #pG.display.flip();
                        #pG.display.update();

            def heuristic(node1, node2):
                dx = abs(node1.position[0] - node2.position[0])
                dy = abs(node1.position[1] - node2.position[1])
                return (dx + dy)

            def getCost(node1, node2):
                if int(node2.position[0] - node1.position[0]) == 0 or int(node2.position[1] - node1.position[1]) == 0:
                    cost = 10  # horizontal/vertical cost
                else:
                    cost = 14  # diagonal cost
                return node1.g + cost
            
        
        class DFS:
            pass;

        class ASTAR_NN:
            pass;

    class Maps:
        MAP1 = 'Map1.txt';
        MAP2 = 'Map2.txt';
        MAP3 = 'Map3.txt';

    class Colors:
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

    #DONE
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

        GameLoop.gMap = mapFile.read().replace("\n", "");

        mapFile.close();

        #Each line in map ends with \n, remove one sign heren and extend Y with one for proper calculations
        mapFile = open(fileToRead, "r");
        GameLoop.gridSizeX = len(mapFile.readline()) - 1;

        GameLoop.gridSizeY = len(mapFile.readlines()) + 1;
        mapFile.close();

        index = 0;

        row = [];

        #Define the value representation of the map for the pathfinding
        print("------------------------------------------------");
        for y in range(0, GameLoop.gridSizeY):

            if len(row) > 0:
                GameLoop.vMap.append(row);
                print(row);
                del(row);
                row = [];

            for x in range(0, GameLoop.gridSizeX):

                if GameLoop.gMap[index] == "X":
                    row.append(1);

                if GameLoop.gMap[index] == "0":
                    row.append(0);

                if GameLoop.gMap[index] == "S":
                    row.append(0);
                    GameLoop.mapStart = (x, y);

                if GameLoop.gMap[index] == "G":
                    row.append(0);
                    GameLoop.mapGoal = (x, y);

                if GameLoop.gMap[index] == "\n":
                    pass;

                index += 1;

        if len(row) > 0:
            GameLoop.vMap.append(row);
            print(row);
            print("------------------------------------------------");
            del(row);

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
        pG.quit();
        pG.init();
        pG.display.set_caption("Nackens Algorithmer");
        getMap(Map);
        GameLoop.gScr = pG.display.set_mode((GameLoop.cellSize * GameLoop.gridSizeX, GameLoop.cellSize * GameLoop.gridSizeY));
        pass;

    def main():

        pG.init();
        pG.display.set_caption("Nackens Algorithmer");

        background = GameLoop.Colors.WHITE;
        keyDict = { K_w: "UP", K_s: "DOWN", K_a: "LEFT", K_d: "RIGHT", K_SPACE: "SPACE" };

        GameLoop.getMap(GameLoop.Maps.MAP3);

        GameLoop.gScr = pG.display.set_mode((GameLoop.cellSize * GameLoop.gridSizeX, GameLoop.cellSize * GameLoop.gridSizeY));
        GameLoop.gScr.fill(background);

        algExe = GameLoop.Algorithms.BFS;
        #algExe = GameLoop.Algorithms.BFS;
        while GameLoop.gameRunning == True:

            for event in pG.event.get():
                if event.type == KEYDOWN:
                    if event.key in keyDict:
                        print(keyDict[event.key]);

            GameLoop.gScr.fill(background);
            GameLoop.drawMap(); #Draw the map itself
            algExe.search(GameLoop.vMap, GameLoop.mapStart, GameLoop.mapGoal);
            #algExe.search(GameLoop.vMap);
            pG.display.flip();
            pG.display.update();
            time.sleep(10.0);
        pG.quit();

        return;

GameLoop.main();