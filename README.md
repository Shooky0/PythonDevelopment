# Python Development

This repository contains a few small Python practice scripts and mini-projects created while learning Python basics.

## Included examples

- `PrimeFinder/primetogether.py`  
  An interactive prime number finder that lets the user:
  - check whether a number is prime/composite
  - print all numbers up to a limit and label each as prime/composite
  - generate the first N prime numbers

- `MeanMedianMode/MeanMedianMode.py`  
  A script that asks for a sequence of numbers and then calculates:
  - mean
  - median
  - mode

- `Due tracker/due_tracker.py`  
  A simple to-do tracker for tasks with due dates. It can:
  - display the current task list with days remaining
  - mark a task as done (moves it to the next due date if a repeat period is set)
  - update dates or task names
  - remove tasks
  - add new tasks

## Running the scripts

From the `PythonDevelopment` folder:

```bash
python3 PrimeFinder/primetogether.py
python3 "MeanMedianMode/MeanMedianMode.py"
python3 "Due tracker/due_tracker.py"
```

## Requirements

The due tracker uses `colorama`.

```bash
pip install colorama
```

The project also includes a `requirements.txt` file with the dependency list.

## Notes

This is a beginner-focused learning repository, so the code is intentionally simple and easy to follow rather than production-ready.
