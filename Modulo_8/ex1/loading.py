#!/usr/bin/env python3

import sys
from importlib import import_module


def check_libraries(name: str) -> str | None:
    try:
        module = import_module(name)
        return (f"{module, '__version__', 'unknown'}")
    except ImportError:
        return None


def install_intruction() -> None:
    print("===================================")
    print("There is a missing libary:")
    print("For install with pip:")
    print(" $> pip install requariments.txt")
    print("For install with Poetry:")
    print(" $> poetry install")
    print(" $> poetry run python loading.py")
    print("===================================")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    libraries_to_check = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical ncomputation ready",
        "requests": "Network access ready",
        "matplotlib": "Vizualization ready",
    }
    missing = []
    print("Checking dependencies:")
    for lib, value in libraries_to_check.items():
        version = check_libraries(lib)
        if version is not None:
            print(f"[OK] {lib} ({version}) - {value}")
        else:
            missing.append(lib)

    if missing:
        install_intruction()
        sys.exit(1)

    import numpy as np
    import pandas as pd
    from matplotlib import pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    gen = np.random.randint(1000, dtype=int, size=1000)

    print("\n===== DATAFRAME ORGANIZATION =====")
    stream = pd.DataFrame(gen)
    print(stream)
    print("==================================")

    plt.figure(figsize=(16, 8))
    plt.plot(stream)
    plt.savefig("matrix_analysis.png")


if __name__ == "__main__":
    main()
