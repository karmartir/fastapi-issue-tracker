from pathlib import Path
import json

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "issues.json"

def load_data():
    """Load all issues from disk, returning an empty list if none are saved."""
    if DATA_FILE.exists():
        # Avoid trying to parse a blank file as JSON.
        with open(DATA_FILE) as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
    return []

def save_data(data):
    """Persist the full issue list as readable JSON."""
    # Create the data folder on first use; exist_ok makes this safe if present.
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
