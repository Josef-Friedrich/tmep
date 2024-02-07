from __future__ import annotations

from typing import Any, Callable, Dict, Union

Values = Dict[str, Any]

FunctionCollection = Dict[str, Callable[..., Union[str, int]]]
