# 🐍 Data Hiding in Modules in Python

## 🔒 What is Data Hiding?
Data hiding is a fundamental concept in object-oriented programming (OOP) that restricts direct access to certain data members of a class or module. In Python, **data hiding** is achieved using:

- **Underscores (`_` and `__`)** 🔹
- **Encapsulation** 📦
- **Modules and Packages** 📁

This ensures that internal details remain protected, allowing access only where necessary. 🚀

---

## 📁 Data Hiding in Modules
Python allows us to **hide data and functions** in modules to prevent accidental modification or unauthorized access. Here’s how:

### 1️⃣ Using Single Underscore `_`
🔹 A single underscore before a variable or function name indicates that it is intended to be **private** (but not strictly enforced).

```python
# my_module.py
_var = "I am hidden but accessible! 😏"

def _secret_function():
    return "Shh! This is a secret function! 🤫"
```

💡 **Note:** The underscore is just a convention; it does not prevent access.

```python
import my_module
print(my_module._var)  # Works, but not recommended! 🚫
```

---

### 2️⃣ Using Double Underscore `__`
🔒 A **double underscore** (`__`) makes the variable or function **strongly private** by name-mangling.

```python
# my_secure_module.py
__password = "SuperSecret123 🔑"

def __private_method():
    return "Access Denied! 🚫"
```

If we try to access it normally:
```python
import my_secure_module
print(my_secure_module.__password)  # ❌ AttributeError: module has no attribute '__password'
```

🔑 **Workaround:** Python **mangles** names, so you can still access it (not recommended 😅):
```python
print(my_secure_module._my_secure_module__password)  # ✅ Works, but avoid using it!
```

---

## 🎭 Encapsulation & Restricted Imports
Instead of exposing everything, you can **control what gets imported** using `__all__`.

```python
# my_encapsulated_module.py
__all__ = ["public_function"]  # Only this function will be accessible

def public_function():
    return "I am accessible! 😀"

def _hidden_function():
    return "You shouldn't see me! 😈"
```

Now, if we do:
```python
from my_encapsulated_module import *
print(public_function())  # ✅ Allowed
print(_hidden_function())  # ❌ NameError: name '_hidden_function' is not defined
```

---

## 🚀 Best Practices for Data Hiding in Python Modules
✅ Use `_` for **internal variables/functions**.  
✅ Use `__` for **strongly private** members.  
✅ Define `__all__` to **control module exports**.  
✅ Follow **PEP 8** naming conventions for clarity.  
✅ Don’t rely on name-mangling for security—use **real encryption** when needed. 🔐

---

## 🎯 Conclusion
Data hiding in Python is a **soft restriction** rather than an absolute rule. While you can still access hidden elements using name-mangling, it is best practice to respect encapsulation principles. 🚀

**Python trusts you! Don't break that trust!** 🤝💙

---

Happy Coding! 🐍💻

