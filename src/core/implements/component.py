from typing import Any, Dict, List
from core.interfaces import IComponent, IModifier
from core import runtime


class Component(IComponent):
    def __init__(
        self,
        kind: str,
        *,
        text: str = "",
        modifier: IModifier | None = None,
        **props: Any,
    ) -> None:
        self.kind = kind
        self.text = text
        self.modifier = modifier
        self.props: Dict[str, Any] = props
        self.children: List[IComponent] = []
        self._token = None

        parent = runtime.current_parent()
        if parent is not None:
            parent.children.append(self)

    def __enter__(self) -> "Component":
        self._token = runtime.push(self)
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        runtime.pop(self._token)
        self._token = None

    def render(self) -> Any:
        from factories import builder_factory
        return builder_factory(self).render()

