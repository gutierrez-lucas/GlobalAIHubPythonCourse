class Staff():
    def __init__(self, name, age, languages):
        self.name = name
        self.age = age
        self.languages = {languages}
        
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
    
    def addLanguages(self, languages):
        self.languages.add(languages)
    
    def updateLanguages(self, old_language, new_languages):
#in case of a input error
        if old_language in self.languages: #check if old lang is present in set
            self.languages.remove(old_language) #remove old
            self.languages.add(new_languages) #add new
            return True
        else: 
            print("there is not language to update like that. check spell")        
            return False
        
    def removeLanguages(self, languages):
        if languages in self.languages: #check if lang is present in set
            self.languages.remove(languages)       
    
    def printInfo(self):
        print("%s is %d old and can speak in %s" %(self.name, self.age, repr(self.languages)))
        
class employees(Staff):
    def __init__(self, name, age, languages):
        super().__init__( name, age, languages)
        self.name = name
        self.age = age
        self.languages = languages
        
class manager(Staff):
    def __init__(self, name, age, languages):
        super().__init__( name, age, languages)
        self.name = name
        self.age = age
        self.languages = languages
        
print("Company Managment System")

w1 = employees("marcos", 20, "portugues")
w1.printInfo()

w2 = manager("rodrigo", 50, "ingles, español, portugues")
w2.printInfo()

