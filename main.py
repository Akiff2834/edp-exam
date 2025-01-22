from comminication_queue import CommunicationQueue
from applicant import Applicant
from company import Company
def main():
    queue = CommunicationQueue()
    # Create applicant and company
    applicant = Applicant("John Doe")
    company = Company("Tech Corp")
    # Applicant applies for a job
    applicant.apply_for_job("Software Engineer", company, queue)
    # Company rejects the application
    company.reject_application(applicant.name, "Software Engineer", "Position filled", queue)
    # Process all events in the queue
    queue.process()
if __name__ == "__main__":
    main()