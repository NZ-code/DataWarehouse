from faker import Faker
import random
import datetime
from Contract import Contract
from Consultation import Consultation
from Client import Client
from Employee import Employee
from Contract import ServiceType

def add_contract_employee(number, employees: list, contracts: list):
    for i in range(number):
        contract = random.choice(contracts)
        employee = random.choice(employees)
        contract.add_employee(employee)
        employee.add_contract(contract)


def main():
    number = 10
    fake = Faker()
    clients = []
    for i in range(number):
        clients.append(Client(fake.name()))

    employees = []
    for i in range(number):
        employees.append(Employee(fake.name(), fake.date(), fake.date()))

    contracts = []
    for i in range(number):
        contracts.append(
            Contract(random.randint(20, 100), random.randint(2, 8), random.choice(clients), fake.date(), fake.date(),
                     random.choice(list(ServiceType)), bool(random.getrandbits(1))))

    add_contract_employee(15,employees,contracts)

    consultations = []
    for i in range(number):
        consultations.append(Consultation(random.randint(2, 8), random.randint(20, 100), random.choice(employees),
                                          random.choice(contracts), fake.date()))

    [print(object) for object in clients]
    print()
    [print(object) for object in consultations]
    print()
    [print(object) for object in contracts]
    print()
    [print(object) for object in employees]


if __name__ == '__main__':
    main()
