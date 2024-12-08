from utils import time_context


def increment(counter, num):
    for _ in range(num):
        counter["value"] += 1


counter = {"value": 0}

with time_context():
    increment(counter, 100_000_000)

print(f"Final counter value: {counter['value']}")