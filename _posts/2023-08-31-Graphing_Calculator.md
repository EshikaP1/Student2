---
toc: true
comments: false
layout: post
title: Graphing Calculator for Pros
description: Lets get ready for some equations!
type: hacks
courses: { compsci: {week: 2} }
---

<html>
<head>
    <title>Graphing Calculator</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.1.0/math.js"></script>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>Graphing Calculator</h1>
    <div>
        <label for="expression">Enter the function (e.g., 'x^2 + sin(x)'):</label>
        <input type="text" id="expression" placeholder="x^2 + sin(x)">
        <button onclick="graphFunction()">Graph</button>
    </div>
    <div id="plot" style="width: 600px; height: 400px;"></div>
    <div>
        <label for="xValue">Enter a value of x:</label>
        <input type="text" id="xValue" placeholder="2">
        <button onclick="evaluateFunction()">Evaluate</button>
        <span id="result"></span>
    </div>

    <script>
        function graphFunction() {
            const expression = document.getElementById("expression").value;
            const xValues = math.range(-10, 10, 0.01).toArray();
            const yValues = xValues.map(x => math.evaluate(expression, { x: x }));

            const data = [{
                x: xValues,
                y: yValues,
                type: 'scatter',
                mode: 'lines',
                name: 'Function'
            }];

            const layout = {
                title: 'Function Graph',
                xaxis: {
                    title: 'x'
                },
                yaxis: {
                    title: 'f(x)'
                }
            };

            Plotly.newPlot('plot', data, layout);
        }

        function evaluateFunction() {
            const expression = document.getElementById("expression").value;
            const xValue = parseFloat(document.getElementById("xValue").value);
            const result = math.evaluate(expression, { x: xValue });
            document.getElementById("result").textContent = `Result: ${result}`;
        }
    </script>
</body>
</html>
