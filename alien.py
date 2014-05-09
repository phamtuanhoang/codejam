import sys, os


class Alien():
    #code
    data = list()
    transmittedWord = list()
    treeStructure = list()
    def input_data(self):
        test = raw_input("input number:")
        self.data = [x for x in list(test) if x!=' ']
        self.process()
    def process(self):
        #input dictionary
        dictionary = list()
        for i in range(0,int(self.data[0])):
            x = raw_input()
            dictionary.append(x)
        #input word
        for i in range(0, int(self.data[1])):
            w = raw_input()
            new = w.replace('(',",")
            new = new.replace(')',",")
            new = new.split(',')
            while True:
                try:
                    new.remove("")
                except ValueError:
                    break
            #break word based on ( and ) and add to data list
            self.transmittedWord.append(new)
       
        for i in range(0, len(self.transmittedWord)):
            self.constructTree(self.transmittedWord[i])
        
        
    #construct tree for transmitted word
    def constructTree(self, data = list()):
        for i in range(0, len(data)):
            for j in range(0, len(list(data[i]))):
                node = list(data[i][j])
                newNode = Tree(node)
                childNodeList = []
                if i < len(data)-1:
                    for k in range(0, len(data[i+1])):    
                        childNode = Tree(data[i+1][k])
                        childNodeList.append(childNode)
                newNode.setChild(childNodeList)   
                self.treeStructure.append(newNode)
        print len(self.treeStructure[0].getChild())
        self.treeRecursive(0)
        
     
    def treeRecursive(self, level = 0):
        #recursive to print tree
        text= "t"*level + repr(self.treeStructure[level].getParent()) + "\n"
        for child in self.treeStructure[level].getChild():
            child.getParent()
            text+= treeRecursive(level+1)
        
        
        
class Tree(object):
    #code
    value = ""
    child = []
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    def setParent(self,parentNode):
        self.value = parentNode
    def setChild(self, childNode = []):
        self.child = childNode
    def getChild(self):
        return self.child
    def getParent(self):
        return self.value
    
    def treeTravel(self, level = 0):
        for 
    
    
    
    
    
if __name__ == '__main__':
    alien = Alien()
    alien.input_data()