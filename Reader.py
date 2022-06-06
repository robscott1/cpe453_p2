from Job import Job


class Reader:

    def __init__(self, filename: str):
        self.filename = filename

    def get_jobs(self) -> list:
        jobs = list()
        with open(self.filename, 'r') as f:
            line = f.readline()
            process_number = 0
            while line:
                job = Job(process_number, *line.split(" "))
                jobs.append(job)
                line = f.readline()
                process_number += 1

        return jobs
