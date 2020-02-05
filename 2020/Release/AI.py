class humanoid():
    name = "Kalle";
    m_pCurrentState = NULL;
    m_Location = "Campus";
    m_Cash = 0;
    m_Hunger = 0;
    m_Thirst = 0;
    m_Energy = 0;
    m_SocialNeed = 0;
    m_WorkSkill = 0;
    m_ROS = 0;
    m_SL = 0;

    def Update():

    def ChangeState():

    def

class State:
    def virtual Enter(humanoid) = 0;
    def virtual Execute(humanoid) = 0;
    def virtual Exit(humanoid) = 0;



