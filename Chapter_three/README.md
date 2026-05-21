# Chapter 3: Functions, Arguments & Modules

This folder contains the core building blocks for writing reusable, scalable Python code.

## Project Structure

* **`args_kwargs.py`** – Demonstrates how to handle unlimited inputs using `*args` (tuples) and `**kwargs` (dictionaries).
* **`maths.py`** – A custom utility module containing reusable calculation functions.
* **`main_app.py`** – The main entry point that ties the ecosystem together by importing functions from `maths.py`.

## Key Lessons Learned

* **Module Shadowing:** Named the utility `maths.py` instead of `math.py` to avoid crashing Python's built-in system library.
* **`__pycache__/`:** Learned that Python automatically compiles imported files into bytecode (`.pyc`) for faster execution. These background cache files are hidden using `.gitignore`.
