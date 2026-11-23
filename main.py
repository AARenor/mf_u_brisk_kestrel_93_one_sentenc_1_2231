import os
from pathlib import Path
import sys


TEXT = "A Russian warship stopped in Libya for fuel, and Ukraine sent seven drones that sank it 1,500 miles from the nearest front line."


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "/output")))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(text.encode("utf-8"))
    print(len(text), file=sys.stderr)


if __name__ == "__main__":
    main()
