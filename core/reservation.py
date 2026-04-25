"""
Reservation entity.

COMPOSITION:
A reservation is composed of Client and Service objects.

POLYMORPHISM:
Cost calculation is delegated to the service object dynamically.

ENCAPSULATION:
Reservation state, duration, and total cost are fully managed
within this class.

ADVANCED EXCEPTION HANDLING:
Invalid reservation states are prevented through explicit
domain exceptions.
"""

import logging
from .exceptions import ReservationError

class Reservation:
    """Reservation entity using composition and polymorphism."""
    def __init__(self, rid, client, service, hours):
        self.id = rid
        self.client = client
        self.service = service
        self.hours = hours
        self.total = 0
        self.status = 'Pending'
        logging.info(f"Reservation created: {self}")
        print(f"[INFO] Reservation created: {self}")

    def confirm(self):
        if self.hours <= 0:
            raise ReservationError("Invalid hours")
        self.total = self.service.calculate_cost(self.hours)
        self.status = 'Confirmed'
        logging.info(f"Reservation confirmed: {self}")
        print(f"[INFO] Reservation confirmed: {self}")
        return self.total

    def cancel(self):
        self.status = 'Cancelled'
        logging.info(f"Reservation cancelled: {self}")

    def __str__(self):
        return f"{self.id} - {self.client.name} - {self.service.name} - ${self.total}"
