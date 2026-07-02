# calculator
A simple command-line calculator built using Python. It performs basic arithmetic operations (+, -, *, /), stores every calculation in a history file, allows users to view calculation history in reverse order (latest first), clear the history, and handles common errors such as invalid input and division by zero.
# 🧮 Simple Calculator using Python

## 📌 Overview

This is a simple command-line calculator built using Python. It allows users to perform basic arithmetic operations, save each calculation to a history file, view previous calculations, and clear the calculation history.

This project is ideal for Python beginners to practice functions, file handling, loops, conditional statements, and user input.

---

## ✨ Features

* ➕ Addition
* ➖ Subtraction
* ✖ Multiplication
* ➗ Division
* 📜 View calculation history
* 🗑 Clear calculation history
* 💾 Automatically saves every calculation
* ⚠ Handles invalid input
* 🚫 Prevents division by zero

---

## 🛠 Technologies Used

* Python 3
* File Handling (`open`, `readlines`, `write`)
* Functions
* Loops
* Conditional Statements

---

## 📂 Project Structure

```text
Simple-Calculator/
│── calculator.py
│── history.txt
└── README.md
```

---

## ▶ How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python calculator.py
```

---

## 💻 Example Usage

```text
--- SIMPLE CALCULATOR (type history, clear or exit) ---

Enter calculation (+ - * /) or command:
8 + 4

RESULT: 12
```

View history:

```text
history
```

Clear history:

```text
clear
```

Exit the program:

```text
exit
```

---

## 📁 History File

All calculations are automatically stored in a file named `history.txt`.

Example:

```text
8 + 4 = 12
10 * 5 = 50
20 / 4 = 5
```

The newest calculations are displayed first when the `history` command is used.

---

## 📚 Concepts Practiced

* Variables
* Functions
* User Input
* Loops
* Conditional Statements
* File Handling
* String Manipulation
* Error Handling
* Python Programming Basics

---

## 🚀 Future Improvements

* Scientific calculator functions
* Graphical User Interface (GUI) using Tkinter
* Support for multiple operations in one expression
* Calculation timestamps
* Memory functions (M+, M-, MR, MC)

---

## 👩‍💻 Author

Developed as a Python learning project to practice programming fundamentals and file handling.
