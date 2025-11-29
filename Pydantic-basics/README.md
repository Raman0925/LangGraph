## Pydantic Learning Path

This folder contains structured notes and examples for learning **Pydantic** from basics to advanced topics.

### 1. Getting Started

- **What is Pydantic?**
  - Data validation and settings management using Python type hints.
  - Ensures data is parsed and validated into well‑typed objects.
- **Install**
  - `pip install pydantic`

#### 1.1 First Model

```python
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool = True


user = User(id=1, name="Raman")
print(user)
print(user.id, type(user.id))
```

- **Key ideas**:
  - Inherit from `BaseModel`.
  - Use type hints to describe fields.
  - Default values are allowed.

---

### 2. Validation & Parsing

- **Type coercion**

```python
User(id="1", name="Raman")  # "1" → 1
```

- **Validation errors**

```python
from pydantic import ValidationError

try:
    User(id="abc", name="Raman")
except ValidationError as e:
    print(e.json())
```

- **Common field types**
  - `int`, `float`, `str`, `bool`
  - `list[T]`, `dict[str, T]`, `tuple`, `set`
  - `datetime`, `date`, `time`, `UUID`, `EmailStr`, etc.

---

### 3. Field Customization

- **Using `Field`**

```python
from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    tags: list[str] = Field(default_factory=list)
```

- **Notes**:
  - `...` means the field is required.
  - `default_factory` is used for dynamic defaults (e.g., empty list).

---

### 4. Nested Models

```python
class Address(BaseModel):
    city: str
    country: str


class Customer(BaseModel):
    name: str
    address: Address


customer = Customer(
    name="Raman",
    address={"city": "Delhi", "country": "India"},
)
```

- Pydantic automatically converts dictionaries to nested models.

---

### 5. Validators (Advanced Basics)

> Note: Syntax differs between Pydantic v1 and v2; this uses **v2 style**.

```python
from pydantic import BaseModel, field_validator


class Account(BaseModel):
    username: str
    age: int

    @field_validator("username")
    @classmethod
    def username_must_be_lower(cls, v: str) -> str:
        if v != v.lower():
            raise ValueError("username must be lowercase")
        return v
```

---

### 6. Model Config (Model Configuration)

> In Pydantic v2, use `model_config`.

```python
from pydantic import BaseModel, ConfigDict


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
```

- **Common config options**:
  - `from_attributes=True`: allows loading from ORM objects.
  - `extra="ignore" | "allow" | "forbid"`: what to do with extra fields.

---

### 7. Settings Management (Environment Variables)

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str
    debug: bool = False

    class Config:
        env_prefix = "APP_"


settings = Settings()  # reads from environment: APP_DB_URL, APP_DEBUG
```

---

### 8. Advanced Topics To Explore Next

These are topics we can expand into separate example files as you learn:

- **Performance**
  - Using `model_validate`, `model_dump`, and `model_copy`.
- **Custom types**
  - Creating your own constrained / custom types.
- **Serialization**
  - Controlling JSON output (include / exclude, aliases).
- **ORM integration**
  - Using Pydantic with SQLAlchemy or other ORMs.
- **Pydantic Dataclasses**
  - Using `pydantic.dataclasses.dataclass` for dataclass-style models.

---

### 9. Suggested Learning Order

1. **Basic models** (`BaseModel`, types, defaults).
2. **Validation & errors** (`ValidationError`, type coercion).
3. **Field customization** (`Field`, constraints).
4. **Nested models** and complex data structures.
5. **Validators** (`field_validator`, cross-field validation).
6. **Model config** and extra fields behavior.
7. **Settings management** for configs and env vars.
8. **Advanced**: custom types, ORM mode, serialization tricks.

You can now create small Python files in this folder (e.g., `01_basic_model.py`, `02_validation.py`, etc.) and implement each section with runnable examples.
