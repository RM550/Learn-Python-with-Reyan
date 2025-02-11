# Literal Type Annotation in Python

## Introduction 📌

The **Literal** type annotation in Python was introduced in **PEP 586** and added in **Python 3.8**. It allows you to specify that a variable or function parameter must have a specific, predefined value. This is useful for enforcing stricter type checking and improving code clarity.

## Why Use Literal Types? 🤔

- Provides **better type safety** by restricting values to predefined constants.
- Improves **code readability** by making expected values explicit.
- Helps **static type checkers** (e.g., MyPy) catch potential errors.
- Can be used for **configuration options, flags, and state management**.

## Syntax 📝

The `Literal` type is imported from the `typing` module:

```python
from typing import Literal
```

### Basic Example 🎯

```python
from typing import Literal

def set_mode(mode: Literal['auto', 'manual', 'off']) -> None:
    print(f"Mode set to: {mode}")

set_mode('auto')  # ✅ Valid
set_mode('manual')  # ✅ Valid
set_mode('on')  # ❌ Type checker will raise an error
```

### Literal with Variables 🎯

```python
ModeType = Literal['light', 'dark']

def set_theme(theme: ModeType) -> None:
    print(f"Theme set to: {theme}")

set_theme('light')  # ✅ Valid
set_theme('dark')  # ✅ Valid
set_theme('blue')  # ❌ Type checker error
```

## Using Literal with Enums 🏆

`Literal` can be combined with **Enum** to provide more structure:

```python
from enum import Enum
from typing import Literal

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

def set_color(color: Literal[Color.RED, Color.GREEN, Color.BLUE]) -> None:
    print(f"Color set to: {color.value}")

set_color(Color.RED)  # ✅ Valid
set_color(Color.GREEN)  # ✅ Valid
set_color('yellow')  # ❌ Type checker error
```

## Combining Literal with Other Types 🧩

You can mix `Literal` with other types using `Union`:

```python
from typing import Union, Literal

def process_value(value: Union[int, Literal['default']]) -> None:
    print(f"Processing: {value}")

process_value(10)  # ✅ Valid
process_value('default')  # ✅ Valid
process_value('random')  # ❌ Type checker error
```

## Literal with Boolean Values ✅❌

```python
def toggle_feature(enable: Literal[True, False]) -> None:
    if enable:
        print("Feature enabled")
    else:
        print("Feature disabled")

toggle_feature(True)  # ✅ Valid
toggle_feature(False)  # ✅ Valid
toggle_feature(1)  # ❌ Type checker error
```

## Literal with Numeric Values 🔢

```python
def set_level(level: Literal[1, 2, 3, 4, 5]) -> None:
    print(f"Level set to: {level}")

set_level(3)  # ✅ Valid
set_level(5)  # ✅ Valid
set_level(10)  # ❌ Type checker error
```

## Benefits of Using Literal 🎉

- **Better IDE support**: Autocompletion and hints in editors like VSCode and PyCharm.
- **Prevents incorrect values**: Static type checkers catch invalid values early.
- **Improves maintainability**: Clearer expected values in function signatures.

## Limitations ⚠️

- **Only works with static type checkers**: Python itself does not enforce type hints at runtime.
- **No dynamic values**: Literal requires hardcoded, predefined values.
- **Can be restrictive**: If the values need to change frequently, `Literal` may not be the best choice.

## Summary 📌

| Feature | Supported? |
|---------|------------|
| Strings | ✅ |
| Integers | ✅ |
| Booleans | ✅ |
| Enums | ✅ |
| Variables | ❌ |
| Dynamic values | ❌ |

## Conclusion 🎯

Using `Literal` in Python provides a stricter and more readable approach to defining function arguments and return values. It helps prevent errors and enhances type safety, especially when used with static type checkers like **MyPy**. However, it should be used wisely, as it can be restrictive when dealing with frequently changing values.

🚀 **Happy Coding!** 🚀

