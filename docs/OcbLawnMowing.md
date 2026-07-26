# OcbLawnMowing

**Location:** `~/code/OcbLawnMowing`

**Purpose:** 7 Days to Die game mod that adds a rideable Lawn Tractor vehicle with mowing and harvesting capabilities. Transforms farming by allowing vehicle-based grass clearing and crop harvesting.

## Tech Stack

- **Framework:** .NET Framework 4.8
- **Engine:** Unity (7 Days to Die)
- **Patching:** 0Harmony (runtime code patching)
- **Type:** Game Mod

## Project Structure

```
OcbLawnMowing/
├── Harmony/                  # Runtime patches
│   ├── LawnMowing.cs         # Main mod entry
│   └── ModXmlPatcher.cs      # XML config patching
├── Library/                  # Core mod logic
│   ├── VPMower.cs            # Vehicle part logic
│   └── ItemActionScythe.cs   # Scythe item action
├── Config/                   # Game XML configs
│   ├── blocks.xml, items.xml, vehicles.xml
│   └── recipes.xml, progression.xml
├── Resources/                 # Embedded resources
├── UIAtlases/                # UI textures
├── Unity/                    # Unity asset sources
└── ModInfo.xml               # Mod metadata
```

## Entry Points

| File | Purpose |
|------|---------|
| `Harmony/LawnMowing.cs` | Main mod entry (`IModApi.InitMod`) |
| `Library/VPMower.cs` | Vehicle part handling mowing logic |
| `Library/ItemActionScythe.cs` | Manual scythe harvesting |

## Vehicle Modifiers (Attachments)

1. **Grass Collector** — Collects grass/bush items
2. **Plant Collector** — Harvests wild plants (cotton, coffee)
3. **Crop Harvester** — Better yield for player crops
4. **Crop Protector** — Prevents mowing player plants
5. **Crop Reseeder** — Auto-reseeds harvested crops

## Dependencies

| Package | Purpose |
|---------|---------|
| 0Harmony | Runtime code patching |
| Assembly-CSharp | 7D2D main assembly |
| UnityEngine | Core Unity runtime |

## Build & Install

```bash
# Compile
00-CompileModule.bat

# Create release
01-CreateRelease.bat
```

## Installation

1. Copy to 7D2D `Mods/` folder
2. Disable EAC (Easy Anti-Cheat)
3. Launch game

## Notes

- Version 2.3.2
- Compatible with 7D2D V1.0 (exp) and A21
- EAC must be disabled (contains custom code)
- 21 harvestable prefab variants (3 damage × 7 colors)
- 27 language translations via DeepL