# 📌 Python Type Annotations Guide 🐍

## 🚀 Introduction
Type annotations in Python help improve code readability, catch potential bugs early, and assist with static analysis tools. They were introduced in **PEP 484** and became widely used in Python 3.5+.

## 📖 Why Use Type Annotations?
✅ Improve code clarity 🧐
✅ Help IDEs with better autocompletion ✨
✅ Assist static type checkers like `mypy` 🔍
✅ Reduce runtime errors 🛑

## 🛠️ Basic Syntax
```python
# Define variable types
name: str = "Reyan"
age: int = 16
is_hacker: bool = True

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Sheru"))  # Output: Hello, Sheru!
```

## 🔥 Complex Data Types
### 📌 Lists, Tuples, and Dictionaries
```python
from typing import List, Tuple, Dict

# List of integers
grades: List[int] = [90, 85, 88]

# Tuple containing different types
data: Tuple[str, int, bool] = ("Python", 3, True)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 95, "Bob": 87}
```

### 📌 Optional Types
```python
from typing import Optional

def get_age(age: Optional[int] = None) -> str:
    if age is None:
        return "Age not provided"
    return f"Age: {age}"
```

## 🎭 Using `Any` for Dynamic Typing
```python
from typing import Any

def process_data(data: Any) -> None:
    print(f"Processing: {data}")
```

## 🎯 Custom Type Aliases
```python
from typing import TypeAlias

# Defining a custom type
UserID: TypeAlias = int

def get_user(id: UserID) -> str:
    return f"User ID: {id}"
```

## 🚦 Type Checking with `mypy`
Install `mypy` using:
```sh
pip install mypy
```
Run type checking:
```sh
mypy script.py
```

## 📌 Summary
✅ Use type hints for better code quality 🏆
✅ Leverage `mypy` for static analysis 🔎
✅ Keep your code maintainable and bug-free! 🛠️🐍

Happy Coding! 🎉🚀

