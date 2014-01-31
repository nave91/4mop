from pom4_userstories import *
from pom4_sprints import *
from pom4_teams import *
import random

"""#################################################################
   #### 
   #### -@author: Naveen Kumar Lekkalapudi
   #### -@note: POM4 Simulation Main Module
   #### -@note: This work is done in affilication with  
   #### -@note: West Virginia University
   #### -@contact: nalekkalapudi@mix.wvu.edu
   #### -@copyright: This work is made for academic research. 
   #### -@copyright: Do not edit without citing POM4 as a reference.
   #### -@reference: POM3
   ####
   ##################################################################"""

class pom4_decisions:
    def __init__(p4d, X):
        p4d.culture = X[0]
        p4d.criticality = X[1]
        p4d.criticality_modifier = X[2]
        p4d.initial_known = X[3]
        p4d.interdependency = X[4]
        p4d.dynamism = X[5]
        p4d.size = int(X[6])
        p4d.plan = int(X[7])
        p4d.team_size = X[8]
        
class pom4:
            
    def simulate(p4, inputs):
    
        # # # # # # # # # # #
        # 0) Initialization #
        # # # # # # # # # # #
        
        POM4_DECISIONS = pom4_decisions(inputs)
        numberOfShuffles = random.randint(2,6)
    
        # # # # # # # # # # # # # # #
        # 1) Generate Requirements  #
        # # # # # # # # # # # # # # #
        
        POM4_USERSTORIES = pom4_userstories(POM4_DECISIONS)
        
        # # # # # # # # # # # 
        # 2) Build Sprints  #
        # # # # # # # # # # #
        
        POM4_SPRINTS = pom4_sprints(POM4_USERSTORIES)

        # # # # # # # # # # # #
        # 2) Initialize teams #
        # # # # # # # # # # # #
        
        POM4_TEAMS = pom4_teams(POM4_SPRINTS, POM4_DECISIONS)
        
        # # # # # # # #
        # 3) Shuffle  #
        # # # # # # # #
        
        
        for shufflingIteration in range(numberOfShuffles):
            for team in POM4_TEAMS.teams:
                team.updateBudget(numberOfShuffles)
                team.collectAvailableTasks(POM4_USERSTORIES)
                team.applySortingStrategy()
                team.executeAvailableTasks()
                team.discoverNewTasks()
                team.updateTasks()
                team.getnewsprint(POM4_TEAMS,POM4_SPRINTS)

        """for i,team in enumerate(POM4_TEAMS.teams): 
            print "___________________TEAM #" + str(i) + "______________________"
            for e,us in enumerate(team.tasksrepo):
                print "> USRSTORY #" + str(e) + ": " + str(us)"""


        # # # # # # # # # # # # #
        # 4) Objective Scoring  #
        # # # # # # # # # # # # #
        
        cost_sum,value_sum,god_cost_sum,god_value_sum,completion_sum,available_sum,total_tasks = 0.0, 0.0, 0.0, 0.0, 0,0,0
        for team in POM4_TEAMS.teams:
            cost_sum += team.cost_total
            value_sum += team.value_total
            available_sum += team.numAvailableTasks
            completion_sum += team.numCompletedTasks
            for task in team.tasksrepo:
                if task.val.visible:
                    total_tasks += 1
            
            for task in team.tasksrepo:
                if task.val.done == True:
                    god_cost_sum += task.val.cost
                    god_value_sum += task.val.value
                    
#        print "cost",cost_sum,"value",value_sum,"completion",completion_sum,"avaiable",available_sum,"tot tasks",total_tasks
        if cost_sum == 0: our_frontier = 0.0
        else: our_frontier =     value_sum /     cost_sum
        
        if god_cost_sum == 0: god_frontier = 0.0
        else: god_frontier = god_value_sum / god_cost_sum
        
        if god_frontier == 0.0: score = 0.0
        else: score        =  our_frontier / god_frontier
        
        if completion_sum == 0: cost = 0
        else: cost = cost_sum/completion_sum
        
        if available_sum == 0: idle = 0
        else: idle = 1 - completion_sum/float(available_sum)
        
        if total_tasks == 0: completion = 0
        else: completion = completion_sum/float(total_tasks)
        
        
        
        return [cost, score, completion, idle]
            
        


# Test Code 
p4 = pom4()
print p4.simulate([0.20, 1.26, 8, 0.95, 100, 10, 2, 5, 20])

 
           
