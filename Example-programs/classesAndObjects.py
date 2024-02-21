class Employee:
    firstName = "jayanth"
    lastName = "pallem"

    #def __init__(self):
       # pass
 
    def getFullName(self):
        return self.firstName +" "+ self.lastName
om= Employee()
print(om.getFullName())
    