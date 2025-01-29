# 📂 Python File Handling - Complete Guide with Methods 🚀

## 🔥 Introduction
File handling is one of the most essential features in Python. It allows us to **create**, **read**, **update**, and **delete** files. Python provides a built-in `open()` function that makes file operations simple and efficient! 📝✨

In this guide, we will cover:
✅ Opening files 📂
✅ Reading files 📖
✅ Writing and appending files ✍️
✅ Deleting files 🗑️
✅ Various file methods 🛠️
✅ Handling file errors ⚠️

---

## 📝 Opening a File
To open a file, we use the `open()` function.

```python
file = open("example.txt", "r")  # Open file in read mode
```

### 📌 File Opening Modes:
| Mode | Description |
|------|-------------|
| `r`  | Read mode (default) - File must exist 📖 |
| `w`  | Write mode - Overwrites if exists, creates if not ✍️ |
| `a`  | Append mode - Adds content at the end without deleting existing data 📌 |
| `x`  | Create mode - Creates a new file, fails if file exists 🚧 |
| `b`  | Binary mode - Used for images, PDFs, etc. 🖼️ |
| `t`  | Text mode (default) - Reads/writes in text format 🔤 |

---

## 📖 Reading a File
We can read a file’s content using different methods.

```python
file = open("example.txt", "r")
content = file.read()  # Reads the whole file
print(content)
file.close()  # Always close the file! 🚨
```

### 🔍 Other Reading Methods:
```python
file.readline()  # Reads one line at a time
file.readlines()  # Reads all lines as a list
```

Example:
```python
file = open("example.txt", "r")
print(file.readline())  # Reads first line
file.close()
```

```python
file = open("example.txt", "r")
lines = file.readlines()
print(lines)  # Prints a list of lines
file.close()
```

---

## ✍️ Writing to a File
To write data to a file, use write (`w`) or append (`a`) mode.

```python
file = open("example.txt", "w")
file.write("Hello, Python World! 🌍🐍")  # Overwrites file content
file.close()
```

To append new content:
```python
file = open("example.txt", "a")
file.write("\nNew line added! 🎉")
file.close()
```

---

## 🔄 Using `with` Statement (Best Practice)
Using `with open()`, files close automatically after operations. 🚀

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # No need to close manually! 😎
```

---

## 🛠️ File Handling Methods
Python provides several methods to interact with files.

### ✅ `write()` – Writing to a File
```python
file = open("test.txt", "w")
file.write("Hello, Python!")
file.close()
```

### ✅ `read()` – Reading Entire File
```python
file = open("test.txt", "r")
content = file.read()
print(content)
file.close()
```

### ✅ `readline()` – Reading One Line
```python
file = open("test.txt", "r")
print(file.readline())
file.close()
```

### ✅ `readlines()` – Reading All Lines as a List
```python
file = open("test.txt", "r")
lines = file.readlines()
print(lines)
file.close()
```

### ✅ `seek()` – Moving Cursor to a Specific Position
```python
file = open("test.txt", "r")
file.seek(5)  # Moves cursor to the 5th byte
print(file.read())
file.close()
```

### ✅ `tell()` – Getting Current Cursor Position
```python
file = open("test.txt", "r")
print(file.tell())  # Prints cursor position
file.close()
```

### ✅ `truncate()` – Cutting File to a Specific Size
```python
file = open("test.txt", "w")
file.write("Hello, Python World!")
file.truncate(5)  # Keeps only first 5 characters
file.close()
```

---

## 📂 Working with Directories
Python’s `os` module allows us to manage folders and directories.

### ✅ Checking If a File Exists
```python
import os
if os.path.exists("example.txt"):
    print("File exists! ✅")
else:
    print("File does not exist! ❌")
```

### ✅ Creating a Directory
```python
import os
os.mkdir("NewFolder")  # Creates a new folder 🏗️
```

### ✅ Renaming a File
```python
import os
os.rename("old_name.txt", "new_name.txt")
```

### ✅ Deleting a File
```python
import os
os.remove("example.txt")  # Deletes a file 🗑️
```

### ✅ Removing a Directory
```python
import os
os.rmdir("NewFolder")
```

---

## ⚠️ Handling File Errors
Errors can occur when working with files. It is crucial to handle them properly to prevent crashes.

### ✅ Common File Errors and Their Fixes
| Error | Cause | Fix |
|-------|-------|-----|
| `FileNotFoundError` | Trying to open a file that does not exist | Check if the file exists using `os.path.exists()` before opening |
| `PermissionError` | Trying to open a file without the right permissions | Use proper access permissions or run with admin privileges |
| `IsADirectoryError` | Attempting to open a directory as a file | Ensure the file path is correct |
| `IOError` | Generic input/output error | Use `try-except` to handle errors gracefully |

### ✅ Using Try-Except to Handle Errors
```python
try:
    file = open("nonexistent.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist! ❌")
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## 🏆 Conclusion
File handling in Python is **powerful and easy!** By mastering these methods, you can efficiently manage files and directories. 💪🔥

✅ Read, write, append files ✍️📖
✅ Use best practices with `with open()` 🔄
✅ Check file existence and delete when necessary 🗑️
✅ Work with directories using `os` module 📂
✅ Handle file errors gracefully ⚠️

If you found this guide useful, give it a ⭐! 🚀😊

