
class Client:
    idGen = 0

    def __init__(self, name):
        Client.idGen += 1
        self.id = self.idGen
        self.name = name

    def __str__(self):
        return "Client( id:" + str(self.id) + ", name:" + str(self.name) + ")"

    def __repr__(self):
        return str(self)