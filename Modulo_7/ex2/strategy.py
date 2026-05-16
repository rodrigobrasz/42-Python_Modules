#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1 import HealCapability, TransformCapability


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
                f"tranform: {creature.transform()}\n"
                f"attack: {creature.attack()}\n"
                f"revert: {creature.revert()}\n"
                )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, HealCapability))

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError("Defensive Error!!!")
        else:
            print(
                f"heal: {creature.heal()}\n"
                f"attack: {creature.attack()}"
                )
