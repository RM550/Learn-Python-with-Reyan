# 🛠️ Union Type in Python

## 📌 Introduction
Python's `Union` type, introduced in **PEP 604 (Python 3.10)**, is used for specifying multiple possible types for a variable, function argument, or return type. This is particularly useful in scenarios where a function or variable can handle different types dynamically. 

Before Python 3.10, `Union` was available via the `typing` module, but newer versions allow a more concise syntax using the `|` operator.

---

## 📝 Syntax

### 1️⃣ Using `Union` from `typing` (Python 3.9 and earlier)
```python
from typing import Union

def process_value(value: Union[int, str]) -> None:
    print(value)
```

### 2️⃣ Using `|` Operator (Python 3.10 and later)
```python
def process_value(value: int | str) -> None:
    print(value)
```
✅ The `|` operator simplifies the syntax, making the code more readable and concise.

---

## 🎯 Use Cases

### 1️⃣ Function Parameters
A function that accepts multiple types can be defined using `Union`:
```python
from typing import Union

def add_numbers(a: int, b: Union[int, float]) -> Union[int, float]:
    return a + b
```
✅ This allows `b` to be either an `int` or a `float`, and the return type is also `Union[int, float]`.

### 2️⃣ Return Types
A function that can return different types based on a condition:
```python
def get_status(code: int) -> str | int:
    if code == 200:
        return "Success"
    return code
```
✅ Here, the function can return either a `str` ("Success") or an `int` (error code).

### 3️⃣ Type Hints for Variables
Using `Union` to define a variable that can hold multiple types:
```python
value: int | float = 10
value = 10.5  # Allowed since it's either int or float
```

---

## 🔬 Practical Examples

### 🏷️ Example 1: Handling Different Input Types
```python
def display_data(data: int | float | str) -> None:
    if isinstance(data, (int, float)):
        print(f"🔢 Number: {data}")
    elif isinstance(data, str):
        print(f"📝 Text: {data}")

display_data(42)  # Output: 🔢 Number: 42
display_data(3.14)  # Output: 🔢 Number: 3.14
display_data("Hello")  # Output: 📝 Text: Hello
```

### 🏷️ Example 2: Using Union with Lists
```python
from typing import Union

def process_items(items: list[Union[int, str]]) -> None:
    for item in items:
        print(f"🔄 Processing {item}")

process_items([1, "hello", 3, "world"])  # Mixed list of int and str
```

### 🏷️ Example 3: Payment Method Selection
```python
from typing import Union

def process_payment(amount: float, method: Union[str, int]) -> None:
    if isinstance(method, str):
        print(f"Processing {amount} payment via {method}.")
    elif isinstance(method, int):
        print(f"Processing {amount} payment using card number {method}.")

process_payment(100.0, "PayPal")  # Output: Processing 100.0 payment via PayPal.
process_payment(250.0, 1234567890123456)  # Output: Processing 250.0 payment using card number 1234567890123456.
```
✅ This function supports both string-based (e.g., "PayPal", "Stripe") and integer-based (e.g., card number) payment methods.

---

## ✅ Advantages of Using `Union`
✔️ **Improved Code Readability** – Makes function signatures clear.
✔️ **Better Type Checking** – Helps static type checkers like `mypy` catch errors.
✔️ **Backward Compatibility** – `Union` from `typing` is still available for older versions.
✔️ **Flexibility** – Allows handling multiple data types efficiently.

---

## ⚠️ Limitations
❌ **Cannot Use with `isinstance()` Directly** – Needs tuple form: `isinstance(x, (int, str))` instead of `isinstance(x, int | str)`.
❌ **Might Reduce Strictness** – If overused, it can make type checking less effective.

---

## 🏁 Conclusion
The `Union` type in Python allows defining variables, function arguments, and return types with multiple possible types. Python 3.10+ introduced the `|` operator, making it more concise and readable. While `Union` improves flexibility and static analysis, it should be used judiciously to maintain clarity and type safety. 🎯

🚀 Happy Coding! 🖥️

