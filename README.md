# Python Backend Practice Projects

This repository contains three Python-based learning projects completed as part of the ALU Web Backend curriculum:

1. Python Variable Annotations Project
2. Python Async Project
3. Python Async Comprehension Project

These projects helped me strengthen my understanding of Python type hints and asynchronous programming with asyncio and comprehensions.

---

## 1. Python Variable Annotations Project

This was the first project I completed and it focuses on applying type annotations in Python to improve code readability, enforce type safety, and build confidence using modern Python practices.

### What I Did

* Annotated variables using built-in types like int, float, str, bool
* Created functions using type hints for arguments and return types
* Applied List, Tuple, Dict, Union, and Callable for more complex structures
* Implemented duck typing for handling generic sequences
* Built higher-order functions that return other functions
* Used mypy to validate types and correct inconsistencies

### Example Tasks

* Adding two floats with annotations
* Concatenating strings with type safety
* Using floor division on floats with annotated return types
* Creating multiplier functions with function return hints
* Safely retrieving values from a dictionary using Union
* Returning typed tuples from a function
* Accepting and returning sequence-like objects using duck typing

### Tools & Concepts

* Python 3.7+ type hinting
* Type checking with mypy
* typing module: List, Tuple, Union, Callable, Any, Optional
* Duck typing concepts in practice

---

## 2. Python Async Project

This project centers on asynchronous programming in Python using the asyncio module and coroutines to manage concurrent tasks efficiently.

### What I Learned

* Writing async functions and using await
* Running coroutines with asyncio
* Managing multiple concurrent tasks
* Measuring asynchronous execution time using time
* Integrating randomness with random.uniform in async workflows

### Files

| File                        | Description                                          |
| --------------------------- | ---------------------------------------------------- |
| 0-basic\_async\_syntax.py   | Waits a random time and returns it                   |
| 1-concurrent\_coroutines.py | Runs multiple coroutines and returns delays in order |
| 2-measure\_runtime.py       | Measures average runtime of wait\_n                  |
| 3-tasks.py                  | Creates an asyncio.Task                              |
| 4-tasks.py                  | Runs multiple async tasks using task function        |

### Requirements Met

* Used Python 3.7 and asyncio
* Followed pycodestyle (v2.5.x)
* Added type hints and documentation
* All files are executable and well-structured

### Resources

* Async IO in Python – Real Python
* asyncio — Python docs
* random.uniform — Python docs

---

## 3. Python Async Comprehension Project

I have done this project as part of the ALU Web Backend curriculum to understand how asynchronous generators and comprehensions work in Python.

This project helped me learn how to:

* Write asynchronous generators using async def and yield
* Use async comprehensions to collect data from async iterables
* Execute coroutines concurrently using asyncio.gather
* Type-annotate asynchronous functions and generators

---

### Tasks Overview

#### 0. Async Generator

Created a coroutine called async\_generator that yields 10 random floats between 0 and 10, one per second.
📁 File: 0-async\_generator.py

---

#### 1. Async Comprehensions

Used an async comprehension to collect 10 random numbers from async\_generator and return them as a list.
📁 File: 1-async\_comprehension.py

---

#### 2. Runtime for Four Parallel Comprehensions

Ran async\_comprehension four times in parallel and measured total runtime using asyncio.gather. The total execution time is around 10 seconds since all comprehensions run concurrently.
📁 File: 2-measure\_runtime.py

---

## Requirements

* Python 3.7
* Follows pycodestyle (v2.5.x)
* All files are executable and include documentation and type hints

---

## Author

Daniel Iryivuze
Projects completed as part of the ALU Web Backend program