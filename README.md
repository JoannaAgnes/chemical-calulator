# chemical-calulator
A simple Python calculator for basic chemical calculations.
# Chemical Calculator

A simple command-line chemical calculator written in Python. The program performs basic stoichiometric calculations using mass, number of moles, and molar mass.

## Features

The calculator currently supports three operations:

1. **Calculate molar mass** – based on mass and number of moles.
2. **Calculate number of moles** – based on mass and molar mass.
3. **Calculate mass** – based on molar mass and number of moles.

Additional features:
- Atomic mass dictionary containing all 118 chemical elements.
- Input validation for numerical values.
- Basic error handling.
- Interactive command-line menu.

## Formulas

The calculator uses the following equations:

| Calculation | Formula |
|---|---|
| Molar mass | M = m / n |
| Number of moles | n = m / M |
| Mass | m = M × n |

Where:
- M – molar mass [g/mol]
- m – mass [g]
- n – amount of substance [mol]

## Technologies

- Python 3
- Built-in Python functions and data structures
- Dictionaries
- Conditional statements
- Functions
- Exception handling

## How to Run

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd chemical-calculator
   ```

3. Run the program:

   ```bash
   python basic-chem-cal.py
   ```

## Project Status

Version 1.0 – Basic functionality implemented.

## Future Improvements

- Support for chemical formulas containing multiple elements and subscripts.
- Automatic molar mass calculation from chemical formulas.
- Expanded input validation.
- Improved user interface.

---

Created as a Python learning project.
