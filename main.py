class Event:
    def __init__(self, payload):
        self.payload = payload

from event import Event

class ApplicationSubmittedEvent(Event):
    def __init__(self, application_name, job_title):
        payload = {"application_name": application_name, "job_title": job_title}
        super().__init__(payload)


from event import Event

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

from application_submitted_event import ApplicationSubmittedEvent

class Applicant:
    def __init__(self, name):
        self.name = name

    def apply_for_job(self, job_title, company, queue):
        event = ApplicationSubmittedEvent(self.name, job_title)
        queue.publish(event)

from application_rejected_event import ApplicationRejectedEvent

class Company:
    def __init__(self, name):
        self.name = name

    def reject_application(self, applicant_name, job_title, reason, queue):
        event = ApplicationRejectedEvent(applicant_name, job_title, reason)
        queue.publish(event)


 

from communication_queue import CommunicationQueue
from applicant import Applicant
from company import Company

def main():
    queue = CommunicationQueue()

    applicant = Applicant("Mehmet")
    company = Company("Muzik company")

    applicant.apply_for_job("Software Engineer", company, queue)

    company.reject_application(applicant.name, "Software Engineer", "Position filled", queue)

    queue.process()

if __name__ == "__main__":
    main()