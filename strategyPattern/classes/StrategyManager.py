# coding=utf-8

from interfaces import Strategy
from classes.ConcreteStrategy import StrategyA, StrategyB


class StrategyManager(object):

    def __init__(self, strategy):
        self.strategy = strategy

    def executeStrategy(self):
        self.strategy.strategy()


strategyA = StrategyA()
strategyB = StrategyB()
manager = StrategyManager(strategyB)
manager.executeStrategy()