# Branch Naming Conventions — GitFlow

## Core Model

GitFlow uses two permanent branches and several short-lived branch types:

| Branch | Permanent | Purpose |
|--------|-----------|---------|
| `main` (or `master`) | Yes | Production-ready code |
| `develop` | Yes | Integration branch for features |

## Branch Types

### Feature branches

```
feature/<ticket-or-short-desc>
feature/PROJ-123
feature/user-authentication
feature/PROJ-456-payment-gateway
```

- **Base**: `develop`
- **Merge into**: `develop`
- **Lifetime**: Until feature is merged

### Bugfix branches

```
bugfix/<ticket-or-short-desc>
bugfix/PROJ-789
bugfix/login-null-pointer
```

- **Base**: `develop`
- **Merge into**: `develop`
- **Lifetime**: Until fix is merged
- **Note**: For bugs found during development (not production). Use `hotfix/` for production issues.

### Release branches

```
release/<version>
release/1.2.0
release/2.0.0-beta.1
```

- **Base**: `develop`
- **Merge into**: `main` AND `develop`
- **Lifetime**: Stabilization period before release
- **Allowed changes**: Bug fixes, release notes, version bumps only — no new features

### Hotfix branches

```
hotfix/<ticket-or-short-desc>
hotfix/PROJ-999
hotfix/critical-payment-bug
hotfix/security-cve-2024-1234
```

- **Base**: `main`
- **Merge into**: `main` AND `develop` (or current release branch)
- **Lifetime**: Emergency fix cycle — short
- **Note**: Increment patch version on merge (e.g., 1.2.0 → 1.2.1)

### Support branches

```
support/<version>
support/1.x
support/2.3.x
```

- **Base**: `main` (at the tagged version)
- **Merge into**: Stays isolated (backport fixes only)
- **Lifetime**: Long-lived for LTS support
- **Note**: Used when multiple major versions must be maintained in parallel

## Naming Rules

1. **Lowercase only** — no uppercase letters
2. **Hyphens as separators** — not underscores or spaces
3. **No special characters** — except `/` for the type prefix and `-` within the name
4. **Ticket prefix is preferred** — `feature/PROJ-123-add-login` > `feature/add-login`
5. **Keep it short and descriptive** — max ~50 chars after the prefix
6. **No trailing slashes or dots**

## Common Mistakes

| Wrong | Correct | Why |
|-------|---------|-----|
| `Feature/AddLogin` | `feature/add-login` | Lowercase + hyphens |
| `fix/login_bug` | `bugfix/login-bug` | Use `bugfix/`, not `fix/`; hyphens not underscores |
| `hotfix` (no suffix) | `hotfix/critical-login-error` | Always add a descriptor |
| `feature/my feature` | `feature/my-feature` | No spaces |

## Branch Lifecycle Example

```
main ────────────────────────────────────────── v1.1.0 ──▶
       \                                      /
develop ─────────────────────────────────────────────────▶
           \              /
feature/foo ──────────────
```

Full feature lifecycle:
```bash
# Start feature
git checkout develop
git pull origin develop
git checkout -b feature/PROJ-123-user-auth

# Work, commit, push...

# Merge back (via MR/PR)
git checkout develop
git merge --no-ff feature/PROJ-123-user-auth
git branch -d feature/PROJ-123-user-auth
```
