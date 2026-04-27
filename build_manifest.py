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
SKIP = {"instructions", "status", ".git", "_notebook", "_old", "node_modules",
        "diagnostics"}

manifest = {"projects": {}, "diagnostics": []}

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
        # Use report.html mtime as the "report generated" timestamp
        report_mtime = None
        if has_report:
            report_mtime = (group_dir / "report.html").stat().st_mtime
        groups.append({
            "group": group_dir.name,
            "has_report": has_report,
            "has_metrics": has_metrics,
            "has_discussion": has_discussion,
            "report_mtime": report_mtime,
        })
    if groups:
        # Sort by report mtime descending (most recent first); unreported at bottom
        groups.sort(key=lambda g: g.get("report_mtime") or 0, reverse=True)
        manifest["projects"][project_dir.name] = groups

# Enumerate diagnostics/ for the dashboard browser. Anything that looks
# like an image (png/jpg/svg/webp) is exposed; the dashboard groups by
# subfolder (the immediate parent's name under diagnostics/) so related
# diagnostics cluster in the UI. Files at the top level (no subfolder)
# go into a synthetic "uncategorized" bucket. Recursion is one level
# deep so nested per-run profile dumps don't clutter the listing.
diag_dir = REPO / "diagnostics"
if diag_dir.is_dir():
    img_exts = {".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif"}
    for p in diag_dir.rglob("*"):
        if not (p.is_file() and p.suffix.lower() in img_exts):
            continue
        rel = p.relative_to(diag_dir)
        # Category = top-level subfolder; "uncategorized" if at root.
        category = rel.parts[0] if len(rel.parts) > 1 else "uncategorized"
        manifest["diagnostics"].append({
            "name": p.name,
            "category": category,
            "path": f"diagnostics/{rel.as_posix()}",
            "mtime": p.stat().st_mtime,
            "size": p.stat().st_size,
        })
    # Newest first within the flat list; the dashboard groups by category.
    manifest["diagnostics"].sort(key=lambda d: d["mtime"], reverse=True)

(REPO / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(f"Wrote manifest.json: {len(manifest['projects'])} projects, "
      f"{sum(len(g) for g in manifest['projects'].values())} groups, "
      f"{len(manifest['diagnostics'])} diagnostic image(s)")
