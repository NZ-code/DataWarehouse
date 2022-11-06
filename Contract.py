

import Employee
from Client import Client
from enum import Enum


class ServiceType(Enum):
    LOGO = 1
    POSTER = 2
    TEXT = 3
    VIDEO = 4
    MEDIA_CARE = 5


class Contract:
    idGen = 0

    def __init__(self, price, client: Client, begin_at, closed_at, service_type: ServiceType,
                 is_accepted: bool):
        Contract.idGen += 1
        self.id = self.idGen
        self.price = price
        self.team_count = 0
        self.client = client
        self.begin_at = begin_at
        self.closed_at = closed_at
        self.service_type = service_type
        self.is_accepted = is_accepted
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        self.team_count = len(self.employees)

    def __str__(self):
        return "Contract( id:" + str(self.id) + ", " + str(self.price) + ", " + str(self.team_count) + ", " + str(
            self.client) + ", " + str(self.begin_at) + ", " + str(self.closed_at) + ", " + str(
            self.service_type) + ", " + str(self.is_accepted) + ", employees:" + str(self.employees) + ")"

    def __repr__(self):
        return str(self)
