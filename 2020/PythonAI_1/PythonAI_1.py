from GameTime import gameTime;
from Humanoid import humanoid;
import time;
import uuid;

clock = gameTime();

#TODO (LAST UPDATED 24/1 2020):
# 1) FIX REST OF STATES AND ALTERNATIVES
# 2) ADD TELECOM FOR MULTI AI COMMS AND FUTURE NOTICES
# 3) TWEAK VALUES FOR OPTIMAL USAGE
# 4) PROFIT

def main():
    print ("")
    print ("Welcome to the AI assignment 1 - Necktron's implementation")
    print ("How many agents do you want to creat?\n")
    
    aOA = None

    while True:
        aOA = int(input("Agents to create: "))

        if aOA <= 0:
            print ("\nHey! We need atleast someone alive\n")

        elif 0 < aOA < 9:
            print ("\nPerfect! Let's go!\n")
            break

        elif aOA >= 9:
            print ("\nThat's alot! Are you sure?\n")

    print ("What will you name the AI:s?")
    name, aID, agents, x = "", uuid.UUID, [], 0

    while x < aOA:
        name = input("Name for AI #" +str(x+1)+ ": ")
        print (name+ ", that's a beautiful name!\n")

        #Assign name to the AI and create it, add it to list of agents
        aID = uuid.uuid1();
        aSpawn = humanoid().humanoid(name, aID, clock);
        #FIX IMPLEMENTATION OF AI IN LIST
        agents.append(aSpawn);

        x += 1

    print ("All names have been assigned!")
    aOA = len(agents)
    print ("A total of " +str(aOA)+ " agents has been created!")

    while aOA > 0:

        if clock.updateRate == 0:
            time.sleep(10);
            print("Time is frozen! Adjust UpdateRate to continue")
            clock.ChangeUR(0.2);

        else:
            #Update all agents 
            time.sleep(clock.updateRate);
            clock.Update();
            print ("Clock is " +clock.cTime);

            x = 0
            while x < len(agents):
                agents[x].Update();
                print ("");
                x += 1;

        if clock.calYears >= 2130:
            print("Ain't no way anyone is living now! They are all dead!")
            agents.clear();
            aOA = 0;

    print ("All AI's have died. Program has reached it's end!")

main();