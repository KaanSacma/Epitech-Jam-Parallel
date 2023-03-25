class State:
    def __init__(self, name):
        self._name = name

    def get(self):
        if self._name == "Static":
            return 0
        elif self._name == "onHover":
            return 1
        elif self._name == "onClick":
            return 2
        else:
            return 0

    def name(self, new_name):
        self._name = new_name
