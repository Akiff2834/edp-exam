from event import Event

class ApplicationSubmittedEvent(Event):
    def __init__(self, application_name, job_title):
        payload = {"application_name": application_name, "job_title": job_title}
        super().__init__(payload)
