# Experiment 10: Python Calculator Using `eval()`

## Subject: Open Source Technology (OST)

### Description
This experiment is the **10th experiment of the Open Source Technology (OST) practical coursework**. It demonstrates the implementation of a simple calculator in Python using the built-in `eval()` function.

The calculator accepts mathematical expressions from the user, evaluates them, and displays the result. It supports basic arithmetic operations, including addition, subtraction, multiplication, division, exponentiation, modulo, and the use of parentheses.

This program is developed for academic and educational purposes to understand Python expressions, exception handling, loops, user input, and the use of built-in functions.

## Objectives
- To understand the use of Python's built-in `eval()` function.
- To implement a calculator that evaluates mathematical expressions.
- To perform basic arithmetic operations using Python.
- To handle common errors, such as division by zero and invalid expressions.
- To understand loops and exception handling in Python.

## Technologies Used
- **Programming Language:** Python
- **Built-in Function:** `eval()`
- **Concepts:** Loops, conditional statements, user input, and exception handling.

## Source Code

```python
def calculator():
    print("===== Python Calculator =====")
    print("Operators: +, -, *, /, **, %")
    print("Type 'exit' to quit.")

    while True:
        expression = input("\nEnter expression: ")

        if expression.lower() == "exit":
            print("Calculator closed.")
            break

        try:
            result = eval(expression)
            print("Result:", result)

        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

        except (SyntaxError, NameError, TypeError):
            print("Error: Invalid mathematical expression.")

        except Exception as e:
            print("Error:", e)


calculator()
```

## Sample Output

```text
===== Python Calculator =====
Operators: +, -, *, /, **, %
Type 'exit' to quit.

Enter expression: 10 + 20 * 3
Result: 70

Enter expression: (50 - 10) / 2
Result: 20.0

Enter expression: 2 ** 5
Result: 32

Enter expression: 10 / 0
Error: Cannot divide by zero.

Enter expression: exit
Calculator closed.
```

## How to Run the Program

1. Install Python on your system.
2. Save the source code in a file named `calculator.py`.
3. Open a terminal or command prompt in the directory containing the file.
4. Execute the following command:

   ```bash
   python calculator.py
   ```

5. Enter a mathematical expression and press Enter to view the result.
6. Type `exit` to terminate the program.

## Conclusion

The experiment successfully demonstrates the implementation of a basic calculator in Python using the `eval()` function. It provides practical experience with expression evaluation, arithmetic operations, loops, user input, and exception handling.

**Note:** The `eval()` function can execute arbitrary Python code. This implementation is intended for academic demonstration and should not be used with untrusted input in production applications.
