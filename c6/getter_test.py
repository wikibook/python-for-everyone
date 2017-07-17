class Clock:
    def __init__(self, hour):
        self._hour = hour

    @property
    def hour(self):
        return self._hour

obj = Clock(11)
print(obj.hour)

