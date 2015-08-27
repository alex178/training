from Iobservable import Iobservable
from Observer import Observer

class Subject(Iobservable):

    def __init__(self, status=0):
        self.status = status
        self.observerList = []

    def anmelden(self,observer):
        self.observerList.append(observer)

    def abmelden(self,observer):
        self.observerList.remove(observer)

    def notify(self):
        for observer in self.observerList:
            observer.update(self.status)

    def setStatus(self, newStatus):
        self.status = newStatus
        self.notify()


observer1 = Observer()
observer2 = Observer()
observer3 = Observer()
s = Subject()
s.anmelden(observer1)
s.anmelden(observer2)
s.anmelden(observer3)
s.setStatus(1)

print("observer1 hat status: ",observer1.status)
print("observer2 hat status: ",observer2.status)
print("observer3 hat status: ",observer3.status)

s.setStatus(2)

print("observer1 hat status: ",observer1.status)
print("observer2 hat status: ",observer2.status)
print("observer3 hat status: ",observer3.status)

s.abmelden(observer3)

s.setStatus(3)

print("observer1 hat status: ",observer1.status)
print("observer2 hat status: ",observer2.status)
print("observer3 hat status: ",observer3.status)
