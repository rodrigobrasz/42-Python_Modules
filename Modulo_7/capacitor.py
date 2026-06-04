#!/usr/bin/env python3

from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability


def test_healing_creatures(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability\n base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_transform_creatures(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability\n base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    heal_fac = HealingCreatureFactory()
    test_healing_creatures(heal_fac)
    print()
    trans_fac = TransformCreatureFactory()
    test_transform_creatures(trans_fac)
