class Event:
    def __init__(self, payload):
        self.payload = payload

class ApplicationSubmittedEvent(Event):
    def __init__(self, application_name, job_title):
        payload = {"application_name": application_name, "job_title": job_title}
        super().__init__(payload)

class ApplicationRejectedEvent(Event):
    def __init__(self, application_name, job_title, reason):
        payload = {"application_name": application_name, "job_title": job_title, "reason": reason}
        super().__init__(payload)

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

class Applicant:
    def __init__(self, name):
        self.name = name

    def apply_for_job(self, job_title, company, queue):
        event = ApplicationSubmittedEvent(self.name, job_title)
        queue.publish(event)

class Company:
    def __init__(self, name):
        self.name = name

    def reject_application(self, applicant_name, job_title, reason, queue):
        event = ApplicationRejectedEvent(applicant_name, job_title, reason)
        queue.publish(event)
