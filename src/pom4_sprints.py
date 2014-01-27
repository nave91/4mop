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
    
    def __init__(sprints,userstories):
        
        #List of sprints
        sprints.collection = []

        #Number of sprints
        sprints.numofsprints = 0
        
        #List of tasks
        sprints.tasks = []
        
        #Number of tasks
        sprints.numoftasks = []

        #collecting stasks from tasks
        sprints.collecttasks(userstories.tasks)
        
        #Building sprints
        sprints.buildsprints()
        
        #Show sprints
        print "######Showing"
        """for i in sprints.collection:
            print i
            print i.time
            print i.value
            print i.cost
            print """""
        
    def __repr__(sprints):
        string = ""
        for i in sprints.collection:
            string += (str(i)+"\n######")
        return string
    
    def collecttasks(sprints,tasks):
        sprints.tasks = tasks
        sprints.numoftasks = len(tasks)

    def addsprint(sprints,Sprint):
        sprints.collection.append(Sprint)
        sprints.numofsprints = len(sprints.collection)
        
    
    def buildsprints(sprints):
        length = len(sprints.tasks)
        print length,"length of staks"
        print "########Building"
        i=0
        while i < (((length/3)*3)-2):
            sprint = Sprint()
            sprint.add_task(sprints.tasks[i])
            sprint.add_task(sprints.tasks[i+1])
            sprint.add_task(sprints.tasks[i+2])
            sprints.addsprint(sprint)
            i += 3
        sprint =Sprint()    
        for j in range(0,length%3):
            sprint.add_task(sprints.tasks[i])
            i += 1
        sprints.addsprint(sprint)
        
    
    
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
        
            
        
