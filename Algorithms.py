"""
Algorithms

These will decide the next job, as well as how long
the processor should relinquish the CPU
"""
from AlgorithmArgs import AlgorithmArgs
from Job import Job

"""
FIFO

Selects the job that has the lowest arrival time.
Maybe algorithm tells processor how long to process based on
what the protocol is.
"""


def first_in_first_out(args: AlgorithmArgs):
    job: Job = min(args.jobs, key=lambda x: x.arrival_time)
    t2c = job.burst
    args.jobs.remove(job)
    job.mark_as_complete()
    return job, t2c


"""
Round Robin

Takes all processes waiting and equally distributes CPU to each
- program uses rr_visits to find the procs that need CPU time
"""


def round_robin(args: AlgorithmArgs):
    available_jobs = sorted(list(filter(lambda x: x.arrival_time <= args.current_time, args.jobs)),
                            key=lambda x: x.arrival_time)
    job = min(available_jobs, key=lambda x: x.rr_visits())
    job.increment_rr_visits()
    if job.cpu_time + args.quantum >= job.burst:
        job.mark_as_complete()
        t2c = job.burst - job.cpu_time if job.cpu_time + args.quantum > job.burst else args.quantum
        job.cpu_time += t2c
        args.jobs.remove(job)
        return job, t2c
    job.cpu_time += args.quantum
    return job, args.quantum


"""
Shortest job remaining next

Can preempt any other threads once it has a shorter remaining time than
another thread. This algorithm takes the decision process one quantum at
a time-- it will reevaluate to see if there is a new process that is 
eligible to start or if it is still the shortest.

Most relevant scenario is when a new process is launched and it is very short.
"""


def shortest_job_next(args: AlgorithmArgs):
    available_jobs = list(filter(lambda x: x.arrival_time <= args.current_time, args.jobs))
    if not available_jobs:
        return False, 1
    job: Job = min(available_jobs, key=lambda x: x.burst - x.cpu_time)
    job.cpu_time += 1
    if job.cpu_time == job.burst:
        job.mark_as_complete()
        args.jobs.remove(job)

    return job, 1
