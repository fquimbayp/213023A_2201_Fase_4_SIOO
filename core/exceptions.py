"""
Custom domain exceptions.

ADVANCED EXCEPTION HANDLING:
Using specific exception types allows the system to separate
validation errors from reservation logic errors and handle them
gracefully without crashing the application.
"""

class ValidationError(Exception): pass
class ReservationError(Exception): pass
