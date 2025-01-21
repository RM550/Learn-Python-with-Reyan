# Real-World Python Dictionary Problems 🌍🐍

This guide explores 5-6 real-world problems where Python dictionaries provide elegant solutions. Each example is packed with explanations, code, and, of course, plenty of emojis! 🎉

---

## 1. Counting Word Frequency in a Text 📖

### Problem:
You have a large text and want to count how many times each word appears.

### Solution:
```python
text = "python is great and python is easy to learn"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
```

### Output:
```
{'python': 2, 'is': 2, 'great': 1, 'and': 1, 'easy': 1, 'to': 1, 'learn': 1}
```

### Explanation:
- Split the text into words using `split()`.
- Use `get()` to check if the word exists in the dictionary. If not, initialize it with 0.
- Increment the count for each occurrence.

---

## 2. Storing and Retrieving Student Grades 📊

### Problem:
Maintain a database of students and their grades. Retrieve a specific student’s grade.

### Solution:
```python
grades = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [70, 75, 80]
}

# Retrieve grades
student = "Bob"
print(f"{student}'s grades: {grades.get(student, 'No record found')}")
```

### Output:
```
Bob's grades: [92, 88, 84]
```

### Explanation:
- Store grades as a list for each student.
- Use `get()` to safely retrieve grades, avoiding errors if the student isn’t found.

---

## 3. Inventory Management for a Store 🛒

### Problem:
Track the inventory of items in a store and update quantities after a sale.

### Solution:
```python
inventory = {
    "apple": 50,
    "banana": 100,
    "orange": 75
}

# Selling 20 apples
item = "apple"
sold_quantity = 20

if inventory.get(item, 0) >= sold_quantity:
    inventory[item] -= sold_quantity
    print(f"Sold {sold_quantity} {item}(s). Remaining: {inventory[item]}.")
else:
    print(f"Not enough {item}(s) in stock!")
```

### Output:
```
Sold 20 apple(s). Remaining: 30.
```

### Explanation:
- Use a dictionary to store item quantities.
- Check availability before deducting the sold quantity.

---

## 4. Analyzing Website Traffic 📈

### Problem:
Track the number of visitors per page on a website.

### Solution:
```python
web_traffic = {
    "/home": 1200,
    "/about": 300,
    "/contact": 150
}

# Adding new visitors to the home page
page = "/home"
new_visitors = 50

web_traffic[page] = web_traffic.get(page, 0) + new_visitors
print(web_traffic)
```

### Output:
```
{'/home': 1250, '/about': 300, '/contact': 150}
```

### Explanation:
- Use dictionary keys as page URLs and values as visitor counts.
- Update visitor counts dynamically using `get()`.

---

## 5. Grouping Students by Grades 🏫

### Problem:
Group students into categories based on their grades (A, B, C, etc.).

### Solution:
```python
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 70,
    "David": 88
}

# Categorize students
categories = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "F": []
}

for student, grade in students.items():
    if grade >= 90:
        categories["A"].append(student)
    elif grade >= 80:
        categories["B"].append(student)
    elif grade >= 70:
        categories["C"].append(student)
    elif grade >= 60:
        categories["D"].append(student)
    else:
        categories["F"].append(student)

print(categories)
```

### Output:
```
{'A': ['Bob'], 'B': ['Alice', 'David'], 'C': ['Charlie'], 'D': [], 'F': []}
```

### Explanation:
- Loop through students and their grades.
- Append student names to the appropriate category based on their grades.

---

## 6. Building a Simple Phonebook 📞

### Problem:
Create a phonebook that stores names and phone numbers. Allow searching for a number by name.

### Solution:
```python
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-666-7777"
}

# Search for a number
name = "Alice"
print(f"{name}'s number: {phonebook.get(name, 'Not found')}")
```

### Output:
```
Alice's number: 123-456-7890
```

### Explanation:
- Store names as keys and phone numbers as values.
- Use `get()` to search safely without raising errors.

---

## Conclusion 🎉

Python dictionaries are incredibly versatile and solve a wide range of real-world problems efficiently. Experiment with these examples, adapt them to your needs, and unlock the true power of dictionaries! 🚀

