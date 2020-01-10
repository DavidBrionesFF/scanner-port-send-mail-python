import csv

class ContextApplication:
    port_context = 0

    def __init__(self):
        self.file_data = "templates/application.properties"
        self.load_data()

    def load_data(self):
        file = open(self.file_data, "r")
        self.data = []

        for line in file.readlines():
            self.data.append(line)
        self.data

    def getPropertie(self, name_prop):
        for line in self.data:
            if line.split("=")[0] == name_prop:
                return line.split("=")[1].rstrip('\n')

appContext = ContextApplication()

def getHosts():
    data = []
    file = open('templates/hosts', 'r')
    for line in file.readlines():
        data.append(str(line))
    return data