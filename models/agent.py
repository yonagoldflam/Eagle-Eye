class Agent:
    def __init__(self, code_name, real_name,location, status, missions_ompleted, id=None):
        self.id = id
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_ompleted

    def __str__(self):
        return f'Agent(id={self.id}, codeName={self.code_name}, realName={self.real_name} location={self.location} status={self.status} missionsCompleted={self.missions_completed})'