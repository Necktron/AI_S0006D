from BaseGameEntity import baseGameEntity;
from GameTime import gameTime;

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
        if self.m_ClockRef.cTime == "08:00":
            self.m_pCurrentState.Exit(self);

        elif self.m_ClockRef.calHour < 8:
            print (self.m_Name+ ": Zzz...");
            self.m_Energy += 3;

    def Exit(self):
         print (self.m_Name+ ": Erghe... Augh! Goodmorning World!")

         if self.m_Cash < 300:
             if self.m_Location != "Downtown Office":
                self.m_GoalLoc = "Downtown Office";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = State_WorkOffice;
                self.ChangeFutureState(newStateG);

             else:
                newStateC = State_WorkOffice;
                self.ChangeCurrentState(newStateC);

         elif self.m_Hunger < 50:
            if self.m_Location != "Restaurant":
               self.m_GoalLoc = "Restaurant";
               newStateC = State_WalkTo;
               self.ChangeCurrentState(newStateC);
               newStateG = State_Eat;
               self.ChangeFutureState(newStateG);

            else:
               newStateC = State_Eat;
               self.ChangeCurrentState(newStateC);

         else:
             pass

#WIP
class State_Eat(State):
    def Enter(self):
        self.m_Location = "Restaurant";
        print (self.m_Name+ ": Ooooh! Tasty food! Yummy!")

    def Execute(self):
        print (self.m_Name+ ": Nom nom nom!");
        self.m_Hunger += 5;

    def Exit(self):
        print (self.m_Name+ ": Ohm nom! Bhaaa, I'm so stuffed now");

        #Exit states, check what todo next

#WIP
class State_Drink(State):
    def Enter(self):
        self.m_Location = "Traversen";
        print (self.m_Name+ ": Hi again! I want some Budvar!");

    def Execute(self):
        print (self.m_Name+ ": *glup glup glup* Whaoeguaoihoa...");
        self.m_Thirst += 7;

    def Exit(self):
        print (self.m_Name+ ": Aaaaah! That was good, bye bye!");

        #Exit states, check what todo next

#WIP
class State_WorkOffice(State):
    def Enter(self):
        self.m_Location = "Downtown Office";
        print (self.m_Name+ ": 'AI Interactive', my work place! Let's get that cash!")

    def Execute(self):
        print (self.m_Name+ ": 01001101101... Beep Boop Office Work!");
        self.m_Cash += 10;

    def Exit(self):
        print (self.m_Name+ ": Phew, hard work pays off! I'm signing out for today!");

        #Exit states, check what todo next

#WIP
class State_WorkHunt(State):
    def Enter(self):
        self.m_Location = "Northern Forest";

    def Execute(self):
        pass

    def Exit(self):
        print (self.m_Name+ ": Time to go home, it's was nice being out here on my hunter spot");

        #Exit states, check what todo next

#WIP
class State_Socialize(State):
    def Enter(self):
        pass

    def Execute(self):
        print(self.m_Name+ ": How's the weather? Have you seen the latest episode of GoT?");
        self.m_SocialNeed += 4;

    def Exit(self):
        print (self.m_Name+ ": Time to go home, it's was nice being out here on my hunter spot");

        #Exit states, check what todo next

#Done-ish
class State_WalkTo(State):
    def Enter(self):
        #HOME START
        #Home and Downtown Office dist
        if self.m_Location == "Home" and self.m_GoalLoc == "Downtown Office" or self.m_Location == "Downtown Office" and self.m_GoalLoc == "Home":
            self.m_distToGoal = 40;

        #Home and The Mall dist
        elif self.m_Location == "Home" and self.m_GoalLoc == "The Mall" or self.m_Location == "The Mall" and self.m_GoalLoc == "Home":
            self.self.m_distToGoal = 16;

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
        self.m_Energy -= 1;
        print(str(self.m_walkedDistance)+ "m traversed");

        if self.m_walkedDistance >= self.m_distToGoal:
            self.m_pCurrentState.Exit(self);

    def Exit(self):
        print ("Destination have been reached!")
        print ("");
        newStateC = self.m_pGoalState;
        self.ChangeCurrentState(newStateC);
        newStateG = None;
        self.ChangeFutureState(newStateG);
        self.m_distToGoal = 0;
        self.m_GoalLoc = None;

#WIP
class State_Die(State):
    def Enter(self):
        self.m_Location = "The Bright Tunnel";
        print (self.m_Name+ " died");

    def Execute(self):
        pass

    def Exit(self):
        print (self.m_Name+ " has been erased from the list of active AI");

        #Exit states, check what todo next

#WIP
class humanoid(baseGameEntity):
    m_pCurrentState = None;
    m_pGoalState = None; #Only used if the agent is not at correct location
    m_Location = None; #In the future we can set this to a vector of spawn, then move it towards a PoI in engine and check vector math for distance
    m_GoalLoc = None; #Wiped upon arrival to location
    m_ClockRef = None;
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

    def humanoid(self, name, aID, clock):
        self.m_Name = name;
        self.m_EntityName = "Humanoid_" +name;
        self.m_EntityID = aID;
        self.m_Location = "Home";
        self.m_ClockRef = clock;
        self.m_Cash = 500;
        self.m_Hunger = 30;
        self.m_Thirst = 100;
        self.m_Energy = 30;
        self.m_SocialNeed = 60;
        self.m_WorkSkill = 20;
        self.m_walkingSpeed = 1;
        self.m_walkedDistance = 0;
        self.m_distToGoal = 0;
        self.m_pCurrentState = State_Sleep;

        return self;

    def Update(self):
        self.m_pCurrentState.Execute(self);

    def ChangeCurrentState(self, newStateC):
        self.m_pCurrentState = None;
        self.m_pCurrentState = newStateC;
        self.m_pCurrentState.Enter(self);

    def ChangeFutureState(self, newStateG):
        self.m_pGoalState = None;
        self.m_pGoalState = newStateG;