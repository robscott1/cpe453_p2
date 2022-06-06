class Job:

    def __init__(self, pid: int, arrival_time: str, burst: str):
        self.pid = pid
        self.arrival_time = int(arrival_time.strip())
        self.burst = int(burst.strip())
        self.waiting = True
        self._complete = False
        self.completion_time = 0
        self._rr_visits = 0
        self.cpu_time = 0

    def is_complete(self):
        return self._complete

    def mark_as_complete(self):
        self._complete = True

    def wait_time(self):
        return self.turnaround_time() - self.burst

    def turnaround_time(self):
        return self.completion_time - self.arrival_time

    def rr_visits(self):
        return self._rr_visits

    def increment_rr_visits(self):
        self._rr_visits += 1

