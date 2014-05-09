import sys,os



class StoreCredit():
    
    #enter number of test case
    test_case = 0
    credit = 0
    item = 0
    item_price = list()
    def input_testCase(self, testCase):
        self.test_case = testCase
        print (self.test_case)
    def input_credit(self, credit):
        self.credit = credit
        print (self.credit)
    def input_no_item(self, item):
        self.item = item
        #asked user to input total price
        price_list = input("Please list of price: ")
        self.item_price = str(price_list).split()
        #check if no of price > no of item
        if len(self.item_price) != self.item:
            print("Not match")
            sys.exit()
    def process_calculation(self):
  
        #loop test case
        for  t in range(0, self.test_case ):
            #input data for each test case
            self.input_credit(int(input("Please enter number credit: ")))
            self.input_no_item(int(input("Please enter number of item: ")))
            for i in range(0, len(self.item_price)):
                print("Process calculation")
                temp = int(self.item_price[i])
                for j in range(i+1, len(self.item_price)):
                    if((int(self.item_price[j]) + temp) == self.credit):
                        print(i)
                        print(j)
                        pass

    def get_user_input(self):
        self.input_testCase(int(input("Please enter number of test case: ")))
        self.process_calculation()
        
    
if __name__ == '__main__':
    credit = StoreCredit()
    credit.get_user_input()
    