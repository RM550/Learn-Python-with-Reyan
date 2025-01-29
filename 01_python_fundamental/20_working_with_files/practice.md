
# Working with Files in Python 📂🐍

In this README, we will explore different problems related to **working with files** in Python. The solutions provided will give you a hands-on approach to working with files and handling them efficiently in Python. Let's get started! 🚀

---

## 1. **Reading a Text File 📖**

### Problem:
Read the contents of a file named `example.txt` and print the content to the console.

### Solution:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Explanation:
- `open('example.txt', 'r')`: Opens the file `example.txt` in read mode (`'r'`).
- `file.read()`: Reads the entire content of the file and stores it in `content`.
- The `with` statement automatically closes the file once we are done with it.

---

## 2. **Writing to a File ✍️**

### Problem:
Write "Hello, World!" to a new file called `output.txt`.

### Solution:

```python
with open('output.txt', 'w') as file:
    file.write('Hello, World!')
```

### Explanation:
- `open('output.txt', 'w')`: Opens the file in write mode (`'w'`). If the file doesn't exist, it will be created.
- `file.write('Hello, World!')`: Writes the string to the file.

---

## 3. **Appending to a File 📝**

### Problem:
Append "Python is awesome!" to an existing file `notes.txt`.

### Solution:

```python
with open('notes.txt', 'a') as file:
    file.write('Python is awesome!\n')
```

### Explanation:
- `open('notes.txt', 'a')`: Opens the file in append mode (`'a'`).
- The string is appended to the end of the file.

---

## 4. **Reading a File Line by Line 📃**

### Problem:
Read a file and print each line one by one.

### Solution:

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

### Explanation:
- The `for line in file` loop reads each line of the file.
- `line.strip()` removes leading and trailing whitespaces.

---

## 5. **Checking if File Exists 📁**

### Problem:
Check if a file `data.txt` exists in the current directory.

### Solution:

```python
import os

if os.path.exists('data.txt'):
    print("File exists!")
else:
    print("File does not exist!")
```

### Explanation:
- `os.path.exists('data.txt')`: Checks if the file exists in the current directory.

---

## 6. **Counting the Number of Lines in a File 🔢**

### Problem:
Count how many lines are there in the file `file.txt`.

### Solution:

```python
with open('file.txt', 'r') as file:
    lines = file.readlines()
    print(f'Total lines: {len(lines)}')
```

### Explanation:
- `file.readlines()` reads all lines into a list.
- `len(lines)` counts the number of lines.

---

## 7. **Reading a Specific Line from a File 📍**

### Problem:
Read the 3rd line of a file `example.txt`.

### Solution:

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines[2].strip())  # Index starts at 0, so 3rd line is at index 2
```

### Explanation:
- `file.readlines()` returns a list of lines.
- `lines[2]` gives us the 3rd line (indexing starts from 0).

---

## 8. **Copying Contents of One File to Another 🪄**

### Problem:
Copy the contents of `source.txt` to `destination.txt`.

### Solution:

```python
with open('source.txt', 'r') as source_file:
    content = source_file.read()

with open('destination.txt', 'w') as dest_file:
    dest_file.write(content)
```

### Explanation:
- First, we open the source file and read its content.
- Then, we open the destination file and write the content to it.

---

## 9. **Handling File Not Found Error ⚠️**

### Problem:
Handle the situation where a file `nonexistent.txt` does not exist.

### Solution:

```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist! Please check the file path.")
```

### Explanation:
- The `try` block attempts to open the file.
- If the file doesn't exist, the `FileNotFoundError` is caught and an appropriate message is displayed.

---

## 10. **Reading a CSV File 📊**

### Problem:
Read a CSV file named `data.csv` and print each row.

### Solution:

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### Explanation:
- `csv.reader(file)` creates a CSV reader object.
- The loop iterates over each row in the CSV file and prints it.

---

## Conclusion 🎉

These are some basic but essential file handling problems in Python. Working with files efficiently is a crucial skill for any developer, and mastering these techniques will allow you to handle files like a pro! Keep experimenting and happy coding! 😄🎉
```

---
