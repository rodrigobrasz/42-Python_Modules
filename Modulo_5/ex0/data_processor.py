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

    def output(self) -> tuple[int, str]:
        if not self._stack:
            raise IndexError("No data to output")
        return self._stack.pop(0)


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
                self._rank += 1
                self._stack.append((self._rank, str(item)))
                self._count += 1
        else:
            self._rank += 1
            self._stack.append((self._rank, str(data)))
            self._count += 1


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
            self._rank += 1
            self._stack.append((self._rank, data))
            self._count += 1
        else:
            for item in data:
                self._rank += 1
                self._stack.append((self._rank, item))
                self._count += 1


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
            self._rank += 1
            self._stack.append((self._rank, log_str))
            self._count += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing NumericProcessor...")
    num = NumericProcessor()
    num_valid = 42
    n_invalid = "Hello"
    print(f"Trying to validate input '{num_valid}':", num.validate(num_valid))
    print(f"Trying to validade inpuy '{n_invalid}':", num.validate(n_invalid))
    print("Test invalid ingestion of string 'foo' without prior validation:")

    try:
        num.ingest("foo")
    except ValueError as e:
        print(f"Got a exception: {e}")

    num_data: list[int | float] = [1, 2, 3, 4, 5]
    num.ingest(num_data)
    print(f"Processing data{num_data}")
    print("Extraction 3 values...")
    for _ in range(3):
        rank, string = num.output()
        print(f"Numeric value {rank}: {string}")

    print("\nTesting TextProcessor...")
    text = TextProcessor()
    t_invalid = 42
    t_valid: list = [
        "Hello",
        "Nexus",
        "World",
    ]
    print(f"Trying to validate input: {t_invalid}:", text.validate(t_invalid))
    print(f"Processing data: {t_valid}")

    print("Extracting 1 Value...")
    text.ingest(t_valid)
    r, s = text.output()
    print(f"Text value {r}: {s}")

    print("\nTesting LogProcessor...")
    log = LogProcessor()
    l_invalid = 42
    l_valid: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Trying to validate input {l_invalid}:", log.validate(l_invalid))

    log.ingest(l_valid)
    print("Extracting 2 values...")
    for _ in range(2):
        r, s = log.output()
        print(f"Log entry {r}: {s}")


if __name__ == "__main__":
    main()
