from .bloodoath import BloodOath
from .cult import Cult

class Follower:

    all = []

    def __init__(self,name,age,life_motto):
        self.name,self.age,self.life_motto = name,age,life_motto
        type(self).all.append(self)

    def join_cult(self,cult):
        cult.recruit_follower(self)

    @classmethod
    def of_a_certain_age(cls,age):
        return [follower for follower in cls.all if follower.age >= age]

    @property
    def cults(self):
        return [cult for cult in Cult.all if self in cult.all_members]

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age = age

    @property
    def life_motto(self):
        return self._life_motto
    
    @life_motto.setter
    def life_motto(self,life_motto):
        self._life_motto = life_motto
