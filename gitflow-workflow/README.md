# gitflow-workflow

Guides Claude through Git workflows: GitFlow branch conventions, Conventional Commits, and MR/PR creation exclusively via `git push` options (GitLab) or `gh pr create` (GitHub) — no GUI required.

## What it does

This skill covers the full GitFlow lifecycle: naming branches correctly (feature/*, bugfix/*, release/*, hotfix/*, support/*), writing well-formed Conventional Commits (feat, fix, chore, docs, style, refactor, test, perf, ci, build, revert), and opening Merge Requests or Pull Requests from the command line. On GitLab it uses native push options (`git push -o merge_request.create ...`); on GitHub it falls back to `gh pr create`. The skill validates branch names and commit messages before acting, corrects common mistakes, and either executes commands directly or generates ready-to-copy shell blocks depending on context.

## Installation

```bash
npx skills add https://github.com/azrod/skills --skill gitflow-workflow
```

## Usage

Activate by describing what you need:

- "Create a feature branch for ticket PROJ-123"
- "What branch should I use for a production hotfix?"
- "Write a commit message for adding OAuth2 login"
- "Open a MR targeting develop"
- "Push my branch and create a draft PR"
- "How do I merge a release branch?"

## Bundled references

| Reference | Content |
|-----------|---------|
| `references/branch-conventions.md` | GitFlow branch types, naming rules, merge targets, common mistakes |
| `references/conventional-commits.md` | Commit types, scopes, breaking changes, footer tokens, examples |
| `references/push-options.md` | GitLab push options and GitHub CLI flags with GitFlow-specific patterns |

## License

MIT
