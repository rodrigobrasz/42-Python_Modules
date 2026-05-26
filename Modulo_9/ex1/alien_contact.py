#!/usr/bin/env python3

from typing import Optional
from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_type: ContactType
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    signal: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_rules(self):
        errors = []
        if not self.contact_id.startswith("AC"):
            errors.append("Contact ID should start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            errors.append("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic\
                and self.witness_count < 3:
            errors.append("Telepathic contact requires at least 3 witnesses")
        if self.signal > 7.0 and not self.message_received:
            errors.append("Strong signals (> 7.0) should include received\
 messages")
        if errors:
            raise ValueError("; ".join(errors))
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.today(),
            location="Area 51, Nevada",
            contact_type="physical",
            signal=6.5,
            duration_minutes=1440,
            witness_count=100,
            message_received='Greetings from Zeta Reticuli',
            is_verified=True,
        )
    except ValueError as e:
        print(e)

    print(f"ID: {valid.contact_id}")
    print(f"Type: {valid.contact_type}")
    print(f"Location: {valid.location}")
    print(f"Signal: {valid.signal}")
    print(f"Duration: {valid.duration_minutes}")
    print(f"Witnesses: {valid.witness_count}")
    print(f"Message: {valid.message_received}")
    print("======================================\n")

    print("Expected Errors")
    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.today(),
            location="Area 51, Nevada",
            contact_type="physical",
            signal=7.5,
            duration_minutes=1440,
            witness_count=5,
            message_received="",
            is_verified=False,
        )
    except ValidationError as e:
        for err in e.errors():
            print("-", err['msg'])


if __name__ == "__main__":
    main()
