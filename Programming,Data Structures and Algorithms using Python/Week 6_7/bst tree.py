class Tree:
    def __init__(self,initval=None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
            self.height = 1
        else:
            self.left = None
            self.right = None
            self.height = 0
        return
    def isempty(self):
        return (self.value == None)
    def isleaf(self):
        return (self.value != None and self.left.isempty() and self.right.isempty())
    #Preorder
    def preorder(self):
        if self.isempty():
            return ([])
        else:
            return ([self.value] + self.left.preorder() + self.right.preorder())
    #Postorder
    def postorder(self):
        if self.isempty():
            return ([])
        else:
            return (self.left.postorder() + self.right.postorder() + [self.value])
    #INORDER
    def inorder(self):
        if self.isempty():
            return ([])
        else:
            return (self.left.inorder() + [self.value] + self.right.inorder())
    def __str__(self):
        return str(self.inorder())
    #To check if a value v occurs in the tree
    def find(self,v):
        if self.isempty():
            return False
        if self.value == v:
            return True
        elif self.value < v:
            return (self.left.find(v))
        else:
            return (self.right.find(v))
    #Minval and Maxval
    def minval(self):
        if self.left.isempty():
            return self.value
        else:
            return self.left.minval()
    def maxval(self):
        if self.right.isempty():
            return self.value
        else:
            return self.right.maxval()
    #Inserting a node
    def insert(self,v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
            self.height = 1
        if self.value == v:
            return
        if v < self.value:
            self.left.insert(v)
            self.left.rebalance()
            self.height = 1 + max(self.left.height,self.right.height)
            return
        if v > self.value:
            self.right.insert(v)
            self.right.rebalance()
            self.height = 1 + max(self.left.height,self.right.height)
            return
    #Deleting a node
    #Prerequisite functions required to delete: makeempty, copyleft, copyright
    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return
    def Copyleft(self):
        self.value = self.left.value
        self.right = self.left.right
        self.left = self.left.left
        return
    def Copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return 
    #Now, the actual delete function
    def delete(self,v):
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v== self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.Copyright()
            elif self.right.isempty():
                self.Copyleft()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
                return
    #Left and right rotate
    def leftrotate(self):
        v = self.value
        vr = self.right.value
        tl = self.left 
        trl = self.right.left
        trr = self.right.right
        
        newleft = Tree(v)
        newleft.left = tl
        newleft.right = trl
        
        self.value = vr
        self.right = trr
        self.left = newleft
        return
    def rightrotate(self):
        v = self.value
        vl = self.left.value
        tr = self.right
        tll = self.left.left
        tlr = self.left.right
        
        newright = Tree(v)
        newright.right = tr
        newright.left = tlr
        
        self.value = vl
        self.right = newright
        self.left = tll
        return
    def rebalance(self):
        if self.left.height - self.right.height == 2:
            self.left.leftrotate()
        if self.left.height - self.right.height == -2:
            self.right.rightrotate()
            

o = Tree()
o.insert(1)
o.insert(2)
o.insert(3)
o.insert(4)
o.insert(5)
o.insert(6)
o.insert(7)


print(o)
print(o.preorder())
print(o.postorder())
print(o.height)

        