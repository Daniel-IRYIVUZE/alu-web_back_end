# Python Backend Practice Projects

This repository contains two Python-based learning projects completed as part of the ALU Web Backend curriculum:

1. **Python Variable Annotations Project**
2. **Python Async Project**

These projects helped me strengthen my understanding of Python type hints and asynchronous programming with asyncio.

---

## 1. Python Variable Annotations Project

This was the first project I completed and it focuses on applying type annotations in Python to improve code readability, enforce type safety, and build confidence using modern Python practices.

### What I Did

* Annotated variables using built-in types like `int`, `float`, `str`, `bool`
* Created functions using type hints for arguments and return types
* Applied `List`, `Tuple`, `Dict`, `Union`, and `Callable` for more complex structures
* Implemented duck typing for handling generic sequences
* Built higher-order functions that return other functions
* Used `mypy` to validate types and correct inconsistencies

### Example Tasks

* Adding two floats with annotations
* Concatenating strings with type safety
* Using floor division on floats with annotated return types
* Creating multiplier functions with function return hints
* Safely retrieving values from a dictionary using `Union`
* Returning typed tuples from a function
* Accepting and returning sequence-like objects using duck typing

### Tools & Concepts

* Python 3.7+ type hinting
* Type checking with `mypy`
* `typing` module: `List`, `Tuple`, `Union`, `Callable`, `Any`, `Optional`
* Duck typing concepts in practice

---

## 2. Python Async Project

This project centers on asynchronous programming in Python using the `asyncio` module and coroutines to manage concurrent tasks efficiently.

### What I Learned

* Writing `async` functions and using `await`
* Running coroutines with `asyncio`
* Managing multiple concurrent tasks
* Measuring asynchronous execution time using `time`
* Integrating randomness with `random.uniform` in async workflows

### Files

| File                         | Description                                          |
| ---------------------------- | ---------------------------------------------------- |
| `0-basic_async_syntax.py`    | Waits a random time and returns it                   |
| `1-concurrent_coroutines.py` | Runs multiple coroutines and returns delays in order |
| `2-measure_runtime.py`       | Measures average runtime of `wait_n`                 |
| `3-tasks.py`                 | Creates an `asyncio.Task`                            |
| `4-tasks.py`                 | Runs multiple async tasks using task function        |

### Requirements Met

* Used Python 3.7 and `asyncio`
* Followed `pycodestyle` (v2.5.x)
* Added type hints and documentation
* All files are executable and well-structured

### Resources

* [Async IO in Python – Real Python](https://realpython.com/async-io-python/)
* [asyncio — Python docs](https://docs.python.org/3/library/asyncio.html)
* [random.uniform — Python docs](https://docs.python.org/3/library/random.html#random.uniform)

---

## Author

**Daniel Iryivuze**
Projects completed as part of the ALU Web Backend program
