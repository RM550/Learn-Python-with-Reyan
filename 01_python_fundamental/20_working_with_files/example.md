# 📜 Python Log Management System - Detailed Guide 🚀

## 🔥 Introduction
A log management system is essential for keeping track of events, errors, and other important activities in an application. Python provides powerful built-in tools for managing logs using the `logging` module. 📑✨

In this guide, we will create a **detailed log management system** that allows us to:
✅ Log messages with different severity levels
✅ Save logs to a file
✅ Format logs with timestamps
✅ Rotate logs to avoid oversized files
✅ Use a custom log handler

---

## 📝 Step 1: Setting Up Logging
Python's `logging` module makes it easy to log messages in a structured way. Let’s start by setting up a basic logger.

```python
import logging

# Configure the logging system
logging.basicConfig(
    level=logging.DEBUG,  # Set logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define log format
    handlers=[
        logging.FileHandler("app.log"),  # Save logs to a file
        logging.StreamHandler()  # Print logs to console
    ]
)

# Creating a logger instance
logger = logging.getLogger()
```

🚀 **Explanation:**
- `level=logging.DEBUG`: Logs messages from DEBUG level and above.
- `format`: Specifies the log structure with timestamp, level, and message.
- `handlers`: Defines where logs will be stored (file + console).
- `getLogger()`: Retrieves the logger instance.

---

## 🔍 Step 2: Logging Messages with Different Levels
The logging module supports multiple severity levels. Let’s use them in our logger.

```python
logger.debug("This is a debug message 🐞")
logger.info("This is an info message ℹ️")
logger.warning("This is a warning message ⚠️")
logger.error("This is an error message ❌")
logger.critical("This is a critical message 🚨")
```

📌 **Severity Levels:**
- `DEBUG` 🐞 – Detailed debugging information.
- `INFO` ℹ️ – General information about application progress.
- `WARNING` ⚠️ – Potential issues that need attention.
- `ERROR` ❌ – A serious issue that has occurred.
- `CRITICAL` 🚨 – A severe issue that needs immediate action.

---

## 🔄 Step 3: Rotating Logs to Avoid Large Files
Large log files can be difficult to manage. We can use `RotatingFileHandler` to automatically create new log files when they reach a certain size.

```python
from logging.handlers import RotatingFileHandler

# Configure rotating file handler
handler = RotatingFileHandler("app.log", maxBytes=1024, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)
```

📌 **How It Works:**
- `maxBytes=1024` – Each log file will be **1 KB max** before a new file is created.
- `backupCount=3` – Keeps the last **3 log files**.
- Older logs will be automatically deleted after reaching the backup limit.

---

## 🛠️ Step 4: Creating a Custom Log Function
Let’s wrap our logging functionality inside a reusable function.

```python
def log_event(level, message):
    if level.lower() == "debug":
        logger.debug(message)
    elif level.lower() == "info":
        logger.info(message)
    elif level.lower() == "warning":
        logger.warning(message)
    elif level.lower() == "error":
        logger.error(message)
    elif level.lower() == "critical":
        logger.critical(message)
    else:
        logger.info("Invalid log level specified! ⚠️")

# Example usage
log_event("info", "Application started successfully! 🚀")
log_event("error", "An unexpected error occurred! ❌")
```

✅ This function makes logging **more flexible** and **reusable** in any application.

---

## 📌 Step 5: Handling Exceptions with Logging
Instead of using `print()`, we should log exceptions for better debugging.

```python
try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except Exception as e:
    logger.exception("An exception occurred! ⚠️")
```

🔎 **Why Use `logger.exception()`?**
- It **automatically** captures the **stack trace** (line number & error details).
- Helps in debugging issues efficiently.

---

## 🏆 Conclusion
Building a log management system in Python is **easy and powerful!** 🎯 This guide covered:
✅ Setting up logging 🎛️
✅ Logging messages with different severity levels 📢
✅ Rotating logs to manage file size 🔄
✅ Creating a custom log function 🛠️
✅ Handling exceptions with logging 🚨

Now, you have a **fully functional log management system** that you can use in your applications. 🚀🔥

If you found this guide useful, give it a ⭐! 😊

