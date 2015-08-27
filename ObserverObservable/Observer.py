

from Iobserver import Iobserver

class Observer(Iobserver):

    def __init__(self):
        self.status = 0

    def update(self,status):
        self.status = status

