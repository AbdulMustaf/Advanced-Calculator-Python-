##Advanced Scientific Calculator

##Overview

The Advanced Scientific Calculator is a Python-based command-line tool that offers various mathematical and scientific functions. It is designed for ease of use, with support for basic arithmetic, advanced mathematical operations, trigonometric functions, logarithms, memory operations, and more. The project also includes a comprehensive test suite to ensure reliability.

#Features

1. Basic Operations

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

Exponentiation (^)

2. Advanced Functions

Factorial computation

Prime number check

Exponential function

3. Trigonometric Functions

Sine (sin)

Cosine (cos)

Tangent (tan)

4. Logarithmic Functions

Base-10 logarithm (log10)

Natural logarithm (ln)

5. Memory Operations

Store a value in memory

Recall the stored value

Clear memory

6. History Management

Tracks previous operations and results

Allows undoing the last operation

7. Error Handling

Handles invalid inputs, such as division by zero, invalid logarithmic values, and negative factorials.

Project Structure

project/
|-- advance_calculator.py     # Main calculator implementation
|-- test_advance_calculator.py # Unit tests for the calculator
|-- README.md                 # Documentation for the project

Usage

Running the Calculator

Clone the repository or download the project files.

Navigate to the project directory in your terminal.

Run the following command to start the calculator:

python advance_calculator.py

Interactive Menu

The calculator provides an interactive menu with the following options:

Perform basic operations (e.g., 5 + 3)

Compute factorials

Check if a number is prime

Perform trigonometric calculations (e.g., sin, cos, tan)

Calculate logarithms (base-10 or natural logarithm)

Compute exponential values (e.g., e^x)

Store, recall, or clear memory

Undo the last operation

Show the history of operations

Exit

Example Input

Basic operation: 5 + 3

Trigonometric function: sin with angle in degrees

Logarithm: log10 of a number

Factorial: Enter a non-negative integer

Testing

Running Unit Tests

The project includes a comprehensive suite of unit tests. To run the tests:

Ensure you have Python installed (version 3.7 or later).

Run the following command from the project directory:

python -m unittest test_advance_calculator.py

Verify that all tests pass successfully.
