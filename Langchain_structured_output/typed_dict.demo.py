from typing import TypedDict

class person(TypedDict):
    name: str
    age: int


new_person: person = {'name': "ayush", 'age':78}

name, age = new_person.values()

print(name)
print(age)
