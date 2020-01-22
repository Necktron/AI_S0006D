#pragma once
class BaseGameEntity
{
	private:
		static int nextValidID;
		void SetID(int val);

	public:
		int ID;

		BaseGameEntity()
		{
		
		}

		BaseGameEntity(int id)
		{
			SetID(id);
		}

		virtual ~BaseGameEntity()
		{
		
		}

		virtual void Update() = 0;

		int GetID() const
		{
			return ID;
		}
};