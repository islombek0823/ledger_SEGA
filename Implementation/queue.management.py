from collections import deque


class QueueManager:

    def _init_(self):
        self.jobs = deque()
        self.job_id = 1

    # Add a new job
    def add_job(self, job_name):
        job = {
            "id": self.job_id,
            "name": job_name,
            "status": "Pending"
        }

        self.jobs.append(job)
        self.job_id += 1

        print("Job added successfully:", job)

    # Get the next job
    def get_next_job(self):
        if self.jobs:
            job = self.jobs.popleft()
            job["status"] = "Running"
            print("Processing job:", job)
            return job

        print("Queue is empty!")
        return None

    # Display all pending jobs
    def show_queue(self):
        print("\nCurrent Queue:")

        for job in self.jobs:
            print(job)


# Test Queue Management
if _name_ == "_main_":

    queue = QueueManager()

    queue.add_job("Job 1")
    queue.add_job("Job 2")
    queue.add_job("Job 3")

    queue.show_queue()

    queue.get_next_job()

    queue.show_queue()
