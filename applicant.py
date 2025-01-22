from application_submitted_event import ApplicationSubmittedEvent # type: ignore

class Applicant:
    def __init__(self, name):
        self.name = name

    def apply_for_job(self, job_title, company, queue):
        event = ApplicationSubmittedEvent(self.name, job_title)
        queue.publish(event)
