from numpy import random
import numpy as np
class initialDepo:
    def __init__(self,deposit):
        deposit=int(input("Enter your initial deposit:"))
        if deposit >=1000 and deposit<=10000:
            deposit=deposit
        else:
            raise Exception
        self.deposit=deposit
    def depoOutput(self):
        print(self.deposit)
class gauseeNum(initialDepo):
    def __init__(self, deposit,intNum):
        super().__init__(deposit)
        intNum=int(input("Enter random number between zero and three:"))
        self.intNum=intNum
    def intNumOutput(self):
        print(self.intNum)
class RandomNumber(gauseeNum):
    def __init__(self, deposit, intNum,randNum):
        super().__init__(deposit, intNum)
        randNum=np.array([0,1,2,3])
        random.shuffle(randNum)
        self.randNum=randNum
    def randNumOutput(self):
        print(self.randNum)
class Results(RandomNumber):
    def __init__(self, deposit, intNum, randNum,win,lose):
        super().__init__(deposit, intNum, randNum)
        win=self.deposit*10
        lose=self.deposit*0
        self.win=win
        self.lose=lose
    def ResultOutput(self):
        if self.intNum==self.randNum[2]:
           print("CONGRATULATION! YOU HAVE WON Ksh",self.win) 
        elif self.intNum!=self.randNum[2]:
           print("SORRY!,Your balance is Ksh",self.lose,"Deposit and try again")
gameOutput=Results("deposit","intNum","randNum","win","lose")
gameOutput.ResultOutput()



