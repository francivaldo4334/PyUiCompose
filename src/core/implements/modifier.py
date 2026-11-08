from typing import Dict
from pyuicompose.interfaces import ColorUnit, IModifier, Unit

from core.common import css_unit


class HtmlTagModifier(IModifier):
    def __init__(self, styles: Dict[str, str] | None = None) -> None:
        self._styles: Dict[str, str] = dict(styles or {})

    def _with(self, **styles: str | None) -> "HtmlTagModifier":
        clean = {k.replace("_", "-"): v for k, v in styles.items() if v not in ("", None)}
        return HtmlTagModifier({**self._styles, **clean})

    @staticmethod
    def _edges(prop, all, left, right, top, bottom, vertical, horizontal) -> Dict[str, str | None]:
        # ordem importa: genérico -> eixo -> lado (o último vence)
        out: Dict[str, str | None] = {}
        if all is not None:
            out[prop] = css_unit(all)
        if vertical is not None:
            out[f"{prop}_top"] = out[f"{prop}_bottom"] = css_unit(vertical)
        if horizontal is not None:
            out[f"{prop}_left"] = out[f"{prop}_right"] = css_unit(horizontal)
        for side, v in (("left", left), ("right", right), ("top", top), ("bottom", bottom)):
            if v is not None:
                out[f"{prop}_{side}"] = css_unit(v)
        return out

    def padding(self, all=None, left=None, right=None, top=None, bottom=None,
                vertical=None, horizontal=None) -> "HtmlTagModifier":
        return self._with(**self._edges("padding", all, left, right, top, bottom, vertical, horizontal))

    def margin(self, all=None, left=None, right=None, top=None, bottom=None,
               vertical=None, horizontal=None) -> "HtmlTagModifier":
        return self._with(**self._edges("margin", all, left, right, top, bottom, vertical, horizontal))

    def background(self, color: ColorUnit | None = None) -> "HtmlTagModifier":
        return self._with(background=color)

    def width(self, value: Unit) -> "HtmlTagModifier":
        return self._with(width=css_unit(value))

    def height(self, value: Unit) -> "HtmlTagModifier":
        return self._with(height=css_unit(value))

    def fill_max_width(self) -> "HtmlTagModifier":
        return self._with(width="100%")

    # detalhe do adaptador (não faz parte do contrato)
    def to_dict(self) -> Dict[str, str]:
        return dict(self._styles)

