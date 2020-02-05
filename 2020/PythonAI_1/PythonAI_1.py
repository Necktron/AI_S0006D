# JONAS H, Februari 2020
from GameTime import gameTime;
from Telecom import telecom;
from Humanoid import humanoid;
import time;
import uuid;
import sys;

clock = gameTime();
phone = telecom();

def main():
    print ("")
    print ("Welcome to the AI assignment 1 - Nacken's implementation")
    print ("How many agents do you want to creat?\n")
    
    aOA = None;
    updateRate = 0;

    #Assign how many AI's to create
    while True:
        uIn = input("Agents to create: ");

        try:
            aOA = int(uIn);

            if aOA <= 0:
                print ("\nHey! We need atleast someone alive");

            elif 0 < aOA < 9:
                print ("\nPerfect! Let's go!");
                break;

            elif aOA >= 9:
                print ("\nThat's alot! Max allowed is 8");

        except ValueError:
            print ("\nNot a valid input, please type a number!");

    print ("What will you name the AI:s?")
    name, aID, agents, x = "", uuid.UUID, [], 0

    #Assign name, ID, clock ref and phone ref to the AI and create it, add it to list of agents
    while x < aOA:
        name = input("Name for AI #" +str(x+1)+ ": ")
        print (name+ ", that's a beautiful name!\n")

        aID = uuid.uuid1();
        aSpawn = humanoid().humanoid(name, aID, clock, phone);
        agents.append(aSpawn);

        x += 1

    print ("All names have been assigned!")
    aOA = len(agents)
    print ("A total of " +str(aOA)+ " agents has been created!")

    x = 0;

    print ("\nPlease assign a value to update rate; the lower it is, the faster it updates! Example: 0.4")
    
    #Assign update rate
    while True:
        uIn = input("Update Rate: ");

        try:
            updateRate = float(uIn);
            break;

        except ValueError:
            print ("\nNot a valid input, please type a number!");

    #Update phonebook with all names
    while x < aOA:
        phone.phoneBook.append(agents[x]);
        phone.posConn += 1;
        x += 1;

    #Core loop for agents update
    while aOA > 0:
        #Update all agents 
        time.sleep(updateRate);
        clock.Update();
        print ("Clock is " +clock.cTime);

        msgToDelete = [];
        #Check if any messages needs to be sent away
        if len(phone.deliveryQueue) > 0:
            for msg in phone.deliveryQueue:
                if msg.msgTimer == clock.cTime:
                    phone.SendMSG(msg);
                    msgToDelete.append(msg);

        #Delete messages that have been sent
        msgIndex = 0;
        while len(msgToDelete) > 0:
            if msgToDelete[0] == phone.deliveryQueue[msgIndex]:
                del phone.deliveryQueue[msgIndex];
                del msgToDelete[0];
                msgIndex = 0;
            else:
                msgIndex += 1;

        #Update all agents
        x = 0
        while x < len(agents):
            agents[x].Update();
            print ("");

            #AI is deleted from list of AI's
            if agents[x].m_Alive == False:
                del agents[x];
                aOA = len(agents);

                del phone.phoneBook[x];
                phone.posConn -= 1;

            else:
                x += 1;

    if clock.calYears >= 2130:
        print("Ain't no way anyone is living now! They're all dead!");
        agents.clear();
        aOA = 0;

    print ("All AI's have died. Program has reached it's end!");
    print ("The last AI survived for a total of " +str(clock.calMonths)+" months, " +str(clock.calDays)+ " days, untill " +clock.cTime+ " o'clock! The year is " +str(clock.calYears));
    print ("");

main();