from .bloodoath import BloodOath

class Cult:

    all = []

    def __init__(self,name,location,founding_year,slogan):
        self.name,self.location,self.founding_year,self.slogan = name,location,founding_year,slogan
        self.all_members = []
        type(self).all.append(self)


    def recruit_follower(self,follower):
        new_followers = self.all_members
        new_followers.append(follower)
        self.all_members = new_followers

    @property
    def cult_population(self):
        return len(self.all_members)
    
    @classmethod
    def find_by_name(cls,name):
        for cult in cls.all:
            if cult.name == name:
                return cult
            
    @classmethod
    def find_by_location(cls,location):
        return [cult for cult in cls.all if cult.location == location]
    
    @classmethod
    def find_by_founding_year(cls,founding_year):
        return [cult for cult in cls.all if cult.founding_year == founding_year]
    

    @property
    def all_members(self):
        return self._all_members
    
    @all_members.setter
    def all_members(self,all_members):
        self._all_members = all_members

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self,location):
        self._location = location


    @property
    def founding_year(self):
        return self._founding_year

    @founding_year.setter
    def founding_year(self,founding_year):
        self._founding_year = founding_year

    @property
    def slogan(self):
        return self._slogan
    
    @slogan.setter
    def slogan(self,slogan):
        self._slogan = slogan