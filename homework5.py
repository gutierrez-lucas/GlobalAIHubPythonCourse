class Animals():
    def __init__(self, group, height, weigth, age):
        self.group = group
        self.height = height
        self.weigth = weigth
        self.age = age
        
    def getGroup(self):
        return self.group

    def getHeight(self):
        return self.height
            
    def getWeigth(self):
        return self.weigth 
    
    def getAge(self):
        return self.age          

class Cat(Animals):
    def __init__(self, group, height, weigth, age, name, breed, color):
        super().__init__(group, height, weigth, age)
        self.name = name
        self.breed = breed
        self.color = color
            
    def printDetails(self):
        print("This animal is a Cat. Belongs to the %s group, is %d cm tall and weigths %d kg. Its name is %s, is %d years old, is color %s and has a %s pedegree" 
              %(self.group, self.height, self.weigth, self.name, self.age, self.color, self.breed))
        
class Dog(Animals):
    def __init__(self, group, height, weigth, age, name, breed, color):
        super().__init__(group, height, weigth, age)
        self.name = name
        self.breed = breed
        self.color = color
            
    def printDetails(self):
        print("This animal is a Dog. Belongs to the %s group, is %d cm tall and weigths %d kg. Its name is %s, is %d years old, is color %s and has a %s pedegree" 
              %(self.group, self.height, self.weigth, self.name, self.age, self.color, self.breed))       
            
    
cat1 = Cat("mamal", 25, 5, 10, "peluzo", "common", "white")
cat1.printDetails()

dog1 = Dog("mammal", 40, 12, 6, "Chuffy", "pug", "black")
dog1.printDetails()