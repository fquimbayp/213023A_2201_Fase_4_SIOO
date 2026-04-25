"""
Consulting service.

POLYMORPHISM:
Defines consulting-specific pricing rules while respecting
the abstract service interface.
"""

import logging
from .service import Service

class ConsultingService(Service):
    def calculate_cost(self, hours):
        cost = self.base_cost * hours * 1.19
        logging.info(f"Consulting cost: {cost}")
        print(f"[INFO] Consulting cost: {cost}")
        return cost
