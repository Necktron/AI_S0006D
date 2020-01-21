#pragma once
#include "AI.h"
#include <iostream>
#include <string>
#include <vector>
#include <unistd.h>

using namespace std;

int main()
{
	string name;
	int amountOfAgents;
	int specialID;
	vector<Humanoid*> agents;
	GameTime* timer = new GameTime;

	cout << "Number of agents: ";
	cin >> amountOfAgents;

	for (int i = 0; i < amountOfAgents; i++)
	{
		srand(time(NULL));
		int specialID = rand() % 100;

		cout << "Name the AI: ";
		cin >> name;
		Humanoid *person = new Humanoid(specialID, name, timer);
		agents.push_back(person);
		cout << "" << endl;
	}

	cout << "All "<< amountOfAgents << " agents are initilized, GLHF with the mayhem!" << endl;

	while (agents .size() > 0)
	{
		sleep(timer->updateRate);

		cout << endl;
		timer->Update();
		cout << endl;

		for (int i = 0; i < agents.size(); i++)
		{
			cout << "* " << agents[i]->agentName << " *" << endl;
			agents[i]->Update();
			cout << endl;
		}
	}
}