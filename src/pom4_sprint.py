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

class Sprint(object):
    
    def __init__(self):
        
        #List of user stories
        self.us = []
        
        #Velocity of Sprint
        self.velocity = 0
        
        #Time under development
        self.time = 0
        
    def add_task(self,stasks):
        self.us.append(stasks.val)
        self.time += stasks.val.estimate
        
    def time(self): return self.time
    
    
