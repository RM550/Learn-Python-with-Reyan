
# The Object Class in Python 🧑‍💻🐍

In **Object-Oriented Programming (OOP)**, everything in Python is an **object**, and every object is an instance of the **Object class**. The **Object class** is the base class for all classes in Python. This means that all classes, whether they are user-defined or built-in, inherit from the `object` class! 🔥

In this README, we will explore:
- What is the **Object class**? 🤔
- How does it work? 🛠️
- What methods and properties are available in the **Object class**? 🔍

Let’s dive into the **Object class** with detailed explanations and fun examples! 🎉

---

## What is the Object Class? 🤓

The `object` class is the **root base class** for all Python classes. When you create a class in Python, it **implicitly inherits** from the `object` class. This means that every class in Python is a subclass of `object` (even if we don't explicitly mention it). 🧬

- **The `object` class** provides essential methods that every object in Python inherits.
- These methods can be overridden in your own classes, but they provide default behaviors that can be useful. 🌟

### Why is the Object Class Important? 🤔

- **Universal Base Class**: Every Python class inherits from `object` directly or indirectly. This ensures that every class has some common methods. 🧩
- **Code Reusability**: The `object` class provides default behavior for methods like `__str__()`, `__repr__()`, and `__eq__()` which can be customized to suit your needs. 🔄

---

## The Default Methods of the Object Class 🛠️

The `object` class defines several important methods. Let's look at them in detail with examples and emojis! 🎨

### 1. `__init__()` Method 🚀

The `__init__()` method is the **constructor** of a class. It is automatically called when a new object is created from a class. It allows you to initialize the object’s attributes. 🔧

- This method is **not part of the `object` class**, but it is inherited by all classes, including the ones that implicitly inherit from `object`. 💡

### Example: `__init__()` Method

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Creating an object of Car class
car = Car("Tesla", "Model S")
car.display_info()  # Output: Car Brand: Tesla, Model: Model S
```

### 2. `__str__()` Method ✨

The `__str__()` method is called by the `str()` function to return a **human-readable string representation** of an object. When you print an object, Python will use this method. If you don’t define it, Python will use a default one from the `object` class. 🖼️

### Example: `__str__()` Method

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

# Creating an object of Car class
car = Car("Tesla", "Model S")
print(car)  # Output: Tesla Model S
```

### 3. `__repr__()` Method 👀

The `__repr__()` method is similar to `__str__()`, but it is meant for **debugging and development**. It returns a string that is ideally an expression that can be used to recreate the object. 🧑‍💻

If you don’t define `__repr__()`, the default implementation will return a string like `<__main__.Car object at 0x00000123>` (memory address of the object). 😅

### Example: `__repr__()` Method

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}')"

# Creating an object of Car class
car = Car("Tesla", "Model S")
print(repr(car))  # Output: Car('Tesla', 'Model S')
```

### 4. `__eq__()` Method ⚖️

The `__eq__()` method is used to compare two objects. It is automatically called when you use the `==` operator to compare two objects. By default, Python compares objects based on their **memory addresses** (if you don’t override this method). 🧠

### Example: `__eq__()` Method

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model

# Creating two objects of Car class
car1 = Car("Tesla", "Model S")
car2 = Car("Tesla", "Model S")

print(car1 == car2)  # Output: True
```

### 5. `__del__()` Method 🧹

The `__del__()` method is a **destructor**. It is called when an object is about to be destroyed (i.e., when it goes out of scope or is explicitly deleted). 👋

- The `__del__()` method is not frequently used, but it can be useful when you need to clean up resources. 🧼

### Example: `__del__()` Method

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __del__(self):
        print(f"{self.brand} {self.model} is being destroyed!")

# Creating an object of Car class
car = Car("Tesla", "Model S")
del car  # Output: Tesla Model S is being destroyed!
```

---

## How to Use the Object Class? 🤔

You don’t need to explicitly inherit from the `object` class because Python automatically does that for you! All user-defined classes in Python implicitly inherit from `object`.

### Example: Implicit Inheritance from Object Class

```python
class Car:  # Implicitly inherits from object class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Creating an object of Car class
car = Car("Tesla", "Model S")
car.display_info()  # Output: Car Brand: Tesla, Model: Model S
```

Even though we don’t explicitly write `class Car(object):`, it is still considered as inheriting from `object`. 🌍

---

## Common Methods Inherited from the Object Class 🧩

- **`__init__(self)`**: Constructor for initializing the object. 🚀
- **`__str__(self)`**: String representation of the object for printing. ✨
- **`__repr__(self)`**: Debugging string representation for the object. 👀
- **`__eq__(self, other)`**: Compare two objects using `==`. ⚖️
- **`__del__(self)`**: Destructor for cleanup when object is deleted. 🧹

---

## Conclusion 🎉

In this README, we explored the **Object class** in Python. We covered the following points:
- Every class in Python implicitly inherits from the `object` class. 🧬
- The `object` class provides essential methods like `__init__()`, `__str__()`, `__repr__()`, and `__eq__()` that every object can inherit. 💡
- These methods help in object initialization, string representation, comparison, and cleanup. 🧩

Remember, even if you don’t explicitly inherit from `object`, all your classes do, so understanding the `object` class is essential to mastering Python OOP! 🚀

Happy coding and keep creating amazing objects! 💻✨
---
