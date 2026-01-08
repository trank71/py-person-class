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
    for family in people:
        person = Person.people[family["name"]]

        if "wife" in family and family["wife"] is not None:
            person.wife = Person.people[family["wife"]]

        if "husband" in family and family["husband"] is not None:
            person.husband = Person.people[family["husband"]]
    return person_list
