"""Data models for the online store application."""

from dataclasses import dataclass


@dataclass
class Product:
    """Represents a single product available in the online store."""

    name: str
    category: str
    price: float
    quantity: int

    @property
    def total_value(self) -> float:
        """Total value of this product's stock (price multiplied by quantity)."""
        return self.price * self.quantity
