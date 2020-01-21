#pragma once
#include <iostream>
#include <string>
#include <time.h>
#include <curses.h>
#include "BaseGameEntity.h"
#include "GameTime.h"

using namespace std;
class Humanoid;

class AI
{
	public:
		AI(string name);
		~AI();
};

class State
{
	public:
		virtual void Execute(Humanoid* humanoid) = 0;
};

class Humanoid : public BaseGameEntity
{
	private:
		State* m_pCurrentState;

	public:
		GameTime* timer;

		string agentName;
		string location;

		int cash;
		int hunger;
		int thirst;
		int energy;
		int socialNeed;
		int workSkill;

		int riskOfSickness;
		float sicknessLevel;

		bool isSick = false;
		bool alive = true;

		Humanoid(int ID, string name, GameTime* timer);
		~Humanoid();

		void Update()
		{
			m_pCurrentState->Execute(this);
		}

		void ChangeState(State* pNewState)
		{
			delete m_pCurrentState;
			m_pCurrentState = pNewState;
		}

		void Rest()
		{
			cout << "Zzz..." << endl;

			if (isSick == true)
			{
				energy += (5 - sicknessLevel);
			}

			else
			{
				energy += 5;
			}

			hunger -= 1;
			thirst -= 1;
			cout << "Current energy level: " << energy << endl;
			cout << "Current hunger level: " << hunger << endl;
			cout << "Current thirst level: " << thirst << endl;
		}

		void Eat()
		{
			cout << "Nom nom nom!" << endl;

			if (isSick == true)
			{
				hunger += (15 - sicknessLevel);
			}

			else
			{
				hunger += 15;
			}

			cash -= 10;
			cout << "Current hunger level: " << hunger << endl;
			cout << "Current wallet: " << cash << "kr" << endl;
		}

		void Drink()
		{
			cout << "Gulp gulp gulp!" << endl;

			if (isSick == true)
			{
				thirst += (10 - sicknessLevel);
			}

			else
			{
				thirst += 10;
			}

			cash -= 5;
			cout << "Current thirst level: " << thirst << endl;
			cout << "Current wallet: " << cash << "kr" << endl;
		}

		void Work()
		{
			cout << "Work work!" << endl;

			if (isSick == true)
			{
				energy -= (10 + sicknessLevel);
			}

			else
			{
				energy -= 10;
			}

			cash += 8 * workSkill;
			socialNeed -= 2;
			hunger -= 5;
			thirst -= 5;
			cout << "Current wallet: " << cash << "kr" << endl;
			cout << "Current social level: " << socialNeed << endl;
			cout << "Current energy level: " << energy << endl;
			cout << "Current hunger level: " << hunger << endl;
			cout << "Current thirst level: " << thirst << endl;
		}

		void Socialize()
		{
			cout << "Blah blah friend stuff!" << endl;
			socialNeed += 6;
			energy -= 5;
			cout << "Current social level: " << socialNeed << endl;
			cout << "Current energy level: " << energy << endl;
		}
};

class State_Sleep : public State
{ 
	public:
		void Execute(Humanoid * humanoid);
};

class State_Eat : public State
{
	public:
		void Execute(Humanoid * humanoid);
};

class State_Drink : public State
{
	public:
		void Execute(Humanoid * humanoid);
};

class State_Work_Office : public State
{
	public:
		void Execute(Humanoid * humanoid);
};

class State_Socialize : public State
{
	public:
		void Execute(Humanoid * humanoid);
};

class State_Die : public State
{
	public:
		void Execute(Humanoid * humanoid);
};