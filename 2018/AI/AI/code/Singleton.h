#pragma once
#ifndef MY_SINGLETON
#define MY_SINGLETON

class Singleton
{
	private:
		int iNum;
		Singleton(){}

		Singleton(const Singleton &);
		/*Singleton& operator=(const Singleton &);*/

	public:
		~Singleton();

		int GetVal() const
		{
			return iNum;
		}

		static Singleton* Instance();
};

#endif