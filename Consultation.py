from Employee import Employee
from Contract import Contract
from datetime import timedelta, date
import random
from Contract import ServiceType
from Client import Client


def add_contract_employee(employee: Employee, contract: Contract):
    contract.add_employee(employee)
    employee.add_contract(contract)


def _gen_contract(client: Client, consultation_date: date, max_contract_end_date):
    date_start = consultation_date
    min_duration_days = 180
    contract_duration = random.randint(min_duration_days, (max_contract_end_date - date_start).days)
    date_end = date_start + timedelta(days=contract_duration)

    return Contract(random.randint(20, 100), client, date_start, date_end,
                    random.choice(list(ServiceType)), bool(random.getrandbits(1)))


class Consultation:
    idGen = 0

    def __init__(self, duration, hourly_rate, employee: Employee, consultation_date: date, client: Client,
                 employees: list, max_contract_end_date):
        Consultation.idGen += 1
        self.id = self.idGen
        self.duration = duration
        self.hourly_rate = hourly_rate
        self.employee = employee
        self.consultation_date = consultation_date
        self.contract = _gen_contract(client, consultation_date, max_contract_end_date)

        possible_project_employees = list(
            filter(lambda e: e.fire_date is None or self.contract.begin_at < e.fire_date, employees))
        project_employees = random.sample(possible_project_employees, k=random.randint(1, 5))
        for employee in project_employees:
            add_contract_employee(employee, self.contract)

    @staticmethod
    def get_header():
        return ['id', 'duration', 'hourly_rate', 'employee_id', 'contract_id','date']

    def get_csv_format(self):
        return [self.id, self.duration, self.hourly_rate, self.employee.id, self.contract.id, self.consultation_date]

    def __str__(self):
        return "Consultation( id:" + str(self.id) + ", duration:" + str(self.duration) + ", hourly_rate:" + str(
            self.hourly_rate) + ", " + str(self.employee) + ", " + str(self.contract) + ", consultation_date:" + str(
            self.consultation_date) + ")"

    def __repr__(self):
        return str(self)
