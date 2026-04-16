#!/usr/bin/env python3
"""Generate manifest.json for the GitHub Pages dashboard.

Scans the repo for <project>/<group>/report.html and emits a JSON file
that the dashboard's JS reads to build the project/group tree.

Run this as a pre-commit hook or manually before pushing.
The engaging-controller should also call this at the end of each cycle.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent
SKIP = {"instructions", "status", ".git", "_notebook", "_old", "node_modules"}

manifest = {"projects": {}}

for project_dir in sorted(REPO.iterdir()):
    if not project_dir.is_dir() or project_dir.name.startswith(".") or project_dir.name in SKIP:
        continue
    groups = []
    for group_dir in sorted(project_dir.iterdir()):
        if not group_dir.is_dir():
            continue
        has_report = (group_dir / "report.html").is_file()
        has_metrics = (group_dir / "metrics.json").is_file()
        has_discussion = (group_dir / "discussion.md").is_file()
        groups.append({
            "group": group_dir.name,
            "has_report": has_report,
            "has_metrics": has_metrics,
            "has_discussion": has_discussion,
        })
    if groups:
        manifest["projects"][project_dir.name] = groups

(REPO / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(f"Wrote manifest.json: {len(manifest['projects'])} projects, "
      f"{sum(len(g) for g in manifest['projects'].values())} groups")
