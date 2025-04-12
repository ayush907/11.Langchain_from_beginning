from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# features of pydantic:
# 1. validation
# 2. impliced type conversion

class Student(BaseModel):

    name : str 
    roll_no : int = 67
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10, default=5, description="A decimal value representing the cgpa of the student")


new_student = {"name": "ayush", "age" : 32, "email": "dhekayush@gmail.com", "cgpa": 8}

student = Student(**new_student)

print(student)
print(type(student))
print(student.name)
print(student.roll_no)
print(student.email)
print(student.cgpa)

# converting the student object into dictionary
student_dict = dict(student)

print(f'the age is : {student_dict["age"]}')

# creating the json
student_json = student.model_dump_json()
print(student_json)
print(type(student_json))     # json string banaata hai 
