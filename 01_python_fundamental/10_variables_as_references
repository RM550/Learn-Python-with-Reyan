# 🐍 Python Variables: Basics & Naming 🎯

Variables in Python are like containers that store data! 💾  
They're super flexible, easy to use, and form the **foundation of programming** in Python. 🚀

---

## 🧠 What Are Variables?  
A variable is like a *label* 🏷️ that you attach to a value to store it for later use. Think of it as a name for a memory space. 🎩✨

### 🤓 Example:
```python
name = "Sheru"  # Storing a string
age = 16        # Storing a number
is_cool = True  # Storing a boolean
```

---

## 🏷️ Rules for Naming Variables (Follow These Like a Pro!)  

1. **Start with a letter or underscore `_`** 🆗  
   ✅ `name`, `_value`  
   ❌ `1name`, `@value`

2. **No special characters!** 🚫  
   ✅ `my_variable`  
   ❌ `my-variable!`

3. **Case-sensitive** 🧐  
   - `Name`, `name`, and `NAME` are all different.  

4. **Keep it meaningful** 🧹  
   ✅ `total_score`  
   ❌ `x123`

5. **Use snake_case for readability** 🐍  
   - Combine words using underscores, like `my_variable`.

---

## 🌈 Variable Types in Python  

Python variables can hold **different types of data**. Here are some examples:  

| Data Type   | Example          | Description                      |
|-------------|------------------|----------------------------------|
| 🅰️ String   | `name = "Sheru"` | Stores text values.              |
| 🔢 Integer  | `age = 16`       | Stores whole numbers.            |
| 🧮 Float    | `pi = 3.14`      | Stores decimal numbers.          |
| ✅ Boolean  | `is_cool = True` | Stores `True` or `False`.        |
| 📋 List     | `numbers = [1, 2, 3]` | Stores a collection of items. |

---

## 🔗 Variables as References: How Python Works  

In Python, **variables act as references** to objects in memory. 🧠 This means:  

- A variable doesn’t store the value itself; instead, it **points** to a memory location where the value (object) is stored.  
- Multiple variables can refer to the same object.

### 🤔 Example 1: Single Reference  
```python
x = [1, 2, 3]  # x points to the list object
```

Here, `x` refers to a list object stored in memory.

### 🤔 Example 2: Shared Reference  
```python
x = [1, 2, 3]  # x points to the list object
y = x          # y now points to the same list object
y.append(4)    # Modifies the shared list
print(x)       # Output: [1, 2, 3, 4]
```

### Key Takeaway:  
If the object is **mutable** (e.g., lists, dictionaries), changes made through one variable will be visible to all variables pointing to the same object.

---

## 🤓 Checking References with `id()`  
The `id()` function in Python returns the memory address of an object. You can use this to verify if two variables refer to the same object.

```python
a = [1, 2, 3]
b = a
print(id(a) == id(b))  # Output: True
```

---

## 🧨 Important Concepts: Mutable vs Immutable  

1. **Immutable Objects** (e.g., integers, strings, tuples)  
   - Cannot be modified after creation.  
   - Reassignment creates a new object.  

   Example:
   ```python
   a = "Hello"
   b = a  # Both refer to the same string object
   b += " World"  # Creates a new string object
   print(a)  # Output: "Hello"
   ```

2. **Mutable Objects** (e.g., lists, dictionaries, sets)  
   - Can be modified in place.  
   - All references to the object reflect the changes.

   Example:
   ```python
   list1 = [1, 2, 3]
   list2 = list1
   list2.append(4)
   print(list1)  # Output: [1, 2, 3, 4]
   ```

---

## 🛑 Common Pitfall: Overwriting References  

When you assign a new value to a variable, it breaks the reference and creates a new one.

```python
x = [1, 2, 3]
y = x  # y refers to the same list
x = [4, 5, 6]  # Now x refers to a new list
print(y)       # Output: [1, 2, 3]
print(x)       # Output: [4, 5, 6]
```

---

## 🧪 Fun With Variables! 🎉  

### Example 1: Multiple Assignments  
You can assign the same object to multiple variables in one line.  

```python
x = y = z = [1, 2, 3]
x.append(4)
print(y)  # Output: [1, 2, 3, 4]
```

### Example 2: Creating Copies to Avoid Shared References  
Use `copy()` or `deepcopy()` to create independent objects.  

```python
import copy
list1 = [1, 2, 3]
list2 = copy.copy(list1)
list2.append(4)
print(list1)  # Output: [1, 2, 3]
print(list2)  # Output: [1, 2, 3, 4]
```

---

## 💡 Pro Tip  
- Always keep in mind whether you're working with **mutable** or **immutable** objects.  
- Use `id()` to debug shared references when you're unsure. 🕵️‍♂️  

---

## 🌟 Ready to Explore More?  
Check out the [Python Official Documentation](https://docs.python.org/3/tutorial/introduction.html#numbers) for an in-depth guide! 📖✨
---
