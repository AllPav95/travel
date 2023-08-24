import json

class TripPlanner:
    def __init__(self):
        self.trip_data = {
            'route': [],
            'tickets': [],
            'packing_list': [],
            'budget': 0
        }

    def add_location(self, name, geo_location):
        self.trip_data['route'].append({'name': name, 'geo_location': geo_location})

    def add_ticket(self, name, details, ticket_type):
        self.trip_data['tickets'].append({'name': name, 'details': details, 'type': ticket_type})

    def add_item_to_packing_list(self, item):
        self.trip_data['packing_list'].append(item)

    def set_budget(self, budget):
        self.trip_data['budget'] = budget

    def export_trip(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.trip_data, file, indent=4)

    def import_trip(self, filename):
        with open(filename, 'r') as file:
            self.trip_data = json.load(file)


trip_planner = TripPlanner()

trip_planner.add_location("Днепр", "49.8193,° N, 24.0602° E")
trip_planner.add_location("Киев", "50.44901° N, 30.5165° E")

trip_planner.add_ticket("Билет на поезд", "Поезд Днепр-Киев", "поезд")
trip_planner.add_ticket("Билет на автобус", "поездка", "работа")

trip_planner.add_item_to_packing_list("сумка")
trip_planner.add_item_to_packing_list("ноут")

trip_planner.set_budget(3000)

trip_planner.export_trip("trip.json")


trip_planner.import_trip("trip.json")

print(trip_planner.trip_data)