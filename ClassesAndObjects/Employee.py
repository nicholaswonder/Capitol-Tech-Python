class Employee:
    def __init__(self, name: str, id: int, department: str, title: str):
        self.name = name
        self.id = id
        self.department = department
        self.title = title

    def GetName(self):
        return self.name

    def SetName(self, name: str):
        self.name = name

    def GetId(self):
        return self.id

    def SetId(self, id: int):
        if id > 0:
            self.id = id

    def GetDep(self):
        return self.department

    def SetDep(self, department: str):
        self.department = department

    def GetTitle(self):
        return self.title

    def SetTitle(self, title: str):
        self.title = title