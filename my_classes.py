import os 

'''Set of functions and classes to produce a network graph'''

class study:
    """This is a study comparing treatments"""
    def __init__(self, study_name):
        self.name = study_name
        self.arms = []
    def add_arm(self, arm):
        self.arms.append(arm)
    def describe(self):
        print "study name: ", self.name
        for arm in range(len(self.arms)):
            self.arms[arm].describe()
    def n_arms(self):
        return len(self.arms)
    def n_levels(self):
        lev = []
        for arm in range(self.n_arms()):
            lev.append(self.arms[arm].n_levels())
        return lev
    def arm_ids(self):
        ids = []
        for arm in range(self.n_arms()):
            ids.append(self.arms[arm].id)
        return ids


class arm:
    """This is the arm in a study"""
    def __init__(self, arm_data):
        self.id= arm_data[0]
        self.level=[]
        self.name=[]
        for i in range(1, len(arm_data),1): 
            self.level.append(i)
            self.name.append(arm_data[i])
    def add_level(self, arm_level, arm_name):
        self.level.append(arm_level)
        self.name.append(arm_name)
    def n_levels(self):
        return len(self.level)
    def describe(self):
        for arm in range(len(self.level)): 
            print "  arm id: ", self.id, "\tlevel: ", self.level[arm], "\tname:", self.name[arm]

