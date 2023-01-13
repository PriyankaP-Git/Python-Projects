class Person:

    def __init__(self):
        self.name= "Sam"
        self.gender="Male"
        self.age=17
        

    def talk(self):
        print("Hi I'm", self.name)

    def vote(self):
        if self.age<18:
            print("I am not eligible to vote")
        else:
            print("I am eligible to vote")

obj= Person()
#Person.talk(obj)
#Person.vote(obj)
obj.talk()
obj.vote()
