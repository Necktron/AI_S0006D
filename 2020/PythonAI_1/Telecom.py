# JONAS H, Februari 2020
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
        msgExtra = None;

        #Message SMS with timer
        def Message( self, msgSender, msgRecieveer, msgClass, msgContent, msgMeetingTime, msgLocation, msgTimer, msgExtra):
            self.msgSender = msgSender;
            self.msgRecieveer = msgRecieveer;
            self.msgClass = msgClass;
            self.msgContent = msgContent;
            self.msgMeetingTime = msgMeetingTime;
            self.msgLocation = msgLocation;
            self.msgTimer = msgTimer;
            self.msgExtra = msgExtra;

            return self;

    class msgTypes(Enum):
        MSG_MeetUp = 1; #Sent to another AI for planning
        MSG_AcceptMeeting = 2; #Sent to another AI for confirmation of meeting
        MSG_DeclineMeeting = 3; #Sent to another AI for confirmation of meeting
        MSG_GotoMeeting = 4; #Sent to yourself for reminder of going to meeting
        MSG_AbortMeeting = 5; #Sent to another AI to abort planned meeting if anything happens
        MSG_ValidateMeeting = 6; #Sent to AI's with planned meeting to see if they can still go
        MSG_Grief = 7; #Sent to all AIs to confirm that something terrible has happend

    phoneBook = [];
    deliveryQueue = [];
    posConn = 0;
    meetingsSpots = [ "The Restaurant", "The Park", "Traversen", "The Mall" ];
    posMeeting = len(meetingsSpots);

    #Messages to write when sending a request to meet up
    MSG_MeetUp_Question = [ "Hey @! Wanna meet up at ¤, §?",
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

    #Messages to print when accepted
    MSG_Accepted_Response = [ "Wohoo! :D",
                                "Nice ^^",
                                "Woop woop :3" ];

    #Messages to print when declined
    MSG_Declined_Response = [ "Whaaaa...!",
                                "Hmmm... :c",
                                "Awww :(",
                                "Booo! Sad :c",
                                "K... ._." ];

    #Messages to write when aborting a meeting
    MSG_Abort_Announcment = [ "Hey @... I'm so sorry but I have to cancel our meeting at ¤, I'm SOO sorry!",
                             "@... I hate to do this, but we can't meet up. Something got in the way",
                             "Oh... I just remembered I had something planned, I'm afraid I have to cancel our plans @",
                             "Sadly I have to cancel our meeting at ¤, sorry @"];

    #Messages to print when socializing
    MSG_Socialize_Conversation = [ "Did you get a new haircut? I like your hair!",
                                  "Hahaha, yeah tell me about it~",
                                  "What's the deal with airplane food??",
                                  "Look at this meme, it's hilarious!",
                                  "And I said; 'No way, that's awesome dude!'",
                                  "You always say something random like that",
                                  "Please don't spoil that movie, I want to see it for myself!" ];

    #Messages to print when a world disaster happens. Nothing dangerous so far, hehehe... >:)
    MSG_WorldDanger_Response = [ "Aaaaah! Oh nooo!",
                                "Whaaaaaaaaaa!! No no no no!!",
                                "Omg, OMG NOO!",
                                "Ooooooooooooohh!!! Ieeeeeeeeeeeeee!!",
                                "Pwhaaa!!!"];

    #Messages to print when you are filthy rich and want to get rid of it on something good or stuff from Amazon
    MSG_MakeItRain = [ "I'm gonna donate some money to charity!",
                      "I'm gonna buy movies from YouTube!",
                      "I'm gonna invest in BitCoin!",
                      "I'm gonna use some money as toilet paper",
                      "I'm gonna donate some money to science!",
                      "I'm gonna donate some money to a kickstarter game project",
                      "I'll make some really fancy confetti",
                      "I'll hide it in a treasure chest and drop the treasure map, it's gone forever!",
                      "I'll buy some clothing for homeless people" ];

    #Messages to print when an AI dies
    MSG_Death_Announcement = [ "I'm sorry to announce, but it seems @ has passed away...",
                              "RIP @, atleast it was a peacefull death",
                              "@ might be gone, but never forgotten <3"];

    #Messages to print when an AI dies
    MSG_Grief_Response = [ "No... noooo....",
                          "*cries*",
                          "Buhuu...",
                          "Whäääää, whääää!",
                          ";_; </3" ];

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

        #Message for going to a meeting - WIP
        elif outMSG.msgClass == 4:
            outMSG.msgRecieveer.m_PhoneRef.ReadMSG(outMSG);

        #Message for aborting a meeting - WIP
        elif outMSG.msgClass == 5:
            outMSG.msgContent = re.sub('[@]', outMSG.msgRecieveer.m_Name, outMSG.msgContent);
            outMSG.msgContent = re.sub('[¤]', outMSG.msgLocation, outMSG.msgContent);

            print ("[" +outMSG.msgSender.m_Name+ " SENT A MESSAGE TO " +outMSG.msgRecieveer.m_Name+ "]");
            print ("Message Content: " +outMSG.msgContent);
            print ("")

            outMSG.msgRecieveer.m_PhoneRef.ReadMSG(outMSG);

        #Message for world chaos - WIP
        elif outMSG.msgClass == 6:
            outMSG.msgRecieveer.m_PhoneRef.ReadMSG(outMSG);

        #Message for announcment of an AI's death - WORKS
        elif outMSG.msgClass == 7:
            outMSG.msgContent = re.sub('[@]', outMSG.msgSender.m_Name, outMSG.msgContent);
            outMSG.msgRecieveer.m_PhoneRef.ReadMSG(outMSG);

    #Read a SMS
    def ReadMSG(self, inMSG):
        #Message for asking an AI to meet up
        if inMSG.msgClass == 1:
            inMSG.msgContent = re.sub('[@]', inMSG.msgRecieveer.m_Name, inMSG.msgContent);
            inMSG.msgContent = re.sub('[¤]', inMSG.msgLocation, inMSG.msgContent);
            inMSG.msgContent = re.sub('[§]', inMSG.msgMeetingTime, inMSG.msgContent);

            #Check if you are avalible, respond with msgClass 2 or 3 - TWEAK VALUES
            if inMSG.msgRecieveer.m_PersonToMeet != None:
                print (inMSG.msgRecieveer.m_Name+" can't meet up with " +inMSG.msgSender.m_Name+ "!");
                outMSG = inMSG.msgRecieveer.m_PhoneRef.SMS().Message(inMSG.msgRecieveer, inMSG.msgSender, 3, telecom.MSG_DeclineMeeting_Response[randint(0, len(telecom.MSG_DeclineMeeting_Response) - 1)], inMSG.msgMeetingTime, inMSG.msgLocation, None, None);
                inMSG.msgRecieveer.m_PhoneRef.SendMSG(outMSG);

            else:
                print (inMSG.msgRecieveer.m_Name+" can meetup with " +inMSG.msgSender.m_Name+ "!");
                outMSG = inMSG.msgRecieveer.m_PhoneRef.SMS().Message(inMSG.msgRecieveer, inMSG.msgSender, 2, telecom.MSG_AcceptMeeting_Response[randint(0, len(telecom.MSG_AcceptMeeting_Response) - 1)], inMSG.msgMeetingTime, inMSG.msgLocation, None, inMSG.msgExtra);
                inMSG.msgRecieveer.m_PhoneRef.SendMSG(outMSG);
                inMSG.msgRecieveer.m_PersonToMeet = inMSG.msgSender;

                #Calculate a 30 min before meetup delay of message sending, message will tell if AI can still meet up
                prepHourStr = inMSG.msgMeetingTime[0:2];
                prepMinStr = inMSG.msgMeetingTime[3:5];

                prepHourInt = int(prepHourStr);
                prepMinInt = int(prepMinStr);

                prepMinInt -= 30;
                if prepMinInt < 0:
                    prepMinInt += 60;
                    prepHourInt -= 1;

                if prepHourInt < 10:
                    prepHourStr = "0" + str(prepHourInt);

                else:
                    prepHourStr = str(prepHourInt);

                if prepMinInt < 10:
                   prepMinStr = "0" + str(prepMinInt);

                else:
                    prepMinStr = str(prepMinInt);

                prepFinal = prepHourStr+ ":" +prepMinStr;

                outMSG = inMSG.msgRecieveer.m_PhoneRef.SMS().Message(inMSG.msgRecieveer, inMSG.msgRecieveer, 6, None, inMSG.msgMeetingTime, inMSG.msgLocation, prepFinal, inMSG.msgExtra);

                print ("Message has been set in queue and will be delivered when the time is right!");

                print ("Message Sender: " +outMSG.msgSender.m_Name);
                print ("Message Recieveer: " +outMSG.msgRecieveer.m_Name);
                print ("Message Class: "  +str(outMSG.msgClass));
                print ("Message Delivery Timer: " +outMSG.msgTimer);

                telecom.deliveryQueue.append(outMSG);
                inMSG.msgRecieveer.m_PersonToMeet = inMSG.msgSender;

                #Calculate a 20 min before meetup delay of message sending, message will tell AI to move to location
                prepHourStr = inMSG.msgMeetingTime[0:2];
                prepMinStr = inMSG.msgMeetingTime[3:5];

                prepHourInt = int(prepHourStr);
                prepMinInt = int(prepMinStr);

                prepMinInt -= 20;
                if prepMinInt < 0:
                    prepMinInt += 60;
                    prepHourInt -= 1;

                if prepHourInt < 10:
                    prepHourStr = "0" + str(prepHourInt);

                else:
                    prepHourStr = str(prepHourInt);

                if prepMinInt < 10:
                   prepMinStr = "0" + str(prepMinInt);

                else:
                    prepMinStr = str(prepMinInt);

                prepFinal = prepHourStr+ ":" +prepMinStr;

                outMSG = inMSG.msgRecieveer.m_PhoneRef.SMS().Message(inMSG.msgRecieveer, inMSG.msgRecieveer, 4, None, inMSG.msgMeetingTime, inMSG.msgLocation, prepFinal, inMSG.msgExtra);

                print ("Message has been set in queue and will be delivered when the time is right!");

                print ("Message Sender: " +outMSG.msgSender.m_Name);
                print ("Message Recieveer: " +outMSG.msgRecieveer.m_Name);
                print ("Message Class: "  +str(outMSG.msgClass));
                print ("Message Delivery Timer: " +outMSG.msgTimer);

                telecom.deliveryQueue.append(outMSG);

        #Message for accepting a meeting - WIP
        elif inMSG.msgClass == 2:
            inMSG.msgContent = re.sub('[@]', inMSG.msgRecieveer.m_Name, inMSG.msgContent);
            inMSG.msgContent = re.sub('[¤]', inMSG.msgLocation, inMSG.msgContent);
            inMSG.msgContent = re.sub('[§]', inMSG.msgMeetingTime, inMSG.msgContent);
            print (inMSG.msgRecieveer.m_Name+ ": " +telecom.MSG_Accepted_Response[randint(0, len(telecom.MSG_Accepted_Response) - 1)]);
            inMSG.msgRecieveer.m_PersonToMeet = inMSG.msgSender;

            #Calculate a 30 min before meetup delay of message sending, message will tell if AI can still meet up
            prepHourStr = inMSG.msgMeetingTime[0:2];
            prepMinStr = inMSG.msgMeetingTime[3:5];

            prepHourInt = int(prepHourStr);
            prepMinInt = int(prepMinStr);

            prepMinInt -= 30;
            if prepMinInt < 0:
                prepMinInt += 60;
                prepHourInt -= 1;

            if prepHourInt < 10:
                prepHourStr = "0" + str(prepHourInt);

            else:
                prepHourStr = str(prepHourInt);

            if prepMinInt < 10:
                prepMinStr = "0" + str(prepMinInt);

            else:
                prepMinStr = str(prepMinInt);

            prepFinal = prepHourStr+ ":" +prepMinStr;

            outMSG = inMSG.msgRecieveer.m_PhoneRef.SMS().Message(inMSG.msgRecieveer, inMSG.msgRecieveer, 6, None, inMSG.msgMeetingTime, inMSG.msgLocation, prepFinal, inMSG.msgExtra);

            print ("Message has been set in queue and will be delivered when the time is right!");

            print ("Message Sender: " +outMSG.msgSender.m_Name);
            print ("Message Recieveer: " +outMSG.msgRecieveer.m_Name);
            print ("Message Class: "  +str(outMSG.msgClass));
            print ("Message Delivery Timer: " +outMSG.msgTimer);

            telecom.deliveryQueue.append(outMSG);
            inMSG.msgRecieveer.m_PersonToMeet = inMSG.msgSender;

            #Calculate a 20 min before meetup delay of message sending
            prepHourStr = inMSG.msgMeetingTime[0:2];
            prepMinStr = inMSG.msgMeetingTime[3:5];

            prepHourInt = int(prepHourStr);
            prepMinInt = int(prepMinStr);

            prepMinInt -= 20;
            if prepMinInt < 0:
                prepMinInt += 60;
                prepHourInt -= 1;

            if prepHourInt < 10:
                prepHourStr = "0" + str(prepHourInt);

            else:
                prepHourStr = str(prepHourInt);

            if prepMinInt < 10:
               prepMinStr = "0" + str(prepMinInt);

            else:
                prepMinStr = str(prepMinInt);

            prepFinal = prepHourStr+ ":" +prepMinStr;

            outMSG = inMSG.msgRecieveer.m_PhoneRef.SMS().Message(inMSG.msgRecieveer, inMSG.msgRecieveer, 4, None, inMSG.msgMeetingTime, inMSG.msgLocation, prepFinal, inMSG.msgExtra);

            print ("Message has been set in queue and will be delivered when the time is right!");

            print ("Message Sender: " +outMSG.msgSender.m_Name);
            print ("Message Recieveer: " +outMSG.msgRecieveer.m_Name);
            print ("Message Class: "  +str(outMSG.msgClass));
            print ("Message Delivery Timer: " +outMSG.msgTimer);

            telecom.deliveryQueue.append(outMSG);

        #Message for declining a meeting - WORKS
        elif inMSG.msgClass == 3:
            inMSG.msgContent = re.sub('[@]', inMSG.msgRecieveer.m_Name, inMSG.msgContent);
            print (inMSG.msgRecieveer.m_Name+ ": " +telecom.MSG_Declined_Response[randint(0, len(telecom.MSG_Declined_Response) - 1)]);

        #Message for prepare to go to meeting - WIP
        elif inMSG.msgClass == 4:
            if inMSG.msgRecieveer.m_Alive == False:
                print (inMSG.msgRecieveer.m_Name+ " is dead, can't deal with this message");

            else:
                if inMSG.msgRecieveer.m_PersonToMeet != None:
                    #Stop what you are doing and goto meeting spot
                    print (inMSG.msgRecieveer.m_Name+ ": I have to go now!");
                    newStateG = State_Socialize;
                    inMSG.msgRecieveer.ChangeGoalState(newStateG);
                    inMSG.msgRecieveer.m_GoalLoc = inMSG.msgLocation;
                    newStateC = State_WalkTo;
                    inMSG.msgRecieveer.ChangeCurrentState(newStateC);

                else:
                    print (inMSG.msgRecieveer.m_Name+ ": Message is no longer relevant, meeting was disbanded");

        #Message for aborting meeting - WIP
        elif inMSG.msgClass == 5:

            inMSG.msgRecieveer.m_PersonToMeet = None;

            print (inMSG.msgRecieveer.m_Name+ ": " +telecom.MSG_Declined_Response[randint(0, len(telecom.MSG_Declined_Response) - 1)]);

            print ("Messages related to the aborted meeting will be deleted to prevent bugged messages in case of new meeting with same AI's in a short while!");

        #Message for validating meeting propability
        elif inMSG.msgClass == 6:
            if inMSG.msgRecieveer.m_Alive == False:
                print (inMSG.msgRecieveer.m_Name+ " is dead, can't deal with this");

            elif inMSG.msgRecieveer.m_Thirst < 50 or inMSG.msgRecieveer.m_Hunger < 50 or inMSG.msgRecieveer.m_Energy < 40:
                if inMSG.msgRecieveer.m_PersonToMeet != None:
                    print (inMSG.msgRecieveer.m_Name+" can't meet up with " +inMSG.msgRecieveer.m_PersonToMeet.m_Name+ "!");
                    outMSG = inMSG.msgRecieveer.m_PhoneRef.SMS().Message(inMSG.msgRecieveer, inMSG.msgRecieveer.m_PersonToMeet, 5, telecom.MSG_DeclineMeeting_Response[randint(0, len(telecom.MSG_DeclineMeeting_Response) - 1)], inMSG.msgMeetingTime, inMSG.msgLocation, None, None);
                    inMSG.msgRecieveer.m_PhoneRef.SendMSG(outMSG);
                    inMSG.msgRecieveer.m_PersonToMeet = None;
                else:
                    print (inMSG.msgRecieveer.m_Name+" can't go to the meeting, it might been cancelled already!");

            else:
                print (inMSG.msgRecieveer.m_Name+ ": I can still meet my friend in a little while!");

        #Message for the passing of AI's
        elif inMSG.msgClass == 7:
            #Cry in sadness
            print (inMSG.msgRecieveer.m_Name+ ": " +telecom.MSG_Grief_Response[randint(0, len(telecom.MSG_Grief_Response) - 1)]);

            #Check if AI had a meeting with desceased AI
            if inMSG.msgRecieveer.m_PersonToMeet == inMSG.msgSender:
                print (inMSG.msgRecieveer.m_Name+ ": We were going to meet later, I guess that's not happening ;_;");