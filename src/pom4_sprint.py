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
        
        #Total Cost of whole Sprint
        self.cost = 0
        
        #Total Value of whole Sprint
        self.value = 0
        
    def __repr__(self):
        string = ""
        for i in self.us:
            string += (str(i.val)+",")
        string += "$"
        return string

    def add_task(self,tasks):
        if tasks != None: self.us.append(tasks)
        self.time += tasks.val.estimate
        self.cost += tasks.val.cost
        self.value += tasks.val.value
        
    def markTasksVisible(self,visible):
        for i in range(len(self.us)):
            self.us[i].val.visible = True
    
    
