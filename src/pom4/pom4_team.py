import math
from pom4_lib import *
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
MAX_EST_VALUE = 30
SPRINT_LENGTH = 30

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
        self.team_estimate = 0
        self.numSprints = 0
    
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

    def getSprint(team):
        sprint = Sprint()
        if team.availableTasks: 
            out = team.buildsprint()
            # Sprint the list
            for i in out:
                sprint.add_task(i)
        team.sprint = sprint
        team.sprint.updatesprint()
        team.numSprints += 1

    def buildsprint(team):
        #Returns list containing prioritized tasks that can be
        #completed in a sprint
#        list = self.availableTasks
        out = [team.availableTasks.pop(0)] #Append first task to list
        sum_out = team.sumOfEst(out)
        #If there are no items left after popping return back
        if not team.availableTasks: 
            return out
        while sum_out < SPRINT_LENGTH:
            #At any time if list is empty then return built out
            if team.availableTasks: breakit = False
            else: break
            for i,j in enumerate(team.availableTasks):
                sum_out = team.sumOfEst(out)
                if (SPRINT_LENGTH - ((int)(sum_out)+j.val.estimate)) >= 0:
                    out.append(j)
                    team.availableTasks.pop(i)
                    break
                elif i == len(team.availableTasks)-1:
                    breakit = True
            sum_out = team.sumOfEst(out)
            if breakit:
                break
        return out
 
    def sumOfEst(team,out):
        #returns sum of estimates
        sumi = 0
        for i in out:
            sumi += i.val.estimate
        return sumi
            
    def executeSprint(team):
        initial_estimate = team.sprint.time
        for task in team.sprint.us:
            if (team.budget - task.val.cost) >= 0:
                team.budget -= task.val.cost
                team.cost_total  += task.val.cost
                team.value_total += task.val.value
                task.val.done = True
#                team.tasksrepo[team.index + i].val.done = True
                team.makeTasksDone(task)
                team.numCompletedTasks += 1
                team.updateTasksEst()
            else:
                team.availableTasks.append(task)
        team.sprint.updatesprint()
        final_estimate = team.sprint.time
        team.team_estimate += final_estimate
        

    def makeTasksDone(team,task):
        ind = team.tasksrepo.index(task)
        team.tasksrepo[ind].val.done =True

    def discoverNewTasks(team):
        team.visible += nextTime(team.decisions.dynamism/10.0)
        team.markTasksVisible()

    def updateTasks(team):
        #Adjust values
        for task in team.tasksrepo:
            change = (random.uniform(0, team.decisions.dynamism) - team.decisions.dynamism/2)*team.decisions.culture/100.0
            task.val.value += (MAX_VALUE * max(0,change))  
    
    def updateTasksEst(team):
        for task in team.sprint.us:
            change = (random.uniform(0, team.decisions.dynamism) - team.decisions.dynamism/2)*team.decisions.culture/10.0
            #print change
            task.val.estimate += (int)(MAX_EST_VALUE * max(0,change))  
            

def nextTime(rateParameter): return -math.log(1.0 - random.random()) / rateParameter                        
def countNotDones(list):
    cnt = 0
    for i in list:
        if i.val.done == False: cnt+= 1
    return cnt
