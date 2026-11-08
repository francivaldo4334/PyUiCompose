from pyuicompose.interfaces import Unit


def css_unit(value: Unit) -> str:
    if isinstance(value, (int, float)):
        return f"{value}px"
    return str(value)


