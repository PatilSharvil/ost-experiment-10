
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
