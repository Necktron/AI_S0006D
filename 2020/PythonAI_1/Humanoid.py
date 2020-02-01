from BaseGameEntity import baseGameEntity;
from GameTime import gameTime;
from random import seed;
from random import randint;
from datetime import datetime;

class State:
    def Enter(self):
        pass

    def Execute(self):
        pass

    def Exit(self):
        pass

#WIP
class State_Sleep(State):
    def Enter(self):
        print (self.m_Name+ ": It will be good with a bit of sleep now! Goodnight!")

    def Execute(self):

        if self.m_Hunger <= 0 or self.m_Thirst <= 0:
            print (self.m_Name+ ": OOOOOF");
            newStateC = State_Die;
            self.ChangeCurrentState(newStateC);
            self.m_pCurrentState.Enter(self);

        elif self.m_ClockRef.cTime == "01:00":
            seed(datetime.now());
            self.m_ROS = randint(0, 30);
            
            if self.m_ROS > 26:
                self.m_Sick = True;
                print (self.m_Name+ ": Sick... lel");
                seed(datetime.now());
                self.m_SL = randint(0, 10);
                print ("Rand SL is: " +str(self.m_SL));

            else:
                self.m_Sick = False;
                self.m_SL = 0;
                print (self.m_Name+ ": Healthy!");

            print (self.m_Name+ ": Zzz...");
            self.m_Hunger -= 1;
            self.m_Energy += 3;

        elif self.m_ClockRef.cTime == "08:00":
            if self.m_Name == "Jonas":
                self.AskToHangout();

            self.m_pCurrentState.Exit(self);

        elif self.m_ClockRef.calHour < 8:
            print (self.m_Name+ ": Zzz...");
            self.m_Hunger -= 1 + self.m_SL;
            self.m_Energy += 3 - self.m_SL;

    def Exit(self):
        print (self.m_Name+ ": Erghe... Augh! Goodmorning World!")

        #FOOD
        if self.m_Hunger < 50 and self.m_Cash >= 20:
            if self.m_Location != "Restaurant":
               self.m_GoalLoc = "Restaurant";
               newStateC = State_WalkTo;
               self.ChangeCurrentState(newStateC);
               newStateG = State_Eat;
               self.ChangeFutureState(newStateG);

            else:
               newStateC = State_Eat;
               self.ChangeCurrentState(newStateC);

        #THIRST
        elif self.m_Thirst < 50 and self.m_Cash >= 10:
            if self.m_Location != "Traversen":
               self.m_GoalLoc = "Traversen";
               newStateC = State_WalkTo;
               self.ChangeCurrentState(newStateC);
               newStateG = State_Eat;
               self.ChangeFutureState(newStateG);

            else:
               newStateC = State_Eat;
               self.ChangeCurrentState(newStateC);

        #SOCIAL
        elif self.m_Thirst < 50 and self.m_Cash >= 10:
            if self.m_Location != "Traversen":
               self.m_GoalLoc = "Traversen";
               newStateC = State_WalkTo;
               self.ChangeCurrentState(newStateC);
               newStateG = State_Eat;
               self.ChangeFutureState(newStateG);

            else:
               newStateC = State_Eat;
               self.ChangeCurrentState(newStateC);

        #WORK
        elif self.m_Cash < 1000:
            #If you own a gun and a little wealthy
            if self.m_OwnsGun == True and self.m_Cash >= 800:
                print (self.m_Name+ ": I own a gun and I have plenty of cash, a hunting day can't hurt that much!");
                if self.m_Location != "Northern Forest":
                    self.m_GoalLoc = "Northern Forest";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_WorkHunt;
                    self.ChangeFutureState(newStateG);

                else:
                    newStateC = State_WorkHunt;
                    self.ChangeCurrentState(newStateC);

            #If you don't own a gun but can afford one
            elif self.m_OwnsGun == False and self.m_Cash >= 500:
                print (self.m_Name+ ": I want to buy a gun so I can hunt");
                self.m_GoalLoc = "The Mall";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = State_WorkHunt;
                self.ChangeFutureState(newStateG);

            #If you don't own a gun and can't afford one
            elif self.m_OwnsGun == False and self.m_Cash < 500:
                print (self.m_Name+ ": I can't afford a gun, reeeeee... Guess I have to work in the office");

                if self.m_Location != "Downtown Office":
                    self.m_GoalLoc = "Downtown Office";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_WorkOffice;
                    self.ChangeFutureState(newStateG);

                else:
                    newStateC = State_WorkOffice;
                    self.ChangeCurrentState(newStateC);

            #If you are low on cash and own a gun, just go to the office
            else:
                if self.m_Location != "Downtown Office":
                    print (self.m_Name+ ": I own a gun, but I need alot of money. It's worth more to work at the office today!");
                    self.m_GoalLoc = "Downtown Office";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_WorkOffice;
                    self.ChangeFutureState(newStateG);

                else:
                    newStateC = State_WorkOffice;
                    self.ChangeCurrentState(newStateC);

        else:
             pass

#WIP
class State_Eat(State):
    def Enter(self):
        print (self.m_Name+ ": Ooooh! Tasty food! Yummy!")

    def Execute(self):
        print (self.m_Name+ ": Nom nom nom!");
        self.m_Hunger += 10 - self.m_SL;
        self.m_Cash -= 25;

    def Exit(self):
        print (self.m_Name+ ": Ohm nom! Bhaaa, I'm so stuffed now");

        #Exit states, check what todo next

#WIP
class State_Drink(State):
    def Enter(self):
        print (self.m_Name+ ": Hi again! I want some Budvar!");

    def Execute(self):
        print (self.m_Name+ ": *glup glup glup* Whaoeguaoihoa...");

        self.m_Thirst += 10 - self.m_SL;
        self.m_Cash -= 25;

    def Exit(self):
        print (self.m_Name+ ": Aaaaah! That was good, bye bye!");

        #Exit states, check what todo next

#WIP
class State_WorkOffice(State):
    def Enter(self):
        print (self.m_Name+ ": 'AI Interactive', my work place! Let's get that cash!")

    def Execute(self):
        print (self.m_Name+ ": 01001101101... Beep Boop Office Work!");
        self.m_Cash += 10;
        self.m_Energy -= 5 + self.m_SL;

    def Exit(self):
        print (self.m_Name+ ": Phew, hard work pays off! I'm signing out for today!");

        #Exit states, check what todo next

#WIP
class State_WorkHunt(State):
    def Enter(self):
        print (self.m_Name+ ": Out in the woods, lalalala")

    def Execute(self):
        print (self.m_Name+ ": Hunt, hunt, hunting goose!")

    def Exit(self):
        print (self.m_Name+ ": Time to go home, it's was nice being out here on my hunter spot");

        #Exit states, check what todo next

#WIP - REQUIER TELECOM SCRIPT
class State_Socialize(State):
    def Enter(self):
        print("Oh hey it's you! Wazzup! :D")

    def Execute(self):
        print(self.m_Name+ ": How's the weather? Have you seen the latest episode of GoT?");

        if self.m_Location == "The Park":
            self.m_SocialNeed += 6 - self.m_SL;

        elif self.m_Location == "The Restaurant":
            self.m_SocialNeed += 4 - self.m_SL;
            self.m_Hunger += 1 - self.m_SL;

        elif self.m_Location == "Traversen":
            self.m_SocialNeed += 4 - self.m_SL;
            self.m_Thirst += 1 - self.m_SL;

    def Exit(self):
        print (self.m_Name+ ": Time to go home, it's was nice being out here on my hunter spot");

        #Exit states, check what todo next

#WIP
class State_Idle(State):
    def Enter(self):
        print (self.m_Name+ ": Not much to do right now, might just stand here in a glorious T-pose to show dominance!");
     
    def Execute(self):
        if self.m_pGoalState == State_Socialize:
            print (self.m_Name+ ": I'm waiting for my friend~");

        elif self.m_pGoalState == State_WorkOffice:
            print (self.m_Name+ ": I'm waiting for office hours to begin");
    
    def Exit(self):
        print (self.m_Name+ ": Back to reality! Now, where was I");

#Done-ish
class State_WalkTo(State):
    def Enter(self):
        #HOME START
        #Home and Downtown Office dist
        if self.m_Location == "Home" and self.m_GoalLoc == "Downtown Office" or self.m_Location == "Downtown Office" and self.m_GoalLoc == "Home":
            self.m_distToGoal = 40;

        #Home and The Mall dist
        elif self.m_Location == "Home" and self.m_GoalLoc == "The Mall" or self.m_Location == "The Mall" and self.m_GoalLoc == "Home":
            self.m_distToGoal = 16;

        #Home and Restaurant dist
        elif self.m_Location == "Home" and self.m_GoalLoc == "Restaurant" or self.m_Location == "Restaurant" and self.m_GoalLoc == "Home":
            self.m_distToGoal = 32;

        #Home and Traversen dist
        elif self.m_Location == "Home" and self.m_GoalLoc == "Traversen" or self.m_Location == "Traversen" and self.m_GoalLoc == "Home":
           self.m_distToGoal = 24;

        #Home and Northern Forest dist
        elif self.m_Location == "Home" and self.m_GoalLoc == "Northern Forest" or self.m_Location == "Northern Forest" and self.m_GoalLoc == "Home":
            self.m_distToGoal = 12;

        #Home and The Park dist
        elif self.m_Location == "Home" and self.m_GoalLoc == "The Park" or self.m_Location == "The Park" and self.m_GoalLoc == "Home":
            self.m_distToGoal = 24;
        #HOME END

        #OFFICE START
        #Downtown Office and The Mall dist
        elif self.m_Location == "Downtown Office" and self.m_GoalLoc == "The Mall" or self.m_Location == "The Mall" and self.m_GoalLoc == "Downtown Office":
            self.m_distToGoal = 20;

        #Downtown Office and Restaurant dist
        elif self.m_Location == "Downtown Office" and self.m_GoalLoc == "Restaurant" or self.m_Location == "Restaurant" and self.m_GoalLoc == "Downtown Office":
            self.m_distToGoal = 8;

        #Downtown Office and Traversen dist
        elif self.m_Location == "Downtown Office" and self.m_GoalLoc == "Traversen" or self.m_Location == "Traversen" and self.m_GoalLoc == "Downtown Office":
            self.m_distToGoal = 16;

        #Downtown Office and Northern Forest dist
        elif self.m_Location == "Downtown Office" and self.m_GoalLoc == "Northern Forest" or self.m_Location == "Northern Forest" and self.m_GoalLoc == "Downtown Office":
            self.m_distToGoal = 60;

        #Downtown Office and The Park dist
        elif self.m_Location == "Downtown Office" and self.m_GoalLoc == "The Park" or self.m_Location == "The Park" and self.m_GoalLoc == "Downtown Office":
            self.m_distToGoal = 10;
        #OFFICE STOP

        #Restaurant START
        #Restaurant and The Mall dist
        elif self.m_Location == "Restaurant" and self.m_GoalLoc == "The Mall" or self.m_Location == "The Mall" and self.m_GoalLoc == "Restaurant":
            self.m_distToGoal = 20;

        #Restaurant and Traversen dist
        elif self.m_Location == "Restaurant" and self.m_GoalLoc == "Traversen" or self.m_Location == "Traversen" and self.m_GoalLoc == "Restaurant":
            self.m_distToGoal = 10;

        #Restaurant and Northern Forest dist
        elif self.m_Location == "Restaurant" and self.m_GoalLoc == "Northern Forest" or self.m_Location == "Northern Forest" and self.m_GoalLoc == "Restaurant":
            self.m_distToGoal = 46;

        #Restaurant and The Park dist
        elif self.m_Location == "Restaurant" and self.m_GoalLoc == "The Park" or self.m_Location == "The Park" and self.m_GoalLoc == "Restaurant":
            self.m_distToGoal = 14;
        #Restaurant STOP

        #TRAVVEN START
        #Traversen and The Mall dist
        elif self.m_Location == "Traversen" and self.m_GoalLoc == "The Mall" or self.m_Location == "The Mall" and self.m_GoalLoc == "Traversen":
            self.m_distToGoal = 12;

        #Traversen and Northern Forest dist
        elif self.m_Location == "Traversen" and self.m_GoalLoc == "Northern Forest" or self.m_Location == "Northern Forest" and self.m_GoalLoc == "Traversen":
            self.m_distToGoal = 34;

        #Traversen and The Park dist
        elif self.m_Location == "Traversen" and self.m_GoalLoc == "The Park" or self.m_Location == "The Park" and self.m_GoalLoc == "Traversen":
            self.m_distToGoal = 16;
        #TRAVVEN STOP

        #THE MALL START
        #The Mall and Northern Forest dist
        elif self.m_Location == "The Mall" and self.m_GoalLoc == "Northern Forest" or self.m_Location == "Northern Forest" and self.m_GoalLoc == "The Mall":
            self.m_distToGoal = 34;

        #The Mall and The Park dist
        elif self.m_Location == "The Mall" and self.m_GoalLoc == "The Park" or self.m_Location == "The Park" and self.m_GoalLoc == "The Mall":
            self.m_distToGoal = 16;
        #THE MALL STOP

        #NORTHERN FOREST START
        #Northern Forest and The Park dist
        elif self.m_Location == "Northern Forest" and self.m_GoalLoc == "The Park" or self.m_Location == "The Park" and self.m_GoalLoc == "Northern Forest":
            self.m_distToGoal = 52;
        #NORTHERN FOREST STOP

        print (self.m_Name+ ": I have to go from " +self.m_Location+ " to " +self.m_GoalLoc+ ". ( Dist = " +str(self.m_distToGoal)+ "m )");
        self.m_Location = "Outside";

    def Execute(self):
        self.m_walkedDistance += self.m_walkingSpeed;
        self.m_Energy -= 1 + self.m_SL;
        print(str(self.m_walkedDistance)+ "m traversed");

        if self.m_walkedDistance >= self.m_distToGoal and self.m_GoalLoc != "The Mall":
            self.m_pCurrentState.Exit(self);

        elif self.m_walkedDistance >= self.m_distToGoal and self.m_GoalLoc == "The Mall":
            self.m_Location = self.m_GoalLoc;
            print ("Destination have been reached!");
            print ("");
            self.m_walkedDistance = 0;
            print (self.m_Name+ ": I'm buying a gun so I can hunt in the woods! (-350kr)");
            self.m_Cash -= 350;
            self.m_OwnsGun = True;
            self.m_GoalLoc = "Northern Forest";
            self.m_pCurrentState.Enter(self);

    def Exit(self):
        if self.m_pGoalState == State_Socialize:
            self.m_Location = self.m_GoalLoc;
            print ("Destination have been reached!");
            print ("");
            newStateC = State_Idle;
            self.ChangeCurrentState(newStateC);
            newStateG = None;
            self.ChangeFutureState(newStateG);
            self.m_distToGoal = 0;
            self.m_GoalLoc = None;
            self.m_PhoneRef.SendMSG

        else:
            self.m_Location = self.m_GoalLoc;
            print ("Destination have been reached!");
            print ("");
            newStateC = self.m_pGoalState;
            self.ChangeCurrentState(newStateC);
            newStateG = None;
            self.ChangeFutureState(newStateG);
            self.m_distToGoal = 0;
            self.m_GoalLoc = None;

#Done-ish
class State_Die(State):
    def Enter(self):
        self.m_Location = "The Bright Tunnel";

    def Execute(self):
        print (self.m_Name+ " died");
        self.m_pCurrentState.Exit(self);

    def Exit(self):
        #print (self.m_Name+ " has been erased from the list of active AI");
        newStateC = None;
        self.ChangeCurrentState(newStateC);
        self.m_Alive = False;

#WIP
class humanoid(baseGameEntity):
    m_pPreviousState = None; #What did the AI do before? In case we want to go back to our previous state
    m_pCurrentState = None;
    m_pGoalState = None; #Only used if the agent is not at correct location
    m_Location = None; #In the future we can set this to a vector of spawn, then move it towards a PoI in engine and check vector math for distance
    m_GoalLoc = None; #Wiped upon arrival to location
    m_ClockRef = None;
    m_PhoneRef = None;
    m_Cash = 0;
    m_Hunger = 0;
    m_Thirst = 0;
    m_Energy = 0;
    m_SocialNeed = 0;
    m_WorkSkill = 0; #How much you gain on a daily basis
    m_walkingSpeed = 0; #How far you get on one tick
    m_walkedDistance = 0; #How far you have traveled towards your goal location
    m_distToGoal = 0; #Wiped upon arrival to location
    m_ROS = 0; #Risk Of Sickness, randomize during night to add a little chaos to everyday life
    m_SL = 0; #Once you get sick, you are in the faith of God, will you just get the flew or the plague?
    m_Alive = True;
    m_Sick = False;
    m_OwnsGun = False;

    def humanoid(self, name, aID, clock, phone):
        seed(datetime.now());

        self.m_Name = name;
        self.m_EntityName = "Humanoid_" +name;
        self.m_EntityID = aID;
        self.m_Location = "Home";
        self.m_ClockRef = clock;
        self.m_PhoneRef = phone;
        self.m_Cash = randint(500, 1000);
        self.m_Hunger = randint(60, 90);
        self.m_Thirst = randint(64, 100);
        self.m_Energy = randint(20, 30);
        self.m_SocialNeed = randint(70, 110);
        self.m_WorkSkill = randint(1, 10);
        self.m_walkingSpeed = randint(3, 8);
        self.m_pCurrentState = State_Sleep;

        return self;

    def Update(self):
        self.m_pCurrentState.Execute(self);

    def ChangeCurrentState(self, newStateC):
        self.m_pCurrentState = None;

        if newStateC == None:
            pass

        else:
            self.m_pCurrentState = newStateC;
            self.m_pCurrentState.Enter(self);

    def ChangeFutureState(self, newStateG):
        self.m_pGoalState = None;
        self.m_pGoalState = newStateG;

    def AskToHangout(self):
        s = self.ConnSender();
        r = self.ConnRecieveer();
        t = self.ConnTime();
        l = self.ConnLocation();
        message = self.m_PhoneRef.SMS().Message(s, r, 1, self.m_PhoneRef.MSG_MeetUp_SendText[randint(0, 2)], t,  self.m_PhoneRef.meetingsSpots[l], None);
        self.m_PhoneRef.SendMSG(message);

    def ConnSender(self):
        return self;

    def ConnRecieveer(self):
        connID = randint(0, self.m_PhoneRef.posConn - 1);
        contactAI = self.m_PhoneRef.phoneBook[connID];

        while contactAI == self.m_Name:
            print ("Can't send message to yourself!");
            connID = randint(0, self.m_PhoneRef.posConn - 1);
            contactAI = self.m_PhoneRef.phoneBook[connID].m_Name;

        return contactAI;

    def ConnTime(self):
        mH = randint(9, 23);
        mM = randint(0, 59);

        if mH < 10:
            mHs = "0" + str(mH);

        else:
            mHs = str(mH);

        if mM < 10:
            mMs = "0" + str(mM);

        else:
            mMs = str(mM);

        mFT = mHs+ ":" +mMs;

        return mFT;

    def ConnLocation(self):
        return randint(0, self.m_PhoneRef.posMeeting - 1);