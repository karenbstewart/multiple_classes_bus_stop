class BusStop:
    def __init__(self, input_bus_stop_name):
        self.name = input_bus_stop_name
        self.queue = []

    def add_to_queue(self, person):
        self.queue.append(person)

    def queue_length(self):
        return len(self.queue)

    def clear(self):
        self.queue.clear()


