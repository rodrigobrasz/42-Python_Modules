#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex0 import CreateFactory
from ex1 import HealCapability, TransformCapability
import ex2


class StrategyError(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def act(self) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, Creature))

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise StrategyError("Normal Error!!!!!")
        else:
            return (creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, TransformCapability))

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError("Agressive Error!!!!")
        else:
            print(
                f"tranform: {creature.transform()}"
                f"attack: {creature.attack()}"
                f"revert: {creature.revert()}"
                )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, HealCapability))

    def act(self, creature: Creature) -> None:
        