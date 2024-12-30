# Identifiers in python 🚀

## 📌 What is an Identifier?
An **identifier** is the name used to identify variables, functions, classes, modules, or other objects in Python. 💡

### Example:
```python
x = 10  # 'x' is an identifier for the variable.
def greet():  # 'greet' is an identifier for the function.
    print("Hello, World!")
```

---

## 🌟 Rules for Naming Identifiers
Identifiers must follow certain rules to be valid in Python. Let's break it down:

1. **Starts with a Letter or Underscore (_):**
   - Must begin with an alphabet (`A-Z` or `a-z`) or an underscore (`_`).

   ```python
   name = "Reyan"  # Valid identifier
   _age = 16  # Valid identifier
   1st_name = "Sheru"  # ❌ Invalid: Cannot start with a number
   ```

2. **Can Include Letters, Numbers, and Underscores:**
   - After the first character, you can use letters, numbers, or underscores.

   ```python
   player1 = "Babar"  # Valid
   player_2 = "Rizwan"  # Valid
   ```

3. **Case-Sensitive:**
   - Python identifiers are case-sensitive.

   ```python
   name = "Sheru"
   Name = "Reyan"
   print(name)  # Outputs: Sheru
   print(Name)  # Outputs: Reyan
   ```

4. **No Reserved Keywords:**
   - Identifiers cannot be Python's reserved keywords.

   ```python
   class = 5  # ❌ Invalid: 'class' is a reserved keyword
   my_class = 5  # ✅ Valid
   ```

---

## 💻 Examples of Valid and Invalid Identifiers

### ✅ Valid Identifiers:
- `name`
- `_value`
- `student_id`
- `average1`

### ❌ Invalid Identifiers:
- `1name` (Starts with a number)
- `student-id` (Contains a hyphen)
- `for` (Reserved keyword)

---

## 🔥 Types of Identifiers

### 1. **Variable Identifiers** 🧮
Used to name variables.
```python
speed = 90
player_name = "Sheru"
```

### 2. **Function Identifiers** 🛠️
Used to name functions.
```python
def calculate_average(a, b):
    return (a + b) / 2
```

### 3. **Class Identifiers** 🏛️
Used to define class names.
```python
class Car:
    def __init__(self, brand):
        self.brand = brand
```

### 4. **Constant Identifiers** 🚩
Used for naming constants (not enforced by Python).
```python
PI = 3.14
GRAVITY = 9.8
```

---

## 🔍 Best Practices for Naming Identifiers

1. **Be Descriptive:** Use meaningful names.
   ```python
   area_of_circle = PI * radius ** 2  # Descriptive
   a = PI * r ** 2  # Not descriptive
   ```

2. **Use Snake Case for Variables and Functions:**
   ```python
   calculate_sum = a + b  # Recommended
   calculateSum = a + b  # Avoid (CamelCase is for classes)
   ```

3. **Use Pascal Case for Classes:**
   ```python
   class Student:
       pass
   ```

4. **Avoid Single Letters (Unless in Loops):**
   ```python
   total_cost = price * quantity  # Good
   t = p * q  # Avoid
   ```

5. **Don’t Use Leading Underscores Unless Necessary:**
   ```python
   _private_variable = 42  # For private variables
   ```

---

## 🧩 Common Mistakes with Identifiers

### ❌ Using Reserved Keywords:
```python
if = 5  # Invalid
```

### ❌ Starting with Numbers:
```python
2fast2furious = "Movie"  # Invalid
```

### ❌ Using Spaces:
```python
user name = "Sheru"  # Invalid
``` 

---

## 📝 Reserved Keywords in Python
Python has several reserved keywords. Here’s the complete list:

| and | as | assert | break |
| --- | --- | ------ | ----- |
| class | continue | def | del |
| elif | else | except | False |
| finally | for | from | global |
| if | import | in | is |
| lambda | None | nonlocal | not |
| or | pass | raise | return |
| True | try | while | with |
| yield | async | await | |

---

## 🛡️ Reserved Identifier Guidelines
Avoid using identifiers that begin with:

- Single underscore (`_`): Used for internal/private variables.
- Double underscore (`__`): Used for name mangling in classes.
- Double underscores at both ends (`__example__`): Used for special methods (dunder methods).

---

## 🤓 Fun Facts About Python Identifiers

- Python doesn’t limit the length of identifiers. Use as many characters as you like! 😄
- Case sensitivity allows for unique names (`value` vs `Value`).
- Underscore `_` is a valid identifier on its own.

---

## 🌈 Summary

| ✅ Rules | 🚫 Don’ts |
| -------- | --------- |
| Start with a letter or underscore | Use spaces |
| Case-sensitive | Start with numbers |
| Avoid reserved keywords | Use special characters |

---

## 🎉 Challenge Yourself!
Try creating valid Python identifiers and write a short script using variables, functions, and classes. Share your script! 📝

---

Keep learning and coding! 🌟
