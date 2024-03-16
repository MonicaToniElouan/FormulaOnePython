
class Team:
    def __init__(self, TeamID: int, TeamName: str, TeamCountry: str, CreationDate: str):
        self._TeamID = TeamID
        self._TeamName = TeamName
        self._TeamCountry = TeamCountry
        self._CreationDate = CreationDate
        
    # GETTERS AND SETTERS
    @property
    def TeamID(self):
        return self._TeamID
    
    @TeamID.setter
    def TeamID(self, value):
        self._TeamID = value

    @property
    def TeamName(self):
        return self._TeamName
    
    @TeamName.setter
    def TeamName(self, value):
        self._TeamName = value

    @property
    def TeamCountry(self):
        return self._TeamCountry
    
    @TeamCountry.setter
    def TeamCountry(self, value):
        self._TeamCountry = value

    @property
    def CreationDate(self):
        return self._CreationDate
    
    @CreationDate.setter
    def CreationDate(self, value):
        self._CreationDate = value
    