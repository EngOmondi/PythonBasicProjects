class Marks:
     def __init__(self,mathematics,English):
         mathematics=int(input("enter your score in Mathematics"))
         self.mathematics=mathematics
         English=int(input("enter your score in English"))
         self.English=English
     
     def averageMarks(self):
         average=(self.mathematics+self.English)/2
         

class moreDetails(Marks):
    def __init__(self, mathematics, English,name,school,fucalty,course):
        super().__init__(mathematics, English)
        name=str(input("Enter your name here:"))
        self.name=name
        school=str(input("Enter the name of your school here:"))
        self.school=school
        fucalty=str(input("Enter the name of your fucalty:"))
        self.fucalty=fucalty
        course=str(input("Enter the name of your course here:"))
        self.course=course

    def objtmoredetails(self):
        x=(self.name,"of the school of",self.school,"fucalty of",self.fucalty,"who is persuing a programm leading to",self.course,"has scored an average marks of",average)
        print(x)
finaloutput=moreDetails("mathematics", "English","name","school","fucalty","course")
finaloutput.objtmoredetails()
