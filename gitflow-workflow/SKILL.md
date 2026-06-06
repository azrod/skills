---
name: gitflow-workflow
description: "Use this skill when the user needs guidance on Git workflows: creating branches following GitFlow conventions (feature/, hotfix/, release/ prefixes), writing Conventional Commits (feat, fix, chore, docs, style, refactor, test, perf, ci, build, revert), or creating Merge Requests/Pull Requests exclusively via git push options or GitHub CLI. Trigger on requests like 'create a feature branch', 'commit this', 'open a MR', 'push and create a PR', 'what branch should I use', or any Git branching/commit/PR workflow question."
---

# GitFlow Workflow Skill

Specialized skill for GitFlow branching, Conventional Commits, and MR/PR creation via Git commands.

## What This Skill Covers

1. **Branch naming** — GitFlow conventions for all branch types
2. **Conventional Commits** — Full standard (feat, fix, chore, docs, style, refactor, test, perf, ci, build, revert) with optional scopes
3. **MR/PR creation** — Via `git push -o` options (GitLab) or `gh pr create` (GitHub), no extra GUI needed

## References

Load the relevant reference file based on the user's need:
- `references/branch-conventions.md` — Branch naming rules, GitFlow model, merge targets
- `references/conventional-commits.md` — Commit types, scopes, breaking changes, examples
- `references/push-options.md` — GitLab push options and GitHub CLI commands for MR/PR creation

Always load the reference file(s) relevant to the current task before responding.

## Workflow

### 1. Identify the user's intent

- Creating/switching to a branch → load `references/branch-conventions.md`
- Writing a commit message → load `references/conventional-commits.md`
- Creating a MR or PR → load `references/push-options.md`
- Full feature workflow → load all three references

### 2. Execute or generate commands

- **Execute directly** when the user says "do it", "run it", "create the branch", or the action is unambiguous and low-risk
- **Generate ready-to-copy commands** when the user is exploring, asking "how to", or when the action is destructive/irreversible
- Always show the command even when executing it, so the user can verify what ran

### 3. Validate before acting

Before creating a branch or commit:
- Confirm the branch name matches GitFlow conventions
- Confirm the commit message follows Conventional Commits format
- If either is wrong, propose a corrected version and explain why

## Quick Reference (inline)

### Branch naming — fast lookup

| Type | Pattern | Target base | Merge into |
|------|---------|-------------|------------|
| Feature | `feature/<ticket-or-desc>` | `develop` | `develop` |
| Bugfix | `bugfix/<ticket-or-desc>` | `develop` | `develop` |
| Release | `release/<version>` | `develop` | `main` + `develop` |
| Hotfix | `hotfix/<ticket-or-desc>` | `main` | `main` + `develop` |
| Support | `support/<version>` | `main` | — |

### Conventional Commit — fast lookup

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types: `feat` `fix` `docs` `style` `refactor` `perf` `test` `build` `ci` `chore` `revert`

Breaking change: add `!` after type → `feat!: remove legacy API`

### MR/PR — fast lookup

**GitLab** (push options):
```bash
git push -o merge_request.create \
         -o merge_request.target=develop \
         -o merge_request.title="feat: my feature" \
         origin feature/my-feature
```

**GitHub** (gh CLI):
```bash
gh pr create --base develop --title "feat: my feature" --body ""
```
