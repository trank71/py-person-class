class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for family in people:
        person = Person.people[family["name"]]

        wife_name = family.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]

        husband_name = family.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]

    return person_list
