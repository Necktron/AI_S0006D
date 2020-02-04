from GameTime import gameTime;
from Telecom import telecom;
from Humanoid import humanoid;
import time;
import uuid;

clock = gameTime();
phone = telecom();

#TODO (LAST UPDATED 3/2 2020):
# 1) FINISH TELECOM WITH ALL MESSAGES FOR BOTH SEND AND READ
# 2) TWEAK VALUES FOR OPTIMAL USAGE
# 3) FIX MESSAGE NBUG WHEN SENDING DELAYED MESSAGES
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

        #Assign name, ID, clock ref and phone ref to the AI and create it, add it to list of agents
        aID = uuid.uuid1();
        aSpawn = humanoid().humanoid(name, aID, clock, phone);
        agents.append(aSpawn);

        x += 1

    print ("All names have been assigned!")
    aOA = len(agents)
    print ("A total of " +str(aOA)+ " agents has been created!")

    x = 0;

    #Update phonebook with all names
    while x < aOA:
        phone.phoneBook.append(agents[x]);
        phone.posConn += 1;
        x += 1;

    #Core loop for agents update
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

            if len(phone.deliveryQueue) > 0:
                msgIndex = 0;
                for msg in phone.deliveryQueue:
                    if msg.msgTimer == clock.cTime:
                        phone.SendMSG(msg);
                        del phone.deliveryQueue[msgIndex];
                        print ("Messages in queue after sending: " +str(len(phone.deliveryQueue)));

                        if len(phone.deliveryQueue) == 1:
                            for msg in phone.deliveryQueue:
                                if msg.msgTimer == clock.cTime:
                                    phone.SendMSG(msg);
                                    del phone.deliveryQueue[msgIndex];

                    msgIndex += 1;
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

main();