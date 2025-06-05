import json
from pathlib import Path
import pytest

# List of JSON files in the repository root to validate
CONFIG_FILES = [
    "manifest.json",
    "plex-media-serverconfig.json",
    "plex-media-servermetaconfig.json",
    "plex-media-serverports.json",
    "plex-media-serverupdates.json",
]

ROOT = Path(__file__).resolve().parents[1]

@pytest.mark.parametrize("file_name", CONFIG_FILES)
def test_json_parsing(file_name):
    """Ensure each JSON configuration file parses correctly."""
    path = ROOT / file_name
    with path.open('r', encoding='utf-8') as f:
        json.load(f)


def test_update_paths_lowercase():
    """Verify update paths use the lowercase 'serverfiles' directory."""
    path = ROOT / "plex-media-serverupdates.json"
    with path.open('r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        for key, value in item.items():
            if isinstance(value, str) and "serverfiles" in value.lower():
                # ensure lowercase usage
                assert "serverFiles" not in value
                assert "serverfiles" in value
        if item.get("UpdateSourceTarget"):
            assert item["UpdateSourceTarget"] == "serverfiles"
