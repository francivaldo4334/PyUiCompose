from typing import Dict
from pyuicompose.interfaces import IBuilder, IComponent
from core.common import css_unit
from core.implements.modifier import HtmlTagModifier

TAGS: Dict[str, str] = {
    "column": "div",
    "row": "div",
    "spacer": "div",
    "text": "span",
    "button": "button",
    "card": "div",
    "divider": "div",
    "box": "div",
    "image": "img",
    "checkbox": "input",
}

BASE_STYLES: Dict[str, Dict[str, str]] = {
    "column": {"display": "flex", "flex-direction": "column"},
    "row": {"display": "flex", "flex-direction": "row"},
}


class HtmlTagBuilder(IBuilder):
    def render(self):
        return 
    def _style_of(self, node: IComponent) -> Dict[str, str]:
        styles = dict(BASE_STYLES.get(node.kind, {}))

        if node.kind == "spacer":
            if node.props.get("height") is not None:
                styles["height"] = css_unit(node.props["height"])
            if node.props.get("width") is not None:
                styles["width"] = css_unit(node.props["width"])

        if isinstance(node.modifier, HtmlTagModifier):
            styles.update(node.modifier.to_dict())  # modifier sobrescreve a base
        return styles

    def _render(self, node: IComponent) -> str:
        tag = TAGS[node.kind]
        styles = self._style_of(node)
        attr_str = f' style="{"; ".join(f"{k}: {v}" for k, v in styles.items())}"' if styles else ""
        inner = node.text + "".join(self._render(c) for c in node.children)
        return f"<{tag}{attr_str}>{inner}</{tag}>"

