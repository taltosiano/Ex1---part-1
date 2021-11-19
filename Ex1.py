import json
import csv
import sys
import random
from Elevators import Elevators
if __name__ == "__main__":
    building_file = open(sys.argv[1],)
    calls_file = open(sys.argv[2],)
    output_file = open(sys.argv[3], 'w', newline='')

    building_str = json.load(building_file)
    calls_list = list(csv.reader(calls_file, delimiter=','))
    output_str = csv.writer(output_file)
    elevator = Elevators(building_str)
    workload = len(elevator.elevatorsArray)
    while calls_list:
        for i in elevator.elevatorsArray:
            for j in range(workload):
                while calls_list and (int(calls_list[0][2]) < i['_minFloor'] or int(calls_list[0][3])<i['_minFloor'] or int(calls_list[0][2]) > i['_maxFloor'] or int(calls_list[0][3]) > i['_maxFloor']):
                    calls_list.pop(0)

                if calls_list:
                    calls_list[0][5] = i['_id']
                    output_str.writerow(calls_list.pop(0))
