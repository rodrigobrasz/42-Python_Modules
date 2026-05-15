#!/usr/bin/env python3

from ex0.creature import Creature
from .capabilites import TransformCapability, HealCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "uses Vine Wip"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self):
        return f"{self._name} uses Petal Dance!"

    def heal(self):
        return f"{self._name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        return f"{self._name} returns to normal."

    def attack(self) -> str:
        if self._transformed is False:
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} performs a boosted strike!"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shiftess into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stabilizes its form."

    def attack(self) -> str:
        if self._transformed is False:
            return f"{self._name} attacks normally"
        else:
            return f"{self._name}unleashes a devastating morph strike!"
