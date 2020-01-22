#pragma once
#include <string>
#include <iostream>

using namespace std;
class GameTime
{
	public:
		int updateRate = 1000;

		int hour = 0;
		int minut = 0;
		int daysPassed = 0;

		void Update()
		{
			minut += 15;

			if (minut >= 60)
			{
				minut = 0;
				hour += 1;

				if (hour >= 24)
				{
					daysPassed += 1;
					hour = 0;
					cout << "Days passed: " << daysPassed << endl;
				}
			}

			string displayHour;
			string displayMin;

			if (hour < 10)
			{
				displayHour = "0" + std::to_string(hour);
			}

			else
			{
				displayHour = std::to_string(hour);
			}

			if (minut == 0)
			{
				displayMin = "0" + std::to_string(minut);
			}

			else
			{
				displayMin = std::to_string(minut);
			}

			string currentTime = displayHour + ":" + displayMin;

			cout << "Time: " << currentTime << endl;
		}
};