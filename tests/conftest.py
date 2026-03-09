import sys
from pathlib import Path

# ensure backend folder is on path so `app` package can be imported
ROOT = Path(__file__).parent.parent.resolve()
BACKEND = ROOT / "backend"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))
