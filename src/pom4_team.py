import math, random
from pom4_sprints import *

"""#################################################################
   #### 
   #### -@author: Naveen Kumar Lekkalapudi
   #### -@note: POM4 Team Management Module
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
        self.tasksrepo = []
        self.sprint = Sprint()
        self.task_cost_total = 0
        self.index = 0
    
    def TotalCost(self):
        total = 0
        for task in self.tasksrepo:
            total+= task.val.cost
        return total
    
    def setPolicy(self, policyInt):
        self.plan = policyInt
        
    def markTasksVisible(self):
        if (self.visible > 1.0): self.visible = 1.0
        for i in range((int)(self.visible*len(self.tasksrepo))):
            self.tasksrepo[i].val.visible = True        

    
    def updateBudget(team, numShuffles):
        totalCost = team.TotalCost()
        team.budget += (totalCost/numShuffles)
        
    def collectAvailableTasks(team, userstories):
        team.availableTasks = []
        for task in team.tasksrepo:
            if task.val.visible == True:
                #if no dependencies and no children on this task, then add to availableTasks list
                if countNotDones(userstories.heap.find_node(task.key).children) == 0:
                    if task.val.done == False:
                        team.availableTasks.append(task)
                        team.numAvailableTasks += 1
#        print "Number of available tasks:",team.numAvailableTasks
    
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

    def getSprint(self):
        sprint = Sprint()
        length = len(self.tasksrepo)
        #Get 3 tasks from taskrepo and add them to team's sprint
        if length > 3:
            for i in range(0,3):
                if self.index < length: 
                    sprint.add_task(self.tasksrepo[self.index])
                self.index += 1
        else:
            for i in range(length):
                if self.index < length: 
                    sprint.add_task(self.tasksrepo[self.index])
                self.index += 1
        #Assign Sprint
        #print sprint
        self.sprint = sprint

    
    def executeSprint(team): 
        i = 0
        for task in team.sprint.us:
            if (team.budget - task.val.cost) >= 0:
                team.budget -= task.val.cost
                team.cost_total  += task.val.cost
                team.value_total += task.val.value
                task.val.done = True
                team.tasksrepo[team.index + i].val.done = True
                team.numCompletedTasks += 1
            i += 1
    def discoverNewTasks(team):
        team.visible += nextTime(team.decisions.dynamism/10.0)
        team.markTasksVisible()

    def updateTasks(team):
        #Adjust values
        for task in team.tasksrepo:
            change = (random.uniform(0, team.decisions.dynamism) - team.decisions.dynamism/2)*team.decisions.culture/100.0
            task.val.value += (MAX_VALUE * max(0,change))  

def nextTime(rateParameter): return -math.log(1.0 - random.random()) / rateParameter                        
def countNotDones(list):
    cnt = 0
    for i in list:
        if i.val.done == False: cnt+= 1
    return cnt
