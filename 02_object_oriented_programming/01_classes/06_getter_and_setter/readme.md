# 🐍 Getters and Setters in Python 🎛️

Encapsulation is a fundamental concept in object-oriented programming (OOP). Getters and setters are tools that help achieve encapsulation by providing controlled access to private or protected attributes in a class. 🎯

---

## 📖 What Are Getters and Setters?

- **Getters**: Methods that retrieve the value of an attribute. 🕵️‍♀️  
- **Setters**: Methods that set or update the value of an attribute. ✍️  

In Python, getters and setters are often used with **private** or **protected** attributes to ensure data integrity and apply validation logic. 🔒

---

## 🤔 Why Use Getters and Setters?

1. **Encapsulation**: Protects sensitive data by restricting direct access to attributes. 🔐  
2. **Validation**: Ensures data being set is valid, preventing bugs or logical errors. ✅  
3. **Flexibility**: Allows modification of how data is retrieved or set without affecting other parts of the code. 🔄  

---

## 🔧 Implementing Getters and Setters

In Python, you can use regular methods or the `@property` decorator to define getters and setters. 🛠️

---

### 🛠️ Using Regular Methods

```python
class Employee:
    def __init__(self, name):
        self.__name = name  # Private attribute

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise ValueError("Name must be a string!")

# Usage
emp = Employee("Alice")
print(emp.get_name())  # Get the name 🎯
emp.set_name("Bob")    # Set a new name ✍️
print(emp.get_name())
```

---

### 🎉 Using the `@property` Decorator (Preferred in Python)

The `@property` decorator simplifies the use of getters and setters by allowing attribute access syntax. 🚀

```python
class Employee:
    def __init__(self, name):
        self.__name = name  # Private attribute

    @property
    def name(self):
        """Getter for name"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Setter for name"""
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise ValueError("Name must be a string!")

# Usage
emp = Employee("Alice")
print(emp.name)  # Access like an attribute 🎯
emp.name = "Bob"  # Set a new name ✍️
print(emp.name)
```

---

## 💡 Key Points About Getters and Setters

1. **Private Attributes**: Indicated by a double underscore (e.g., `__attribute`), these cannot be accessed directly outside the class. 🔒  
2. **Validation**: Setters allow you to add validation or logic before changing an attribute's value. 🛡️  
3. **Flexibility**: By using properties, you can seamlessly switch from direct attribute access to getter/setter methods without affecting the codebase. 🔄  

---

## 📝 Example with Validation

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    @property
    def balance(self):
        """Getter for balance"""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter for balance with validation"""
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount

# Usage
account = BankAccount(1000)
print(account.balance)  # Get balance 🎯
account.balance = 1500  # Update balance ✍️
print(account.balance)

# This will raise an error
# account.balance = -500
```

---

## 🔍 When to Use Getters and Setters

- **When data validation is required**: Use setters to enforce rules. ✅  
- **For sensitive data**: Use getters to restrict read-only access if needed. 🔐  
- **When attributes might change**: Use properties for flexibility without breaking existing code. ⚡  

---

## 🎯 Advantages of Using Getters and Setters

- 🛡️ **Enhanced Security**: Protect sensitive or critical data.  
- 🧹 **Improved Code Maintainability**: Centralize validation or transformation logic.  
- 🔄 **Flexibility**: Change implementation details without altering the interface.  

---

## 🚀 Conclusion

Getters and setters are powerful tools in Python for implementing encapsulation. By using the `@property` decorator, you can write cleaner and more Pythonic code while maintaining control over how attributes are accessed and modified. 🐍✨

**Pro Tip**: Use getters and setters when you need control or validation. For simple attributes, direct access is sufficient in Python. 🚀

---
