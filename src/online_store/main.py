"""Application entry point for the online store console application."""

import sys

from online_store.config import CURRENCY, LOW_STOCK_THRESHOLD
from online_store.models import Product
from online_store.services import (
    InvalidProductDataError,
    add_product,
    calculate_stock_value,
    filter_by_category,
    find_low_stock_products,
    find_most_expensive,
    find_product,
    sort_by_price,
)


def create_demo_products() -> list[Product]:
    """Create a demo list of products for demonstration purposes."""
    products: list[Product] = []
    add_product(products, "Laptop Lenovo IdeaPad", "Electronics", 24999.0, 5)
    add_product(products, "Wireless Mouse", "Electronics", 349.0, 40)
    add_product(products, "Office Chair", "Furniture", 3200.0, 12)
    add_product(products, "Desk Lamp", "Furniture", 599.0, 25)
    add_product(products, "Smartphone Xiaomi", "Electronics", 12999.0, 4)
    return products


def print_products(products: list[Product]) -> None:
    """Print a formatted table of products."""
    print("\nProducts:")
    for product in products:
        print(
            f"{product.name:26}"
            f"{product.category:13}"
            f"{product.price:10.2f} {CURRENCY}"
            f"{product.quantity:6} pcs"
        )


def print_menu() -> None:
    """Print the console menu."""
    print()
    print("1. Show all products")
    print("2. Add product")
    print("3. Find product by name")
    print("4. Filter by category")
    print("5. Show most expensive product")
    print("6. Show total stock value")
    print("7. Show products sorted by price")
    print("8. Show low stock products")
    print("9. Exit")


def run_menu(products: list[Product]) -> None:
    """Run an interactive menu-driven console interface."""
    while True:
        print_menu()
        command = input("Select command: ").strip()

        if command == "1":
            print_products(products)
        elif command == "2":
            name = input("Name: ").strip()
            category = input("Category: ").strip()
            try:
                price = float(input("Price: ").strip())
                quantity = int(input("Quantity: ").strip())
                add_product(products, name, category, price, quantity)
                print("Product added.")
            except (InvalidProductDataError, ValueError) as error:
                print(f"Error: {error}")
        elif command == "3":
            name = input("Product name: ").strip()
            product = find_product(products, name)
            if product is not None:
                print_products([product])
            else:
                print("Product not found.")
        elif command == "4":
            category = input("Category: ").strip()
            result = filter_by_category(products, category)
            print_products(result)
        elif command == "5":
            best = find_most_expensive(products)
            if best is not None:
                print(
                    f"\nMost expensive product: {best.name} "
                    f"({best.price:.2f} {CURRENCY})"
                )
        elif command == "6":
            value = calculate_stock_value(products)
            print(f"\nTotal stock value: {value:.2f} {CURRENCY}")
        elif command == "7":
            print_products(sort_by_price(products))
        elif command == "8":
            low_stock = find_low_stock_products(products, LOW_STOCK_THRESHOLD)
            print_products(low_stock)
        elif command == "9":
            print("Goodbye.")
            break
        else:
            print("Unknown command.")


def main() -> None:
    """Run the demo scenario and, optionally, the interactive menu."""
    products = create_demo_products()
    print_products(products)

    category = "Electronics"
    electronics = filter_by_category(products, category)
    print(f"\nProducts in category '{category}':")
    print_products(electronics)

    stock_value = calculate_stock_value(products)
    print(f"\nTotal stock value: {stock_value:.2f} {CURRENCY}")

    best = find_most_expensive(products)
    if best is not None:
        print(
            f"\nMost expensive product: {best.name} "
            f"({best.price:.2f} {CURRENCY})"
        )

    found = find_product(products, "Office Chair")
    if found is not None:
        print(f"\nProduct found: {found.name}, category {found.category}")

    print("\nProducts sorted by price:")
    print_products(sort_by_price(products))

    low_stock = find_low_stock_products(products, LOW_STOCK_THRESHOLD)
    print(f"\nLow stock products (quantity < {LOW_STOCK_THRESHOLD}):")
    print_products(low_stock)

    if "--menu" in sys.argv:
        run_menu(products)


if __name__ == "__main__":
    main()
