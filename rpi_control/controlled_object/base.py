class ControlledMeta(type):
    def __new__(cls, name, bases, dic):
        if 'is_controllable' not in dic:
            dic['is_controllable'] = True
        return super().__new__(cls, name, bases, dic)

class RaspObject(metaclass=ControlledMeta):
    def __init__(self, channel):
        self.channel = channel

    def __call__(self):
        pass