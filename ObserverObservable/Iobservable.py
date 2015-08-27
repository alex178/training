from abc import abstractmethod

class Iobservable:
    @abstractmethod
    def anmelden(self,observer):
        pass

    @abstractmethod
    def abmelden(self,observer):
        pass

    @abstractmethod
    def notify(self):
        pass
