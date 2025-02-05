

## 🔥 **Introduction to Python Types**  

Python is a **dynamically typed** language, meaning you don’t need to explicitly define the type of a variable—it’s determined at runtime. However, Python has a rich set of built-in **data types** that help in managing different kinds of data efficiently.  

In this guide, we’ll cover **all Python types**, including:  
✔ **Primitive Types (int, float, bool, str, etc.)**  
✔ **Collection Types (list, tuple, set, dict, etc.)**  
✔ **Advanced Types (NoneType, complex, frozenset, etc.)**  
✔ **User-Defined Types (Classes & Objects)**  
✔ **Type Hinting in Python**  

---

# 🏗 **1️⃣ Primitive Data Types in Python**  

### 📌 **1. Integer (`int`)**  
The `int` type is used for whole numbers (positive, negative, or zero).  

```python
x = 10
y = -5
z = 0

print(type(x))  # Output: <class 'int'>
```

✅ **Supports operations** like `+`, `-`, `*`, `//`, `%`, `**`  

### 📌 **2. Floating-Point (`float`)**  
The `float` type is used for decimal or fractional numbers.  

```python
a = 10.5
b = -2.3
c = 3.14

print(type(a))  # Output: <class 'float'>
```

✅ **Supports operations** like `+`, `-`, `*`, `/`, `**`  

### 📌 **3. Boolean (`bool`)**  
Booleans represent `True` or `False`.  

```python
is_python_fun = True
is_sky_green = False

print(type(is_python_fun))  # Output: <class 'bool'>
```

✅ **Used in conditions, comparisons, and logical operations.**  

### 📌 **4. String (`str`)**  
Strings are sequences of characters enclosed in quotes (`""` or `''`).  

```python
name = "Reyan Mumtaz"
message = 'Python is awesome!'

print(type(name))  # Output: <class 'str'>
```

✅ **Supports operations** like concatenation (`+`), repetition (`*`), slicing (`[start:end]`).  

---

# 🔄 **2️⃣ Collection Data Types in Python**  

### 📌 **1. List (`list`)** 📝  
A `list` is an **ordered, mutable collection** that can store different types of elements.  

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]

print(type(fruits))  # Output: <class 'list'>
```

✅ **Supports operations** like indexing, slicing, `.append()`, `.remove()`, `.sort()`  

### 📌 **2. Tuple (`tuple`)** 📦  
A `tuple` is an **ordered, immutable collection**.  

```python
coordinates = (10.5, 20.8)
colors = ("red", "green", "blue")

print(type(coordinates))  # Output: <class 'tuple'>
```

✅ **Immutable** (cannot be modified after creation). Faster than lists!  

### 📌 **3. Set (`set`)** 🔥  
A `set` is an **unordered collection of unique elements**.  

```python
unique_numbers = {1, 2, 3, 3, 4, 4}

print(unique_numbers)  # Output: {1, 2, 3, 4}
print(type(unique_numbers))  # Output: <class 'set'>
```

✅ **Supports operations** like union (`|`), intersection (`&`), `.add()`, `.remove()`.  

### 📌 **4. Dictionary (`dict`)** 🗂  
A `dict` is an **unordered collection of key-value pairs**.  

```python
student = {"name": "Reyan", "age": 16, "language": "Python"}

print(student["name"])  # Output: Reyan
print(type(student))  # Output: <class 'dict'>
```

✅ **Keys must be unique**, values can be of any type.  

---

# 🧮 **3️⃣ Numeric Types in Python**  

### 📌 **1. Complex Numbers (`complex`)**  
Python supports complex numbers using `j` as the imaginary unit.  

```python
c = 2 + 3j

print(type(c))  # Output: <class 'complex'>
```

✅ **Supports operations** like addition, subtraction, magnitude (`abs()`).  

---

# ⚡ **4️⃣ Special Data Types in Python**  

### 📌 **1. `NoneType` (The `None` Value)**  
`None` represents the absence of a value.  

```python
x = None

print(type(x))  # Output: <class 'NoneType'>
```

✅ **Used for placeholders, optional parameters, and function return values.**  

### 📌 **2. `frozenset` (Immutable Set)**  
A `frozenset` is an **immutable version** of a set.  

```python
fs = frozenset([1, 2, 3, 4])

print(type(fs))  # Output: <class 'frozenset'>
```

✅ **Cannot be modified after creation.**  

---

# 🏗 **5️⃣ User-Defined Types (Classes & Objects)**  

Python allows users to define custom data types using **classes**.  

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Tesla", "Model S")

print(type(my_car))  # Output: <class '__main__.Car'>
```

✅ **Allows object-oriented programming (OOP) in Python!**  

---

# 🎨 **6️⃣ Type Hinting in Python (Type Annotations)**  

Python 3.5+ introduced **type hints** to specify expected data types.  

```python
def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(10, 5))  # Output: 15
```

✅ **Helps in better code readability and debugging.**  

---

# 🏆 **Conclusion**  

Python offers a **wide range of data types** for efficient programming. Knowing the right type for the right problem is **key to writing optimized code**!  

🔹 **Primitive types**: `int`, `float`, `bool`, `str`  
🔹 **Collection types**: `list`, `tuple`, `set`, `dict`  
🔹 **Advanced types**: `NoneType`, `complex`, `frozenset`  
🔹 **User-defined types**: Classes & objects  
🔹 **Type Hinting**: Enhances code clarity  

**🚀 Now go and explore Python types in your own projects!** 🐍🔥  
