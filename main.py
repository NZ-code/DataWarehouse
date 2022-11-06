from faker import Faker
import random
from datetime import timedelta, date
from Contract import Contract
from Consultation import Consultation
from Client import Client
from Employee import Employee
from Contract import ServiceType


def add_contract_employee(employees: list, contracts: list):
    for contract in contracts:
        for i in range(random.randint(1, 5)):
            employee = random.choice(employees)
            contract.add_employee(employee)
            employee.add_contract(contract)

def genEmployee(start_range:date, end_range:date):
    # case 1 : company start = start_range  T1 = end_range
    fake = Faker()
    hire_date =fake.date_between(start_range, end_range)
    
    min_work_days = 60
    min_month = timedelta(days=min_work_days)
    max_work_days = (end_range - hire_date).days
    
    chance_of_firing = 10
    fire_date = None
    if max_work_days > min_work_days and random.randint(0,100) < chance_of_firing:
        work_duration = random.randint(min_work_days,max_work_days)
        fire_date  = hire_date + timedelta(days = work_duration)
    return Employee(fake.name(), hire_date, fire_date)
def genConsultation(employees:list,end_range:date):
    fake = Faker()
    consultant = employees.choise()
    consultation_date = fake.date_between(consultant.hire_date, consultant.fire_date or end_range)
    
  
def main():
    company_start = date(year=2006, month=3, day=20)
    t1 = date(year=2010, month=8, day=27)
    number = 10
    fake = Faker()
    
    employees = []
    for i in range(number):
        employees.append(genEmployee(company_start, t1))


    clients = []
    for i in range(number):
        clients.append(Client(fake.name()))

    

    contracts = []
    for i in range(number):
        contracts.append(
            Contract(random.randint(20, 100), random.choice(clients), fake.date(), fake.date(),
                     random.choice(list(ServiceType)), bool(random.getrandbits(1))))

    add_contract_employee(employees,contracts)

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

    for contract in contracts:
        for employee in contract.employees:
            print(str(contract.id) +","+str(employee.id))

if __name__ == '__main__':
    main()
