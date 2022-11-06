from faker import Faker
import random
from datetime import timedelta, date
from Contract import Contract
from Consultation import Consultation
from Client import Client
from Employee import Employee
from Contract import ServiceType


def gen_employee(start_range: date, end_range: date):
    # case 1 : company start = start_range  T1 = end_range
    fake = Faker()
    hire_date = fake.date_between(start_range, end_range)

    min_work_days = 60
    max_work_days = (end_range - hire_date).days

    chance_of_firing = 10
    fire_date = None
    if max_work_days > min_work_days and random.randint(0, 100) < chance_of_firing:
        work_duration = random.randint(min_work_days, max_work_days)
        fire_date = hire_date + timedelta(days=work_duration)
    return Employee(fake.name(), hire_date, fire_date)


def gen_consultation(employees: list, end_range: date, clients: list):
    fake = Faker()
    consultant = random.choice(employees)
    consultation_date = fake.date_between(consultant.hire_date, consultant.fire_date or end_range)
    return Consultation(random.randint(2, 8), random.randint(20, 100), consultant, consultation_date,
                        random.choice(clients), employees)


def firing_machine(employees:list, start_range: date, end_range: date):
    fired_employees = random.choices(employees, k = random.randint(1,len(employees)//3))
    for employee in fired_employees:
        fired_date = Faker().date_between(start_range, end_range)
        employee.fired_date = fired_date
def main():

    ## t1
    company_start = date(year=2006, month=3, day=20)
    t1 = date(year=2010, month=8, day=27)
    t2 = date(year=2016, month=10, day=13)
    number = 100
    fake = Faker()

    employees = []
    for i in range(number):
        employees.append(gen_employee(company_start, t1))

    clients = []
    for i in range(number):
        clients.append(Client(fake.name()))

    consultations = []
    for i in range(number):
        consultations.append(gen_consultation(employees, t1, clients))

    # [print(object) for object in clients]
    # print()
    # [print(object) for object in consultations]
    # print()
    # [print(object) for object in employees]

    ## t2

    firing_machine(employees, t1, t2)

if __name__ == '__main__':
    main()
