class details:
    n = int(input("enter the number of items : "))
    def __init__(self):
        
        self.l1 = []
        for i in range(1 , details.n+1):
            print("enter the name of item ",i," : ")
            self.e = input()
            self.l1.append(self.e)
    def detail(self):
        self.l2 = []
        for self.i1 in range(1 , details.n+1):
            print("enter the price of item " , self.i1 , ": ")
            self.e1 = int(input())
            self.l2.append(self.e1)
    
    def code(self):
        self.l3 = []
        for self.i2 in range(1 , details.n+1):
            print("enter the code of items ",self.i2,": ")
            self.e2 = input()
            self.l3.append(self.e2)
        
class display(details):
    def __init__(self):
        details.__init__(self)
        
        self.res = 0

    def result(self):
        print("********************DETAILS OF ITEMS********************")
        #details.detail(self)
        #details.code(self)
        print("number of items : " , details.n)
        self.res = self.l1
        print("name of items : " , self.res)
        self.res = self.l2
        print("price of items : ",self.res)
        self.res = self.l3
        print("code of items : " , self.res)

    def total(self):
        self.res = sum(self.l2)
        print("Total price",self.res)

obj = display()
obj.detail()
obj.code()
obj.result()
obj.total()