#!/usr/bin/env python3
"""
Enhanced Hello Fanra application with multiple modes
"""
import sys
import json
from datetime import datetime

def hello_fanra(mode="simple", name="Fanra"):
    """Return greeting based on mode"""
    greetings = {
        "simple": f"Hello {name}!",
        "formal": f"Greetings, {name}. Welcome to the autonomous coding test.",
        "casual": f"Hey {name}! 👋 Ready to code?",
        "json": json.dumps({
            "message": f"Hello {name}!",
            "timestamp": datetime.now().isoformat(),
            "mode": mode,
            "project": "fanra-test"
        }, indent=2),
        "ascii": f"""
    ╔══════════════════════╗
    ║   Hello {name}! 👋      ║
    ║  Autonomous Coding    ║
    ║      Test Project     ║
    ╚══════════════════════╝
"""
    }
    return greetings.get(mode, greetings["simple"])

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "simple"
    name = sys.argv[2] if len(sys.argv) > 2 else "Fanra"
    print(hello_fanra(mode, name))

if __name__ == "__main__":
    main()