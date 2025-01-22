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