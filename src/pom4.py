from pom4_userstories import *
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
        
        for i in POM4_USERSTORIES.tasks:
            print i
    

# Test Code 
p4 = pom4()
print p4.simulate([0.20, 1.26, 8, 0.95, 100, 10, 2, 5, 20])

 
           
