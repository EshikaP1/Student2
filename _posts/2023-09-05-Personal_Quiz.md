---
toc: true
comments: false
layout: post
title: Personal Quiz
description: Time to see how much you know me!
type: hacks
courses: { compsci: {week: 1} }
---

<html>
<head>
    <title>Quiz</title>
</head>
<body>
    <h1>Quiz</h1>
    
    <div id="questions">
        <!-- Question 1 -->
        <div class="question">
            <p>What is my favorite color?</p>
            <div class="options">
                <input type="checkbox" id="q1-option1" data-correct="true"> <label for="q1-option1">blue</label><br>
                <input type="checkbox" id="q1-option2"> <label for="q1-option2">green</label><br>
                <input type="checkbox" id="q1-option3"> <label for="q1-option3">purple</label><br>
                <input type="checkbox" id="q1-option4"> <label for="q1-option4">pink</label><br>
            </div>
            <div class="result"></div>
        </div>

        <!-- Question 2 -->
        <div class="question">
            <p>What is my favorite food?</p>
            <div class="options">
                <input type="checkbox" id="q2-option1"> <label for="q2-option1">Oranges</label><br>
                <input type="checkbox" id="q2-option2"> <label for="q2-option2">Pasta</label><br>
                <input type="checkbox" id="q2-option3" data-correct="true"> <label for="q2-option3">Panneer</label><br>
                <input type="checkbox" id="q2-option4"> <label for="q2-option4">Cookies</label><br>
            </div>
            <div class="result"></div>
        </div>

        <!-- Question 3 -->
        <div class="question">
            <p>Where do I live</p>
            <div class="options">
                <input type="checkbox" id="q3-option1"> <label for="q3-option1">India</label><br>
                <input type="checkbox" id="q3-option2"> <label for="q3-option2">Moon</label><br>
                <input type="checkbox" id="q3-option3" data-correct="true"> <label for="q3-option3">Canada</label><br>
                <input type="checkbox" id="q3-option4"> <label for="q3-option4">USA</label><br>
            </div>
            <div class="result"></div>
        </div>
    </div>

    <script>
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', () => {
                checkAnswer(checkbox);
            });
        });

        function checkAnswer(checkbox) {
            const questionDiv = checkbox.closest('.question');
            const correctCheckbox = questionDiv.querySelector('input[data-correct="true"]');
            const resultElement = questionDiv.querySelector('.result');

            if (checkbox.isEqualNode(correctCheckbox)) {
                if (checkbox.checked) {
                    resultElement.textContent = "Correct";
                } else {
                    resultElement.textContent = "";
                }
            } else {
                if (checkbox.checked) {
                    resultElement.textContent = "Incorrect";
                } else {
                    resultElement.textContent = "";
                }
            }
        }
    </script>
</body>
</html>
