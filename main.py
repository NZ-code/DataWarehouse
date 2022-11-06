from faker import Faker
import random
import datetime
from Contract import Contract
from Consultation import Consultation
from Client import Client
from Employee import Employee


def main():
    number = 10
    fake = Faker()
    clients = []
    for i in range(number):
        clients.append(Client(fake.name()))

    [print(object) for object in clients]
    print()

    employees = []
    for i in range(number):
        employees.append(Employee(fake.name(), fake.date(), fake.date()))

    [print(object) for object in employees]
    print()

    contracts = []
    for i in range(number):
        contracts.append(Contract)

    [print(object) for object in contracts]
    print()

    consultations = []
    for i in range(number):
        consultations.append(Consultation(random.randint(2, 8), random.randint(20, 100), random.choice(employees),
                                          random.choice(contracts), fake.date()))

    [print(object) for object in consultations]
    print()


if __name__ == '__main__':
    main()
