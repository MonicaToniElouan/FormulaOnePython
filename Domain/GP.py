
class GP:
    def __init__(self, gpID: int, gpName: str, gpCountry: str):
        self._gpID = gpID
        self._gpName = gpName
        self._gpCountry = gpCountry
    

    
    # GETTERS AND SETTERS
    @property
    def GPID(self):
        return self._gpID
    
    @GPID.setter
    def GPID(self, value):
        self._gpID = value

    @property
    def GPName(self):
        return self._gpName
    
    @GPName.setter
    def GPName(self, value):
        self._gpName = value

    @property
    def GPCountry(self):
        return self._gpCountry
    
    @GPCountry.setter
    def GPCountry(self, value):
        self._gpCountry = value

    
        