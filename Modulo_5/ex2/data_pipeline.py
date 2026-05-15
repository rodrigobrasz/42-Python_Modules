#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVOutput:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        output_str = ""
        for x in data:
            output_str += f"{x[1]},"
        output_str = output_str.rstrip(",")
        print("CSV Output")
        print(f"{output_str}")


class JsonOutput:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        output_str = ""
        for x in data:
            output_str += f"\"item_{x[0]}\": {x[1]}, "
        output_str = output_str.rstrip(", ")
        print("Json Output")
        print(f"{{{output_str}}}")


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
        if len(self._stack) == 0:
            print("No data to output")
            return
        if not self._stack:
            raise IndexError("No data to output")
        return self._stack.pop(0)

    def _send(self, element: str) -> None:
        self._stack.append((self._count, element))
        self._count += 1

    def stats(self) -> tuple[str, int]:
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
    def __init__(self):
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for process in self.processors:
            pipeline_output = []
            for _ in range(nb):
                if len(process._stack) > 0:
                    pipeline_output.append(process.output())
                else:
                    break

            if pipeline_output:
                plugin.process_output(pipeline_output)


def main() -> None:
    print("\n=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    dt = DataStream()

    print("\n== DataStream statistics ==\n")
    dt.print_processors_stats()

    print("Registering Processors")
    number = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    dt.register_processor(number)
    dt.register_processor(txt)
    dt.register_processor(log)

    batch_1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message':
          'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
        42,
        ['Hi', 'five']
        ]
    print(f"Send first batch of data on stream: {batch_1}")
    dt.process_stream(batch_1)

    print("\n== DataStream statistics ==\n")
    dt.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVOutput()
    dt.output_pipeline(3, csv_plugin)

    print("\n== DataStream statistics ==\n")
    dt.print_processors_stats()

    batch_2 = [
            21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                {'log_level': 'NOTICE', 'log_message':
                  'Certificate expires in 10 days'}],
            [32, 42, 64, 84, 128, 168], 'World hello'
                ]
    print(f"Send another batch of data: {batch_2}")
    dt.process_stream(batch_2)

    print("\n== DataStream statistics ==\n")
    dt.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JsonOutput()
    dt.output_pipeline(5, json_plugin)

    print("\n== DataStream statistics ==\n")
    dt.print_processors_stats()

if __name__ == "__main__":
    main()
