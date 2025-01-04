# 📚 Python Data Types

Python is a versatile programming language that supports a variety of data types. In this README, we'll discuss **Python's data types** and their **properties**, along with how to check a data type. 🚀✨

---

## 🔢 Basic Data Types

### 1. **Numeric Types** 🔢
Python has three numeric types:

- **int**: Integers (e.g., `1`, `42`, `-7`) ➕
- **float**: Floating-point numbers (e.g., `3.14`, `-0.001`) 🌊
- **complex**: Complex numbers (e.g., `2+3j`, `-1j`) 🔮

```python
# Examples:
a = 10  # int
b = 3.14  # float
c = 2 + 3j  # complex

# Check type:
print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'complex'>
```

---

### 2. **Text Type** 📝

- **str**: Strings are used to represent text (e.g., `'Hello'`, `"World"`). ✍️

```python
# Example:
text = "Python is awesome!"  # str

# Check type:
print(type(text))  # Output: <class 'str'>
```

---

### 3. **Sequence Types** 📜

- **list**: Ordered and mutable (e.g., `[1, 2, 3]`) ✅
- **tuple**: Ordered but immutable (e.g., `(1, 2, 3)`) 🔒
- **range**: Represents a sequence of numbers (e.g., `range(5)`) 🎯

```python
# Examples:
my_list = [1, 2, 3]  # list
my_tuple = (1, 2, 3)  # tuple
my_range = range(5)  # range

# Check type:
print(type(my_list))  # Output: <class 'list'>
print(type(my_tuple))  # Output: <class 'tuple'>
print(type(my_range))  # Output: <class 'range'>
```

---

### 4. **Mapping Type** 🗺️

- **dict**: Stores key-value pairs (e.g., `{ 'name': 'Sheru', 'age': 16 }`). 🔑

```python
# Example:
my_dict = {"name": "Sheru", "age": 16}

# Check type:
print(type(my_dict))  # Output: <class 'dict'>
```

---

### 5. **Set Types** 🔄

- **set**: Unordered and unique elements (e.g., `{1, 2, 3}`) 🎲
- **frozenset**: Immutable version of set (e.g., `frozenset({1, 2, 3})`) 🧊

```python
# Examples:
my_set = {1, 2, 3}  # set
my_frozenset = frozenset({1, 2, 3})  # frozenset

# Check type:
print(type(my_set))  # Output: <class 'set'>
print(type(my_frozenset))  # Output: <class 'frozenset'>
```

---

### 6. **Boolean Type** ⚡

- **bool**: Represents True/False values. 🟢🔴

```python
# Example:
status = True  # bool

# Check type:
print(type(status))  # Output: <class 'bool'>
```

---

### 7. **Binary Types** 💾

- **bytes**: Immutable sequence of bytes (e.g., `b"hello"`) 📂
- **bytearray**: Mutable sequence of bytes (e.g., `bytearray(5)`) 🔧
- **memoryview**: Memory view of another binary object. 🧠

```python
# Examples:
data = b"hello"  # bytes
mutable_data = bytearray(5)  # bytearray
view = memoryview(data)  # memoryview

# Check type:
print(type(data))  # Output: <class 'bytes'>
print(type(mutable_data))  # Output: <class 'bytearray'>
print(type(view))  # Output: <class 'memoryview'>
```

---

## 🔍 Checking Data Types 🔎

In Python, you can check the type of a variable using the `type()` function:

```python
x = 42
print(type(x))  # Output: <class 'int'>
```

If you want to check for a specific type, use `isinstance()`:

```python
x = 42
print(isinstance(x, int))  # Output: True
```

---

## 🔥 Summary 📝

| **Type**      | **Example**          | **Description**                |
|---------------|----------------------|--------------------------------|
| **int**       | `42`                 | Integer numbers               |
| **float**     | `3.14`               | Decimal numbers               |
| **complex**   | `1+2j`               | Complex numbers               |
| **str**       | `'hello'`            | Text                          |
| **list**      | `[1, 2, 3]`          | Ordered, mutable collection   |
| **tuple**     | `(1, 2, 3)`          | Ordered, immutable collection |
| **dict**      | `{key: value}`       | Key-value pairs               |
| **set**       | `{1, 2, 3}`          | Unordered, unique elements    |
| **bool**      | `True` or `False`    | Boolean values                |
| **bytes**     | `b"hello"`          | Binary data                   |

---

### 💬 Suggestions or Questions? 🤔
If you have any questions or suggestions, feel free to share! 😊🚀

Happy coding😊🚀

---
