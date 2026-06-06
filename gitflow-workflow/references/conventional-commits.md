# Conventional Commits Reference

Specification: https://www.conventionalcommits.org/en/v1.0.0/

## Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Rules

- **type**: lowercase, from the allowed list below
- **scope**: optional, in parentheses — describes the part of codebase affected
- **description**: imperative mood, lowercase, no period at end, max ~72 chars
- **body**: optional, separated from description by a blank line, explains *why* not *what*
- **footer**: optional, separated by blank line — used for `BREAKING CHANGE` or issue references

## Commit Types

| Type | When to use |
|------|-------------|
| `feat` | A new feature for the user |
| `fix` | A bug fix for the user |
| `docs` | Documentation changes only (README, comments, etc.) |
| `style` | Formatting, missing semicolons, whitespace — no logic change |
| `refactor` | Code restructuring without feature change or bug fix |
| `perf` | Performance improvement |
| `test` | Adding or updating tests |
| `build` | Changes to build system or external dependencies (webpack, npm, etc.) |
| `ci` | Changes to CI/CD configuration files and scripts |
| `chore` | Maintenance tasks that don't modify src or test files |
| `revert` | Reverts a previous commit |

## Scopes

Scopes are optional but recommended for larger codebases. Use consistent names across the project.

Common scope examples:
- `auth`, `api`, `ui`, `db`, `config`, `deps`, `core`, `cli`
- Or component/module names: `payment`, `notifications`, `search`

```
feat(auth): add OAuth2 login support
fix(api): handle null response from payment gateway
docs(readme): update installation instructions
```

## Breaking Changes

Two ways to mark a breaking change:

**Option 1 — `!` after type (preferred, visible in subject line):**
```
feat!: remove support for Node 14
feat(api)!: rename user endpoints
```

**Option 2 — Footer `BREAKING CHANGE:`:**
```
feat: allow provided config object to extend other configs

BREAKING CHANGE: `extends` key in config file is now used for extending other config files
```

Both can be combined:
```
feat(api)!: rename /users to /accounts

BREAKING CHANGE: All endpoints under /users are now under /accounts.
Clients must update their base URLs accordingly.
```

## Footers

Footer format: `<token>: <value>` or `<token> #<value>`

```
fix: prevent racing of requests

Reviewed-by: Jane Doe
Refs: #123
```

Common footer tokens:
- `BREAKING CHANGE: <description>`
- `Closes #<issue-number>`
- `Fixes #<issue-number>`
- `Refs: #<issue-number>`
- `Co-authored-by: Name <email>`
- `Reviewed-by: Name`

## Examples

### Simple feature
```
feat: add dark mode support
```

### Feature with scope
```
feat(ui): add dark mode toggle to settings panel
```

### Bug fix with issue reference
```
fix(auth): redirect loop on token expiry

When the access token expired, the refresh logic entered an infinite
redirect loop because the token check ran before the refresh completed.

Closes #456
```

### Breaking change
```
feat(api)!: require authentication on all endpoints

Previously, GET /health and GET /version were public.
Both now require a valid Bearer token.

BREAKING CHANGE: Unauthenticated requests to any endpoint now return 401.
```

### Chore (dependency update)
```
chore(deps): bump axios from 1.3.0 to 1.6.0
```

### Revert
```
revert: feat(auth): add OAuth2 login support

This reverts commit abc1234 because it introduced a regression
in the existing username/password flow.
```

### Multi-line body
```
refactor(payment): extract Stripe client into standalone service

The payment logic was scattered across three controllers.
Centralizing it in PaymentService makes it easier to test,
mock in integration tests, and swap providers in the future.
```

## Common Mistakes

| Wrong | Correct | Why |
|-------|---------|-----|
| `Fix login bug` | `fix: fix login bug` | Missing type prefix |
| `feat: Added dark mode` | `feat: add dark mode` | Imperative mood, no past tense |
| `feat: add dark mode.` | `feat: add dark mode` | No trailing period |
| `FIX: login bug` | `fix: login bug` | Lowercase type |
| `feat : add dark mode` | `feat: add dark mode` | No space before colon |
| `update stuff` | `chore: update build configuration` | Must have a type and be descriptive |

## Versioning Impact (SemVer)

| Commit type | SemVer bump |
|------------|-------------|
| `fix` | PATCH (1.0.**1**) |
| `feat` | MINOR (1.**1**.0) |
| `feat!` or `BREAKING CHANGE` | MAJOR (**2**.0.0) |
| Everything else | No bump (or tooling-dependent) |
