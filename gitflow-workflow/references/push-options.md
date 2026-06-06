# MR/PR Creation via Push Options and CLI

## GitLab — Push Options (`git push -o`)

Push options allow creating and configuring Merge Requests directly from `git push` without touching the GitLab UI.

### Basic MR creation

```bash
git push -o merge_request.create origin feature/my-feature
```

### Full MR with all common options

```bash
git push \
  -o merge_request.create \
  -o merge_request.target=develop \
  -o merge_request.title="feat(auth): add OAuth2 login" \
  -o merge_request.description="Implements OAuth2 flow. Closes #123" \
  -o merge_request.label="feature" \
  -o merge_request.label="backend" \
  -o merge_request.assign="john.doe" \
  -o merge_request.milestone="v2.0" \
  -o merge_request.remove_source_branch \
  origin feature/PROJ-123-oauth2-login
```

### Available push options

| Option | Description |
|--------|-------------|
| `merge_request.create` | Create a new MR (required to trigger creation) |
| `merge_request.target=<branch>` | Target branch (default: repo default branch) |
| `merge_request.title="<title>"` | MR title |
| `merge_request.description="<desc>"` | MR description |
| `merge_request.label="<label>"` | Add a label (repeat for multiple) |
| `merge_request.assign="<username>"` | Assign to a user (repeat for multiple) |
| `merge_request.milestone="<name>"` | Set milestone |
| `merge_request.remove_source_branch` | Delete branch after merge |
| `merge_request.squash` | Enable squash on merge |
| `merge_request.draft` | Mark as draft/WIP |
| `merge_request.merge_when_pipeline_succeeds` | Auto-merge when pipeline passes |

### Draft MR

```bash
git push \
  -o merge_request.create \
  -o merge_request.target=develop \
  -o merge_request.title="feat: work in progress" \
  -o merge_request.draft \
  origin feature/my-feature
```

### Common GitFlow patterns

**Feature → develop:**
```bash
git push \
  -o merge_request.create \
  -o merge_request.target=develop \
  -o merge_request.title="feat(scope): description" \
  -o merge_request.remove_source_branch \
  origin feature/PROJ-123-my-feature
```

**Hotfix → main:**
```bash
git push \
  -o merge_request.create \
  -o merge_request.target=main \
  -o merge_request.title="fix: critical bug description" \
  -o merge_request.label="hotfix" \
  -o merge_request.remove_source_branch \
  origin hotfix/critical-payment-bug
```

**Release → main:**
```bash
git push \
  -o merge_request.create \
  -o merge_request.target=main \
  -o merge_request.title="chore(release): v1.2.0" \
  -o merge_request.label="release" \
  origin release/1.2.0
```

### Notes

- Push options require GitLab 11.10+ for basic options, 12.x+ for full support
- Multiple `-o` flags are additive
- If an MR already exists for the branch, push options are ignored (use the API to update)
- Quotes around option values are required when the value contains spaces

---

## GitHub — GitHub CLI (`gh pr create`)

The `gh` CLI is the recommended way to create PRs from the command line on GitHub.

### Basic PR creation (interactive)

```bash
gh pr create
```

Interactive mode prompts for title, body, base branch, and reviewers.

### Non-interactive PR creation

```bash
gh pr create \
  --base develop \
  --title "feat(auth): add OAuth2 login" \
  --body "Implements OAuth2 flow. Closes #123"
```

### Full PR with all common options

```bash
gh pr create \
  --base develop \
  --title "feat(auth): add OAuth2 login" \
  --body "Implements OAuth2 flow.\n\nCloses #123" \
  --label "feature" \
  --label "backend" \
  --assignee "john-doe" \
  --reviewer "jane-doe" \
  --reviewer "team/backend" \
  --milestone "v2.0" \
  --draft
```

### Available flags

| Flag | Short | Description |
|------|-------|-------------|
| `--base <branch>` | `-B` | Target branch |
| `--title "<title>"` | `-t` | PR title |
| `--body "<body>"` | `-b` | PR body/description |
| `--body-file <file>` | `-F` | Read body from a file |
| `--draft` | `-d` | Create as draft PR |
| `--label <label>` | `-l` | Add label (repeat for multiple) |
| `--assignee <user>` | `-a` | Assign to user (repeat for multiple) |
| `--reviewer <user>` | `-r` | Request review (repeat for multiple) |
| `--milestone <name>` | `-m` | Set milestone |
| `--head <branch>` | `-H` | Source branch (default: current) |
| `--fill` | | Use commit info to fill title/body |
| `--fill-first` | | Use first commit only for fill |
| `--web` | `-w` | Open PR creation in browser |

### Draft PR

```bash
gh pr create \
  --base develop \
  --title "feat: work in progress" \
  --draft
```

### Common GitFlow patterns

**Feature → develop:**
```bash
gh pr create \
  --base develop \
  --title "feat(scope): description" \
  --body "## Summary\n\nCloses #PROJ-123"
```

**Hotfix → main:**
```bash
gh pr create \
  --base main \
  --title "fix: critical bug description" \
  --label "hotfix" \
  --body "## Root Cause\n\n...\n\n## Fix\n\n..."
```

**Release → main:**
```bash
gh pr create \
  --base main \
  --title "chore(release): v1.2.0" \
  --label "release" \
  --body "Release v1.2.0 — see CHANGELOG.md"
```

### Auto-fill from commits

```bash
# Use commit messages to populate PR title and body automatically
gh pr create --base develop --fill
```

### Check PR status after creation

```bash
gh pr status         # PRs related to current branch
gh pr view           # View current branch's PR
gh pr view --web     # Open in browser
gh pr checks         # View CI status
```

### Notes

- `gh` must be authenticated: run `gh auth login` first
- `--fill` is useful for single-commit branches with good commit messages
- For team/org reviewers use `--reviewer org/team-slug`
- Body supports Markdown; use `\n` in shell or `--body-file` for multiline content
