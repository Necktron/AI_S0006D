#include "Singleton.h"

//Singleton& Singleton::operator=(const Singleton &)
//{
//	Singleton& tempFill = new const Singleton;
//	return tempFill;
//}

Singleton::~Singleton()
{

}

Singleton* Singleton::Instance()
{
	static Singleton instance;

	return &instance;
}