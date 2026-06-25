"""The explorer web server: a static SPA plus a small read-only JSON API.

`counters server` serves the bundled single-page explorer (index.html + logos)
and three endpoints backed by the index store. See app.py for details.
"""

from .app import run

__all__ = ["run"]
