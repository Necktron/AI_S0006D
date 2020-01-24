from BaseGameEntity import baseGameEntity;
from GameTime import gameTime;

class State:
    def Enter(self):
        pass

    def Execute(self):
        pass

    def Exit(self):
        pass

class State_Sleep(State):
    def Enter(self):
        print (self.m_Name+ ": It will be good with a bit of sleep now! Goodnight!")

    def Execute(self):
        if self.m_ClockRef.cTime == "08:00":
            self.m_pCurrentState.Exit(self);

        elif self.m_ClockRef.calHour < 8:
            print (self.m_Name+ ": Zzz...")

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

class State_Eat(State):
    def Enter(self):
        self.m_Location = "Restaurant";
        print (self.m_Name+ ": Ooooh! Tasty food! Yummy!")

    def Execute(self):
        self.Eat();

    def Exit(self):
        pass

class State_Drink(State):
    def Enter(self):
        self.m_Location = "Traversen";
        pass

    def Execute(self):
        pass

    def Exit(self):
        pass

class State_WorkOffice(State):
    def Enter(self):
        self.m_Location = "Downtown Office";
        print (self.m_Name+ ": 'AI Interactive', my work place! Let's get that cash!")

    def Execute(self):
        self.WorkOffice();

    def Exit(self):
        pass

class State_WorkHunt(State):
    def Enter(self):
        self.m_Location = "Northern Forest";

    def Execute(self):
        pass

    def Exit(self):
        pass

class State_Socialize(State):
    def Enter(self):
        pass

    def Execute(self):
        pass

    def Exit(self):
        pass

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

    def Execute(self):
        self.Walk();

    def Exit(self):
        pass

class State_Die(State):
    def Enter(self):
        pass

    def Execute(self):
        pass

    def Exit(self):
        pass

class humanoid(baseGameEntity):
    m_pCurrentState = None;
    m_pGoalState = None; #Only used if the agent is not at correct location
    m_Location = None; #In the future we can set this to a vector of spawn, then move it towards a PoI in engine and check vector math for distance
    m_GoalLoc = None;
    m_ClockRef = None;
    m_Cash = 0;
    m_Hunger = 0;
    m_Thirst = 0;
    m_Energy = 0;
    m_SocialNeed = 0;
    m_WorkSkill = 0;
    m_walkingSpeed = 0;
    m_walkedDistance = 0;
    m_distToGoal = 0;
    m_ROS = 0;
    m_SL = 0;

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
        self.m_walkingSpeed = 10;
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

    def Rest(self):
        self.m_Energy += 1;

    def Eat(self):
        print (self.m_Name+ ": Nom nom nom!");
        self.m_Hunger += 1;

    def Drink(self):
        pass

    def WorkOffice(self):
        print (self.m_Name+ ": 01001101101... Beep Boop Office Work!");
        self.m_Cash += 1;

    def WorkHunt(self):
        pass

    def Socialize(self):
        pass

    def Walk(self):
        self.m_walkedDistance += self.m_walkingSpeed;
        self.m_Energy -= 1;
        print(str(self.m_walkedDistance)+ "m traversed");

        if self.m_walkedDistance >= self.m_distToGoal:
            print ("Destination have been reached!")
            print ("");
            newStateC = self.m_pGoalState;
            self.ChangeCurrentState(newStateC);
            newStateG = None;
            self.ChangeFutureState(newStateG);
            self.m_distToGoal = 0;
            self.m_GoalLoc = None;