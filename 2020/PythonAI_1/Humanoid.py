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
            self.m_ROS = randint(0, 80);
            
            if self.m_ROS > 76:
                self.m_Sick = True;
                print (self.m_Name+ ": Sick... lel");
                seed(datetime.now());
                self.m_SL = randint(0, 2);
                print ("Rand SL is: " +str(self.m_SL));

            else:
                self.m_Sick = False;
                self.m_SL = 0;
                print (self.m_Name+ ": Healthy!");

            print (self.m_Name+ ": Zzz...");
            self.m_Energy += 3;

        elif self.m_ClockRef.cTime == "08:00":
            if self.m_SocialNeed < 500:
                if self.m_PhoneRef.posConn > 1:
                    self.AskToHangout();
                else:
                    print (self.m_Name+ ": The world is so lonely :c");

            self.m_pCurrentState.Exit(self);

        elif (self.m_ClockRef.calHour < 8 or self.m_ClockRef.calHour > 21) or self.m_Energy < 60:
            print (self.m_Name+ ": Zzz...");
            self.m_Energy += 1;

    def Exit(self):
        if self.m_pGoalState == State_Socialize:
            newStateC = State_WalkTo;
            self.ChangeCurrentState(newStateC);

        else:
            print (self.m_Name+ ": Erghe... Augh! Goodmorning World!")

            #FOOD
            if self.m_Hunger < 50 and self.m_Cash >= 400:
                if self.m_Location != "The Restaurant":
                   self.m_GoalLoc = "The Restaurant";
                   newStateC = State_WalkTo;
                   self.ChangeCurrentState(newStateC);
                   newStateG = State_Eat;
                   self.ChangeGoalState(newStateG);

                else:
                   newStateC = State_Eat;
                   self.ChangeCurrentState(newStateC);

            #THIRST
            elif self.m_Thirst < 50 and self.m_Cash >= 400:
                if self.m_Location != "Traversen":
                   self.m_GoalLoc = "Traversen";
                   newStateC = State_WalkTo;
                   self.ChangeCurrentState(newStateC);
                   newStateG = State_Eat;
                   self.ChangeGoalState(newStateG);

                else:
                   newStateC = State_Eat;
                   self.ChangeCurrentState(newStateC);

            #SOCIAL
            elif self.m_SocialNeed < 4 and self.m_Cash >= 200:
                if self.m_Location != "Traversen":
                   self.m_GoalLoc = "Traversen";
                   newStateC = State_WalkTo;
                   self.ChangeCurrentState(newStateC);
                   newStateG = State_Eat;
                   self.ChangeGoalState(newStateG);

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
                        self.ChangeGoalState(newStateG);

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
                    self.ChangeGoalState(newStateG);

                #If you don't own a gun and can't afford one
                elif self.m_OwnsGun == False and self.m_Cash < 500:
                    print (self.m_Name+ ": I can't afford a gun, reeeeee... Guess I have to work in the office");

                    if self.m_Location != "Downtown Office":
                        self.m_GoalLoc = "Downtown Office";
                        newStateC = State_WalkTo;
                        self.ChangeCurrentState(newStateC);
                        newStateG = State_WorkOffice;
                        self.ChangeGoalState(newStateG);

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
                        self.ChangeGoalState(newStateG);

                    else:
                        newStateC = State_WorkOffice;
                        self.ChangeCurrentState(newStateC);

#WIP
class State_Eat(State):
    def Enter(self):
        print (self.m_Name+ ": Ooooh! Tasty food! Yummy!")

    def Execute(self):
        print (self.m_Name+ ": Nom nom nom!");
        self.m_Hunger += 6 - self.m_SL;
        self.m_Cash -= 5;
        print (self.m_Name+ " (CASH): " +str(self.m_Cash));
        print (self.m_Name+ " (HUNGER): " +str(self.m_Hunger));

        if self.m_Cash < 40 or self.m_Hunger > 380:
            if self.m_SocialNeed < 500:
                if self.m_PhoneRef.posConn > 1:
                    self.AskToHangout();
                else:
                    print (self.m_Name+ ": The world is so lonely :c");

            self.m_pCurrentState.Exit(self);

    def Exit(self):
        if self.m_Hunger > 380:
            print (self.m_Name+ ": Ohm nom! Bhaaa, I'm so stuffed now");

        #SLEEP
        if self.m_Energy < 30:
            if self.m_Location != "Home":
                self.m_GoalLoc = "Home";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = State_Sleep;
                self.ChangeGoalState(newStateG);

            else:
                newStateC = State_Sleep;
                self.ChangeCurrentState(newStateC);

        if self.m_pPreviousState == State_WorkOffice:
            print (self.m_Name+ ": I'm going back to work now");

            if self.m_Location != "Downtown Office":
                self.m_GoalLoc = "Downtown Office";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = self.m_pPreviousState;
                self.ChangeGoalState(newStateG);

            else:
                newStateC = self.m_pPreviousState;
                self.ChangeCurrentState(newStateC);

        #THIRST
        elif self.m_Thirst < 30 and self.m_Cash >= 50:
            if self.m_Location != "Traversen":
                self.m_GoalLoc = "Traversen";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = State_Eat;
                self.ChangeGoalState(newStateG);

            else:
                newStateC = State_Eat;
                self.ChangeCurrentState(newStateC);

        #Time to move home
        elif self.m_ClockRef.calHour >= 19:
                print (self.m_Name+ ": I think I'm going home for today!");

                if self.m_Location != "Home":
                    self.m_GoalLoc = "Home";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_Sleep;
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_Sleep;
                    self.ChangeCurrentState(newStateC);

        #WORK
        elif self.m_Cash < 1000:
            #If you own a gun and a little wealthy
            if self.m_OwnsGun == True and self.m_Cash >= 500:
                print (self.m_Name+ ": I own a gun and I have plenty of cash, a hunting day can't hurt that much!");
                if self.m_Location != "Northern Forest":
                    self.m_GoalLoc = "Northern Forest";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_WorkHunt;
                    self.ChangeGoalState(newStateG);

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
                self.ChangeGoalState(newStateG);

            #If you don't own a gun and can't afford one
            elif self.m_OwnsGun == False and self.m_Cash < 500:
                print (self.m_Name+ ": I can't afford a gun, reeeeee... Guess I have to work in the office");

                if self.m_Location != "Downtown Office":
                    self.m_GoalLoc = "Downtown Office";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_WorkOffice;
                    self.ChangeGoalState(newStateG);

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
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_WorkOffice;
                    self.ChangeCurrentState(newStateC);

#WIP
class State_Drink(State):
    def Enter(self):
        print (self.m_Name+ ": Ooooh! A cold refreshing drink!")

    def Execute(self):
        print (self.m_Name+ ": *glub glub glub* Hahahaaa, waahgerhugha!");
        self.m_Thirst += 14 - self.m_SL;
        self.m_Cash -= 5;
        print (self.m_Name+ " (CASH): " +str(self.m_Cash));
        print (self.m_Name+ " (THIRST): " +str(self.m_Thirst));

        if self.m_Cash < 40 or self.m_Thirst > 240:
            if self.m_SocialNeed < 500:
                if self.m_PhoneRef.posConn > 1:
                    self.AskToHangout();
                else:
                    print (self.m_Name+ ": The world is so lonely :c");

            self.m_pCurrentState.Exit(self);

    def Exit(self):
        if self.m_Thirst > 240:
            print (self.m_Name+ ": Ghaaa! That was refreshing!");

        #SLEEP
        if self.m_Energy < 30:
            if self.m_Location != "Home":
                self.m_GoalLoc = "Home";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = State_Sleep;
                self.ChangeGoalState(newStateG);

            else:
                newStateC = State_Sleep;
                self.ChangeCurrentState(newStateC);

        if self.m_pPreviousState == State_WorkOffice:
            print (self.m_Name+ ": I'm going back to work now");

            if self.m_Location != "Downtown Office":
                self.m_GoalLoc = "Downtown Office";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = self.m_pPreviousState;
                self.ChangeGoalState(newStateG);

            else:
                newStateC = self.m_pPreviousState;
                self.ChangeCurrentState(newStateC);

        #HUNGER
        elif self.m_Hunger < 30 and self.m_Cash >= 50:
            if self.m_Location != "The Restaurant":
                self.m_GoalLoc = "The Restaurant";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = State_Eat;
                self.ChangeGoalState(newStateG);

            else:
                newStateC = State_Eat;
                self.ChangeCurrentState(newStateC);

        #Time to move home
        elif self.m_ClockRef.calHour >= 19:
            print (self.m_Name+ ": I think I'm going home for today!");

            if self.m_Location != "Home":
                self.m_GoalLoc = "Home";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = State_Sleep;
                self.ChangeGoalState(newStateG);

            else:
                newStateC = State_Sleep;
                self.ChangeCurrentState(newStateC);

        #WORK
        elif self.m_Cash < 1000:
            #If you own a gun and a little wealthy
            if self.m_OwnsGun == True and self.m_Cash >= 500:
                print (self.m_Name+ ": I own a gun and I have plenty of cash, a hunting day can't hurt that much!");
                if self.m_Location != "Northern Forest":
                    self.m_GoalLoc = "Northern Forest";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_WorkHunt;
                    self.ChangeGoalState(newStateG);

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
                self.ChangeGoalState(newStateG);

            #If you don't own a gun and can't afford one
            elif self.m_OwnsGun == False and self.m_Cash < 500:
                print (self.m_Name+ ": I can't afford a gun, reeeeee... Guess I have to work in the office");

                if self.m_Location != "Downtown Office":
                    self.m_GoalLoc = "Downtown Office";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_WorkOffice;
                    self.ChangeGoalState(newStateG);

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
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_WorkOffice;
                    self.ChangeCurrentState(newStateC);

#WIP
class State_WorkOffice(State):
    def Enter(self):
        print (self.m_Name+ ": 'AI Interactive', my work place! Let's get that cash!")

    def Execute(self):

        if self.m_Hunger <= 0 or self.m_Thirst <= 0:
            print (self.m_Name+ ": OOOOOF");
            newStateC = State_Die;
            self.ChangeCurrentState(newStateC);
            self.m_pCurrentState.Enter(self);

        elif self.m_ClockRef.calHour >= 17 or self.m_Cash > 2000 or self.m_Hunger < 25 or self.m_Thirst < 20 or self.m_Energy < 30:
            if self.m_SocialNeed < 500 and self.m_pFutureState == None:
                if self.m_PhoneRef.posConn > 1:
                    self.AskToHangout();
                else:
                    print (self.m_Name+ ": The world is so lonely :c");

            self.m_pCurrentState.Exit(self);

        else:
            print (self.m_Name+ ": 01001101101... Beep Boop Office Work!");
            self.m_Cash += 2;
            self.m_SocialNeed -= 1;
            self.m_Energy -= 1 + self.m_SL;
            self.m_Hunger -= 1 + self.m_SL;
            self.m_Thirst -= 1 + self.m_SL;

    def Exit(self):
        if self.m_pGoalState == State_Socialize:
            newStateC = State_WalkTo;
            self.ChangeCurrentState(newStateC);

        else:
            #SLEEP
            if self.m_Energy < 30:

                print (self.m_Name+ ": Phew, hard work pays off! I'm signing out for today!");

                if self.m_Location != "Home":
                    self.m_GoalLoc = "Home";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_Sleep;
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_Sleep;
                    self.ChangeCurrentState(newStateC);

            #FOOD
            elif self.m_Hunger < 25 and self.m_Cash >= 40:

                print (self.m_Name+ ": I'm quite hungry! I'm signing out for now!");
                newStateP = State_WorkOffice;
                self.ChangePreviousState(newStateP);

                if self.m_Location != "The Restaurant":
                    self.m_GoalLoc = "The Restaurant";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_Eat;
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_Eat;
                    self.ChangeCurrentState(newStateC);

            #THIRST
            elif self.m_Thirst < 20 and self.m_Cash >= 50:

                print (self.m_Name+ ": I'm quite thirsty! I'm signing out for now!");

                if self.m_Location != "Traversen":
                    self.m_GoalLoc = "Traversen";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_Drink;
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_Drink;
                    self.ChangeCurrentState(newStateC);

            #Time to move home
            elif self.m_ClockRef.calHour >= 17:
                    print (self.m_Name+ ": I think I'm going home for today!");

                    if self.m_Location != "Home":
                        self.m_GoalLoc = "Home";
                        newStateC = State_WalkTo;
                        self.ChangeCurrentState(newStateC);
                        newStateG = State_Sleep;
                        self.ChangeGoalState(newStateG);

                    else:
                        newStateC = State_Sleep;
                        self.ChangeCurrentState(newStateC);

            #WORK
            else:
                #If you own a gun and a little wealthy
                if self.m_OwnsGun == True and self.m_Cash >= 800:
                    print (self.m_Name+ ": I own a gun and I have plenty of cash, a hunting day can't hurt that much!");
                    if self.m_Location != "Northern Forest":
                        self.m_GoalLoc = "Northern Forest";
                        newStateC = State_WalkTo;
                        self.ChangeCurrentState(newStateC);
                        newStateG = State_WorkHunt;
                        self.ChangeGoalState(newStateG);

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
                    self.ChangeGoalState(newStateG);

#WIP
class State_WorkHunt(State):
    def Enter(self):
        print (self.m_Name+ ": Out in the woods, lalalala")

    def Execute(self):

        if self.m_Hunger <= 0 or self.m_Thirst <= 0 or self.m_SocialNeed <= 0:
            print (self.m_Name+ ": OOOOOF");
            newStateC = State_Die;
            self.ChangeCurrentState(newStateC);
            self.m_pCurrentState.Enter(self);

        if self.m_ClockRef.calHour >= 19 or self.m_Cash > 2000 or self.m_Hunger < 25 or self.m_Thirst < 20 or self.m_Energy < 30:

            print (self.m_Name+ ": Finished hunting for today! I got a total of " +str(self.m_huntingScore)+ " elks today!");
            self.m_Cash += self.m_huntingScore * 250;
            print (self.m_Name+ " got a total of " +str(self.m_huntingScore * 250)+ "kr today from hunting!");
            self.m_huntingScore = 0;

            if self.m_SocialNeed < 500:
                if self.m_PhoneRef.posConn > 1:
                    self.AskToHangout();
                else:
                    print (self.m_Name+ ": The world is so lonely :c");

            self.m_pCurrentState.Exit(self);

        else:
            print (self.m_Name+ ": Hunt, hunt, hunting!");
            self.m_SocialNeed -= 1;
            self.m_Energy -= 1 + self.m_SL;
            self.m_Hunger -= 1 + self.m_SL;
            self.m_Thirst -= 1 + self.m_SL;

            ASC = randint(0, 100);
            if ASC > 92:
                print (self.m_Name+ ": OMG! An elk! Time for a shot!");

                HTC = randint(0, 50);
                if HTC > 30:
                    self.m_huntingScore += 1;
                    print (self.m_Name+ ": YES! I got a hit!");
                    print (self.m_Name+ " has a total of " +str(self.m_huntingScore)+ " elks today!");

                else:
                    print (self.m_Name+ ": Awww... I missed");

    def Exit(self):

        if self.m_pGoalState == State_Socialize:
            newStateC = State_WalkTo;
            self.ChangeCurrentState(newStateC);

        else:
            #SLEEP
            if self.m_Energy < 30:
                print (self.m_Name+ ": Argh! I'm so tired, time to go home and sleep");

                if self.m_Location != "Home":
                    self.m_GoalLoc = "Home";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_Sleep;
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_Sleep;
                    self.ChangeCurrentState(newStateC);

            #FOOD
            elif self.m_Hunger < 25 and self.m_Cash >= 40:

                print (self.m_Name+ ": I'm quite hungry! I'm leaving my hunting spot for now!");
                newStateP = State_WorkHunt;
                self.ChangePreviousState(newStateP);

                if self.m_Location != "The Restaurant":
                    self.m_GoalLoc = "The Restaurant";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_Eat;
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_Eat;
                    self.ChangeCurrentState(newStateC);

            #THIRST
            elif self.m_Thirst < 20 and self.m_Cash >= 50:

                print (self.m_Name+ ": I'm quite thirsty! I'm leaving my hunting spot for now!");
                newStateP = State_WorkHunt;
                self.ChangePreviousState(newStateP);

                if self.m_Location != "Traversen":
                    self.m_GoalLoc = "Traversen";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_Drink;
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_Drink;
                    self.ChangeCurrentState(newStateC);

            #Time to move home
            elif self.m_ClockRef.calHour >= 19:
                print (self.m_Name+ ": I think I'm going home for today!");

                if self.m_Location != "Home":
                    self.m_GoalLoc = "Home";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_Sleep;
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_Sleep;
                    self.ChangeCurrentState(newStateC);

            #WORK
            elif self.m_Cash < 2000:
                #If you own a gun and a little wealthy
                if self.m_OwnsGun == True and self.m_Cash >= 800:
                    print (self.m_Name+ ": I own a gun and I have plenty of cash, a hunting day can't hurt that much!");
                    if self.m_Location != "Northern Forest":
                        self.m_GoalLoc = "Northern Forest";
                        newStateC = State_WalkTo;
                        self.ChangeCurrentState(newStateC);
                        newStateG = State_WorkHunt;
                        self.ChangeGoalState(newStateG);

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
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_Sleep;
                    self.ChangeCurrentState(newStateC);
        #Exit states, check what todo next

#WIP - REQUIER TELECOM SCRIPT
class State_Socialize(State):
    def Enter(self):
        print(self.m_Name+ ": Oh hey it's you! Wazzup! :D")

    def Execute(self):

        if self.m_Hunger <= 0 or self.m_Thirst <= 0:
            print (self.m_Name+ ": OOOOOF");
            newStateC = State_Die;
            self.ChangeCurrentState(newStateC);
            self.m_pCurrentState.Enter(self);

        if self.m_SocialNeed > 1750 or self.m_Cash < 60 or self.m_Energy < 50:
            print (self.m_Name+ ": I'm sorry but I have to go now");
            self.m_PersonToMeet.m_pCurrentState.Exit(self.m_PersonToMeet);
            self.m_pCurrentState.Exit(self);

        else:
            if self.m_PersonToMeet.m_SocialNeed <= 1750 or self.m_PersonToMeet.m_Cash >= 60:
                print (self.m_Name+ ": " +self.m_PhoneRef.MSG_Socialize_Conversation[randint(0, len(self.m_PhoneRef.MSG_Socialize_Conversation) - 1)]);

            if self.m_Location == "The Park":
                self.m_SocialNeed += 60 - self.m_SL;

            elif self.m_Location == "The Restaurant":
                self.m_SocialNeed += 60 - self.m_SL;
                self.m_Hunger += 1 - self.m_SL;
                self.m_Energy -= 1;
                self.m_Cash -= 10;

            elif self.m_Location == "Traversen":
                self.m_SocialNeed += 65 - self.m_SL;
                self.m_Thirst += 1 - self.m_SL;
                self.m_Energy -= 1;
                self.m_Cash -= 5;

    def Exit(self):
        print (self.m_Name+ ": Bye " +self.m_PersonToMeet.m_Name+ "! See you another time!");
        newStateF = None;
        self.ChangeFutureState(newStateF); #Set to none to let people know they can be met again

        #SLEEP
        if self.m_Energy < 50:
            if self.m_Location != "Home":
                self.m_GoalLoc = "Home";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = State_Sleep;
                self.ChangeGoalState(newStateG);

            else:
                newStateC = State_Sleep;
                self.ChangeCurrentState(newStateC);

        #FOOD
        elif self.m_Hunger < 50 and self.m_Cash >= 400:
            if self.m_Location != "The Restaurant":
                self.m_GoalLoc = "The Restaurant";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = State_Eat;
                self.ChangeGoalState(newStateG);

            else:
                newStateC = State_Eat;
                self.ChangeCurrentState(newStateC);

        #THIRST
        elif self.m_Thirst < 50 and self.m_Cash >= 400:
            if self.m_Location != "Traversen":
                self.m_GoalLoc = "Traversen";
                newStateC = State_WalkTo;
                self.ChangeCurrentState(newStateC);
                newStateG = State_Eat;
                self.ChangeGoalState(newStateG);

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
                    self.ChangeGoalState(newStateG);

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
                self.ChangeGoalState(newStateG);

            #If you don't own a gun and can't afford one
            elif self.m_OwnsGun == False and self.m_Cash < 500:
                print (self.m_Name+ ": I can't afford a gun, reeeeee... Guess I have to work in the office");

                if self.m_Location != "Downtown Office":
                    self.m_GoalLoc = "Downtown Office";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_WorkOffice;
                    self.ChangeGoalState(newStateG);

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
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_WorkOffice;
                    self.ChangeCurrentState(newStateC);
        #Exit states, check what todo next

#WIP
class State_Idle(State):
    def Enter(self):
        print (self.m_Name+ ": What should I do now? Hmmm");
     
    def Execute(self):

        if self.m_Hunger <= 0 or self.m_Thirst <= 0 or self.m_SocialNeed <= 0:
            print (self.m_Name+ ": OOOOOF");
            newStateC = State_Die;
            self.ChangeCurrentState(newStateC);
            self.m_pCurrentState.Enter(self);

        self.m_Hunger -= 1;
        self.m_Thirst -= 1;
        self.m_SocialNeed -= 1;

        if self.m_pGoalState == State_Socialize:
            if self.m_PersonToMeet.m_Location == self.m_Location:
                newStateC = self.m_pGoalState;
                self.ChangeCurrentState(newStateC);
                newStateG = None;
                self.ChangeGoalState(newStateG);

            else:
                print (self.m_Name+ ": I'm waiting for my friend~");

        elif self.m_pGoalState == State_WorkOffice:
            print (self.m_Name+ ": I'm waiting for office hours to begin");

        elif self.m_Location == "Home":
            #FOOD
            if self.m_Hunger < 30 and self.m_Cash >= 40:
                print (self.m_Name+ ": I'm quite hungry! I need some food before going to bed!");
                newStateP = State_Sleep;
                self.ChangePreviousState(newStateP);

                if self.m_Location != "The Restaurant":
                    self.m_GoalLoc = "The Restaurant";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_Eat;
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_Eat;
                    self.ChangeCurrentState(newStateC);

            #THIRST
            elif self.m_Thirst < 30 and self.m_Cash >= 50:
                print (self.m_Name+ ": I'm quite thirsty! I need a drink before going to bed!");

                newStateP = State_Sleep;
                self.ChangePreviousState(newStateP);

                if self.m_Location != "Traversen":
                    self.m_GoalLoc = "Traversen";
                    newStateC = State_WalkTo;
                    self.ChangeCurrentState(newStateC);
                    newStateG = State_Drink;
                    self.ChangeGoalState(newStateG);

                else:
                    newStateC = State_Drink;
                    self.ChangeCurrentState(newStateC);

            elif self.m_ClockRef.calHour < 21 or (self.m_ClockRef.calHour <= 21 and self.m_ClockRef.calMin < 50):
                    print (self.m_Name+ ": Watching TV and just relaxing before going to bed");

            elif self.m_ClockRef.calHour >= 22:
                if self.m_SocialNeed < 500:
                    if self.m_PhoneRef.posConn > 1:
                        self.AskToHangout();
                    else:
                        print (self.m_Name+ ": The world is so lonely :c");

                newStateC = self.m_pGoalState;
                self.ChangeCurrentState(newStateC);
                newStateG = None;
                self.ChangeGoalState(newStateG);
                self.ChangePreviousState(newStateG);

            else:
                print (self.m_Name+ ": Preparing to go to bed, brushing teeth and putting on my pyamas");
    
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
        elif self.m_Location == "Home" and self.m_GoalLoc == "The Restaurant" or self.m_Location == "The Restaurant" and self.m_GoalLoc == "Home":
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

        #Downtown Office and The Restaurant dist
        elif self.m_Location == "Downtown Office" and self.m_GoalLoc == "The Restaurant" or self.m_Location == "The Restaurant" and self.m_GoalLoc == "Downtown Office":
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

        #The Restaurant START
        #The Restaurant and The Mall dist
        elif self.m_Location == "The Restaurant" and self.m_GoalLoc == "The Mall" or self.m_Location == "The Mall" and self.m_GoalLoc == "The Restaurant":
            self.m_distToGoal = 20;

        #The Restaurant and Traversen dist
        elif self.m_Location == "The Restaurant" and self.m_GoalLoc == "Traversen" or self.m_Location == "Traversen" and self.m_GoalLoc == "The Restaurant":
            self.m_distToGoal = 10;

        #The Restaurant and Northern Forest dist
        elif self.m_Location == "The Restaurant" and self.m_GoalLoc == "Northern Forest" or self.m_Location == "Northern Forest" and self.m_GoalLoc == "The Restaurant":
            self.m_distToGoal = 46;

        #The Restaurant and The Park dist
        elif self.m_Location == "The Restaurant" and self.m_GoalLoc == "The Park" or self.m_Location == "The Park" and self.m_GoalLoc == "The Restaurant":
            self.m_distToGoal = 14;
        #The Restaurant STOP

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
        self.m_Hunger -= 1;
        self.m_Thirst -= 1;
        self.m_Energy -= 1 + self.m_SL;
        self.m_SocialNeed -= 1;
        print(self.m_Name+ ": " +str(self.m_walkedDistance)+ "m traversed");

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

        print ("Destination have been reached!");
        print ("");
        self.m_Location = self.m_GoalLoc;
        self.m_walkedDistance = 0;
        self.m_distToGoal = 0;

        if self.m_pGoalState == State_Socialize:
            newStateC = State_Idle;
            self.ChangeCurrentState(newStateC);
            self.m_GoalLoc = None;

        elif self.m_pGoalState == State_Sleep and self.m_ClockRef.calHour < 21:
            newStateC = State_Idle;
            self.ChangeCurrentState(newStateC);
            self.m_GoalLoc = None;

        else:
            newStateC = self.m_pGoalState;
            self.ChangeCurrentState(newStateC);
            newStateG = None;
            self.ChangeGoalState(newStateG);
            self.m_GoalLoc = None;

#Done-ish
class State_Die(State):
    def Enter(self):
        self.m_Location = "The Bright Tunnel";

    def Execute(self):
        self.m_pCurrentState.Exit(self);

    def Exit(self):
        self.DeathAnnounce();
        newStateC = None;
        self.ChangeCurrentState(newStateC);
        self.m_Alive = False;

#WIP
class humanoid(baseGameEntity):
    m_pPreviousState = None; #What did the AI do before? In case we want to go back to our previous state
    m_pCurrentState = None;
    m_pGoalState = None; #Only used if the agent is not at correct location
    m_pFutureState = None; #Used for planing activities a bit into the future
    m_Location = None; #In the future we can set this to a vector of spawn, then move it towards a PoI in engine and check vector math for distance
    m_GoalLoc = None; #Wiped upon arrival to location
    m_ClockRef = None;
    m_PhoneRef = None;
    m_Cash = 0;
    m_Hunger = 0;
    m_Thirst = 0;
    m_Energy = 0;
    m_SocialNeed = 0;
    m_PersonToMeet = None;
    m_huntingScore = 0; #How many elks did you shoot today?
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
        self.m_Cash = randint(200, 300);
        self.m_Hunger = randint(200, 260);
        self.m_Thirst = randint(350, 400);
        self.m_Energy = randint(180, 200);
        self.m_SocialNeed = randint(1400, 2360);
        self.m_walkingSpeed = randint(2, 4);
        self.m_pCurrentState = State_Sleep;

        return self;

    #DONE
    def Update(self):
        self.m_pCurrentState.Execute(self);

    #DONE
    def ChangePreviousState(self, newStateP):
        self.m_pPreviousState = None;

        if newStateP == None:
            pass

        else:
            self.m_pPreviousState = newStateP;

    #DONE
    def ChangeCurrentState(self, newStateC):
        self.m_pCurrentState = None;

        if newStateC == None:
            pass

        else:
            self.m_pCurrentState = newStateC;
            self.m_pCurrentState.Enter(self);

    #DONE
    def ChangeGoalState(self, newStateG):
        self.m_pGoalState = None;
        self.m_pGoalState = newStateG;

        #DONE
    def ChangeFutureState(self, newStateF):
        self.m_pFutureState = None;
        self.m_pFutureState = newStateF;

    #DONE
    def AskToHangout(self):
        s = self.ConnSender();
        r = self.ConnRecieveer();
        t = self.ConnTime();
        l = self.ConnLocation();
        message = self.m_PhoneRef.SMS().Message(s, r, 1, self.m_PhoneRef.MSG_MeetUp_Question[randint(0, len(self.m_PhoneRef.MSG_MeetUp_Question) - 1)], t,  self.m_PhoneRef.meetingsSpots[l], None);
        self.m_PhoneRef.SendMSG(message);

    #DONE
    def DeathAnnounce(self):
        print ("I'm sad to announce that " +self.m_Name+ " has passed away </3");

        for i in self.m_PhoneRef.phoneBook:
            if i.m_Name == self.m_Name:
                pass;
            else:
                s = self.ConnSender();
                message = self.m_PhoneRef.SMS().Message(s, i, 7, self.m_PhoneRef.MSG_Death_Announcement[randint(0, len(self.m_PhoneRef.MSG_Death_Announcement) - 1)], None,  None, None);
                self.m_PhoneRef.SendMSG(message);

    #DONE
    def ConnSender(self):
        return self;

    #DONE
    def ConnRecieveer(self):
        connID = randint(0, self.m_PhoneRef.posConn - 1);
        contactAI = self.m_PhoneRef.phoneBook[connID];

        while contactAI.m_Name == self.m_Name:
            print ("Can't send message to yourself!");
            connID = randint(0, self.m_PhoneRef.posConn - 1);
            contactAI = self.m_PhoneRef.phoneBook[connID];

        return contactAI;

    #DONE
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

    #DONE
    def ConnLocation(self):
        return randint(0, self.m_PhoneRef.posMeeting - 1);