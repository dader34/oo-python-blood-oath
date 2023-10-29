class BloodOath:

    all = []

    def __init__(self,initiation_date,follower,cult):
        self.initiation_date = initiation_date
        cult.recruit_follower(follower)
        type(self).all.append(self)

    @property
    def initiation_date(self):
        return self._initiation_date
    
    @initiation_date.setter
    def initiation_date(self,initiation_date):
        self._initiation_date = initiation_date