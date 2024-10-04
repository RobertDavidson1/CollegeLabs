from flask import Flask, render_template, request, jsonify
import sympy as sp

app = Flask(__name__)

# Define the symbols globally
x, y, z = sp.symbols('x y z')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    data = request.get_json()
    user_function = data.get('function')

    try:
        # Parse the function
        expr = sp.sympify(user_function, locals={'x': x, 'y': y, 'z': z})

        # First partial derivatives
        fx = sp.factor(sp.simplify(sp.diff(expr, x)))
        fy = sp.factor(sp.simplify(sp.diff(expr, y)))
        fz = sp.factor(sp.simplify(sp.diff(expr, z)))

        # Second pure partial derivatives
        fxx = sp.factor(sp.simplify(sp.diff(fx, x)))
        fyy = sp.factor(sp.simplify(sp.diff(fy, y)))
        fzz = sp.factor(sp.simplify(sp.diff(fz, z)))

        # Second mixed partial derivatives
        fxy = sp.factor(sp.simplify(sp.diff(fx, y)))
        fxz = sp.factor(sp.simplify(sp.diff(fx, z)))
        fyz = sp.factor(sp.simplify(sp.diff(fy, z)))

        # Convert expressions to LaTeX
        results = [
            # First partials
            {'label': '\\frac{\\partial f}{\\partial x}', 'value': sp.latex(fx), 'type': 'first'},
            {'label': '\\frac{\\partial f}{\\partial y}', 'value': sp.latex(fy), 'type': 'first'},
            {'label': '\\frac{\\partial f}{\\partial z}', 'value': sp.latex(fz), 'type': 'first'},
            # Second pure partials
            {'label': '\\frac{\\partial^2 f}{\\partial x^2}', 'value': sp.latex(fxx), 'type': 'second_pure'},
            {'label': '\\frac{\\partial^2 f}{\\partial y^2}', 'value': sp.latex(fyy), 'type': 'second_pure'},
            {'label': '\\frac{\\partial^2 f}{\\partial z^2}', 'value': sp.latex(fzz), 'type': 'second_pure'},
            # Second mixed partials
            {'label': '\\frac{\\partial^2 f}{\\partial x \\partial y}', 'value': sp.latex(fxy), 'type': 'second_mixed'},
            {'label': '\\frac{\\partial^2 f}{\\partial x \\partial z}', 'value': sp.latex(fxz), 'type': 'second_mixed'},
            {'label': '\\frac{\\partial^2 f}{\\partial y \\partial z}', 'value': sp.latex(fyz), 'type': 'second_mixed'},
        ]

        return jsonify({'success': True, 'results': results})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
