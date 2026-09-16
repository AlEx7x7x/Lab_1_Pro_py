"""Basic tests for the services module."""

from online_store.services import (
    add_product,
    calculate_stock_value,
    find_most_expensive,
)


def test_calculate_stock_value() -> None:
    products = []
    add_product(products, "Item A", "Cat", 10.0, 2)
    add_product(products, "Item B", "Cat", 5.0, 4)
    assert calculate_stock_value(products) == 40.0


def test_find_most_expensive() -> None:
    products = []
    add_product(products, "Item A", "Cat", 10.0, 2)
    add_product(products, "Item B", "Cat", 25.0, 1)
    best = find_most_expensive(products)
    assert best is not None
    assert best.name == "Item B"
