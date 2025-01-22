from Comminication_queue import CommunicationQueue # type: ignore
from applicant_submitted_event import Applicant
from applicant_rejected_event import Company

def main():
    queue = CommunicationQueue()

    applicant = Applicant("Mehmet")
    company = Company("Muzik company")

    applicant.apply_for_job("Software Engineer", company, queue)

    company.reject_application(applicant.name, "Software Engineer", "Position filled", queue)
    
    queue.process()

if __name__ == "__main__":
    main()