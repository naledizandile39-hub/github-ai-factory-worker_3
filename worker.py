"""Basic health check for this worker workspace."""

from pathlib import Path

def check_workspace():
    required = [Path("README.md")]
    missing = [str(p) for p in required if not p.exists()]

    if missing:
        print("Missing files:", ", ".join(missing))
        return False

    print("Workspace health: OK")
    return True

if __name__ == "__main__":
    raise SystemExit(0 if check_workspace() else 1)
