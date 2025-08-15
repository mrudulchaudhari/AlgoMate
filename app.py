from flask import Flask, render_template, request, url_for
from main import ExpressionConverter, MathFunctions
from array_module import SortingFunctions, ArraySearch, ArrayOperations

app = Flask(__name__, static_folder='static')
app.config['VERSION'] = '1.0.0'

# Initialize classes once
converter = ExpressionConverter()
math_funcs = MathFunctions()
sort_func = SortingFunctions()
search_func = ArraySearch()
operations_func = ArrayOperations()


@app.route("/")
def index():
    """Home page with navigation to tools"""
    return render_template("index.html", active_page="home")


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
                expression = "".join(expression_input.split())
                result, steps = selected_method(expression)
            except IndexError:
                result = "Error: Invalid expression. Please check your operands and operators."
            except Exception as e:
                result = f"An unexpected error occurred: {str(e)}"

    return render_template(
        "convert.html",
        result=result,
        steps=steps,
        expression_input=expression_input,
        conversion_input=conversion_input,
        active_page="convert"
    )


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

    return render_template(
        "math.html",
        result=result,
        number_input=number_input,
        operation_input=operation_input,
        active_page="math"
    )


@app.route("/array", methods=["GET", "POST"])
def array_toolkit():
    """Unified page for Array Search, Sorting, and Operations"""
    active_sub = request.args.get("sub", "sorting")  # default to sorting
    result = None
    steps = []
    numbers_input = ""
    search_element_input = ""
    search_algorithm_input = "linear"  # default
    algorithm_input = ""
    operation_input = ""
    algo_name = ""
    operation_name = ""

    if request.method == "POST":
        numbers_input = request.form.get("numbers", "").strip()
        numbers = [int(x.strip()) for x in numbers_input.split(",") if x.strip().isdigit()]

        if active_sub == "search":
            search_element_input = request.form.get("search_element", "").strip()
            search_algorithm_input = request.form.get("search_algorithm", "linear").strip()

            if not search_element_input.isdigit():
                result = "Error: Please enter a valid number to search."
            else:
                elem = int(search_element_input)
                if search_algorithm_input == "linear":
                    result, steps = search_func.linear_search_debug(numbers, elem)
                elif search_algorithm_input == "binary":
                    # Check if array is sorted
                    if numbers == sorted(numbers):
                        result, steps = search_func.binary_search_debug(numbers, elem)
                    else:
                        result = "Error: Binary search requires a sorted array. Please enter a sorted array."
                else:
                    result = "Error: Invalid search algorithm selected."

        elif active_sub == "sorting":
            algorithm_input = request.form.get("algorithm", "").strip()
            algo_map = {
                "bubble": ("Bubble Sort", sort_func.bubble_sort_debug),
                "insertion": ("Insertion Sort", sort_func.insertion_sort_debug),
                "selection": ("Selection Sort", sort_func.selection_sort_debug),
                "merge": ("Merge Sort", sort_func.merge_sort_debug),
                "counting": ("Counting Sort", sort_func.counting_sort_debug),
                "quick": ("Quick Sort", sort_func.quick_sort_debug),
            }
            if algorithm_input in algo_map:
                algo_name, func = algo_map[algorithm_input]
                result, steps = func(numbers)
            else:
                result = "Error: Invalid algorithm selected."

        elif active_sub == "operations":
            operation_input = request.form.get("operation", "").strip()
            op_map = {
                "sum": ("Sum", operations_func.sum_array),
                "product": ("Product", operations_func.product_array),
                "reverse": ("Reverse", operations_func.reverse_array),
                "rotate_left": ("Rotate Left", operations_func.rotate_left),
                "rotate_right": ("Rotate Right", operations_func.rotate_right),
                "remove_duplicates": ("Remove Duplicates", operations_func.remove_duplicates),
                "max_min": ("Max / Min", operations_func.max_min),
            }
            if operation_input in op_map:
                operation_name, func = op_map[operation_input]
                result = func(numbers)
            else:
                result = "Error: Invalid operation selected."

    return render_template(
        "array.html",
        active_sub=active_sub,
        result=result,
        steps=steps,
        numbers_input=numbers_input,
        search_element_input=search_element_input,
        search_algorithm_input=search_algorithm_input,
        algorithm_input=algorithm_input,
        operation_input=operation_input,
        algo_name=algo_name,
        operation_name=operation_name,
        active_page="array"
    )


if __name__ == "__main__":
    app.run(debug=True)