class myClass:
    def __init__(self,name,age,position):
        self.name=name
        self.age=age
        self.position=position
    def myObjectMethod(self):
        print("These are the details of fidel castro","name is",self.name,"age is",self.age,"years","position is",self.position)     

myObject=myClass("fidel",56,"president")
myObject.myObjectMethod()
