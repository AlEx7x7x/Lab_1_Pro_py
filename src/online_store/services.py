"""Business logic for the online store application."""

from online_store.models import Product


class InvalidProductDataError(Exception):
    """Raised when product data violates business rules (custom exception)."""


def add_product(
    products: list[Product],
    name: str,
    category: str,
    price: float,
    quantity: int,
) -> Product:
    """Validate input data and add a new product to the list."""
    if not name.strip():
        raise InvalidProductDataError("Product name cannot be empty.")
    if price < 0:
        raise InvalidProductDataError("Price cannot be negative.")
    if quantity < 0:
        raise InvalidProductDataError("Quantity cannot be negative.")

    product = Product(
        name=name.strip(),
        category=category.strip(),
        price=price,
        quantity=quantity,
    )
    products.append(product)
    return product


def calculate_stock_value(products: list[Product]) -> float:
    """Calculate the total value of all remaining stock."""
    return sum(product.total_value for product in products)


def find_product(
    products: list[Product],
    name: str,
) -> Product | None:
    """Find a product by its name (case-insensitive)."""
    for product in products:
        if product.name.lower() == name.lower():
            return product
    return None


def filter_by_category(
    products: list[Product],
    category: str,
) -> list[Product]:
    """Return all products that belong to the given category."""
    return [
        product
        for product in products
        if product.category.lower() == category.lower()
    ]


def find_most_expensive(
    products: list[Product],
) -> Product | None:
    """Find the product with the highest price."""
    if not products:
        return None
    return max(products, key=lambda product: product.price)


def sort_by_price(
    products: list[Product],
    descending: bool = False,
) -> list[Product]:
    """Return a new list of products sorted by price."""
    return sorted(
        products,
        key=lambda product: product.price,
        reverse=descending,
    )


def find_low_stock_products(
    products: list[Product],
    threshold: int,
) -> list[Product]:
    """Return products whose quantity is below the given threshold."""
    return [product for product in products if product.quantity < threshold]
