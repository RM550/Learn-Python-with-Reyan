# 🐍 TypedDict in Python

## 📌 Introduction
`TypedDict` is a feature in Python introduced in **PEP 589** (Python 3.8) that allows defining dictionary-like structures with fixed keys and specified value types. It provides **type hints** for dictionaries where each key has a known value type, helping to ensure correctness in large codebases.

Unlike normal dictionaries, `TypedDict` does not enforce types at runtime but serves as a static type checker tool, enhancing code reliability and maintainability.

---

## ✅ Why Use `TypedDict`?
- 🔍 **Static Type Checking**: Helps catch type errors before runtime.
- 📖 **Improved Readability**: Makes dictionary structures more explicit.
- 💡 **Better Code Completion**: Works well with IDEs and linters.
- 🏗 **Structured Data Representation**: Ensures dictionaries follow a specific schema.

---

## 🚀 Basic Usage
To define a `TypedDict`, import it from the `typing` module and create a class that inherits from `TypedDict`.

```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

person: Person = {"name": "John Doe", "age": 30}  # ✅ Correct
person = {"name": "John Doe", "age": "thirty"}  # ❌ Type error
```

Here, `Person` is a `TypedDict` where `name` must be a string and `age` must be an integer.

---

## 🔄 Required and Optional Keys
By default, all keys in a `TypedDict` are required. However, you can define optional keys using `NotRequired` (introduced in Python 3.9) or `total=False`.

### Using `NotRequired`
```python
from typing import TypedDict, NotRequired

class Employee(TypedDict):
    name: str
    salary: int
    department: NotRequired[str]  # 🔹 Optional key

emp: Employee = {"name": "Alice", "salary": 50000}  # ✅ Valid
emp = {"name": "Alice", "salary": 50000, "department": "HR"}  # ✅ Valid
```

### Using `total=False`
```python
class Student(TypedDict, total=False):
    name: str
    grade: int

stu: Student = {"name": "Bob"}  # ✅ Valid
stu = {"name": "Bob", "grade": 10}  # ✅ Valid
```
When `total=False`, all keys become optional by default.

---

## 🏗 Extending `TypedDict`
You can extend a `TypedDict` using inheritance.
```python
class BaseUser(TypedDict):
    username: str
    email: str

class AdminUser(BaseUser):
    is_admin: bool

admin: AdminUser = {"username": "admin", "email": "admin@example.com", "is_admin": True}  # ✅ Valid
```

This allows for better structuring of hierarchical data types.

---

## 🔒 Read-only `TypedDict`
From Python 3.11 onwards, you can create immutable `TypedDict` structures using `final`.
```python
from typing import final

@final
class Config(TypedDict):
    API_KEY: str
    DEBUG: bool
```
This prevents further subclassing of `Config`.

---

## 🏗 Nested `TypedDict`
`TypedDict` can contain other `TypedDict` types, allowing complex structures.
```python
class Address(TypedDict):
    street: str
    city: str

class User(TypedDict):
    name: str
    age: int
    address: Address

user: User = {
    "name": "Tom",
    "age": 28,
    "address": {"street": "123 Main St", "city": "New York"}
}  # ✅ Valid
```

---

## 🔍 Differences Between `TypedDict` and `dataclass`
| Feature | TypedDict | dataclass |
|---------|----------|-----------|
| 🛠 Enforced at Runtime? | No | Yes |
| 🔒 Immutable Support? | No (unless manually enforced) | Yes (with `frozen=True`) |
| 🏷 Type Checking | Static (via MyPy) | Static & Runtime |
| 📌 Use Case | Dictionary-like structures | Object-oriented models |

---

## ✅ Type Checking with `mypy`
Since `TypedDict` is a static typing feature, it's best used with a type checker like **mypy**.

### Installing `mypy`
```sh
pip install mypy
```

### Running `mypy`
```sh
mypy script.py
```
This will check for any type inconsistencies in your code.

---

## 🎯 Conclusion
`TypedDict` is a powerful tool for adding type safety to dictionary-like data structures in Python. It improves code clarity, maintainability, and reduces runtime errors when used correctly with static type checkers like `mypy`.

If you’re working on large projects or APIs with structured data, `TypedDict` is a great way to ensure correctness while maintaining the flexibility of dictionaries. 🚀

