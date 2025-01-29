# 📂 Python File Handling - Detailed Guide 🚀

## 🔥 Introduction
File handling is a very important feature of Python that allows us to create, read, update, and delete files. Using Python's `open()` function, we can easily perform these operations. 📝✨

## 📌 Opening a File
To open any file in Python, we use the `open()` function.

```python
file = open("example.txt", "r")  # 'r' means read mode
```

Different modes we can use:
- `'r'` - Read mode (default)
- `'w'` - Write mode (overwrites the file)
- `'a'` - Append mode (adds new content without deleting)
- `'x'` - Exclusive creation mode
- `'b'` - Binary mode (for images, PDFs, etc.)
- `'t'` - Text mode (default)

## 📖 Reading a File
If we want to read the content of a file, we use the `read()` function.

```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()  # Closing the file is necessary! 🚨
```

Alternatively, we can use `readline()` and `readlines()`:

```python
file = open("example.txt", "r")
print(file.readline())  # Reads only one line
file.close()
```

```python
file = open("example.txt", "r")
lines = file.readlines()  # Reads all lines as a list
print(lines)
file.close()
```

## ✍️ Writing to a File
If we want to write to a file, we use `w` or `a` mode.

```python
file = open("example.txt", "w")
file.write("Hello, Python World! 🌍🐍")
file.close()
```

Using append mode to add new content:

```python
file = open("example.txt", "a")
file.write("\nNew line added! 🎉")
file.close()
```

## 🔄 Using `with` Statement (Best Practice)
When we use the `with` statement, the file automatically closes. This is a best practice! 😎

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## 🔍 Checking if a File Exists
If we want to check whether a file exists, we can use the `os` module:

```python
import os
if os.path.exists("example.txt"):
    print("File exists! ✅")
else:
    print("File does not exist! ❌")
```

## ❌ Deleting a File
If we want to delete a file, we use `os.remove()`:

```python
import os
os.remove("example.txt")
print("File deleted successfully! 🗑️")
```

If we want to check first whether the file exists:

```python
import os
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted! 🗑️")
else:
    print("File not found! 🚫")
```

## 📂 Working with Directories
To manage folders or directories, we use the `os` module:

```python
import os
os.mkdir("NewFolder")  # Creates a new folder 🏗️
```

If we want to rename a directory:

```python
import os
os.rename("NewFolder", "RenamedFolder")
```

If we want to delete an empty directory:

```python
import os
os.rmdir("RenamedFolder")
```

## 🏆 Conclusion
File handling in Python is very powerful and easy! By following this guide, you can become a master of file handling. 💪🔥

If you liked this guide, please give a ⭐! 🚀😊

