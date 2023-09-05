from flask import Flask, render_template, request, jsonify
from sympy import symbols, diff, integrate, limit, simplify, latex, sympify

app = Flask(__name__)

# Define the variable
x = symbols('x')

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <title>Graphing Calculator</title>
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="mb-4">Graphing Calculator</h1>
            <form id="calculator-form">
                <div class="form-group">
                    <textarea id="expression" class="form-control" placeholder="Enter your expression"></textarea>
                </div>
                <div class="form-group">
                    <select id="operation" class="form-control">
                        <option value="evaluate">Evaluate</option>
                        <option value="derivative">Derivative</option>
                        <option value="integral">Integral</option>
                        <option value="limit">Limit</option>
                    </select>
                </div>
                <div class="form-group">
                    <input id="limit-point" class="form-control" type="number" placeholder="Limit Point (if applicable)">
                </div>
                <button type="submit" class="btn btn-primary">Calculate</button>
            </form>
            <div id="result" class="mt-4"></div>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.min.js"></script>
        <script>
            $(document).ready(function() {
                $('#calculator-form').submit(async function(e) {
                    e.preventDefault();

                    const expression = $('#expression').val();
                    const operation = $('#operation').val();
                    const limitPoint = $('#limit-point').val();

                    const response = await fetch('/calculate', {
                        method: 'POST',
                        body: new URLSearchParams({ expression, operation, limit_point: limitPoint }),
                        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    });

                    const data = await response.json();

                    if (data.error) {
                        $('#result').html(`<p class="text-danger">Error: ${data.error}</p>`);
                    } else {
                        $('#result').html(`<p class="text-success">Result: ${data.result}</p>`);
                    }
                });
            });
        </script>
    </body>
    </html>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    operation = request.form['operation']
    
    try:
        expr = sympify(expression)
        
        if operation == 'evaluate':
            result = simplify(expr)
        elif operation == 'derivative':
            result = diff(expr, x)
        elif operation == 'integral':
            result = integrate(expr, x)
        elif operation == 'limit':
            limit_point = float(request.form['limit_point'])
            result = limit(expr, x, limit_point)
        
        return jsonify({'result': latex(result)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)