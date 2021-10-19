class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.color = color
        self.company = company
        self.model=model
        self.speedLimit= speedLimit
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerating")

audi = Car("A3", "blue","audi",80)
print(audi.color)
print(audi.model, audi.company)