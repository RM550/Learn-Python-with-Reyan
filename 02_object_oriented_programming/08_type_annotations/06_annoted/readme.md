# Annotated Type in Type Annotations (Python)

## Introduction 📌

The **Annotated** type annotation in Python was introduced in **PEP 593** and added in **Python 3.9**. It allows developers to attach metadata to type hints, enabling additional information for static type checkers, runtime validation, and documentation.

## Why Use `Annotated`? 🤔

- **Adds metadata to types**: Helps provide extra context.
- **Enhances static analysis**: Type checkers can use metadata to enforce constraints.
- **Useful for validation**: Can integrate with libraries like `pydantic` and `attrs`.
- **Improves documentation**: Clearer function signatures.

## Syntax 📝

The `Annotated` type is imported from the `typing` module:

```python
from typing import Annotated
```

### Basic Example 🎯

```python
from typing import Annotated

def process_data(value: Annotated[int, "Must be positive"]) -> None:
    print(f"Processing: {value}")

process_data(10)  # ✅ Valid
process_data(-5)  # ⚠️ No runtime enforcement (metadata only)
```

## Using `Annotated` for Validation 🚀

Since `Annotated` does not enforce rules at runtime, you can use libraries like `pydantic` for validation.

```python
from typing import Annotated
from pydantic import BaseModel, Field

class User(BaseModel):
    age: Annotated[int, Field(ge=18)]  # Age must be >= 18

user = User(age=20)  # ✅ Valid
user = User(age=15)  # ❌ Raises validation error
```

## Combining `Annotated` with Multiple Metadata 📦

You can attach multiple metadata values:

```python
from typing import Annotated

def set_temperature(temp: Annotated[float, "Celsius", "Must be between 0 and 100"]) -> None:
    print(f"Temperature set to: {temp}")

set_temperature(25.5)  # ✅ Valid
```

## `Annotated` with Callable Metadata ⚡

Functions can be used as metadata:

```python
from typing import Annotated, Callable

def validate_positive(value: int) -> int:
    if value < 0:
        raise ValueError("Value must be positive")
    return value

PositiveInt = Annotated[int, validate_positive]

def process_number(num: PositiveInt) -> None:
    print(f"Processing: {num}")

process_number(10)  # ✅ Valid
process_number(-5)  # ❌ Raises ValueError
```

## Using `Annotated` with Type Aliases 🔗

```python
from typing import Annotated

NonNegativeInt = Annotated[int, "Must be >= 0"]

def set_value(value: NonNegativeInt) -> None:
    print(f"Value set to: {value}")

set_value(5)  # ✅ Valid
set_value(-1)  # ⚠️ No runtime enforcement
```

## `Annotated` with `dataclasses` 🏗️

```python
from dataclasses import dataclass
from typing import Annotated

@dataclass
class Person:
    name: Annotated[str, "Full name required"]
    age: Annotated[int, "Age must be positive"]

p = Person(name="John Doe", age=30)  # ✅ Valid
```

## Benefits of Using `Annotated` 🎉

- **Improves documentation**: Adds meaningful metadata to type hints.
- **Integrates with validation frameworks**: Libraries like `pydantic` can use it.
- **Encourages better type annotations**: More expressive and structured code.

## Limitations ⚠️

- **No enforcement at runtime**: Python does not enforce metadata automatically.
- **Dependent on third-party tools**: Libraries like `pydantic` are needed for validation.
- **Not all type checkers support it**: Some static analyzers may not fully utilize metadata.

## Summary 📌

| Feature | Supported? |
|---------|------------|
| Basic Metadata | ✅ |
| Multiple Metadata | ✅ |
| Callable Metadata | ✅ |
| Runtime Enforcement | ❌ (Requires additional tools) |
| Integration with `pydantic` | ✅ |

## Conclusion 🎯

Using `Annotated` in Python allows developers to provide extra information on type hints, making code **more readable, structured, and useful** for static analysis and validation frameworks. However, since Python does not enforce metadata at runtime, it is often used in combination with libraries like **pydantic** for validation.

🚀 **Happy Coding!** 🚀

