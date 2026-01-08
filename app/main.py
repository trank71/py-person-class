class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        one_person = Person(person["name"], person["age"])
        person_list.append(one_person)

    return person_list
