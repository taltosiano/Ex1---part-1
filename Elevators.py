class Elevators:
    elevatorsArray = []

    def __init__(self, building):
        for i in building['_elevators']:
            i['_currFloor'] = i['_minFloor']
            self.elevatorsArray.append(i)

    def print(self):
        for i in self.elevatorsArray:
            print(i)
