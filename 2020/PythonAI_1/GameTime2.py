class GameTime:

    updateRate = 1000;

    hour = 0;
    min = 0;
    days = 0;

    disHour = "";
    disMin = "";
    time = "";

    def Update():
        min += 1;

        if min >= 60:
            min = 0;
            hour += 1;

            if hour >= 24:
                days += 1;
                hour = 0;
                print (days+ "passed");

        if hour < 10:
            disHour = "0" + str(hour);

        else:
            disHour = str(hour);

        if min == 0:
            disMin = "0" + str(min);

        else:
            disMin = str(min);

        time = disHour+ ":" +disMin;
        print ("Time: " +time);
