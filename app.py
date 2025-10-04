from flask import Flask, render_template, request, url_for
from main import ExpressionConverter, MathFunctions
from array_module import SortingFunctions, ArraySearch, ArrayOperations, StatisticalOperations

app = Flask(__name__, static_folder='static')
app.config['VERSION'] = '1.0.0'

# Initialize classes once
converter = ExpressionConverter()
math_funcs = MathFunctions()
sort_func = SortingFunctions()
search_func = ArraySearch()
operations_func = ArrayOperations()
statistical_funcs = StatisticalOperations()


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
    result = None
    number_input = ""
    number2_input = ""
    operation_input = ""

    if request.method == "POST":
        operation_input = request.form.get("operation", "").strip()
        number_input = request.form.get("number", "").strip()
        number2_input = request.form.get("number2", "").strip()

        if operation_input in ["lcm", "hcf"]:
            # ✅ for two-number operations
            if number_input.isdigit() and number2_input.isdigit():
                num1 = int(number_input)
                num2 = int(number2_input)
                try:
                    if operation_input == "lcm":
                        result = math_funcs.lcm(num1, num2)
                    elif operation_input == "hcf":
                        result = math_funcs.hcf(num1, num2)
                except Exception as e:
                    result = f"An error occurred: {str(e)}"
            else:
                result = "Error: Please enter valid integers for both numbers."
        else:
            # ✅ for single-number operations
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
        number2_input=number2_input,
        operation_input=operation_input,
        active_page="math"
    )




@app.route("/array", methods=["GET", "POST"])
def array_toolkit():
    active_sub = request.args.get("sub", "sorting")  # default to sorting
    result = None
    steps = []
    numbers_input = ""
    search_element_input = ""
    search_algorithm_input = "linear"
    algorithm_input = ""
    operation_input = ""
    algo_name = ""
    operation_name = ""
    number2_input = ""
    error = None

    if request.method == "POST":
        numbers_input = request.form.get("numbers", "").strip()

        try:
            numbers = [int(x.strip()) for x in numbers_input.split(",") if x.strip()]
        except ValueError:
            return render_template(
                "array.html",
                active_sub=active_sub,
                result="Error: Please enter valid integers only.",
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

        if not numbers:
            result = "Error: Please enter at least one number."

        elif active_sub == "search":
            search_element_input = request.form.get("search_element", "").strip()
            search_algorithm_input = request.form.get("search_algorithm", "linear").strip()

            if not search_element_input.isdigit():
                result = "Error: Please enter a valid number to search."
            else:
                elem = int(search_element_input)
                if search_algorithm_input == "linear":
                    result, steps = search_func.linear_search_debug(numbers, elem)
                elif search_algorithm_input == "binary":
                    if numbers == sorted(numbers):
                        result, steps = search_func.binary_search_debug(numbers, elem)
                    else:
                        result = "Error: Binary search requires a sorted array."
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
            number2_input = request.form.get("number2", "").strip()  # ✅ capture k if provided
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
                if operation_input in ["rotate_left", "rotate_right"]:
                    try:
                        k = int(number2_input)
                        result = func(numbers, k)
                    except ValueError:
                        result = "Error: Please enter a valid integer for k."
                else:
                    result = func(numbers)
            else:
                result = "Error: Invalid operation selected."


        elif active_sub == "statistics":
            statistics_input = request.form.get("statistics", "").strip()
            op_map = {
                "mean": ("Mean", statistical_funcs.mean),
                "median": ("Median", statistical_funcs.median),
                "mode": ("Mode", statistical_funcs.mode),
                "variance": ("Variance", statistical_funcs.variance),
            }
            if statistics_input in op_map:
                operation_name, func = op_map[statistics_input]
                try:
                    result = func(numbers)
                except Exception as e:
                    result = f"An error occurred while computing {operation_name.lower()}: {str(e)}"

            elif statistics_input in ['stddev']:
                result = "HIHI: Will add these soon."
            else:
                result = "Error: Invalid statistics operation selected."

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
        number2_input=number2_input,
        active_page="array"
    )

if __name__ == "__main__":
    app.run(debug=True)