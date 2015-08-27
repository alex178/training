from abc import abstractmethod

class Iobserver:
    @abstractmethod
    def update(self):
        pass
