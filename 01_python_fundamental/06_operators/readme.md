# 🚀 Python Operators Cheat Sheet

Operators are an integral part of any programming language! They allow us to manipulate values, make comparisons, and much more. Let's dive into **Operators in Python**! 😎

---

## 🛠️ Types of Operators

There are 7 basic categories of operators in Python:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators

---

## ➕ Arithmetic Operators

These are used for mathematical operations.

| Operator | Description       | Example         |
|----------|-------------------|-----------------|
| `+`      | Addition          | `3 + 2 = 5`     |
| `-`      | Subtraction       | `5 - 2 = 3`     |
| `*`      | Multiplication    | `3 * 2 = 6`     |
| `/`      | Division          | `6 / 2 = 3.0`   |
| `%`      | Modulus (Remainder) | `5 % 2 = 1`  |
| `**`     | Exponentiation    | `2 ** 3 = 8`    |
| `//`     | Floor Division    | `7 // 2 = 3`    |

```python
# Example
x = 10
y = 3
print(x + y)  # 13 😍
print(x % y)  # 1 🎉
```

---

## 🔗 Assignment Operators

These are used to assign and update values in variables.

| Operator | Example  | Equivalent |
|----------|----------|------------|
| `=`      | `x = 5`  | Assign     |
| `+=`     | `x += 3` | `x = x + 3`|
| `-=`     | `x -= 3` | `x = x - 3`|
| `*=`     | `x *= 3` | `x = x * 3`|
| `/=`     | `x /= 3` | `x = x / 3`|
| `%=`     | `x %= 3` | `x = x % 3`|

```python
x = 5
x += 3  # x becomes 8 🤩
print(x)
```

---

## 🤔 Comparison Operators

These compare values and return `True` or `False`.

| Operator | Description           | Example          |
|----------|-----------------------|------------------|
| `==`     | Equal to              | `5 == 5` -> True |
| `!=`     | Not equal to          | `5 != 2` -> True |
| `>`      | Greater than          | `5 > 3` -> True  |
| `<`      | Less than             | `5 < 3` -> False |
| `>=`     | Greater than or equal | `5 >= 5` -> True |
| `<=`     | Less than or equal    | `5 <= 4` -> False|

```python
# Example
x = 10
y = 20
print(x > y)  # False 🙃
print(x <= y)  # True 😎
```

---

## 🧠 Logical Operators

These are used to evaluate multiple conditions.

| Operator | Description            | Example                |
|----------|------------------------|------------------------|
| `and`    | Both conditions true   | `True and False -> False` |
| `or`     | At least one true      | `True or False -> True`|
| `not`    | Inverts condition      | `not True -> False`    |

```python
x = 5
y = 10
print(x > 2 and y < 20)  # True 😍
print(not(x > y))  # True 😎
```

---

## 🛠️ Bitwise Operators

These perform binary operations.

| Operator | Description | Example       |
|----------|-------------|---------------|
| `&`      | AND         | `5 & 3 = 1`   |
| `|`      | OR          | `5 | 3 = 7`   |
| `^`      | XOR         | `5 ^ 3 = 6`   |
| `~`      | NOT         | `~5 = -6`     |
| `<<`     | Left Shift  | `5 << 1 = 10` |
| `>>`     | Right Shift | `5 >> 1 = 2`  |

---

## 🔍 Membership Operators

These check if a value exists in a sequence.

| Operator | Description         | Example         |
|----------|---------------------|-----------------|
| `in`     | Value is present    | `'a' in 'apple'`|
| `not in` | Value not present   | `'x' not in 'apple'`|

```python
fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)  # True 🍎
print('grape' not in fruits)  # True 🍇
```

---

## 🆔 Identity Operators

These check if two variables share the same memory location.

| Operator | Description       | Example        |
|----------|-------------------|----------------|
| `is`     | Same identity     | `x is y`       |
| `is not` | Different identity| `x is not y`   |

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)  # True 🥳
print(x is z)  # False 😅
```

---

## 🔥 Quick Tips

- **Experiment!** 🧪 Try implementing each operator yourself.
- Use Python's REPL (Read-Eval-Print Loop) for quick testing. ⚡

Python operators are powerful and enable you to implement complex logic with ease! 💪✨
