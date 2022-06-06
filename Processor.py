from Reader import Reader
from Scheduler import Scheduler


class Processor:

    def __init__(self, reader: Reader, scheduler: Scheduler):
        self.reader = reader
        self.scheduler = scheduler
        self.time_elapsed = 0
        self.jobs = self.reader.get_jobs()
        self.completed_jobs = []

    def process(self):
        jobs = self.jobs
        while jobs:
            job, time = self.scheduler.next_job(jobs, self.time_elapsed)
            self.time_elapsed += time
            if job and job.is_complete():
                self.completed_jobs.append(job)
                job.completion_time = self.time_elapsed

        for job in sorted(self.completed_jobs, key=lambda x: x.pid):
            print(f"Job {job.pid}: "
                  f"Wait -> {job.wait_time()}; "
                  f"Turnaround -> {job.turnaround_time()}; ")

        self.calculate_averages()

    def calculate_averages(self):
        wait_times = [x.wait_time() for x in self.completed_jobs]
        average_wait = sum(wait_times) / len(wait_times)
        turnaround_times = [x.turnaround_time() for x in self.completed_jobs]
        average_turnaround = sum(turnaround_times) / len(turnaround_times)
        print(f"Average Turnaround: {average_turnaround}\n"
              f"Average Wait: {average_wait}")
