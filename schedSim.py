import subprocess
import sys

algorithms = set(["RR", "SRTN", "FCFS"])

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 schedSim <file> -p <algorithm> [ -q <quantum>]")
        exit()
    filename = args[1]
    try:
        p_idx = args.index("-p")
    except ValueError:
        print("Usage: python3 schedSim <file> -p <algorithm> [ -q <quantum>]")
        exit()
    if p_idx == -1:
        print("Error: algorithm flag missing: -p <algorithm>")
        exit()
    algorithm = args[p_idx + 1]
    if algorithm not in algorithms:
        algorithm = "FCFS"
    if algorithm == "RR":
        try:
            q_idx = args.index("-q")
            quantum = args[q_idx + 1]
        except ValueError:
            print("Usage: python3 schedSim <file> -p <algorithm> [ -q <quantum>]")
            exit()

        subprocess.run(["python3", "main.py", filename, algorithm, quantum])
    else:
        subprocess.run(["python3", "main.py", filename, algorithm])

if __name__ == "__main__":
    main()