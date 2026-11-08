from typing import Any, Callable, ParamSpec
from functools import wraps
from core.factories import builder_factory
from core.interfaces import IComponent

P = ParamSpec("P")

def composable(
    component_fuction:Callable[P, Any],
) -> Callable[P,IComponent]:
    @wraps(component_fuction)
    def wrapper(*args: P.args, **kwargs:P.kwargs) -> IComponent:
        view = component_fuction(*args, **kwargs)
        builder = builder_factory(view)
        return view

    return wrapper

