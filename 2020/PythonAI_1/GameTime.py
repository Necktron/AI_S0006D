class gameTime():

    updateRate = 0.000001;

    calHour = 0;
    calMin = 0;
    calDays = 0;
    calMonths = 0;
    calYears = 2020;

    cHour = None;
    cMin = None;
    cTime = None;

    #Adjust updateRate during runtime
    def ChangeUR(self, float):
        global updateRate
        self.updateRate = float;

    #Update clock system
    def Update(self):
        global calHour
        global calMin
        global calDays
        global calMonths;
        self.calMin += 1;

        if self.calMin >= 60:
            self.calMin = 0;
            self.calHour += 1;

            if self.calHour >= 24:
                self.calDays += 1;
                self.calHour = 0;
                print ("");
                print (str(self.calDays)+ " days have past");
                print ("");

                if self.calDays >= 30:
                    self.calMonths += 1;
                    self.calDays = 0;
                    print ("");
                    print (str(self.calMonths)+ " months have past");
                    print ("");

                    if self.calMonths >= 12:
                        self.calYears += 1;
                        self.calMonths = 0;
                        print ("");
                        print(str(self.calYears)+ " is here, HAPPY NEW YEAR!");
                        print ("");

        if self.calHour < 10:
            self.cHour = "0" + str(self.calHour);

        else:
            self.cHour = str(self.calHour);

        if self.calMin < 10:
            global cMin
            self.cMin = "0" + str(self.calMin);

        else:
            self.cMin = str(self.calMin);

        global cTime
        self.cTime = self.cHour+ ":" +self.cMin;
        return self.cTime;
        #COMPLETE, DO NOT TOUCH