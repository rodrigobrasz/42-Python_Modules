#!/usr/bin/env python3

from typing import Generator
import random

actions = [
    "run",
    "eat",
    "grab",
    "sleep",
    "swin",
    "move",
    "realease",
    "climb",
]

players = [
    "Alice",
    "Bob",
    "Carlos",
    "Jessica",
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        choose_action = random.choice(actions)
        choose_name = random.choice(players)
        yield (choose_action, choose_name)


def consume_event(events: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    events10 = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {events10}")

    for ev in consume_event(events10):
        print(f"Got event from list: {ev}")
        print(f"Remains in list: {events10}")


if __name__ == "__main__":
    main()
