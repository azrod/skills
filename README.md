# azrod/skills

![banner](./banner.png)
[![skills.sh](https://skills.sh/b/azrod/skills)](https://skills.sh/azrod/skills)

A collection of agent skills for Claude following the [agentskills.io](https://agentskills.io) standard.

## Installation

Install a specific skill:

```bash
npx skills add https://github.com/azrod/skills --skill <skill-name>
```

Install all skills globally:

```bash
npx skills add https://github.com/azrod/skills -g
```

## Skills

| Skill | Description | Install |
|-------|-------------|---------|
| [`skill-creator`](./skill-creator) | Guides Claude through creating, editing, packaging, and iterating on agent skills | `npx skills add https://github.com/azrod/skills --skill skill-creator` |
| [`gitflow-workflow`](./gitflow-workflow) | GitFlow branch conventions, Conventional Commits, and MR/PR creation via git push options or gh CLI | `npx skills add https://github.com/azrod/skills --skill gitflow-workflow` |

## License

MIT
