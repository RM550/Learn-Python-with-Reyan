
# Overriding Methods in OOP Python 🧑‍💻🐍

**Overriding Methods** is a key concept in **Object-Oriented Programming (OOP)**. It allows a **child class** to provide its own implementation of a method that is already defined in its **parent class**. This is a fundamental feature of polymorphism in OOP, allowing for more flexible and dynamic code. 💡

In this README, we will cover:
- What is **Method Overriding**? 🤔
- Why is Method Overriding important in OOP? 🧩
- How to **Override Methods** in Python? 🔄
- Examples with detailed explanations and emojis! 🎨

Let’s dive in! 🎉

---

## What is Method Overriding? 🔄

**Method Overriding** happens when a **child class** defines a method with the same name as a method in its **parent class**. When you create an object of the child class and call the overridden method, Python will use the child class's version of the method, not the parent class's version.

### Key Points to Remember:
- The method in the child class **has the same name** as the method in the parent class. 🔄
- The child class can **change or extend** the functionality of the parent method. 🌱
- Overriding allows the child class to provide a **specific implementation** of a method while retaining the same interface. 🎨

---

## Why is Method Overriding Important? 🤩

Method overriding plays an important role in OOP because it allows:
- **Polymorphism**: The same method can have different behaviors based on the object type (parent or child class). 🌈
- **Customization**: Child classes can modify or extend the functionality of the inherited methods. 🔧
- **Code Reusability**: Inherited methods from the parent class can be reused, while also being tailored to suit the child class. 🔄

---

## How to Override Methods in Python? 🧑‍🔧

In Python, overriding a method is simple! Just define a method with the same name in the child class, and Python will automatically use that version when called from the child class object. 🧩

### Basic Syntax for Overriding Methods:

```python
class ParentClass:
    def method_name(self):
        # Parent class method
        pass

class ChildClass(ParentClass):
    def method_name(self):
        # Overridden method in child class
        pass
```

### Example 1: Overriding a Method 🐕

```python
class Animal:
    def speak(self):
        print("Animal makes a sound 🐾")

class Dog(Animal):
    def speak(self):  # Overriding the 'speak' method
        print("Dog barks 🐕")

# Creating an object of Dog class
dog = Dog()
dog.speak()  # Output: Dog barks 🐕
```

In the above example:
- The `Dog` class inherits from the `Animal` class.
- The `Dog` class overrides the `speak()` method from the `Animal` class to change its behavior.
- When `dog.speak()` is called, Python uses the `Dog` class's version of `speak()`, not the `Animal` class's version.

---

## Method Overriding with Arguments 💬

Method overriding can also be done for methods that take **arguments**. The child class method can accept the same or different arguments compared to the parent class's method. 🧑‍💻

### Example 2: Overriding Method with Arguments

```python
class Animal:
    def speak(self, sound):
        print(f"Animal says {sound} 🐾")

class Dog(Animal):
    def speak(self, sound="Woof"):  # Overriding with a default argument
        print(f"Dog barks {sound} 🐕")

# Creating an object of Dog class
dog = Dog()
dog.speak("Bow-Wow")  # Output: Dog barks Bow-Wow 🐕
```

Here:
- The `Dog` class overrides the `speak()` method of `Animal`.
- The `Dog` class adds a **default argument** (`sound="Woof"`) to the method, making it more flexible.
- You can pass a custom argument when calling `dog.speak("Bow-Wow")`, or it will default to `"Woof"` if no argument is provided.

---

## Calling Parent Class Method Inside Overridden Method 🏗️

Sometimes, you want to **extend** the functionality of the parent class’s method rather than completely replace it. You can do this by calling the parent class’s method from inside the child class's method using `super()`. 🔄

### Example 3: Using `super()` to Extend Functionality 🧩

```python
class Animal:
    def speak(self):
        print("Animal makes a sound 🐾")

class Dog(Animal):
    def speak(self):  # Overriding and extending the parent method
        super().speak()  # Calling parent class method
        print("Dog barks 🐕")

# Creating an object of Dog class
dog = Dog()
dog.speak()
# Output: 
# Animal makes a sound 🐾
# Dog barks 🐕
```

In this example:
- The `Dog` class overrides the `speak()` method from the `Animal` class.
- However, it calls `super().speak()` to first invoke the parent class's method and then adds additional functionality (barking).
- This way, the parent class’s behavior is **extended** rather than completely replaced.

---

## Overriding Methods with Return Values 🔄

In Python, you can override methods that return a value. The child class can change the return value or modify it based on specific logic. 🔄

### Example 4: Overriding Methods with Return Values 💰

```python
class Vehicle:
    def fuel_efficiency(self):
        return "Fuel efficiency: 15 km/l 🚗"

class ElectricCar(Vehicle):
    def fuel_efficiency(self):  # Overriding with a custom return value
        return "Fuel efficiency: 100 km/kWh ⚡"

# Creating an object of ElectricCar class
electric_car = ElectricCar()
print(electric_car.fuel_efficiency())  # Output: Fuel efficiency: 100 km/kWh ⚡
```

In this example:
- The `Vehicle` class has a method `fuel_efficiency()` that returns the fuel efficiency of a regular car.
- The `ElectricCar` class overrides this method to return the fuel efficiency for an electric car.
- When `electric_car.fuel_efficiency()` is called, it uses the overridden method in the `ElectricCar` class.

---

## Benefits of Method Overriding 🎨

- **Customization**: Allows child classes to modify or extend parent class functionality. 🧑‍🔧
- **Polymorphism**: The same method name can have different behaviors in different classes. 🌈
- **Code Reusability**: You can reuse code from the parent class and only change what’s necessary. 🔄

---

## Conclusion 🎉

In this README, we explored the concept of **Method Overriding** in Python, where a **child class** provides its own implementation of a method that is already defined in the **parent class**. We covered:
- How to override methods in Python 🔄
- The benefits of overriding methods in OOP 🧩
- **4 practical examples** that demonstrate method overriding in action 🎨

Method overriding helps make your code more flexible, reusable, and dynamic. It is an essential tool in creating clean, maintainable, and efficient OOP code. 🚀

Happy coding and enjoy overriding those methods! 💻✨
---
