#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import cast
from ex0.creature import Creature
from ex1 import HealCapability, TransformCapability


class IvalidCreature(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, Creature))

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise IvalidCreature("Ivalid Creature")
        creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        # garante que é Creature e também TransformCapability
        return isinstance(creature, Creature) and\
               isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise IvalidCreature("Ivalid Creature")

        t = cast(TransformCapability, creature)
        print(
            f"tranform: {t.transform()}\n"
            f"attack: {creature.attack()}\n"
            f"revert: {t.revert()}\n"
        )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature) and\
            isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise IvalidCreature("Ivalid Creature")

        h = cast(HealCapability, creature)
        print(
            f"heal: {h.heal()}\n"
            f"attack: {creature.attack()}"
        )
