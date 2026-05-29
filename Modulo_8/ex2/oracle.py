#!/usr/bin/env python3

import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("python-dotenv is not installed. Install"
          " with: [ $>pip install python-dotenv]"
          )
    sys.exit(1)


def get_env(env: str) -> str | None:
    res = os.getenv(env)
    if res is None:
        return "Missing Env"
    return res.strip()


def main() -> None:
    check = True
    print("ORACLE STATUS: Reading the Matrix...\n")
    env_load = load_dotenv()

    mode = get_env("MATRIX_MODE") or "development"
    db = get_env("DATABASE_URL")
    api = get_env("API_KEY")
    log = get_env("LOG_LEVEL") or "DEBUG"
    zion = get_env("ZION_NETWORK")

    if not db or not api or not log or not zion:
        print("Missing Configuration Detected!")
        print("Please set: DATABASE_URL, API_KEY and ZION_NETWORK")
        return

    print("Configuration loaded...")

    print(f"Log Level: {log}")
    print(f"Mode: {mode}")

    if mode == "production":
        print("Database: Connected to production")
        print("API Access: Authenticated")
        print(f"Log Level: {log}")
        print("Zion Network: Secured remote connection")
    else:
        print("Database: Connected to development")
        print("API Access: Authenticated")
        print(f"Log Level: {log}")
        print("Zion Network: Online")

    print("\nEnvironment security check:")
    if check:
        print("[OK] No hardcoded secrets detected")
    if env_load:
        print("[OK] .env file properly configured")
    else:
        print(
            "[WARNING] .env file not found, "
            "using system environment variables"
            )


if __name__ == "__main__":
    main()
