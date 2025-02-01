# Method Injection in Python 🔄💉

**Method Injection** is another form of **Dependency Injection (DI)** where dependencies are passed directly to methods of a class, rather than being injected through the constructor or setter methods. This allows the class to receive dependencies only when specific methods need them.

Unlike **Constructor Injection** and **Setter Injection**, which inject dependencies into the class for the entire lifetime of the object, **Method Injection** provides dependencies **on-demand** for specific method calls.

---

## 1. What is Method Injection? 🤔

In **Method Injection**, dependencies are provided as arguments to a **method** rather than being set on the class itself. This type of injection is useful when dependencies are only needed for a specific operation and not for the whole object's lifecycle.

### Why Method Injection?
- **On-demand dependencies**: Dependencies are provided only when they are needed, making the class less coupled and more flexible.
- **Method-specific**: When a method requires specific dependencies that are not needed by the entire class, method injection ensures that only the relevant dependencies are passed at the appropriate time.
- **Less overhead**: If dependencies are only used occasionally, there's no need to inject them at the object creation time or store them in the class for the whole object lifecycle.

---

## 2. How Method Injection Works 🚀

Here’s how Method Injection works step-by-step:

1. **Create the Class**: You define the class with methods that require specific dependencies.
2. **Call Method with Dependency**: When invoking a method, the required dependency is passed directly to it as an argument.
3. **Use Dependency Inside Method**: The method can use the provided dependency for its specific task.

Let’s look at an example to understand it better.

---

## 3. Example of Method Injection 🏗️

Let’s consider a `PaymentProcessor` class that requires a **PaymentGateway** for processing payments. Instead of having the **PaymentGateway** as a class-level dependency, we’ll inject it when needed in the method that processes payments.

### Step 1: Create the Dependency (PaymentGateway)

```python
class PaymentGateway:
    def process_payment(self, amount: float):
        print(f"Processing payment of {amount} units.")
```

### Step 2: Inject Dependency via Method (PaymentProcessor)

```python
class PaymentProcessor:
    def process_order(self, amount: float, gateway: PaymentGateway):  # Dependency is injected here
        print(f"Order received. Total amount: {amount}")
        gateway.process_payment(amount)  # Using the dependency in the method
        print("Order processed successfully!")
```

### Step 3: Instantiate and Call Method with Dependency

```python
# Create the dependency (PaymentGateway)
gateway = PaymentGateway()

# Create the PaymentProcessor object
payment_processor = PaymentProcessor()

# Inject the dependency into the method when calling it
payment_processor.process_order(100.0, gateway)
```

**Output**:
```
Order received. Total amount: 100.0
Processing payment of 100.0 units.
Order processed successfully!
```

### Key Points:
- The **PaymentProcessor** class does not store the **PaymentGateway** dependency.
- The **PaymentGateway** dependency is injected when calling the `process_order` method.
- The method can use the dependency only when it needs to process the payment, and it does not require the dependency to be available for the entire object's lifecycle.

---

## 4. Benefits of Method Injection 🌟

### 1. **On-Demand Dependencies** 🔄
   - Method Injection allows you to inject dependencies only when they are needed. This makes your class more flexible and less coupled, as it doesn’t hold on to unnecessary dependencies when they are not required.

### 2. **Reduced Overhead** 🔋
   - If dependencies are only used for specific operations or conditions, you don’t need to store them within the class or inject them during object creation. This reduces unnecessary overhead.

### 3. **Improved Testability** 🧪
   - Method Injection allows you to easily mock or replace dependencies for specific method calls, making it easier to test individual methods with their required dependencies.

### 4. **Encapsulation** 🛡️
   - By providing dependencies only when needed in specific methods, Method Injection helps to encapsulate the logic of dependency usage. Dependencies are localized and only accessible within the methods where they are passed.

---

## 5. Real-World Example: Method Injection in Action 🏙️

Let’s consider a **ReportGenerator** class that requires a **Logger** only when generating a report. The `Logger` dependency is passed directly to the method, rather than being stored in the class.

```python
class Logger:
    def log(self, message: str):
        print(f"Log: {message}")

class ReportGenerator:
    def generate_report(self, data: str, logger: Logger):  # Logger injected into method
        print(f"Generating report with data: {data}")
        logger.log("Report generation started.")
        print(f"Report generated: {data}")
        logger.log("Report generation completed.")

# Create the dependency
logger = Logger()

# Create the ReportGenerator object
report_generator = ReportGenerator()

# Inject the dependency when calling the method
report_generator.generate_report("Sales Report Data", logger)
```

**Output**:
```
Generating report with data: Sales Report Data
Log: Report generation started.
Report generated: Sales Report Data
Log: Report generation completed.
```

### Key Points:
- The **Logger** dependency is injected **only when generating the report**.
- This approach is flexible, as the **Logger** is not needed by the entire class, just by the `generate_report` method.

---

## 6. When to Use Method Injection? 📅

Method Injection is useful when:
- **Dependencies are method-specific**: The class does not need the dependency throughout its lifecycle, but only for a specific task.
- **On-demand flexibility**: You only want to inject dependencies when they are actually needed for a method call.
- **Reduced resource usage**: If a dependency is resource-intensive, you may want to instantiate it only when needed for a specific operation.
- **Improved readability and testability**: By passing dependencies explicitly to methods, you make your code more readable and easier to test.

---

## 7. Method Injection vs. Other Types of Dependency Injection ⚖️

### 1. **Constructor Injection** 🔑
   - **Pros**: Dependencies are provided upfront, making the object **immutable** and ensuring that all dependencies are available from the beginning.
   - **Cons**: Less flexible if you only need the dependency for certain operations.

### 2. **Setter Injection** 🔄
   - **Pros**: Dependencies can be injected or modified after object creation.
   - **Cons**: The class needs to manage state, and dependencies can be set **anytime**, which might lead to an inconsistent object state.

### 3. **Method Injection** 💉
   - **Pros**: Dependencies are injected **on-demand** for specific methods, making it flexible and lightweight.
   - **Cons**: Dependencies are not stored in the class, which might make the class state harder to track in more complex scenarios.

---

## 8. Conclusion 🚀

Method Injection is a great way to provide **on-demand** dependencies for specific methods, improving the flexibility and testability of your classes. It reduces overhead by ensuring dependencies are only passed when needed, making your code more efficient and easier to maintain.

If your class has method-specific dependencies or if dependencies are only required occasionally, **Method Injection** is an ideal pattern to use. It allows for a lightweight approach, keeping your objects clean and flexible! 🌟
