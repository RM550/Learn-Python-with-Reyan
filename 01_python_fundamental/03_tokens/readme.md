# Tokens in python 🚀🐍

Tokens are the **building blocks** of any Python program. Each piece of text in your code that the Python interpreter understands is a token. Think of them as the vocabulary of the Python language! 📖✨

---

## 📜 Types of Tokens in Python

Python has **five primary types** of tokens:

1. **Keywords** 🏷️
2. **Identifiers** 🔤
3. **Literals** 🔢
4. **Operators** ➕
5. **Punctuators** 📝

Let’s dive into each with detailed explanations and examples! 🎯

---

### 1. **Keywords** 🏷️

- These are reserved words in Python. You **cannot use them** as variable names, function names, or any other identifiers.
- Keywords convey specific meanings and perform certain actions.

#### Examples of Keywords:

```python
# Using keywords in Python
def my_function():
    if True:
        print("Hello, Keywords!")
```

📌 **Note:** Keywords are case-sensitive, meaning `if` is valid but `If` is not.

---

### 2. **Identifiers** 🔤

- Identifiers are the **names** you give to variables, functions, classes, etc.
- Must follow these rules:
  - Can contain letters (A-Z, a-z), digits (0-9), and underscores (_).
  - Cannot start with a digit.
  - Cannot use keywords.

#### Examples of Identifiers:

```python
# Valid identifiers
my_variable = 10
_name = "Sheru"
number1 = 5

# Invalid identifiers
# 1variable = 10  # Starts with a digit
# for = 5         # Uses a keyword
```

✅ Valid: `_temp`, `value1`, `my_function`
❌ Invalid: `1variable`, `for`, `@name`

---

### 3. **Literals** 🔢

- Literals represent **constant values** in Python.

#### Types of Literals:

1. **String Literals** 📚:
   ```python
   # String literal example
   text = "Hello, Python!"
   print(text)
   ```

2. **Numeric Literals** 🔢:
   ```python
   # Numeric literal examples
   x = 10    # Integer
   y = 3.14  # Float
   z = 1 + 2j  # Complex
   print(x, y, z)
   ```

3. **Boolean Literals** ✅:
   ```python
   # Boolean literal example
   is_active = True
   print(is_active)
   ```

4. **Special Literal** `None` ✨:
   ```python
   # Special literal example
   value = None
   print(value)
   ```

---

### 4. **Operators** ➕

- Operators perform operations on variables and values. They are classified into different types:

#### Examples of Operators:

1. **Arithmetic Operators** ➕:
   ```python
   # Arithmetic operator examples
   addition = 10 + 5
   multiplication = 10 * 5
   print(addition, multiplication)
   ```

2. **Comparison Operators** ⚖️:
   ```python
   # Comparison operator example
   is_greater = 5 > 3
   print(is_greater)
   ```

3. **Logical Operators** 🤔:
   ```python
   # Logical operator example
   result = True and False
   print(result)
   ```

4. **Assignment Operators** 🖊️:
   ```python
   # Assignment operator example
   x = 10
   x += 5  # Equivalent to x = x + 5
   print(x)
   ```

---

### 5. **Punctuators** 📝

- These are symbols that structure Python code.

#### Examples of Punctuators:

```python
# Example of punctuators

def greet(name):
    print(f"Hello, {name}!")

greet("Sheru")

my_list = [1, 2, 3]  # [] for lists
my_dict = {"key": "value"}  # {} for dictionaries
```

---

## ✨ Fun Fact About Tokens:

Python uses **whitespace** and **indentation** instead of `{}` to define blocks. This makes the code cleaner and more readable! 👌

---

## 🎉 Complete Example Using All Tokens:

```python
# Keywords, Identifiers, Literals, Operators, Punctuators
def calculate_area(length, width):
    area = length * width  # Multiply dimensions
    if area > 0:
        return area
    else:
        return None

# Call the function
print(calculate_area(10, 5))
```

---

## 🏁 Summary

- Tokens are the smallest units of a Python program.
- Understanding tokens helps you write better, error-free code.

---

🌟 **Keep exploring Python,happy coding!** 🐍💻
