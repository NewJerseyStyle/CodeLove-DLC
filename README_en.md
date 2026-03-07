# CodeLove DLC Template

DLC development template for Source Realm. Use this template to create expansion content that can be integrated with the main story.

[繁體中文](README.md) | [English](README_en.md)

## Quick Start

### 📖 DLC Development Workflow

1. **Copy from the template DLC folder** and rename it to your DLC name.
2. **Modify `config.rpy`** (name, author, description, version).
3. **Modify character definitions (`characters.rpy`) and script files (`events/`)**.
4. **Launch the game locally** and specify the DLC path for testing.
5. **Pack the entire folder** and upload it to your preferred platform (itch.io, GitHub, personal website, etc.).

> 💡 **The official team does not provide community DLC review or hosting services. Please distribute and promote your work freely.**

### 1. Use This Template

Click the **"Use this template"** button on the GitHub page, or:

```bash
# Clone the template
git clone https://github.com/NewJerseyStyle/CodeLove-DLC.git my-dlc
cd my-dlc
rm -rf .git && git init  # Re-initialize as your project
```

### 2. Rename

```bash
# Global replacement (editor recommended)
# template_dlc → your_dlc_name
# template_char → your_char_id
# TEMPLATE → YOUR_CHAPTER_PREFIX
```

## Packaging and Installation

### Method 1: Pack as ZIP (Recommended)

1. Pack the DLC folder into a ZIP.
2. Users download and extract it into the main game's `game/` directory.

**Extraction Location**:

```
SourceRealm/
└── game/        ← Can be extracted anywhere inside this folder
    └── CodeLove-YourDLC/      ← Your DLC folder
        ├── config.rpy
        ├── characters.rpy
        ├── events/
        └── endings.rpy
```

**Important**:
- It can be extracted into **any subdirectory** under the `game/` directory.
- Not limited to `game/rpy/dlc/`, as long as it's under `game/`.
- Ren'Py will automatically load all `.rpy` files.

### Method 2: Direct Copy

Users can directly copy the folder into the `game/` directory.

### Verify Installation

1. Launch the game.
2. Press the developer console key (usually `Shift+O` or `Shift+D`).
3. Enter `call debug_dlc_status`.
4. Check if "Installed DLC count" is > 0.

## File Structure

```
your_dlc/
├── README.md           # Documentation
├── config.rpy          # DLC configuration and region registration
├── characters.rpy      # Character definitions
├── events/             # Event files
│   └── YOUR_01.rpy
└── endings.rpy         # Ending definitions
```

## Development Steps

Refer to the [DLC Developer Guide](DLC_DEVELOPER_GUIDE_en.md) for detailed instructions.

## Testing

1. Place the DLC folder into the main game's `game/` directory (any subdirectory works).
2. Launch the game.
3. Use `call debug_dlc_status` to check if it's registered.
4. Confirm if it appears in the plaza under "Go to other regions".

## Release Checklist

- [ ] All files use UTF-8 encoding.
- [ ] Images placed in `images/YourLanguage/`.
- [ ] Update README with installation instructions.
- [ ] Pack as ZIP (include the entire folder).
- [ ] Create a Release on GitHub.
- [ ] Test a fresh installation (from download to running).

## FAQ

### Q: Where should the DLC folder be placed?

A: Anywhere under the `game/` directory. For example:
- `game/YourDLC/`
- `game/rpy/dlc/your_dlc/`
- `game/mods/your_dlc/`

As long as it's under `game/`, Ren'Py will find it.

### Q: Why doesn't the "Go to other regions" option appear?

A: Check the following:
1. Is the DLC correctly registered? (Check with `debug_dlc_status`)
2. Is the region's `unlock_condition` met?
3. Has the main game completed necessary chapters (e.g., C_01)?

### Q: How to reference main game variables in DLC?

A: Use `store.variable_name`:
```python
if store.cee_relationship == "FUNCTIONAL":
    # Perform some action
    pass
```

## Region-Oriented Design

DLC uses a **Region-Oriented** design:

```
Plaza (Main Hub)
    ├── Memory Vault (Cee)
    ├── Contract Bureau (Jawa)
    └── [Go to other regions]        ← Automatically shows registered DLC regions
            ├── Zen Garden (Py-DLC)
            └── Your Region
```

**Advantages**:
- DLC has its own region, not interfering with the main story.
- Regions manage their own events and unlock conditions internally.
- Players can enter and exit freely, no forced time alignment required.

## Reference Example

Full runnable example: [CodeLove-Py-DLC](https://github.com/NewJerseyStyle/CodeLove-Py-DLC)

## Support

- [DLC_DEVELOPER_GUIDE_en.md](https://github.com/NewJerseyStyle/CodeLove/blob/main/docs/DLC_DEVELOPER_GUIDE_en.md) - Full Development Guide
- [DLC_QUICK_REFERENCE_en.md](https://github.com/NewJerseyStyle/CodeLove/blob/main/docs/DLC_QUICK_REFERENCE_en.md) - Quick Reference

## License

MIT License (or adjusted according to main game license)
