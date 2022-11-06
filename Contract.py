import Employee
from Client import Client
from enum import Enum


class ServiceType(Enum):
    LOGO = 'logo'
    POSTER = 'poster'
    TEXT = 'text'
    VIDEO = 'video'
    MEDIA_CARE = 'media care'

    def __str__(self):
        return str(self.value)


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
        self._employees = []

    def get_employees(self):
        return self._employees

    def add_employee(self, employee: Employee):
        self._employees.append(employee)
        self.team_count = len(self._employees)

    def __str__(self):
        return "Contract( id:" + str(self.id) + ", " + str(self.price) + ", " + str(self.team_count) + ", " + str(
            self.client) + ", " + str(self.begin_at) + ", " + str(self.closed_at) + ", " + str(
            self.service_type) + ", " + str(self.is_accepted) + ", employees:" + str(self._employees) + ")"

    def __repr__(self):
        return str(self)

    @staticmethod
    def get_header():
        return ['id', 'price', 'team_count', 'client_id', 'begin_at', 'closed_at', 'service_type', 'is_accepted']

    def get_csv_format(self):
        return [self.id, self.price, self.team_count, self.client.id, self.begin_at, self.closed_at, self.service_type,
                self.is_accepted]
