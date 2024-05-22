class Base:
    def __init__(self):
        self.num = 10
        self.string = "HelloWorld!"
        self.t = None
    def helloWorld(self) :
        return self.string
    
    def NumSquare(self):
        return self.num * self.num
    
    def getT(self, any):
        self.t = any

    def twice(self):
        return self.t + self.t
