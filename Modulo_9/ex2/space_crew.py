#!/usr/bin/env python3

from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> "SpaceMission":
        errors = []
        if not self.mission_id.startswith("M"):
            errors.append("Mission ID must start with 'M'")

        leader = False
        for i in self.crew:
            if i.rank in (Rank.commander, Rank.captain):
                leader = True
            if not leader:
                errors.append("Must have at least one commander or captain")

        num_experienced = 0
        for cm in self.crew:
            if cm.years_experience >= 5:
                num_experienced += 1
        if num_experienced < (len(self.crew) + 1) // 2:
            errors.append(
                          "For missions longer than 365 days, at least 50%"
                          " of the crew must h  ave 5+ years of experience."
                          )

        for cm in self.crew:
            if not cm.is_active:
                errors.append("All crew members must be active.")
                break

        if errors:
            raise ValueError("; ".join(errors))
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    try:
        validate = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            launch_date=datetime.today(),
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C00001",
                    name="Sarah",
                    rank="commander",
                    age=45,
                    specialization="Mission Commander",
                    years_experience=20,
                ),
                CrewMember(
                    member_id="C00002",
                    name="Arthur",
                    rank="captain",
                    age=35,
                    specialization="Navigator",
                    years_experience=7,
                ),
                CrewMember(
                    member_id="C00003",
                    name="Alice",
                    rank="officer",
                    age=32,
                    specialization="Novice",
                    years_experience=4,
                ),
            ],
        )
        print("=========================================")
        print("Valid mission created:")
        print(f"Mission: {validate.mission_name}")
        print(f"ID: {validate.mission_id}")
        print(f"Destination: {validate.destination}")
        print(f"Duration: {validate.duration_days}")
        print(f"Budget: {validate.budget_millions}")
        print("Crew members:")
        for person in validate.crew:
            print(f"- {person.name} ({person.rank}) - {person.specialization}")
    except ValidationError as e:
        for err in e.errors():
            print("-", err['msg'])
    print("=========================================\n")

    print("Invalid Mission:")
    try:
        validate = SpaceMission(
            mission_name="Solo Exploration",
            mission_id="M2025_SOLO",
            destination="Venus",
            launch_date=datetime.today(),
            duration_days=500,
            budget_millions=900.0,
            crew=[
                CrewMember(
                    member_id="C10001",
                    name="Bob",
                    rank="officer",
                    age=33,
                    specialization="Comms",
                    years_experience=2,
                ),
                CrewMember(
                    member_id="C10002",
                    name="Gloria",
                    rank="commander",
                    age=29,
                    specialization="Pilot",
                    years_experience=15,
                ),
                CrewMember(
                    member_id="C00003",
                    name="Alice",
                    rank="officer",
                    age=32,
                    specialization="Novice",
                    years_experience=25,
                ),
            ],
        )
    except ValidationError as e:
        for err in e.errors():
            print("-", err['msg'])


if __name__ == "__main__":
    main()
