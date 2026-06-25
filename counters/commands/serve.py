"""`counters server` — serve the explorer SPA + read-only JSON API.

Thin wrapper: argument parsing/dispatch lives in counters.__main__; the actual
HTTP server (routes, static assets, record shaping) lives in counters.server.
"""

from __future__ import annotations

from ..config import Config
from ..server import run


def cmd_server(config: Config, host: str, port: int) -> int:
    return run(config, host=host, port=port)
