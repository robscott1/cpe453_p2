class AlgorithmArgs:

  def __init__(self, jobs: list, current_time: int, quantum=None):
    self.jobs = jobs
    self.current_time = current_time
    self.quantum = quantum

