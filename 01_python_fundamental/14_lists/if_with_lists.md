# 📝 Using `if` Statements with Lists in Python 🐍✨

Welcome to this guide on using `if` statements with Python lists! 🚀 `if` statements are incredibly useful for controlling program flow based on certain conditions. When combined with lists, they unlock powerful possibilities! 💪 Let's explore this topic step by step, with examples and plenty of emojis! 🎉

---

## 🌟 Why Use `if` Statements with Lists? 🤔

By using `if` statements with lists, you can:

1. **Check for the presence of items** 🔍
2. **Filter or process elements** 🎛️
3. **Perform actions conditionally** 🛠️
4. **Implement custom logic** 🧠

These combinations make your programs smarter and more efficient. 🚀

---

## 🔧 Examples of Using `if` Statements with Lists 📖

Here are some mature examples demonstrating how to use `if` statements with lists. 🎉

### 1. Checking if an Element Exists in a List 🔍

```python
fruits = ["🍎", "🍌", "🍓", "🍇"]

if "🍓" in fruits:
    print("Yay! 🍓 is in the list!")
else:
    print("No 🍓 found!")

# Output: Yay! 🍓 is in the list!
```

---

### 2. Filtering Elements Based on a Condition 🔧

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)
# Output: Even numbers: [2, 4, 6]
```

---

### 3. Using `if` Inside List Comprehensions 🛠️

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]

print("Even numbers:", even_numbers)
# Output: Even numbers: [2, 4, 6]
```

---

### 4. Checking Multiple Conditions with `if-elif-else` 🌈

```python
ages = [10, 18, 25, 30, 15]

for age in ages:
    if age < 18:
        print(f"Age {age}: Minor 🚸")
    elif age < 25:
        print(f"Age {age}: Young Adult 🎓")
    else:
        print(f"Age {age}: Adult 🧑‍💼")

# Output:
# Age 10: Minor 🚸
# Age 18: Young Adult 🎓
# Age 25: Adult 🧑‍💼
# Age 30: Adult 🧑‍💼
# Age 15: Minor 🚸
```

---

### 5. Conditional Processing of Nested Lists 🔗

```python
matrix = [[1, 2], [3, 4], [5, 6]]
sums = []

for row in matrix:
    if sum(row) > 5:
        sums.append(sum(row))

print("Sums greater than 5:", sums)
# Output: Sums greater than 5: [7, 11]
```

---

### 6. Removing Items Based on a Condition 🗑️

```python
numbers = [10, 15, 20, 25, 30]
numbers = [num for num in numbers if num % 10 == 0]

print("Numbers divisible by 10:", numbers)
# Output: Numbers divisible by 10: [10, 20, 30]
```

---

## 🎯 Summary Table 📝

| Concept                        | Description                                |
|--------------------------------|--------------------------------------------|
| `if` with `in`                | Check if an item exists in a list         |
| Filtering with loops           | Extract items based on conditions         |
| List comprehensions with `if` | Shorter, cleaner filtering and mapping    |
| Nested conditions              | Handle multiple cases in a loop           |
| Removing items conditionally   | Keep only the items you need              |

---

## 🚀 Practice Time! 🏋️‍♂️

Try using `if` statements with lists in your projects to make them more dynamic and intelligent. 💡 Don't hesitate to experiment and unleash the full power of Python! 🐍✨

---
