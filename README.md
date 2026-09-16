# Online Store

Навчальний проєкт з дисципліни «Професійний Python».
Лабораторна робота №1, Варіант 3 — «Інтернет-магазин».

## Description

Консольний застосунок для обліку товарів інтернет-магазину:
додавання товарів, пошук, фільтрація за категорією, обчислення
вартості залишків та визначення найдорожчого товару.

## Requirements

Python 3.11+

## Installation

```
python -m venv .venv
```

Activate the virtual environment:

```
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux / macOS
```

```
python -m pip install -e .
```

## Run

```
python -m online_store.main
```

or, with the interactive menu:

```
python -m online_store.main --menu
```

or via console command:

```
online-store
```

### Example run

```
Products:
Laptop Lenovo IdeaPad     Electronics    24999.00 UAH     5 pcs
Wireless Mouse            Electronics      349.00 UAH    40 pcs
Office Chair              Furniture       3200.00 UAH    12 pcs
Desk Lamp                 Furniture        599.00 UAH    25 pcs
Smartphone Xiaomi         Electronics    12999.00 UAH     4 pcs

Total stock value: 244326.00 UAH

Most expensive product: Laptop Lenovo IdeaPad (24999.00 UAH)
```

## Project structure

`src/online_store/models.py`
Data models (`Product` dataclass).

`src/online_store/services.py`
Business logic: adding products, search, filtering, sorting,
statistics, custom exception `InvalidProductDataError`.

`src/online_store/config.py`
Configuration constants (`CURRENCY`, `LOW_STOCK_THRESHOLD`).

`src/online_store/main.py`
Application entry point and menu-driven console interface.

## Author

Student: Name Surname
Group: XX-00
