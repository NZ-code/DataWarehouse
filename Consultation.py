from Employee import Employee
from Contract import Contract

class Consultation:
    idGen = 0

    def __init__(self, duration, hourly_rate, employee: Employee, contract: Contract, date):
        Consultation.idGen += 1
        self.id = self.idGen
        self.duration = duration
        self.hourly_rate = hourly_rate
        self.employee = employee
        self.contract = contract
        self.date = date

    def __str__(self):
        return "Consultation( id:" + str(self.id) + ", duration:" + str(self.duration) + ", hourly_rate:" + str(
            self.hourly_rate) + ", " + str(self.employee) + ", " + str(self.contract) + ", date:" + str(self.date) + ")"

    def __repr__(self):
        return str(self)
