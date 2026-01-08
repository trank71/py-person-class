class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = [
        Person(person_one["name"], person_one["age"])
        for person_one in people
    ]

    for family in people:
        person = Person.people[family["name"]]

        wife_name = family.get("wife")
        if wife_name is not None:
            if wife_name not in Person.people:
                raise ValueError(
                    f"Wife {wife_name} not found for {person.name}"
                )
            person.wife = Person.people[wife_name]

        husband_name = family.get("husband")
        if husband_name is not None:
            if husband_name not in Person.people:
                raise ValueError(
                    f"Husband {husband_name} not found for {person.name}"
                )
            person.husband = Person.people[husband_name]

    return person_list
