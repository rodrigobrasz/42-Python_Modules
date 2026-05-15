#!/usr/bin/env python3

import alchemy.grimoire

print("=== Kaboon 0 ===")
print("Using grimoire module directly")
print("Testing record light spell:", end="")
print(alchemy.grimoire.light_spellbook.light_spell_record("Fantasy", "earth, wind, fire"))
