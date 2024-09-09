# phase-3-code-challenge-week-2-coffee-shop

## Overview
This project models a simple coffee shop domain using object-oriented programming principles. It includes three main entities: `Customer`, `Coffee`, and `Order`, with relationships modeled between them.

# Getting Started

# Prerequisites

- Python 3.x
- Pipenv

# Installation

1. Clone the repository:

```bash
git clone git@github.com:Thazar-r/phase-3-code-challenge-week-2-coffee-shop.git
cd phase-3-code-challenge-week-2-coffee-shop
```

2. Install dependencies:

```bash
pipenv install
```

# Running the Application

To run the application, use the following command:

```bash
pipenv run python main.py
```

# Running Tests

To run the tests, use the following command:

```bash
PYTHONPATH=. pipenv run pytest
```

# Project Structure

- `customer.py`: Manages customer information, including customer names and loyalty points.
- `coffee.py`: Manages coffee types and details, such as coffee names, prices, and sizes.
- `order.py`: Manages customer orders, including order creation, updates, and tracking.
- `tests/`: Contains unit tests for the application to ensure all functionalities work as expected.

# Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.