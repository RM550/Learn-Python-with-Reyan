# 📌 Comprehensive Guide to Python Type Annotations 🐍

## 🚀 Introduction
Python is a dynamically typed language, meaning variables do not require explicit type declarations. However, with the introduction of **PEP 484** in Python 3.5, Type Annotations were introduced to help improve code readability, maintainability, and debugging.

Type annotations **do not** enforce types at runtime but assist developers and tools in catching potential issues before execution. They work with **static type checkers** like `mypy` and improve IDE support for better autocompletion and hints.

## 🔍 Why Use Type Annotations?
Type annotations offer numerous benefits, including:
- ✅ **Improved Readability**: Clarifies expected input and output types.
- ✅ **Better IDE Support**: Provides enhanced autocompletion and linting.
- ✅ **Static Analysis**: Tools like `mypy` detect type errors before runtime.
- ✅ **Easier Maintenance**: Helps teams understand function signatures more easily.
- ✅ **Reduction in Bugs**: Early detection of type mismatches.

## 📌 Basic Syntax of Type Annotations
The fundamental syntax of type annotations involves specifying variable and function types:

### 🔹 Variable Annotations
```python
name: str = "Reyan"
age: int = 16
is_hacker: bool = True
```

### 🔹 Function Annotations
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

In this function, `name` is expected to be a `str`, and the function will return a `str`.

## 🔥 Advanced Type Annotations

### 📌 Annotating Collections
Python's `typing` module provides generic types for lists, tuples, sets, and dictionaries:

```python
from typing import List, Tuple, Dict, Set

# List of integers
grades: List[int] = [90, 85, 88]

# Tuple with multiple types
data: Tuple[str, int, bool] = ("Python", 3, True)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 95, "Bob": 87}

# Set of unique strings
users: Set[str] = {"Alice", "Bob", "Charlie"}
```

### 📌 Using `Any` for Dynamic Typing
If a function can accept **any type**, use `Any`:

```python
from typing import Any

def process_data(data: Any) -> None:
    print(f"Processing: {data}")
```

### 📌 Type Aliases
For improved code clarity, define custom type aliases:

```python
from typing import TypeAlias

UserID: TypeAlias = int

def get_user(id: UserID) -> str:
    return f"User ID: {id}"
```

### 📌 Callable (Function Signatures)
Use `Callable` to annotate functions passed as arguments:

```python
from typing import Callable

def execute_operation(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
```

### 📌 Typed Dictionaries
Define dictionaries with specific key-value types:

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

user: User = {"name": "Reyan", "age": 16}
```

### 📌 Generics (Reusable Type Variables)
For functions or classes that work with multiple types:

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

int_box = Box[int](10)
str_box = Box[str]("Hello")
```

## 🚦 Type Checking with `mypy`
Python does **not** enforce type checking at runtime, but `mypy` can analyze type correctness.

### 🔹 Install `mypy`
```sh
pip install mypy
```

### 🔹 Run Type Checking
```sh
mypy script.py
```

## 🎯 Best Practices for Type Annotations
✅ Use type hints **consistently** in all functions and variables.

✅ Prefer `Optional[T]` over `Union[T, None]` for readability.

✅ Use `Any` **sparingly** to avoid negating type safety.

✅ Always test your code with `mypy` to catch potential issues.

✅ Use `TypeAlias` for improved readability in large codebases.

✅ Avoid over-annotating obvious types (e.g., `x: int = 5` is redundant).

## 📌 Summary
🚀 Type annotations in Python improve **readability, maintainability, and debugging**.
🔍 Use **typing module** for advanced type hints.
🛠️ Leverage `mypy` for **static type checking**.

By adopting type annotations, you can make your Python code more robust, maintainable, and less error-prone! 🎉🐍

Happy Coding! 🚀

