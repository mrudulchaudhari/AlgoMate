from flask import Flask, render_template, request
from main import (
    prefix_to_postfix_debug,
    prefix_to_infix_debug,
    postfix_to_infix_debug,
    postfix_to_prefix_debug,
    infix_to_postfix_debug,
    infix_to_prefix_debug,
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    steps = []
    if request.method == "POST":
        expression = request.form.get("expression", "").replace(" ", "")
        conversion = request.form.get("conversion", "")

        if conversion == "prefix_to_postfix":
            result, steps = prefix_to_postfix_debug(expression)
        elif conversion == "prefix_to_infix":
            result, steps = prefix_to_infix_debug(expression)
        elif conversion == "postfix_to_infix":
            result, steps = postfix_to_infix_debug(expression)
        elif conversion == "postfix_to_prefix":
            result, steps = postfix_to_prefix_debug(expression)
        elif conversion == "infix_to_postfix":
            result, steps = infix_to_postfix_debug(expression)
        elif conversion == "infix_to_prefix":
            result, steps = infix_to_prefix_debug(expression)
        # else:
        #     result = "Invalid conversion type"
        #     steps = []

        print("Converted:", result)  # 👈 debug
        print("Steps:")
        for s in steps:
            print(s)
    
    return render_template("index.html", result=result, steps=steps)


if __name__ == "__main__":
    app.run(debug=True)
    # print("Input:", expression)
    # print("Result:", result)
    # print("Steps:")
    # for step in steps:
    #     print(step)
