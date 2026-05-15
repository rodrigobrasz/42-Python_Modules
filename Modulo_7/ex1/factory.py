#!/usr/bin/env python3

from ex0.creature_fac import CreateFactory, Creature
from .creatures import Morphagon, Bloomelle, Shiftling, Sproutling


class HealingCreatureFactory(CreateFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreateFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
