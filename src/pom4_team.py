import math, random
from pom4_sprints import *

"""#################################################################
   #### 
   #### -@author: Naveen Kumar Lekkalapudi
   #### -@note: POM4 User Stories Requirements Tree Module
   #### -@note: This work is done in affilication with  
   #### -@note: West Virginia University
   #### -@contact: nalekkalapudi@mix.wvu.edu
   #### -@copyright: This work is made for academic research. 
   #### -@copyright: Do not edit without citing POM4 as a reference.
   #### -@reference: POM3
   ####
   ##################################################################"""

MAX_VALUE = 1500

class Team(object):
    def __init__(self, decisions):
        
        self.decisions = decisions
        
        self.team_size = decisions.team_size
        self.plan = decisions.plan
        self.size = decisions.size
        self.visible = 1-decisions.initial_known                
        self.known = 0
        self.cost_total = 0.0
        self.value_total = 0.0
        self.numAvailableTasks = 0
        self.numCompletedTasks = 0
        self.budget = 0
        self.tasks = []
        self.sprint = Sprint()
        self.task_cost_total = 0

    def getsprint(self,sprint):
        self.sprint = sprint
        for userstory in sprint.us:
            self.tasks.append(userstory)
    
    def getnewsprint(self, pom4_teams, sprints):
        index = pom4_teams.index
        if index < len(sprints.collection): 
            self.getsprint(sprints.collection[index])
            index += 1
            pom4_teams.index = index

    def TotalCost(self):
        self.task_cost_total += self.sprint.cost
        #print self.task_cost_total
        return self.task_cost_total
    
    def setPolicy(self, policyInt):
        self.plan = policyInt
        
    def markTasksVisible(self):
        if (self.visible > 1.0): self.visible = 1.0
        self.sprint.markTasksVisible(self.visible)
        for task in self.tasks:
            task.val.visible = True
        
    def updateBudget(team, numShuffles):
        totalCost = team.TotalCost()
        team.budget += (totalCost/numShuffles)
        #print "Total Budget:",team.budget
        
    def collectAvailableTasks(team, userstories):
        team.availableTasks = []
        for userstory in team.sprint.us:
            if userstory.val.visible == True:
                #if no dependencies and no children on this task, then add to availableTasks list
                if countNotDones(userstories.heap.find_node(userstory.key).children) == 0:
                    if userstory.val.done == False:
                        team.availableTasks.append(userstory)
        team.numAvailableTasks += len(team.availableTasks)
        #print "Number of available tasks:",team.numAvailableTasks
    
    def applySortingStrategy(team):
        
        #method 0: Cost Ascending
        #method 1: Cost Descending
        #method 2: Value Ascending
        #method 3: Value Descending
        #method 4: Cost/Value Ascending
        #method 5: Cost/Value Descending
        
        if team.plan == 0:   team.availableTasks.sort(key=lambda cv: cv.val.cost)
        elif team.plan == 1: team.availableTasks.sort(key=lambda cv: cv.val.cost, reverse=True)
        elif team.plan == 2: team.availableTasks.sort(key=lambda cv: cv.val.value)
        elif team.plan == 3: team.availableTasks.sort(key=lambda cv: cv.val.value, reverse=True)
        elif team.plan == 4: team.availableTasks.sort(key=lambda cv: cv.val.cost/cv.val.value)
        elif team.plan == 5: team.availableTasks.sort(key=lambda cv: cv.val.cost/cv.val.value, reverse=True)
    
    def executeAvailableTasks(team): 
        for userstory in team.availableTasks:
            if (team.budget - userstory.val.cost) >= 0:
                team.budget -= userstory.val.cost
                team.cost_total  += userstory.val.cost
                team.value_total += userstory.val.value
                userstory.val.done = True
                team.numCompletedTasks += 1
                team.tasks.append(userstory)
                
    def discoverNewTasks(team):
        team.known += nextTime(team.decisions.dynamism/10.0)

    def updateTasks(team):
        #Adjust values
        for userstory in team.sprint.us:
            change = (random.uniform(0, team.decisions.dynamism) - team.decisions.dynamism/2)*team.decisions.culture/100.0
            userstory.val.value += (MAX_VALUE * max(0,change))  

def nextTime(rateParameter): return -math.log(1.0 - random.random()) / rateParameter                        
def countNotDones(list):
    cnt = 0
    for i in list:
        if i.val.done == False: cnt+= 1
    return cnt
