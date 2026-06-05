#!/usr/bin/env python3
"""
Quick validation script for skills - minimal version

Usage:
    quick_validate.py <skill_directory>
    quick_validate.py --help

Exit codes:
    0 - skill is valid
    1 - validation failed or error
"""

import sys
import os
import re
from pathlib import Path

try:
    import yaml
    _HAS_YAML = True
except ImportError:
    _HAS_YAML = False

HELP_TEXT = """\
Usage: quick_validate.py <skill_directory>

Validates a skill directory against the agentskills.io standard.

Arguments:
  skill_directory   Path to the skill folder (must contain SKILL.md)

Checks performed:
  - SKILL.md exists with valid YAML frontmatter
  - 'name' field present, hyphen-case, ≤ 64 chars, matches directory name
  - 'description' field present, no angle brackets, ≤ 1024 chars
  - 'compatibility' field ≤ 500 chars (if present)

Exit codes:
  0   Skill is valid
  1   Validation failed or error
"""

def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)

    # Check SKILL.md exists
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    # Read and validate frontmatter
    content = skill_md.read_text()
    if not content.startswith('---'):
        return False, "No YAML frontmatter found"

    # Extract frontmatter raw block
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_raw = match.group(1)

    # Check required fields presence (fast path before YAML parse)
    if 'name:' not in frontmatter_raw:
        return False, "Missing 'name' in frontmatter"
    if 'description:' not in frontmatter_raw:
        return False, "Missing 'description' in frontmatter"

    # Parse YAML for accurate field extraction (fallback to regex if pyyaml unavailable)
    if _HAS_YAML:
        try:
            frontmatter = yaml.safe_load(frontmatter_raw) or {}
        except yaml.YAMLError as e:
            return False, f"Invalid YAML in frontmatter: {e}"
    else:
        # Minimal regex-based extraction when pyyaml is not installed
        frontmatter = {}
        for line in frontmatter_raw.splitlines():
            kv = re.match(r'^(\w[\w-]*):\s*(.*)', line)
            if kv:
                frontmatter[kv.group(1)] = kv.group(2).strip()

    # --- Validate name ---
    name = str(frontmatter.get('name', '')).strip()
    if not name:
        return False, "Missing 'name' in frontmatter"

    if not re.match(r'^[a-z0-9-]+$', name):
        return False, f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)"
    if name.startswith('-') or name.endswith('-') or '--' in name:
        return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
    if len(name) > 64:
        return False, f"Name '{name}' exceeds 64 characters (current: {len(name)})"

    # Name must match the parent directory name
    expected_name = skill_path.name
    if name != expected_name:
        return False, f"Name '{name}' does not match directory name '{expected_name}'"

    # --- Validate description ---
    description = str(frontmatter.get('description', '')).strip()
    if not description:
        return False, "Missing 'description' in frontmatter"
    if '<' in description or '>' in description:
        return False, "Description cannot contain angle brackets (< or >)"
    if len(description) > 1024:
        return False, f"Description exceeds 1024 characters (current: {len(description)})"

    # --- Validate compatibility (optional) ---
    if 'compatibility' in frontmatter:
        compatibility = str(frontmatter['compatibility']).strip()
        if len(compatibility) > 500:
            return False, f"Compatibility exceeds 500 characters (current: {len(compatibility)})"

    return True, "Skill is valid!"

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] in ('--help', '-h'):
        print(HELP_TEXT, end='')
        sys.exit(0)

    if len(sys.argv) != 2:
        sys.stderr.write("Usage: quick_validate.py <skill_directory>\n")
        sys.stderr.write("Try 'quick_validate.py --help' for more information.\n")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)