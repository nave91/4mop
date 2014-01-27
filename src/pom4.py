from pom4_userstories import *
from pom4_sprints import *
from pom4_teams import *
import random

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
                team.getnewsprint(POM4_TEAMS,POM4_SPRINTS)
                team.discoverNewTasks()
                team.updateTasks()
            
        


# Test Code 
p4 = pom4()
print p4.simulate([0.20, 1.26, 8, 0.95, 100, 10, 2, 5, 20])

 
           
