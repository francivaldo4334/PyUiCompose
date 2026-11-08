from typing import Any, Callable, Dict
from pyuicompose.interfaces import IBuilder, IComponent, IModifier

FACTORIES: Dict[str, Callable[..., Any]] = {}

def _get(name: str) -> Callable[..., Any]:
    try:
        return FACTORIES[name]
    except KeyError:
        raise RuntimeError(
            f"Factory '{name}' não registrada. "
            "Chame register() no AppConfig.ready()."
        ) from None

def builder_factory(component_tree: IComponent) -> IBuilder:
    return _get("builder_factory")(component_tree)


def modifier_factory(*args, **kwargs) -> IModifier:
    return _get("modifier_factory")(*args, **kwargs)


def component_factory(kind: str, **props) -> IComponent:
    key = "component_factory"
    try:
        component_factory_class = _get(key)
    except RuntimeError:
        from pyuicompose.implements.component import Component
        component_factory_class = Component

    return component_factory_class(kind, **props)


