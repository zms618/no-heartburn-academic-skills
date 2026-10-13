"""Build ready-to-upload ChatGPT plugin ZIPs from the maintained source tree."""

from __future__ import annotations

import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "downloads"


def add_tree(archive: ZipFile, source: Path, archive_prefix: str) -> None:
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(source).as_posix()
        if any(part in {".git", "__pycache__", ".pytest_cache", ".mypy_cache"} for part in path.parts):
            continue
        if relative.count("/") == 0 and path.name in {"README.md", "README.en.md"}:
            continue
        archive.write(path, f"{archive_prefix}/{relative}")


def validate_markdown_links(package: Path) -> None:
    """Fail the build if a bundled Markdown file points to a missing local file."""
    with ZipFile(package) as archive:
        packaged_files = set(archive.namelist())
        broken: list[str] = []
        for name in sorted(packaged_files):
            if not name.lower().endswith(".md"):
                continue
            source = archive.read(name).decode("utf-8", errors="replace")
            for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", source):
                target = target.split("#", 1)[0].split("?", 1)[0].strip()
                if not target or target.startswith("#") or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                parts: list[str] = []
                for part in (Path(name).parent / target).as_posix().split("/"):
                    if part == "..":
                        if parts:
                            parts.pop()
                    elif part not in {"", "."}:
                        parts.append(part)
                resolved = "/".join(parts)
                if resolved not in packaged_files:
                    broken.append(f"{name}: {target} -> {resolved}")
        if broken:
            raise ValueError(f"Broken Markdown links in {package.name}:\n" + "\n".join(broken))


def build_package(
    filename: str,
    manifest: Path,
    metadata: Path,
    runtime_trees: list[tuple[Path, str]],
    license_file: Path,
    package_files: list[tuple[Path, str]] | None = None,
) -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT / filename
    with ZipFile(destination, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        archive.write(manifest, "plugin.json")
        archive.write(metadata, ".codex-plugin/plugin.json")
        archive.write(license_file, "LICENSE")
        for source, archive_path in package_files or []:
            archive.write(source, archive_path)
        for source, prefix in runtime_trees:
            add_tree(archive, source, prefix)


def main() -> None:
    build_package(
        "paper-reading-v0.7.0.zip",
        ROOT / "plugin.json",
        ROOT / ".codex-plugin/plugin.json",
        [(ROOT / "skills/paper-reading", "skills/paper-reading")],
        ROOT / "LICENSE",
    )
    idea = ROOT / "skills/research-idea-discovery"
    build_package(
        "research-idea-discovery-v4.0.19.zip",
        idea / "plugin.json",
        idea / ".codex-plugin/plugin.json",
        [
            (idea / "references", "references"),
            (idea / "scripts", "scripts"),
            (idea / "skills", "skills"),
        ],
        ROOT / "LICENSE",
    )
    mentor = ROOT / "skills/ai-mentor"
    build_package(
        "ai-mentor-v1.4.0.zip",
        mentor / "plugin.json",
        mentor / ".codex-plugin/plugin.json",
        [
            (mentor / "assets", "assets"),
            (mentor / "handbook", "handbook"),
            (mentor / "handbook-en", "handbook-en"),
            (mentor / "skills", "skills"),
        ],
        mentor / "LICENSE",
        [(mentor / "CONTRIBUTING.md", "CONTRIBUTING.md")],
    )
    for package in sorted(OUTPUT.glob("*.zip")):
        validate_markdown_links(package)
    print(f"Built plugin packages in {OUTPUT}")


if __name__ == "__main__":
    main()
