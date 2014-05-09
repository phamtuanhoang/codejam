import sys,os

class ReverseWord():
    #code
    testcase = 0
    sentence = list()
    def enterWord(self, ):
        test = input("Enter number of test case: ")
        
        sen = input("Please enter input to reverse: ")
        self.sentence = str(sen).split(" ")
        
    def reverseword(self):
        print(len(self.sentence)) 
        for i in range(len(self.sentence) -1,-1,-1):
            print(self.sentence[i])
            input("Stop")

if __name__ == '__main__':
    reverse = ReverseWord()
    reverse.enterWord()
    reverse.reverseword()
    
    
    
