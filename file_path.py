import sys,os

class filepath:
    testcase = 0
    data = list()
    filepath = 0
    createdir = 0
    dirList = list()
    dirCreate = list()
    totalCommand = 0
    def input_data(self):
        self.testcase = raw_input("")
        #loop through test case
        for i in range(0, int(self.testcase)):
            input_filepath = raw_input("")
            data = [ x for x in list(input_filepath)  if x != ' ']
            self.input_dir(int(data[0]), int(data[1]))
        #reset everything
        self.totalCommand = 0
        self.dirList = list()
        self.dirCreate = list()
        self.data = list()
        
    def input_dir(self,dirNo, dirCreate):
        for i in range(0,dirNo):
            dirName = raw_input("input dir name:")
            newdirName = dirName.split('/')
            del newdirName[0]
            self.dirList.append(list(newdirName))
        
        #dir to create
        for i in range(0,dirCreate):
            dirName = raw_input("input create dir: ")
            newDirName = dirName.split('/')
            del newDirName[0]
            self.dirCreate.append(list(newDirName))
        
        #count command
        self.count_command()
        
    def count_command(self):
        #loop through each dir want to create
        commandNo = 0
        matchingList= list()
        
        for i in range(0, len(self.dirCreate)):
            #loop through each dir in the target dir
            noCommand = 0
            matchingList = self.count_matching(self.dirCreate[i], self.dirList)
            self.dirList.append(self.dirCreate[i])
            #count no of command to create new dir
            indexOfExisting = matchingList.index(max(matchingList))
            #get the length of existing then minus
            noCommand = len(self.dirCreate[i]) - max(matchingList) 
            #get repeated unique dir
            self.totalCommand += noCommand
        
        print 'Total Command: '
        print self.totalCommand
       
       
            
    def count_matching(self, createDir,directoryList):
        countList = list()
        repeatDir = 0
        for i in range(0, len(directoryList)):
            count = 0
            for j in range(0, len(createDir)):
                if createDir[j] in directoryList[i]:
                    #compare if index is same
                    if createDir[j] == directoryList[i][j]:
                        count += 1 
                else:
                    break
            countList.append(count)
        return countList    
    def checkCreatedDir(self,createDir, pos):
        for i in range(0, len(self.dirCreate)):
            if i in self.dirCreate[i]:
                if createDir == self.dirCreate[i][pos]:
                    return True
                else:
                    return False
                
                      
         
         
if __name__ == '__main__':
    filepath = filepath()
    filepath.input_data()