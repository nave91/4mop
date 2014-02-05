from pom4_userstories_tree import *
import pom4_lib

"""#################################################################
   #### 
   #### -@author: Naveen Kumar Lekkalapudi
   #### -@note: POM4 User Stories Heap Module
   #### -@note: This work is done in affilication with  
   #### -@note: West Virginia University
   #### -@contact: nalekkalapudi@mix.wvu.edu
   #### -@copyright: This work is made for academic research. 
   #### -@copyright: Do not edit without citing POM4 as a reference.
   #### -@reference: POM3
   ####
   ##################################################################"""

def random_cost(): return pom4_lib.random.randint(1, 100)
def random_value(): return pom4_lib.random.randint(1, 100)
def random_estimate(): return pom4_lib.random.randint(1, 30) #upto sprint length

class pom4_userstories:
    
    def __init__(userstories, decisions):
        userstories.heap = userstories_tree()
        userstories.count = int(2.5*[3,10,30,100,300][decisions.size])
        userstories.decisions = decisions
        
        for i in range(userstories.count):
            userstories.heap.add_root(Userstory((decisions.size+1)*random_cost(), random_value(), random_estimate()), 'Base UsrStry #' + str('%.3d'%(i+1)))
            
            parent = userstories.heap.tree[i]
            userstories.recursive_adder(parent, 1)
            
        #Add dependencies
        for i in range(userstories.count):
            rand = pom4_lib.random.randint(1,1000)
            if (rand <=15):
                #pick a userstory at this level, of the next base tree
                level = 0
                if ((i+1) < len(userstories.heap.tree)):
                    req_node = userstories.heap.tree[i+1]
                    adderDie = pom4_lib.random.randint(1,100)
                    if adderDie <= decisions.interdependency: 
                        userstories.add_dependency(userstories.heap.tree[i], req_node)
            userstories.recursive_dep_adder(userstories.heap.tree[i], i, 1)
            
        #linearize the list
        userstories.tasks = userstories.heap.traverse()
        
        #testing
        #for i in userstories.tasks:
        #    print i


    def add_children(self, num, parent, level):
        for c in range(num):
            parent.add_child(Userstory(random_cost(), random_value(), random_estimate()),
                             "+"*level + 'Child-' + parent.key[0]
                             + parent.key[len(parent.key)-3]
                             + parent.key[len(parent.key)-2]
                             + parent.key[len(parent.key)-1]
                             + ' #' + str('%.3d'%(c+1)),level)
            self.recursive_adder(parent.children[c],level+1)
            
    def add_dependency(self, dep_node, req_node):
        #Add a dependency from this node to another node at 
        # the same level of the next root
        #We store the key of the requirement_node in the list of 
        # the dependent_node's dependencies
        dep_node.dependencies.append(req_node)
        
    def recursive_adder(self, parent, level):
        #Random exponential chance that we add child node:
        rand = pom4_lib.random.randint(1,1000)
        odds = [15, 30, 60, 120, 240]
        
        for numChildren,chance in enumerate(odds):
            if rand <= chance:
                self.add_children(5-numChildren, parent, level)
                break
            
    def recursive_dep_adder(self, parent, rootIndex, level):
        
        if len(parent.children) > 0 and ((rootIndex+1) < len(self.heap.tree)):
            if level <= self.heap.tree[rootIndex+1].max_depth():
                rand = pom4_lib.random.randint(1,1000)
                odds = [15, 30, 60, 120, 240]
                
                if level >= 5: oddsInd = 4
                else: oddsInd = level
                
                if rand <= odds[oddsInd]:
                    #pick a random child at this level of this root
                    rand = pom4_lib.random.randint(0,len(parent.children)-1)
                    randChild = parent.children[rand]
                    
                    #pick a random node at the level of the next root
                    levelNodes = self.heap.get_level(self.heap.tree[rootIndex+1], level)
                    rand = pom4_lib.random.randint(0, len(levelNodes)-1)
                    
                    #add dependency from randChild to levelNodes[rand]
                    adderDie = pom4_lib.random.randint(1,100)
                    if adderDie <= self.decisions.interdependency: 
                        self.add_dependency(randChild, levelNodes[rand])
                for child in parent.children:
                    self.recursive_dep_adder(child, rootIndex, level+1)
        
