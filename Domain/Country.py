
class Country:
    def __init__(self, countryID: str, countryName: str, countryPopulation: int):
        self._countryID = countryID
        self._countryName = countryName
        self._countryPopulation = countryPopulation
    
    

    # GETTERS AND SETTERS
    @property
    def CountryID(self):
        return self._countryID
    
    @CountryID.setter
    def CountryID(self, value):
        self._countryID = value
    
    @property
    def CountryName(self):
        return self._countryName
    
    @CountryName.setter
    def CountryName(self, value):
        self._countryName = value

    @property
    def CountryPopulation(self):
        return self._countryPopulation

    @CountryPopulation.setter
    def CountryPopulation(self, value):
        self._countryPopulation = value