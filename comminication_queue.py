class CommunicationQueue:
    def __init__(self):
        self.queue = []
    def publish(self, event):
        self.queue.append(event)
        print(f"Event published: {event.__class__.__name__} with payload: {event.payload}")
    def process(self):
        while self.queue:
            event = self.queue.pop(0)
            print(f"Processing event: {event.__class__.__name__} with payload: {event.payload}")
            