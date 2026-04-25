"""
Abstract service definition.

ABSTRACTION:
Defines the concept of a service without specifying pricing logic.

POLYMORPHISM:
Concrete services override calculate_cost() to provide different
pricing strategies at runtime.
"""

from abc import ABC, abstractmethod

class Service(ABC):
    def __init__(self, sid, name, base_cost):
        self.id = sid
        self.name = name
        self.base_cost = base_cost

    @abstractmethod
    def calculate_cost(self, hours): pass

    def __str__(self): return f"{self.id} - {self.name}"
