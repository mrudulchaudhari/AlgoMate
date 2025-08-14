from flask import Flask, render_template, request, url_for
from main import ExpressionConverter, MathFunctions

app = Flask(__name__, static_folder='static')

# Initialize classes once
converter = ExpressionConverter()
math_funcs = MathFunctions()


@app.route("/")
def index():
    """Home page with navigation to tools"""
    return render_template("index.html")


@app.route("/convert", methods=["GET", "POST"])
def convert():
    """Handles expression conversion logic"""
    result = None
    steps = None
    expression_input = ""
    conversion_input = ""

    if request.method == "POST":
        expression_input = request.form.get("expression", "").strip()
        conversion_input = request.form.get("conversion", "").strip()

        # Dictionary mapping conversion type to method
        conversion_methods = {
            "prefix_to_postfix": converter.prefix_to_postfix_debug,
            "prefix_to_infix": converter.prefix_to_infix_debug,
            "postfix_to_infix": converter.postfix_to_infix_debug,
            "postfix_to_prefix": converter.postfix_to_prefix_debug,
            "infix_to_postfix": converter.infix_to_postfix_debug,
            "infix_to_prefix": converter.infix_to_prefix_debug,
        }

        selected_method = conversion_methods.get(conversion_input)

        if not expression_input:
            result = "Error: Please enter an expression."
        elif not selected_method:
            result = "Error: Invalid conversion type selected."
        else:
            try:
                # Remove spaces from the expression before processing
                expression = "".join(expression_input.split())
                result, steps = selected_method(expression)
            except IndexError:
                result = "Error: Invalid expression. Please check your operands and operators."
            except Exception as e:
                result = f"An unexpected error occurred: {str(e)}"

    return render_template("convert.html", result=result, steps=steps, expression_input=expression_input, conversion_input=conversion_input)


@app.route("/math", methods=["GET", "POST"])
def math_page():
    """Handles math operations like factorial, prime check, etc."""
    result = None
    number_input = ""
    operation_input = ""

    if request.method == "POST":
        operation_input = request.form.get("operation", "").strip()
        number_input = request.form.get("number", "").strip()

        if number_input.isdigit():
            num = int(number_input)
            try:
                if operation_input == "factorial":
                    result = math_funcs.factorial(num)
                elif operation_input == "fibonacci":
                    result = math_funcs.fibonacci(num)
                elif operation_input == "is_prime":
                    result = math_funcs.is_prime(num)
                elif operation_input == "next_prime":
                    result = math_funcs.next_prime(num)
                else:
                    result = "Error: Invalid operation selected."
            except Exception as e:
                result = f"An error occurred: {str(e)}"
        else:
            result = "Error: Please enter a valid non-negative integer."

    return render_template("math.html", result=result, number_input=number_input, operation_input=operation_input)


if __name__ == "__main__":
    app.run(debug=True)