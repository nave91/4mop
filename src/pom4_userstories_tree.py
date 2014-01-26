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

class Userstory(object):
    
    def __init__(self, c, v):
        
        #cost of the userstory
        self.cost = c
        
        #value of the userstory
        self.value = v
        
        #if the task is visible
        self.visible = False
        
    def __repr__(self): return "User Story. Cost: " + str(self.cost) + ", Value: " + str(self.value) + ")"

class userstories_node(object):
    def __init__(self, v, k, p=None, c=[], l=0):
        self.val = v
        self.key = k
        self.parent = p
        self.children = c
        self.level = l
        self.dependencies = []
        
    def add_child(self, v, k, l):
        self.children.append(userstories_node(v, k, self, [], l))
    
    def __repr__(self):
        if self.parent:
            return ("-"*self.level + "{Key: " + str(self.key) + ", Val: " + str(self.val) + ", ParentKey = " + self.parent.key + " Dep: "+str(self.dependencies) + "}")
        else:
            return ("-"*self.level + "{Key: " + self.key + ", Val: " + str(self.val) + ", ParentKey = None" + " Dep: " + str(self.dependencies) + "}")

        
    def show(self):
        print(self)
        for child in self.children:
            child.show()
            
    def iterative_search(self, k):
        for child in self.children:
            if child.key == k: return child
            else:
                result = child.iterative_search(k)
                if result: return result
    
    def max_depth(self):
        max = 0
        for child in self.children:
            if child.level > max: max = child.level
            m = child.max_depth()
            if m > max: max = m
        return max
    
    def traverse(self):
        list = []
        for child in self.children:
            list.append(child)
            to_add = child.traverse()
            for i in to_add:
                list.append(i)
        return list
    
class userstories_tree(object):
    
    def __init__(self):
        self.tree = []
    
    def add_root(self, v, k):
        self.tree.append(userstories_node(v, k, None, [], 0))
    
    def get_root(self, k):
        for root in self.tree:
            if root.key == k: return root
    
    def find_node(self, k):
        for root in self.tree:
            if root.key == k: return root
            else:
                result = root.iterative_search(k)
                if result: return result
    
    def get_level(self, root, level):
        list = []
        if (root.level < level):
            for child in root.children:
                list.append(self.get_level(child, level))
        elif (root.level == level):
            list.append(root.key)
        return list
    
    def traverse(self):
        list = []
        for root in self.tree:
            list.append(root)
            to_add = root.traverse()
            for i in to_add:
                list.append(i)
        return list
    
    def show(self):
        for root in self.tree:
            root.show()

