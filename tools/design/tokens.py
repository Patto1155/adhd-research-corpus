"""Load the shared design tokens (tools/design/tokens.json).

Used by the chart scripts (tools/charts/*.py) and by the reader and explorer
builders, so the static charts and both HTML tools draw from one palette, one
type scale and one set of radii. Standard library only.
"""

import json
from pathlib import Path

TOKENS_PATH = Path(__file__).resolve().parent / "tokens.json"
_CACHE = None


def load():
    global _CACHE
    if _CACHE is None:
        _CACHE = json.loads(TOKENS_PATH.read_text(encoding="utf-8"))
    return _CACHE


def colors(mode):
    """Colour tokens for 'light' or 'dark' as a plain dict."""
    return dict(load()["color"][mode])


def _var(name):
    return "--" + name.replace("ink2", "ink-2").replace("_", "-")


def _block(c):
    return " ".join(f"{_var(k)}: {v};" for k, v in c.items())


def css():
    """CSS custom properties: light on :root, dark under prefers-color-scheme and [data-theme]."""
    t = load()
    light, dark = t["color"]["light"], t["color"]["dark"]
    r = t["radius"]
    base = (_block(light) + f' --font: {t["font"]["ui"]}; --mono: {t["font"]["mono"]};'
            + " " + " ".join(f"--radius-{k}: {v}px;" for k, v in r.items() if k != "pill")
            + " --radius-pill: 999px;")
    d = _block(dark) + " color-scheme: dark;"
    return (
        "/* Shared tokens from tools/design/tokens.json (inserted by the builder). */\n"
        f":root {{ {base} }}\n"
        f'@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ {d} }} }}\n'
        f':root[data-theme="dark"] {{ {d} }}\n'
    )


def inject(template):
    """Replace the /*__TOKENS__*/ marker in an HTML template with the token CSS."""
    if "/*__TOKENS__*/" not in template:
        raise SystemExit("template is missing the /*__TOKENS__*/ marker")
    return template.replace("/*__TOKENS__*/", css())
