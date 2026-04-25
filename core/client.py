"""
Client entity.

INHERITANCE:
This class inherits from the abstract Entity class.

ENCAPSULATION:
Client data and validation rules are contained within the same
class, preventing invalid states.

ADVANCED EXCEPTION HANDLING:
Validation errors raise domain-specific exceptions instead of
generic runtime exceptions.
"""

import logging
from .entity import Entity
from .exceptions import ValidationError

class Client(Entity):
    """Client entity demonstrating encapsulation and inheritance."""
    def __init__(self, cid, name, email):
        self.id = cid
        self.name = name
        self.email = email
        self.validate()
        logging.info(f"Client created: {self}")
        print(f"[INFO] Client created: {self}")

    def validate(self):
        if not self.name:
            raise ValidationError("Name required")
        if '@' not in self.email:
            raise ValidationError("Invalid email")

    def __str__(self):
        return f"{self.id} - {self.name}"
