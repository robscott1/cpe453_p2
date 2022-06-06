import sys

from Algorithms import first_in_first_out, round_robin, shortest_job_next
from Processor import Processor
from Reader import Reader
from Scheduler import Scheduler

algorithms = {
    "RR": round_robin,
    "SRTN": shortest_job_next,
    "FCFS": first_in_first_out
}

def main():
    reader = Reader(sys.argv[1])
    algorithm = algorithms[sys.argv[2]]
    scheduler_args = [algorithm]

    if sys.argv[2] == "RR":
        scheduler_args.append(int(sys.argv[3]))

    scheduler = Scheduler(*scheduler_args)

    processor = Processor(reader, scheduler)
    processor.process()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
