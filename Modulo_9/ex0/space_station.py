#!/usr/bin/env python3

import sys
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=30)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True


def main() -> None:

    print("Space Station Data Validation")
    print("========================================")
    try:
        validation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=10,
            power_level=85.5,
            oxygen_level=10.3,
            last_maintenance=datetime.today(),
            is_operational=True,
        )
    except ValidationError:
        print("Error!!")
        sys.exit()

    print(f"ID: {validation.station_id}")
    print(f"Name: {validation.name}")
    print(f"Crew: {validation.crew_size} people")
    print(f"Power: {validation.power_level}%")
    print(f"Oxygen: {validation.oxygen_level}%")
    if validation.is_operational:
        print("Status: Operational")
    else:
        print("nao")
    print(f"{validation.last_maintenance}")
    print("========================================")

    print("Expected validation error:")
    try:
        validation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=100,
            power_level=85.5,
            oxygen_level=10.3,
            last_maintenance=datetime.today(),
            is_operational=True,
        )
    except ValidationError as e:
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
