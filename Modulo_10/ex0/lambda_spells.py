#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    min_power = min(mages, key=lambda x: x["power"])["power"]
    max_power = max(mages, key=lambda x: x["power"])["power"]
    av_power = round(sum(map(lambda x: x["power"], mages)) / len(mages), 2)
    print(av_power)
    return {
        "min_power": min_power, "max_power": max_power,
        "avarage_power": av_power,
        }


def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 999},
        {"name": "Ancient Tome", "power": 777},
        {"name": "Crystal Orb", "power": 888}
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifact = artifact_sorter(artifacts)
    first = sorted_artifact[0]
    second = sorted_artifact[1]
    print(
        f"{first['name']} ({first['power']} power) comes"
        f"before {second['name']} ({second['power']} power)"
        )

    transformed = spell_transformer(spells)
    print(" ".join(transformed))


if __name__ == "__main__":
    main()
