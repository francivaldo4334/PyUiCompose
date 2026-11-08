from pyuicompose.decorators import composable
from pyuicompose.factories import component_factory
from pyuicompose.interfaces import IComponent, IModifier, Unit


@composable
def Column(modifier: IModifier | None = None) -> IComponent:
    return component_factory("column", modifier=modifier)

@composable
def Row(modifier: IModifier | None = None) -> IComponent:
    return component_factory("row", modifier=modifier)

@composable
def Spacer(height: Unit | None = None, width: Unit | None = None) -> IComponent:
    return component_factory("spacer", height=height, width=width)

@composable
def Box(modifier: IModifier | None = None) -> IComponent:
    return component_factory("box", modifier=modifier)

@composable
def Divider(modifier: IModifier | None = None) -> IComponent:
    return component_factory("divider", modifier=modifier)








