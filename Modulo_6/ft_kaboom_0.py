#!/usr/bin/env python3

from alchemy.grimoire import light_spellbook

print("=== Kaboon 0 ===")
print("Using grimoire module directly")
print("Testing record light spell:", end="")
print(light_spellbook.light_spell_record("Fantasy", "earth, wind, fire"))
