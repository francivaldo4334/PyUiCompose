from contextvars import ContextVar
from typing import Any, Tuple

_STACK: ContextVar[Tuple[Any, ...]] = ContextVar("pc_stack", default=())

def current_parent() -> Any | None:
    stack = _STACK.get()
    return stack[-1] if stack else None

def push(node: Any):
    return _STACK.set(_STACK.get() + (node,))


def pop(token):
    _STACK.reset(token)



