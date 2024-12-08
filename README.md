# Kill GIL

This project accompanies my talk at [PyCon Wrocław 2024](https://www.pyconwroclaw.com/), titled **"Kill GIL: How Python 3.13 Changes Concurrent Programming"**. It benchmarks dummy CPU-bound tasks to compare performance with and without the Global Interpreter Lock (GIL) in Python 3.13.

- **Presentation slides**: [Link](https://docs.google.com/presentation/d/1hvnMgj0W6hUq1CkNNbYi5CjQBFqC8R1E2h-ExEUMrs4/edit?usp=sharing)
- **Presentation recording**: TBD

## Prerequisites

- `uv`
- `python3.13t`

## Execution

### With GIL

```sh
PYTHON_GIL=1 uv run <script>.py
```

### Without GIL

```sh
PYTHON_GIL=0 uv run <script>.py
```

### Using the Script
Alternatively, use the included script to run both benchmarks:

```sh
./run.sh
```

## Results

The results of the benchmark vary not only between machines but also between runs. This is because it is up to the operating system to decide which CPU core a thread should be assigned to. However, the key takeaways from the presentation remain the same:

1. GIL prevents any parallelization of CPU-bound tasks, making it impossible to improve performance using threads.

2. Threads with frequent access to shared memory do not scale well.

### With GIL

```sh
===== Running single_thread.py =====
Execution time: 6.459282 seconds
Final counter value: 100000000
===== Finished  =====


===== Running multi_thread_share.py =====
Execution time: 6.744378 seconds
Final counter value: 100000000
===== Finished  =====


===== Running multi_thread_share_lock.py =====
Execution time: 23.893897 seconds
Final counter value: 100000000
===== Finished  =====


===== Running multi_thread_private.py =====
Execution time: 6.728547 seconds
Final counter value: 100000000
===== Finished  =====
```

### Without GIL
```sh
===== Running single_thread.py =====
Execution time: 6.473970 seconds
Final counter value: 100000000
===== Finished  =====


===== Running multi_thread_share.py =====
Execution time: 10.617835 seconds
Final counter value: 11665934
===== Finished  =====


===== Running multi_thread_share_lock.py =====
Execution time: 175.884980 seconds
Final counter value: 100000000
===== Finished  =====


===== Running multi_thread_private.py =====
Execution time: 1.605419 seconds
Final counter value: 100000000
===== Finished  =====
```

## Code Images

- [Bytcode instructions of the increment function](https://www.ray.so/#title=pycon.py&background=false&padding=16&theme=clerk&language=python&code=TE9BRF9GQVNUICAgICAgICAgICAgICAgIDAgKGNvdW50ZXIpCkxPQURfQ09OU1QgICAgICAgICAgICAgICAxICgndmFsdWUnKQpDT1BZICAgICAgICAgICAgICAgICAgICAgMgpDT1BZICAgICAgICAgICAgICAgICAgICAgMgpCSU5BUllfU1VCU0NSCkxPQURfQ09OU1QgICAgICAgICAgICAgICAyICgxKQpCSU5BUllfT1AgICAgICAgICAgICAgICAxMyAoKz0pClNXQVAgICAgICAgICAgICAgICAgICAgICAzClNXQVAgICAgICAgICAgICAgICAgICAgICAyClNUT1JFX1NVQlNDUgpKVU1QX0JBQ0tXQVJEICAgICAgICAgICAxOCAodG8gTDEp&width=520)
- [Single Thread Execution](https://www.ray.so/#title=pycon.py&background=false&padding=16&theme=clerk&language=python&code=ZGVmIGluY3JlbWVudChjb3VudGVyLCBudW0pOgogICAgZm9yIF8gaW4gcmFuZ2UobnVtKToKICAgICAgICBjb3VudGVyWyJ2YWx1ZSJdICs9IDEKCmNvdW50ZXIgPSB7InZhbHVlIjogMH0KaW5jcmVtZW50KGNvdW50ZXIsIDEwMF8wMDBfMDAwKQ)
- [Multi-Thread w/ Shared Memory Execution](https://www.ray.so/#title=pycon.py&background=false&padding=16&theme=clerk&language=python&code=ZGVmIGluY3JlbWVudChjb3VudGVyLCBudW0pOgogICAgZm9yIF8gaW4gcmFuZ2UobnVtKToKICAgICAgICBjb3VudGVyWyJ2YWx1ZSJdICs9IDEKCm51bV90aHJlYWRzID0gb3MuY3B1X2NvdW50KCkKY291bnRlciA9IHsidmFsdWUiOiAwfQoKdGhyZWFkcyA9IFsKICAgIHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWluY3JlbWVudCwgYXJncz0oY291bnRlciwgMTAwXzAwMF8wMDAgLy8gbnVtX3RocmVhZHMpKQogICAgZm9yIF8gaW4gcmFuZ2UobnVtX3RocmVhZHMpCl0KZm9yIHRocmVhZCBpbiB0aHJlYWRzOiB0aHJlYWQuc3RhcnQoKQ&darkMode=true&width=null)
- [Multi-Thread w/ Shared w/ Lock Execution](https://www.ray.so/#title=pycon.py&background=false&padding=16&theme=clerk&language=python&code=bG9jayA9IHRocmVhZGluZy5Mb2NrKCkKCmRlZiBpbmNyZW1lbnQoY291bnRlciwgbnVtKToKICAgIGZvciBfIGluIHJhbmdlKG51bSk6CiAgICAgICAgd2l0aCBsb2NrOgogICAgICAgICAgICBjb3VudGVyWyJ2YWx1ZSJdICs9IDEKCm51bV90aHJlYWRzID0gb3MuY3B1X2NvdW50KCkKY291bnRlciA9IHsidmFsdWUiOiAwfQoKdGhyZWFkcyA9IFsKICAgIHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWluY3JlbWVudCwgYXJncz0oY291bnRlciwgMTAwXzAwMF8wMDAgLy8gbnVtX3RocmVhZHMpKQogICAgZm9yIF8gaW4gcmFuZ2UobnVtX3RocmVhZHMpCl0KZm9yIHRocmVhZCBpbiB0aHJlYWRzOiB0aHJlYWQuc3RhcnQoKQ&darkMode=true&width=null)
- [Multi-Thread w/ Private Memory Execution](https://www.ray.so/#title=pycon.py&background=false&padding=16&theme=clerk&language=python&code=ZGVmIGluY3JlbWVudChjb3VudGVyLCBudW0pOgogICAgZm9yIF8gaW4gcmFuZ2UobnVtKToKICAgICAgICBjb3VudGVyWyJ2YWx1ZSJdICs9IDEKCm51bV90aHJlYWRzID0gb3MuY3B1X2NvdW50KCkKY291bnRlcnMgPSBbeyJ2YWx1ZSI6IDB9IGZvciBfIGluIHJhbmdlKG51bV90aHJlYWRzKV0KCnRocmVhZHMgPSBbCiAgICB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1pbmNyZW1lbnQsIGFyZ3M9KGNvdW50ZXIsIDEwMF8wMDBfMDAwIC8vIG51bV90aHJlYWRzKSkKICAgIGZvciBjb3VudGVyIGluIGNvdW50ZXJzCl0KZm9yIHRocmVhZCBpbiB0aHJlYWRzOiB0aHJlYWQuc3RhcnQoKQ&darkMode=true&width=null)
- [python 3.13t installation](https://www.ray.so/#title=pycon.py&background=false&padding=16&theme=clerk&language=shell&code=IyBpbnN0YWxsYXRpb24gCnB5ZW52IGluc3RhbGwgMy4xM3QKCiMgY2hlY2sgaWYgR0lMIGVuYWJsZWQKcHl0aG9uCj4-PiBpbXBvcnQgc3lzCj4-PiBzeXMuX2lzX2dpbF9lbmFibGVkKCkKCiMgcnVuIHcvbyBHSUwKUFlUSE9OX0dJTD0wIHB5dGhvbiBmb28ucHk&darkMode=true&width=null)