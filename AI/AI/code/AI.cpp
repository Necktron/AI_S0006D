#include "AI.h"

AI::AI(string name)
{
	
}

Humanoid::Humanoid(int uniqeID, string name, GameTime* mainTimer)
{
	this->timer = mainTimer;
	this->ID = uniqeID;
	this->agentName = name;
	this->location = "Home";
	this->cash = 30;
	this->hunger = 60;
	this->thirst = 50;
	this->energy = 40;
	this->socialNeed = 60;
	this->workSkill = 1;

	this->m_pCurrentState = new State_Sleep;

	cout << name << " is now initilized!" << endl;
}

Humanoid::~Humanoid()
{

}

void State_Sleep::Execute(Humanoid* humanoid)
{
	if (humanoid->hunger > 0 && humanoid->thirst > 0 && humanoid->timer->hour >= 8)
	{
		cout << "Wakey wakey! ^w^" << endl;

		srand(time(NULL));
		humanoid->riskOfSickness = rand() % 100;
		humanoid->sicknessLevel = rand() % 5 + 1;

		if(humanoid->riskOfSickness > 80 && humanoid->isSick == false)
		{
			humanoid->isSick = true;
			cout << "Oh nooo! " << humanoid->agentName << " is sick! Suffer from the purge! o,..,o </3" << endl;
			cout << "Sickness level: " << humanoid->sicknessLevel << "...!" << endl;
		}

		else if(humanoid->riskOfSickness < 80 && humanoid->isSick == true)
		{
			humanoid->isSick = false;
			cout << "Yaaay! " << humanoid->agentName << " is cured! <3" << endl;
		}

		humanoid->ChangeState(new State_Eat());
	}

	else if (humanoid->hunger <= 0)
	{
		cout << "ZzzRGH...! </3" << endl;
		humanoid->ChangeState(new State_Die());
	}

	else if (humanoid->thirst <= 0)
	{
		cout << "ZzzRGH...! </3" << endl;
		humanoid->ChangeState(new State_Die());
	}

	else
	{
		humanoid->Rest();
	}
};

void State_Eat::Execute(Humanoid* humanoid)
{
	//DARK EVENTS
	if (humanoid->socialNeed <= 0)
	{
		cout << "I hate my life... ;_; </3" << endl;
		cout << endl;
		cout << "*BANG*" << endl;
		humanoid->ChangeState(new State_Die());
	}

	else if (humanoid->energy <= 0)
	{
		cout << "Argh! My heart! ;_; </3" << endl;
		humanoid->ChangeState(new State_Die());
	}

	else if (humanoid->hunger <= 0)
	{
		cout << "So... hungry... ;_; </3" << endl;
		humanoid->ChangeState(new State_Die());
	}

	else if (humanoid->thirst <= 0)
	{
		cout << "So... thirsty... ;_; </3" << endl;
		humanoid->ChangeState(new State_Die());
	}
	//NO MORE DARK EVENTS

	else if (humanoid->hunger < 70 && humanoid->cash >= 10)
	{
		humanoid->Eat();
	}

	else if (humanoid->thirst < 20 && humanoid->cash >= 5)
	{
		cout << "Im thirsty!" << endl;
		humanoid->ChangeState(new State_Drink());
	}

	else if (humanoid->cash < 10 && (humanoid->timer->hour >= 9 && humanoid->timer->hour <= 19))
	{
		cout << "I need money for food! Gotta work!" << endl;
		humanoid->ChangeState(new State_Work_Office());
	}

	else if (humanoid->socialNeed < 15 && humanoid->isSick != true)
	{
		cout << "I havent seen my friends in a while! Let's go meet them!" << endl;
		humanoid->ChangeState(new State_Socialize());
	}

	else if (humanoid->timer->hour >= 9 && humanoid->timer->hour <= 19)
	{
		cout << "Let's go to work, I can make some extra money" << endl;
		humanoid->ChangeState(new State_Work_Office());
	}

	else if (humanoid->socialNeed < 15 && humanoid->isSick == true)
	{
		cout << "I havent seen my friends in a while! But I dont want them to get sick... :c" << endl;
		humanoid->ChangeState(new State_Eat());
	}

	else
	{
		cout << "NOTHING" << endl;
	}
};

void State_Drink::Execute(Humanoid* humanoid)
{
	//DARK EVENTS
	if (humanoid->socialNeed <= 0)
	{
		cout << "I hate my life... ;_; </3" << endl;
		cout << endl;
		cout << "*BANG*" << endl;
		humanoid->ChangeState(new State_Die());
	}

	else if (humanoid->energy <= 0)
	{
		cout << "Argh! My heart! ;_; </3" << endl;
		humanoid->ChangeState(new State_Die());
	}

	else if (humanoid->hunger <= 0)
	{
		cout << "So... hungry... ;_; </3" << endl;
		humanoid->ChangeState(new State_Die());
	}

	else if (humanoid->thirst <= 0)
	{
		cout << "So... thirsty... ;_; </3" << endl;
		humanoid->ChangeState(new State_Die());
	}
	//NO MORE DARK EVENTS

	else if (humanoid->thirst < 80 && humanoid->cash >= 5)
	{
		humanoid->Drink();
	}

	else if (humanoid->hunger < 20 && humanoid->cash >= 10)
	{
		cout << "Im hungry!" << endl;
		humanoid->ChangeState(new State_Eat());
	}

	else if (humanoid->cash < 5 && (humanoid->timer->hour >= 9 && humanoid->timer->hour <= 19))
	{
		cout << "I need money for drinks! Gotta work!" << endl;
		humanoid->ChangeState(new State_Work_Office());
	}

	else if (humanoid->socialNeed < 15 && humanoid->isSick != true)
	{
		cout << "I havent seen my friends in a while! Let's go meet them!" << endl;
		humanoid->ChangeState(new State_Socialize());
	}

	else if (humanoid->timer->hour >= 9 && humanoid->timer->hour <= 19)
	{
		cout << "Let's go to work, I can make some extra money" << endl;
		humanoid->ChangeState(new State_Work_Office());
	}

	else if (humanoid->socialNeed < 15 && humanoid->isSick == true)
	{
		cout << "I havent seen my friends in a while! But I dont want them to get sick... :c" << endl;
		humanoid->ChangeState(new State_Drink());
	}

	else
	{
		cout << "NOTHING" << endl;
	}
};

void State_Work_Office::Execute(Humanoid* humanoid)
{
	{
		//DARK EVENTS
		if (humanoid->socialNeed <= 0)
		{
			cout << "I hate my life... ;_; </3" << endl;
			cout << endl;
			cout << "*BANG*" << endl;
			humanoid->ChangeState(new State_Die());
		}

		else if (humanoid->energy <= 0)
		{
			cout << "Argh! My heart! ;_; </3" << endl;
			humanoid->ChangeState(new State_Die());
		}

		else if (humanoid->hunger <= 0)
		{
			cout << "So... hungry... ;_; </3" << endl;
			humanoid->ChangeState(new State_Die());
		}

		else if (humanoid->thirst <= 0)
		{
			cout << "So... thirsty... ;_; </3" << endl;
			humanoid->ChangeState(new State_Die());
		}
		//NO MORE DARK EVENTS

		//NORMAL EVENTS
		else if ((humanoid->energy > 20 && humanoid->hunger > 20 && humanoid->thirst > 20 && humanoid->socialNeed > 20 && (humanoid->timer->hour >= 9 && humanoid->timer->hour <= 19)))
		{
			humanoid->Work();
		}

		else if (humanoid->energy <= 20 && humanoid->energy > 0)
		{
			cout << "I really need some sleep... o_o" << endl;
			humanoid->ChangeState(new State_Sleep());
		}

		else if (humanoid->hunger <= 20 && humanoid->cash < 10)
		{
			cout << "All this work made me hungry, but I can't afford it right now!" << endl;
			humanoid->Work();
		}

		else if (humanoid->hunger <= 20)
		{
			cout << "All this work made me hungry, time for food!" << endl;
			humanoid->ChangeState(new State_Eat());
		}

		else if (humanoid->thirst <= 20 && humanoid->cash < 5)
		{
			cout << "All this work made me thirsty, but I can't afford it right now!" << endl;
			humanoid->Work();
		}

		else if (humanoid->thirst <= 20)
		{
			cout << "All this work made me thirsty, time for a drink!" << endl;
			humanoid->ChangeState(new State_Drink());
		}

		else if (humanoid->socialNeed <= 20 && humanoid->energy > 20 && humanoid->isSick != true)
		{
			cout << "I havent seen my friends in a while! Let's go meet them!" << endl;
			humanoid->ChangeState(new State_Socialize());
		}

		else if (humanoid->socialNeed <= 20 && humanoid->energy > 20 && humanoid->isSick == true)
		{
			cout << "I havent seen my friends in a while! But I dont want them to get sick... :c" << endl;
			humanoid->Work();
		}

		else
		{
			cout << "Jobs done!" << endl;
			cout << "Now I can do what I want!" << endl;
			humanoid->ChangeState(new State_Socialize());
		}
	}
};

void State_Socialize::Execute(Humanoid* humanoid)
{
	if (humanoid->socialNeed > 70 || humanoid->energy < 20 /* || (timeOfDay <= 9 || timeOfDay >= 19)*/)
	{
		cout << "Gotta go guys! See ya!" << endl;
		humanoid->ChangeState(new State_Sleep());
	}

	else
	{
		humanoid->Socialize();
	}
};

void State_Die::Execute(Humanoid* humanoid)
{
	humanoid->alive = false;
	cout << "It's over... " << humanoid->agentName << " is dead... Rest In Piece </3" << endl;
	cout << humanoid->agentName << " survived for a total of " << humanoid->timer->daysPassed << "days and " << humanoid->timer->hour << " hours!" <<endl;
};