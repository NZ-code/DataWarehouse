from typing import List

import Contract

class Employee:
    idGen = 0

    def __init__(self, name, hire_date, fire_date):
        Employee.idGen += 1
        self.id = self.idGen
        self.name = name
        self.hire_date = hire_date
        self.fire_date = fire_date
        self.contracts = []

    def add_contract(self, contract: Contract):
        self.contracts.append(contract)

    def __str__(self):
        return "Employee( id:" + str(self.id) + ", name:" + str(self.name) + ", hire_date:" + str(
            self.hire_date) + ", fire_date:" + str(self.fire_date)+")"

    def __repr__(self):
        return str(self)