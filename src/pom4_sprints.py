from pom4_sprint import *

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

class pom4_sprints(object):
    
    def __init__(sprints,Sprint):
        
        #List of sprints
        sprints.collection = []
        
        #List of tasks
        sprints.stasks = []
        
    def collecttasks(sprints,tasks):
        sprints.stasks = tasks

    def addsprint(sprints,Sprint):
        sprints.collection.append(Sprint)
        
    def buildsprints(sprints):
        pass
    
    def func_name(stasks,item,alist):
        if stasks:
            item = list.pop(0)
            if item.val.estimate >= 30:
                alist.append(item)
            else:
                temp = 0
                templ = [item]
                for i in range(0,len(stasks)):
                    if stasks[i].val.estimate + item.val.estimate <=30:
                        temp = stasks.pop(i)
                        templ.append(temp)
                        break
                if temp == 0: alist.append(templ)
                f(list,templ,los)
        
            
        
