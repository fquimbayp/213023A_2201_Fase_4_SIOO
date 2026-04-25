"""
Room reservation service.

POLYMORPHISM:
Overrides calculate_cost() with room-specific cost logic.
"""

import logging
from .service import Service

class RoomService(Service):
    def calculate_cost(self, hours):
        cost = self.base_cost * hours
        logging.info(f"Room cost: {cost}")
        print(f"[INFO] Room cost: {cost}")
        return cost
