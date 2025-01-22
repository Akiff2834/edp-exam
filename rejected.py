from event import Event

class ApplicationRejectedEvent(Event):
    def __init__(self, application_name, job_title, reason):
        payload = {"application_name": application_name, "job_title": job_title, "reason": reason}
        super().__init__(payload)