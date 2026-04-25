"""
Abstract base entity.

ABSTRACTION:
This class defines a validation contract for all domain entities.
Concrete classes must decide how validation is implemented, while
the rest of the system relies only on this abstract definition.
"""

from abc import ABC, abstractmethod
class Entity(ABC):
    @abstractmethod
    def validate(self): pass
