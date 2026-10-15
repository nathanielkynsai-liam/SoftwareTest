"""
Core Application module for DevOps pipeline verification.
"""

def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculates discounted price with boundary validations."""
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount must be non-negative.")
    if discount_percent > 100:
        raise ValueError("Discount cannot exceed 100%.")
    return round(price * (1 - discount_percent / 100.0), 2)


def authenticate_user(username: str, role: str) -> bool:
    """Basic role-based access validation."""
    valid_roles = ["admin", "developer", "tester"]
    return bool(username and role in valid_roles)