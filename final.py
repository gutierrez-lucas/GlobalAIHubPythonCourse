#######
#FINAL PROJECT
#######
# Company Management System: Determinae the names and ages of employees, company manager
# and the languages they canspeak. Then write a program that will print the languages that 
# any of the employees can speak. In this project, complete the project by creating two classes
# named "employees" and "manager"
#######
# IT WASENT CLEAR FOR ME WHAT WAS THE PRECISE ASSIGNAMENT REGARDING THE LANGUAGE PRINT CAPABILITY
# SO I OPT TO PRINT WICH STAFF MEMBERS COULD TALK IN EVERY AND EACH LANGUAGE ONE BY ONE
#######

availableLanguages = {"Spanish":[], "French":[], "English":[], "Turkish":[]}
# it may be a more efficient way to do it, probably iteration between the attributes of each class instance
# but it doesnt seems to be that direct and easy, so I will fill a dictonary in wich each key is a language
# and each value of that key is a list of names
    
class Staff():
    def __init__(self, name, age, languages):
        self.name = name
        self.age = age
        self.languages = {languages}
    
    def checkLanguages(self):
#checks wich languages does the 'name' person speaks and if add the name to the language in a dictonary        
        if ("English" in self.languages) == True:
            if (self.name in availableLanguages.get("English")) == False:
#this is quite horrible because of the repetition but a list (the value of the language key)
#allows duplicates, and if this method is called
#by error more than once, it will duplicate the name in the language
                availableLanguages.get("English").append(self.name)
        if ("Spanish" in self.languages) == True:
            if (self.name in availableLanguages.get("Spanish")) == False:
                availableLanguages.get("Spanish").append(self.name)
        if ("French" in self.languages) == True:
            if (self.name in availableLanguages.get("French")) == False:
                availableLanguages.get("French").append(self.name)
        if ("Turkish" in self.languages) == True:
            if (self.name in availableLanguages.get("Turkish")) == False:
                availableLanguages.get("Turkish").append(self.name)
    
    def getName(self):
        return self.name
    
    def updateName(self, name):
        self.name = name
    
    def getAge(self):
        return self.age
    
    def updateAge(self, age):
        self.age = age    
    
    def getLanguages(self):
        return self.languages
    
    def addLanguages(self, _languages):
        self.languages.add(_languages)
    
    def updateLanguages(self, old_language, new_languages):
#in case of a input error
        if old_language in self.languages: #check if old lang is present in set
            self.languages.remove(old_language) #remove old
            self.languages.add(new_languages) #add new
            return True
        else: 
            print("there is not language to update like that. check spell")        
            return False
        
    def removeLanguages(self, _languages):
        if _languages in self.languages: #check if lang is present in set
            self.languages.remove(_languages)       
    
    def printInfo(self):
        print("%s is %d old and can speak in %s" %(self.name, self.age, repr(self.languages)))
        
# i didnt find any differences in attributes between 'employees' and 'manager' for the precise project assignament
# (may be salary coeficient  to auto calculate the later ?) so this two classes inherits the exact same class
class employees(Staff):
    def __init__(self, name, age, languages):
        super().__init__( name, age, languages)
        self.name = name
        self.age = age
        self.languages = {languages}
        
class manager(Staff):
    def __init__(self, name, age, languages):
        super().__init__( name, age, languages)
        self.name = name
        self.age = age
        self.languages = {languages}
        
def printStaffbyLangugage():
    print("\nThe following eployees can talk in Spanish: ")
    for i in range(0,len(availableLanguages.get("Spanish"))):
        print(availableLanguages.get("Spanish")[i])
        
    print("\nThe following eployees can talk in English: ")
    for i in range(0,len(availableLanguages.get("English"))):
        print(availableLanguages.get("English")[i])
        
    print("\nThe following eployees can talk in Turkish: ")
    for i in range(0,len(availableLanguages.get("Turkish"))):
        print(availableLanguages.get("Turkish")[i])
        
    print("\nThe following eployees can talk in French: ")
    for i in range(0,len(availableLanguages.get("French"))):
        print(availableLanguages.get("French")[i])
        
print("Company Managment System")

e1 = employees("Luis Ponse", 23, "English")
e1.addLanguages("Spanish")
e1.checkLanguages()
e2 = employees("Andres Ignez", 22, "English")
e2.checkLanguages()
e3 = employees("Maria Lopez", 29, "English")
e3.addLanguages("Spanish")
e3.checkLanguages()
e4 = employees("Julia Rodriguez", 21, "English")
e4.addLanguages("French")
e4.checkLanguages()
e5 = employees("Juan Pablo Gomez", 31, "English")
e5.addLanguages("Turkish")
e5.checkLanguages()
e6 = employees("Esteban Muñoz", 22, "English")
e6.checkLanguages()
e7 = employees("Juan Perez", 30, "English")
e7.checkLanguages()
e8 = employees("Pedro Gomez", 24, "English")
e8.addLanguages("Turkish")
e8.addLanguages("Spanish")
e8.checkLanguages()
e9 = employees("Andrea Estevez", 26, "English")
e9.checkLanguages()
e10 = employees("Roque Perez", 35, "English")
e10.checkLanguages()

m1 = manager("Andre Gomez", 52, "English")
m1.addLanguages("Spanish")
m1.addLanguages("Turkish")
m1.checkLanguages()
m2 = manager("Luis Perez", 56, "English")
m2.addLanguages("Spanish")
m2.addLanguages("French")
m2.checkLanguages()
m3 = manager("Pedro Rodriguez", 40, "English")
m3.addLanguages("Spanish")
m3.checkLanguages()
m4 = manager("Ernesto Lopez", 64, "English")
m4.addLanguages("French")
m4.checkLanguages()
m5 = manager("Luisina Olaizola", 65, "English")
m5.addLanguages("Turkish")
m5.checkLanguages()

printStaffbyLangugage()