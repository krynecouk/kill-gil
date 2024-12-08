import os
import threading

from utils import time_context


def increment(counter, num):
    for _ in range(num):
        counter["value"] += 1


num_threads = os.cpu_count()
counter = {"value": 0}

with time_context():
    threads = [
        threading.Thread(target=increment, args=(counter, 100_000_000 // num_threads))
        for _ in range(num_threads)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

print(f"Final counter value: {counter['value']}")
