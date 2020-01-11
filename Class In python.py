class Person:
    def setfullname(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def getfullname(self):
        print(self.firstname, self.lastname)

personname = Person()
personname.setfullname("Aashish", "Gupta")
personname.getfullname()
