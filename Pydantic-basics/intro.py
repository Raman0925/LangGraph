from pydantic import BaseModel, Field
class Person(BaseModel){
    name: str = Field(..., description="The name of the person")
    age: int = Field(..., description="The age of the person")
    email: str = Field(..., description="The email of the person")
    phone: str = Field(..., description="The phone number of the person")
    address: str = Field(..., description="The address of the person")
    city: str = Field(..., description="The city of the person")
    state: str = Field(..., description="The state of the person")
    zip: str = Field(..., description="The zip code of the person")
    country: str = Field(..., description="The country of the person")
    is_student: bool = Field(..., description="Whether the person is a student")
}

person = Person(name="John Doe", age=25, email="john.doe@example.com", phone="1234567890", address="123 Main St", city="Anytown", state="CA", zip="12345", country="USA", is_student=True)
print(person)