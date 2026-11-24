# Calculator

A simple command-line calculator with addition, subtraction, multiplication, and division.

## Installation

No installation required. Ensure you have Python 3.8+ available.

## Usage

```bash
python calculator.py add 5 3
# Result: 8.0

python calculator.py subtract 10 4
# Result: 6.0

python calculator.py multiply 6 7
# Result: 42.0

python calculator.py divide 15 3
# Result: 5.0
```

## API

- `add(a, b)` - returns the sum of a and b
- `subtract(a, b)` - returns the result of subtracting b from a
- `multiply(a, b)` - returns the product of a and b
- `divide(a, b)` - returns the result of dividing a by b (raises ValueError if b is 0)