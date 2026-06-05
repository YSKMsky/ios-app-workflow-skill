#!/usr/bin/env python3
import re
import sys
import json
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
CONFIG = ROOT / "config.json"


def fail(errors, message):
    errors.append(message)


def parse_frontmatter(text, errors):
    if not text.startswith("---\n"):
        fail(errors, "SKILL.md must start with YAML frontmatter")
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(errors, "SKILL.md frontmatter must close with ---")
        return {}
    raw = text[4:end]
    if "<" in raw or ">" in raw:
        fail(errors, "YAML frontmatter must not contain < or >")
    if yaml:
        try:
            data = yaml.safe_load(raw) or {}
        except Exception as exc:
            fail(errors, f"YAML frontmatter is invalid: {exc}")
            return {}
    else:
        data = {}
        for line in raw.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
    return data


def check_description(data, errors):
    desc = str(data.get("description", ""))
    if not desc:
        fail(errors, "description is required")
        return
    if not desc.startswith("Use when"):
        fail(errors, "description should start with 'Use when'")
    if "Do not use" not in desc:
        fail(errors, "description should include a negative trigger with 'Do not use'")
    if len(desc) > 650:
        fail(errors, f"description is too long: {len(desc)} characters")


def check_loading_map(text, errors):
    refs = sorted(set(re.findall(r"`((?:references|examples)/[^`]+\.md)`", text)))
    for ref in refs:
        path = ROOT / ref
        if not path.exists():
            fail(errors, f"missing loading-map file: {ref}")


def check_config(errors):
    if not CONFIG.exists():
        return
    try:
        data = json.loads(CONFIG.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(errors, f"config.json is invalid JSON: {exc}")
        return
    required = [
        "default_language",
        "user_coding_level",
        "default_platform",
        "figma_default",
        "default_validation_style",
    ]
    for key in required:
        if key not in data:
            fail(errors, f"config.json missing required key: {key}")


def check_package_clean(errors):
    forbidden = [".DS_Store", "README.md"]
    for name in forbidden:
        for path in ROOT.rglob(name):
            fail(errors, f"forbidden file in skill package: {path.relative_to(ROOT)}")


def check_size(text, errors):
    words = len(re.findall(r"\S+", text))
    if words > 1200:
        fail(errors, f"SKILL.md is too long: {words} words")


def main():
    errors = []
    if not SKILL.exists():
        fail(errors, "SKILL.md not found")
    else:
        text = SKILL.read_text(encoding="utf-8")
        data = parse_frontmatter(text, errors)
        check_description(data, errors)
        check_loading_map(text, errors)
        check_size(text, errors)
    check_config(errors)
    check_package_clean(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Skill validation OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
