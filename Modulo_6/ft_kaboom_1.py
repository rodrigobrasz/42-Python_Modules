#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== Kaboon 1 ===")
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        print(dark_spell_record("Curse of Bats", "frogs and bats"))
    except ImportError as e:
        print(f"{e}")
