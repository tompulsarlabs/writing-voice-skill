#!/usr/bin/env python3
"""Install one maintained writing skill with portable discovery links."""
import argparse
import shutil
from pathlib import Path

NAME = "writing-voice-custom"
SOURCE = Path(__file__).resolve().parents[1] / NAME
FILES = ("SKILL.md", "eval.md", "agents/openai.yaml")


def install(root, personal, check):
    canonical = root / ".agents" / "skills" / NAME
    aliases = [root / host / "skills" / NAME for host in
               ((".codex", ".claude", ".cursor") if personal else (".claude", ".cursor"))]
    # Check all conflicts before any writes. Never replace a different skill.
    for alias in aliases:
        if alias.is_symlink():
            if alias.resolve() != canonical.resolve():
                raise SystemExit(f"Conflicting link: {alias}")
        elif alias.exists():
            raise SystemExit(f"Existing independent installation: {alias}; reconcile it before linking.")
    if canonical.is_symlink():
        raise SystemExit(f"Canonical path is a symlink: {canonical}")
    if canonical.exists():
        expected = {Path(f) for f in FILES}
        existing = {f.relative_to(canonical) for f in canonical.rglob('*') if f.is_file()}
        if existing - expected:
            raise SystemExit(f"Unmanaged files at {canonical}; reconcile before updating.")
    if not check:
        canonical.mkdir(parents=True, exist_ok=True)
        for relative in FILES:
            target = canonical / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(SOURCE / relative, target)
        for alias in aliases:
            alias.parent.mkdir(parents=True, exist_ok=True)
            if not alias.is_symlink():
                alias.symlink_to(Path("../../.agents/skills") / NAME, target_is_directory=True)
    for relative in FILES:
        target = canonical / relative
        if not target.is_file() or target.read_bytes() != (SOURCE / relative).read_bytes():
            raise SystemExit(f"Missing or outdated: {target}")
    for alias in aliases:
        if not alias.is_symlink() or alias.resolve() != canonical.resolve():
            raise SystemExit(f"Missing discovery link: {alias}")
        if (alias / "SKILL.md").read_bytes() != (SOURCE / "SKILL.md").read_bytes():
            raise SystemExit(f"Outdated discovery path: {alias}")
    print(f"Verified {canonical} and {len(aliases)} discovery links")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--user", action="store_true", help="Install for Codex, Claude Code, and Cursor")
    group.add_argument("--project", type=Path, help="Install portable files inside a project; commit them for cloud use")
    p.add_argument("--check", action="store_true", help="Read-only comparison with this source version")
    args = p.parse_args()
    install(Path.home() if args.user else args.project.resolve(), args.user, args.check)
