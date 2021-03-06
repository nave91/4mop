from pom4_team import *
import math

"""#################################################################
   #### 
   #### -@author: Naveen Kumar Lekkalapudi
   #### -@note: POM4 Teams (collection) Management Module
   #### -@note: This work is done in affilication with  
   #### -@note: West Virginia University
   #### -@contact: nalekkalapudi@mix.wvu.edu
   #### -@copyright: This work is made for academic research. 
   #### -@copyright: Do not edit without citing POM4 as a reference.
   #### -@reference: POM3
   ####
   ##################################################################"""

class pom4_teams:
    def __init__(p4t, userstories, decisions):
        p4t.teams = []
        p4t.decisions = decisions
        
        #Index of sprints Collection
        p4t.index = 0

        # Build Each Team
        total_size = 0

        while (total_size < userstories.count):
            #specific sized teams
            p4t.teams.append(Team(decisions))
            total_size += decisions.team_size

        # Assign Initial Tasks to Each Team
        begin = 0
        for team in p4t.teams:
            percent = (float)(team.team_size) / (float)(total_size)
            end = (int)(begin+math.ceil(percent*len(userstories.tasks))-1)
            for k in range(begin, end):
                team.tasksrepo.append(userstories.tasks[k])
            begin = end
        if ((end) < len(userstories.tasks)):
            for i in range(len(userstories.tasks) - (end)):
                p4t.teams[len(p4t.teams)-1].tasksrepo.append(userstories.tasks[begin+i])
        
        
        # Mark Initial Visibility of Tasks for Each Team
        for team in p4t.teams:
            team.markTasksVisible()
        
        # Apply Effect of Boehm-Turner Personnel Scales to Task Costs
        scales_alpha = [0.45, 0.50, 0.55, 0.60, 0.65]
        scales_beta  = [0.40, 0.30, 0.20, 0.10, 0.00]
        scales_gamma = [0.15, 0.20, 0.25, 0.30, 0.35]
        for team in p4t.teams:
            
            numAlphas = scales_alpha[decisions.size]*team.team_size
            numBetas = scales_beta[decisions.size]*team.team_size
            numGammas = scales_gamma[decisions.size]*team.team_size
            #print numAlphas, numBetas, numGammas
            team.alpha = numAlphas
            team.beta = numBetas
            team.gamma = numGammas
            team.power = team.alpha + 1.22*team.beta + 1.6*team.gamma
            
            for task in team.tasksrepo:
                task.val.cost += task.val.cost * ((numAlphas + 1.22*numBetas + 1.6*numGammas)/100.0)
                
                #apply efect of criticality 
                task.val.cost = task.val.cost * (team.decisions.criticality_modifier ** team.decisions.criticality)


        
        #Print Out of Teams & Requirements
          
        """for i,team in enumerate(p4t.teams): 
            print "___________________TEAM #" + str(i) + "______________________"
            for e,us in enumerate(team.tasksrepo):
                print "> USRSTORY #" + str(e) + ": " + str(us)"""
        
