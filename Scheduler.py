from AlgorithmArgs import AlgorithmArgs


class Scheduler:

    def __init__(self, algorithm, quantum=1):
        self.algorithm = algorithm
        self.quantum = quantum

    def next_job(self, jobs: list, current_time: int):
        args = AlgorithmArgs(jobs, current_time, self.quantum)
        return self.algorithm(args)
