#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._stack: list[tuple[int, str]] = []
        self._count: int = 0
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def _send(self, item: str) -> None:
        self._stack.append((self._rank, item))
        self._count += 1
        self._rank += 1

    def output(self) -> tuple[int, str]:
        if not self._stack:
            raise IndexError("No data to output")
        return self._stack.pop(0)

    def stats(self) -> dict[str, int]:
        return {
            "processed": self._count,
            "pending": len(self._stack)
        }


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list) and len(data) > 0:
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._send(str(item))
        else:
            self._send(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list) and len(data) > 0:
            for item in data:
                if not isinstance(item, (str)):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, str):
            self._send(data)
        else:
            for item in data:
                self._send(item)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True

        if isinstance(data, list) and len(data) > 0:
            for item in data:
                if not isinstance(item, dict):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Ivalid log data")

        if isinstance(data, dict):
            data = [data]

        for item in data:
            log_str = f"{item.get('log_level')}: {item.get('log_message')}"
            self._send(log_str)


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            checked = False
            for process in self.processors:
                try:
                    if process.validate(data):
                        process.ingest(data)
                        checked = True
                        break
                except Exception as e:
                    print(f"Process Excption: {e}")
                    checked = True
                    break
            if not checked:
                print(f"DataStream error - Can't "
                      f"process element in stream:: {data}")

    def print_processors_stats(self) -> None:
        if len(self.processors) == 0:
            print("No processor found, no data")
            return
        for i, proc in enumerate(self.processors):
            name = proc.__class__.__name__
            name = name.replace("Processor", " Processor")
            stats = proc.stats()
            print(
                f"{name}: total {stats['processed']} items processed,"
                f"remaining {stats['pending']} on processor"
                )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)

    data_batch = [
        'Hello world',
        [3.14, -1, 2.71,],
        [{'log_level': 'WARNING', 'log_message':
          'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five', 'palmeiras', 'Rodrigo']
    ]

    print(f"Send first batch of data on stream: {data_batch}")
    stream.process_stream(data_batch)

    stream.print_processors_stats()

    print("\nRegistering other data processors")
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(txt_proc)
    stream.register_processor(log_proc)

    print("Send the same batch again")
    stream.process_stream(data_batch)

    stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors:"
        " Numeric 3, Text 2, Log 1"
        )
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        txt_proc.output()
    for _ in range(1):
        log_proc.output()

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
