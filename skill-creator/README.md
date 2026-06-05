# skill-creator

Guides Claude through creating, editing, packaging, and iterating on agent skills following the [agentskills.io](https://agentskills.io) standard.

## What it does

This skill walks Claude through the full skill creation lifecycle: understanding requirements, planning what resources to bundle, initializing a new skill from template, writing a quality `SKILL.md`, and packaging the result for distribution. It enforces the agentskills.io spec at each step — frontmatter, structure, naming conventions — and catches common mistakes before they become problems. Three bundled scripts handle the mechanical parts so Claude can focus on the content.

## Installation

```bash
npx skills add https://github.com/azrod/skills --skill skill-creator
```

## Usage

Activate by describing what you want to build or fix:

- "Create a new skill for processing CSV files"
- "How do I write a good skill description?"
- "Package my skill for distribution"
- "My skill validation is failing, the name doesn't match"

## Bundled scripts

| Script | Purpose |
|--------|---------|
| `scripts/init_skill.py` | Initialize a new skill directory from template |
| `scripts/package_skill.py` | Validate and package a skill into a zip for distribution |
| `scripts/quick_validate.py` | Validate a skill's structure and frontmatter |

## License

MIT
