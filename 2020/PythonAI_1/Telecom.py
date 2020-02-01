from Humanoid import State_Socialize;
from Humanoid import State_WalkTo;
from Humanoid import humanoid;
from random import randint;
from random import seed;
from enum import Enum;
import re;

class telecom():

    class SMS():
        msgSender = "";
        msgRecieveer = "";
        msgClass = 0;
        msgContent = "";
        msgMeetingTime = "";
        msgLocation = "";
        msgTimer = None;

        #Message SMS with timer
        def Message(self, msgSender, msgRecieveer, msgClass, msgContent, msgMeetingTime, msgLocation, msgTimer):
            self.msgSender = msgSender;
            self.msgRecieveer = msgRecieveer;
            self.msgClass = msgClass;
            self.msgContent = msgContent;
            self.msgMeetingTime = msgMeetingTime;
            self.msgLocation = msgLocation;
            self.msgTimer = msgTimer;

            return self;

    class msgTypes(Enum):
        MSG_MeetUp = 1; #Sent to another AI for planning
        MSG_AcceptMeeting = 2; #Sent to another AI for confirmation of meeting
        MSG_DeclineMeeting = 3; #Sent to another AI for confirmation of meeting
        MSG_GotoMeeting = 4; #Sent to yourself for reminder of going to meeting
        MSG_WaitingForSocializing = 5; #Sent to another AI to confirm that you are ready to socialize
        MSG_WorldDanger = 6; #Sent to all AIs to confirm that something terrible has happend
        MSG_Grief = 7; #Sent to all AIs to confirm that something terrible has happend

    phoneBook = [];
    deliveryQueue = [];
    posConn = 0;
    meetingsSpots = [ "The Restaurant", "The Park", "Traversen" ];
    posMeeting = len(meetingsSpots);

    #Messages to write when sending a request to meet up
    MSG_MeetUp_SendText = [ "Hey @! Wanna meet up at ¤, §?",
                            "Yo! I'm bored, let's hangout! How about we meet at ¤ around §?",
                            "@! I want to hang out, will you meet me around § at ¤?" ];

    #Messages to write when accepting a meet up
    MSG_AcceptMeeting_Response = [ "Sure, that sounds nice! I'll see you there @ at §",
                                    "Ey! @! Absolutley, § is perfect! I'll meet you there!",
                                    "I'll be there §! See you soon @!",
                                    "Alright, we'll meet up at ¤ then!" ];

    #Messages to write when declining a meet up
    MSG_DeclineMeeting_Response = [ "It sounds fun @, but I have to decline... Maybe another time!",
                                    "Sorry @, I have already other plans for today",
                                    "Meeeh, I don't feel like it, nothing personal @. Another day, promise!",
                                    "I can't because I'm busy, sorry @!" ];

    #Messages to print when declined
    MSG_Declined_Response = [ "Whaaaa...!",
                                "Hmmm... :c",
                                "Awww :(",
                                "Booo! Sad :c" ];

    #Messages to print when a world disaster happens
    MSG_WorldDanger_Response = [ "Aaaaah! Oh nooo!",
                                "Whaaaaaaaaaa!! No no no no!!",
                                "Omg, OMG NOO!",
                                "Ooooooooooooohh!!! Ieeeeeeeeeeeeee!!",
                                "Pwhaaa!!!"];

    #Messages to print when an AI dies
    MSG_Grief_Response = [ "No... NO... *cry cry*",
                            "Urghuhuuuu...",
                            "Ehhhh... whääääää!",
                            "It's a sad day, wuhuuhuuuu" ];

    #Send a message
    def SendMSG(self, outMSG):

        #Message for planing a meeting - WIP
        if outMSG.msgClass == 1:
            outMSG.msgContent = re.sub('[@]', outMSG.msgRecieveer.m_Name, outMSG.msgContent);
            outMSG.msgContent = re.sub('[¤]', outMSG.msgLocation, outMSG.msgContent);
            outMSG.msgContent = re.sub('[§]', outMSG.msgMeetingTime, outMSG.msgContent);

            if outMSG.msgTimer != None:
                print ("Message has been set in queue and will be delivered when the time is right!");

            else:
                print ("[" +outMSG.msgSender.m_Name+ " SENT A MESSAGE TO " +outMSG.msgRecieveer.m_Name+ "]");
                print ("Message Content: " +outMSG.msgContent);
                print ("")

                outMSG.msgRecieveer.m_PhoneRef.ReadMSG(outMSG);

        #Message for accepting a meeting - WIP
        elif outMSG.msgClass == 2:
            outMSG.msgContent = re.sub('[@]', outMSG.msgRecieveer.m_Name, outMSG.msgContent);
            outMSG.msgContent = re.sub('[¤]', outMSG.msgLocation, outMSG.msgContent);
            outMSG.msgContent = re.sub('[§]', outMSG.msgMeetingTime, outMSG.msgContent);

            if outMSG.msgTimer != None:
                print ("Message has been set in queue and will be delivered when the time is right!");

            else:
                print ("[" +outMSG.msgSender.m_Name+ " SENT A MESSAGE TO " +outMSG.msgRecieveer.m_Name+ "]");
                print ("Message Content: " +outMSG.msgContent);
                print ("")

                outMSG.msgRecieveer.m_PhoneRef.ReadMSG(outMSG);

        #Message for declining a meeting - WIP
        elif outMSG.msgClass == 3:
            outMSG.msgContent = re.sub('[@]', outMSG.msgRecieveer.m_Name, outMSG.msgContent);

            if outMSG.msgTimer != None:
                print ("Message has been set in queue and will be delivered when the time is right!");

            else:
                print ("[" +outMSG.msgSender.m_Name+ " SENT A MESSAGE TO " +outMSG.msgRecieveer.m_Name+ "]");
                print ("Message Content: " +outMSG.msgContent);
                print ("")

                outMSG.msgRecieveer.m_PhoneRef.ReadMSG(outMSG);

    #Read a SMS
    def ReadMSG(self, inMSG):
        if inMSG.msgClass == 1:
            inMSG.msgContent = re.sub('[@]', inMSG.msgRecieveer.m_Name, inMSG.msgContent);
            inMSG.msgContent = re.sub('[¤]', inMSG.msgLocation, inMSG.msgContent);
            inMSG.msgContent = re.sub('[§]', inMSG.msgMeetingTime, inMSG.msgContent);

            #Check if you are avalible, respond with msgClass 2 or 3 - TWEAK VALUES
            if inMSG.msgRecieveer.m_Energy < 20 or inMSG.msgRecieveer.m_Hunger < 20 or inMSG.msgRecieveer.m_Thirst < 20:
                print (inMSG.msgRecieveer.m_Name+" is too tired, can't meetup with " +inMSG.msgSender.m_Name+ "!");
                outMSG = inMSG.msgRecieveer.m_PhoneRef.SMS.Message(self, inMSG.msgRecieveer, inMSG.msgSender, 3, telecom.MSG_DeclineMeeting_Response[randint(0, len(telecom.MSG_DeclineMeeting_Response) - 1)], inMSG.msgMeetingTime, inMSG.msgLocation, None);
                inMSG.msgRecieveer.m_PhoneRef.SendMSG(outMSG);

            else:
                print (inMSG.msgRecieveer.m_Name+" can meetup with " +inMSG.msgSender.m_Name+ "!");
                outMSG = inMSG.msgRecieveer.m_PhoneRef.SMS.Message(self, inMSG.msgRecieveer, inMSG.msgSender, 2, telecom.MSG_AcceptMeeting_Response[randint(0, len(telecom.MSG_AcceptMeeting_Response) - 1)], inMSG.msgMeetingTime, inMSG.msgLocation, None);
                inMSG.msgRecieveer.m_PhoneRef.SendMSG(outMSG);
                #Send a message to yourself for prepared meeting

        #Message for accepting a meeting - WIP
        elif inMSG.msgClass == 2:
            inMSG.msgContent = re.sub('[@]', inMSG.msgRecieveer.m_Name, inMSG.msgContent);
            inMSG.msgContent = re.sub('[¤]', inMSG.msgLocation, inMSG.msgContent);
            inMSG.msgContent = re.sub('[§]', inMSG.msgMeetingTime, inMSG.msgContent);
            #Send a message to yourself for prepared meeting

        #Message for declining a meeting - WORKS
        elif inMSG.msgClass == 3:
            inMSG.msgContent = re.sub('[@]', inMSG.msgRecieveer.m_Name, inMSG.msgContent);
            print (inMSG.msgRecieveer.m_Name+ ": " +telecom.MSG_Declined_Response[randint(0, len(telecom.MSG_Declined_Response) - 1)]);

        elif inMSG.msgClass == 4:
            #Stop what you are doing and goto meeting spot
            print (inMSG.msgRecieveer.m_Name+": I have to go now!");
            inMSG.msgRecieveer.m_pCurrentState.Exit(self);
            inMSG.msgRecieveer.m_GoalLoc(msgLocation);
            newStateC = State_WalkTo;
            inMSG.msgRecieveer.ChangeCurrentState(newStateC);
            newStateG = State_Socialize;
            inMSG.msgRecieveer.ChangeFutureState(newStateG);

        elif inMSG.msgClass == 5:
            #SCREAM IN FEAR
            print (inMSG.msgRecieveer.m_Name+ ": " +telecom.MSG_WorldDanger_Response[randint(0, len(telecom.MSG_WorldDanger_Response) - 1)]);

        elif inMSG.msgClass == 6:
            #Cry in sadness
            print (inMSG.msgRecieveer.m_Name+ ": " +telecom.MSG_Grief_Response[randint(0, len(telecom.MSG_Grief_Response) - 1)]);