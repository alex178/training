# coding=utf-8

from interfaces import Strategy

class StrategyA(Strategy):

    def strategy(self):
        print "Strategy A wird ausgeführt"

class StrategyB(Strategy):

    def strategy(self):
        print "Strategy B wird ausgeführt"