from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Self, Union
from pathlib import Path
from typing import Union, BinaryIO



FunctionComponent = Callable[..., Any]

Unit = Union[int, float, str]

ColorUnit = str

TextUnit = str

ImageSource = Union[str, Path, BinaryIO]


class IModifier(ABC):
    """Contrato de estilização. Imutável e encadeável: cada chamada devolve nova instância."""

    @abstractmethod
    def padding(
        self,
        all: Unit | None = None,
        left: Unit | None = None,
        right: Unit | None = None,
        top: Unit | None = None,
        bottom: Unit | None = None,
        vertical: Unit | None = None,
        horizontal: Unit | None = None,
    ) -> Self: ...

    @abstractmethod
    def margin(
        self,
        all: Unit | None = None,
        left: Unit | None = None,
        right: Unit | None = None,
        top: Unit | None = None,
        bottom: Unit | None = None,
        vertical: Unit | None = None,
        horizontal: Unit | None = None,
    ) -> Self: ...

    @abstractmethod
    def background(self, color: ColorUnit | None = None) -> Self: ...

    @abstractmethod
    def width(self, value: Unit) -> Self: ...

    @abstractmethod
    def height(self, value: Unit) -> Self: ...

    @abstractmethod
    def fill_max_width(self) -> Self: ...


class IComponent(ABC):
    """Contrato de um nó da árvore de UI."""

    kind: str
    text: str
    modifier: IModifier | None
    props: Dict[str, Any]
    children: List["IComponent"]

    @abstractmethod
    def __enter__(self) -> Self: ...

    @abstractmethod
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

    @abstractmethod
    def render(self) -> Any: ...


class IBuilder(ABC):
    """Contrato do adaptador de renderização (árvore -> saída da plataforma)."""

    def __init__(self, tree: IComponent) -> None:
        self.tree = tree

    @abstractmethod
    def render(self) -> Any: ...

