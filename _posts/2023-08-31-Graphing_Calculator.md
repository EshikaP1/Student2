---
toc: true
comments: false
layout: post
title: Graphing Calculator for Pros
description: Lets get ready for some equations!
type: hacks
courses: { compsci: {week: 1} }
---

```

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("Graphing Calculator")

    while True:
        print("\nOptions:")
        print("1. Graph a function")
        print("2. Calculate the derivative")
        print("3. Calculate the integral")
        print("4. Evaluate a function")
        print("5. Quit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            graph_function()
        elif choice == '2':
            calculate_derivative()
        elif choice == '3':
            calculate_integral()
        elif choice == '4':
            evaluate_function()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def graph_function():
    expression = input("Enter the function (e.g., 'x**2 + sin(x)'): ")
    x_min = float(input("Enter the minimum x value: "))
    x_max = float(input("Enter the maximum x value: "))
    
    x = np.linspace(x_min, x_max, 400)
    y = [sp.sympify(expression).subs('x', xi).evalf() for xi in x]
    
    plt.plot(x, y)
    plt.title("Function Graph")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()

def calculate_derivative():
    expression = input("Enter the function for which you want to calculate the derivative: ")
    x = sp.symbols('x')
    derivative = sp.diff(expression, x)
    print("Derivative:", derivative)

def calculate_integral():
    expression = input("Enter the function for which you want to calculate the integral: ")
    x = sp.symbols('x')
    integral = sp.integrate(expression, x)
    print("Integral:", integral)

def evaluate_function():
    expression = input("Enter the function (e.g., 'x**2 + sin(x)'): ")
    value = float(input("Enter the value of x: "))
    result = sp.sympify(expression).subs('x', value).evalf()
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
