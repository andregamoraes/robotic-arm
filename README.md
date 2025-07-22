# Robotic Arm Package Sorter

This repository contains a solution for the **Robotic Automation Factory** challenge, where the goal is to implement a function that sorts packages into the correct stack based on their dimensions and weight.

## Objective

Dispatch packages into the correct stack using the following rules:

### Classification rules:

- A package is **bulky** if:
  - Its **volume** (width × height × length) is **≥ 1,000,000 cm³**, **or**
  - Any dimension is **≥ 150 cm**

- A package is **heavy** if:
  - Its **mass** is **≥ 20 kg**

### Stack destinations:

- `STANDARD`: Not bulky and not heavy
- `SPECIAL`: Bulky **or** heavy
- `REJECTED`: Bulky **and** heavy

### Run the tests

```bash
python test_sort_packages.py
```

## Example usage

```
from sort_packages import sort

print(sort(100, 100, 50, 10))      # STANDARD
print(sort(200, 200, 200, 30))     # REJECTED
print(sort(150, 50, 50, 10))       # SPECIAL
```

## Files

| File                    | Description                                          |
|-------------------------|------------------------------------------------------|
| `sort_packages.py`      | Contains the implementation of the `sort` function  |
| `test_sort_packages.py` | Unit tests using Python's built-in `unittest`       |