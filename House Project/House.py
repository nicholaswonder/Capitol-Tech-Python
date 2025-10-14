class House:
    def __init__(self, door: bool, window: bool):
        self.DoorOpen = door
        self.WindowOpen = window

    def SetDoor(self, door: bool):
        self.DoorOpen = door

    def SetWindow(self, window: bool):
        self.WindowOpen = window

    def GetDoor(self):
        return self.DoorOpen

    def GetWindow(self):
        return self.WindowOpen