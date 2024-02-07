from __future__ import annotations

from typing import Any, Callable, Dict

Values = Dict[str, Any]

FunctionCollection = Dict[str, Callable[..., str | int]]
