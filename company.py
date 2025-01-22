from event import ApplicationRejectedEvent
class Company:
    def __init__(self, name):
        self.name = name
    def reject_application(self, applicant_name, job_title, reason, queue):
        event = ApplicationRejectedEvent(applicant_name, job_title, reason)
        queue.publish(event)