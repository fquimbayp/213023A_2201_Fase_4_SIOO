"""
Equipment rental service.

POLYMORPHISM:
Implements a rental-based pricing strategy by overriding
calculate_cost().
"""

import logging
from .service import Service

class EquipmentRentalService(Service):
    def calculate_cost(self, hours):
        cost = self.base_cost * hours * 1.1
        logging.info(f"Equipment cost: {cost}")
        print(f"[INFO] Equipment cost: {cost}")
        return cost
