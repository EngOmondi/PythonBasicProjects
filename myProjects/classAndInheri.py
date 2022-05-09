class myClass:
    def __init__(self,name,age):
        
        name=str(input("Enter your name:")) 
        self.name=name
        
        age=int(input("Enter your age:")) 
        self.age=age
    def myObjectMethod(self):  
        print("my details",self.age ,self.age, " years")  
class students(myClass):
    def __init__(self, name, age,adm):
        super().__init__(name, age)
        
        adm=input("Enter your admission number :")
        self.adm=adm
    def abc(self):
        print(self.adm)
class subjects(students):
    def __init__(self, name, age, adm,english,kiswahili,math,chem,bio):
        super().__init__(name, age, adm) 
        
        english=int(input("Enter marks scored in english:")) 
        self.english=english    
        
        kiswahili=int(input("Enter marks scored in kiswahili:")) 
        self.kiswahili=kiswahili
        
        math=int(input("Enter marks scored in math:")) 
        self.math=math
        
        chem=int(input("Enter marks scored in chem:")) 
        self.chem=chem
       
        bio=int(input("Enter marks scored in bio:"))
        self.bio=bio 
    def subjects(self): 
        print(self.english,self.kiswahili,self.math,self.chem,self.bio)
class totalMarks(subjects):
    def __init__(self, name, age, adm, english, kiswahili, math, chem, bio,total):
        super().__init__(name, age, adm, english, kiswahili, math, chem, bio)
        
        total=(self.english + self.kiswahili + self.math + self.chem + self.bio)
        self.total=total
    def marks(self):
        print(self.total)

class myAverage(totalMarks):
    def __init__(self, name, age, adm, english, kiswahili, math, chem, bio, total,average):
        super().__init__(name, age, adm, english, kiswahili, math, chem, bio, total)    
        
        average=(self.total/5)
        self.average=average
    def myMean(self):
        print(self.average)
class gradingSystem(myAverage):
    def __init__(self, name, age, adm, english, kiswahili, math, chem, bio, total, average,grade):
        super().__init__(name, age, adm, english, kiswahili, math, chem, bio, total, average)
        self.grade=grade
        if self.average>=80 and self.average<=100:
            self.grade="A"
        elif self.average>=70 and self.average<=79:
            self.grade="B"
        elif self.average>=60 and self.average<=69:
            self.grade="C"
        elif self.average>=50 and self.average<=59:
            self.grade="D"
        elif self.average>=40 and self.average<=49:
            self.grade="E"
        elif self.average>=0 and self.average<=39:
            self.grade="F"
        else:
            self.grade="N/A"
    def myGrade(self): 
        print("Thank",self.name, "for completing your term. your total marks is:",self.total,
        "And the average marks is",self.average,"Therefore you have grade:",self.grade) 

myGradingSystem=gradingSystem("name","age","adm","english","kiswahili","math","chem","bio","total","average","grade")      







