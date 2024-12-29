"""Helper functions for the semantix package."""

import dataclasses
from enum import Enum
from typing import Any, Dict, Tuple, Type, get_type_hints

from pydantic import BaseModel, create_model

from pydantic_core import PydanticUndefined


def pydantic_to_dataclass(
    klass: Type[BaseModel], classname: str
) -> Any:  # noqa: ANN401
    """
    Dataclass from Pydantic model.

    Transferred entities:
        * Field names
        * Type annotations, except of Annotated etc
        * Default factory or default value

    Validators are not transferred.

    Order of fields may change due to dataclass's positional arguments.

    """
    # https://stackoverflow.com/questions/78327471/how-to-convert-pydantic-model-to-python-dataclass
    dataclass_args = []
    for name, info in klass.model_fields.items():
        if info.default_factory is not None:
            dataclass_field = dataclasses.field(
                default_factory=info.default_factory,
            )
            dataclass_arg = (name, info.annotation, dataclass_field)
        elif info.default is not PydanticUndefined:
            dataclass_field = dataclasses.field(
                default=info.get_default(),
            )
            dataclass_arg = (name, info.annotation, dataclass_field)
        else:
            dataclass_arg = (name, info.annotation)  # type: ignore
        dataclass_args.append(dataclass_arg)
    dataclass_args.sort(key=lambda arg: len(arg) > 2)
    return dataclasses.make_dataclass(
        classname or f"{klass.__name__}",
        dataclass_args,
    )


def create_class(
    classname: str, fields: Dict[str, Tuple[Type, Any]], desc: str = ""
) -> Any:  # noqa: ANN401
    """
    Create a dataclass with the given fields.

    Parameters:
    - classname (str): The name of the class to be created.
    - fields (Dict[str, Tuple[Type, Any]]): A dictionary containing the fields of the class, where the keys are the field names and the values are tuples containing the field type and default value.
    - desc (str, optional): Description of the class. Defaults to "".

    Returns:
    - Any: The created dataclass.

    """  # noqa: E501
    pydantic_model = create_model(classname, **fields)
    datacls = pydantic_to_dataclass(pydantic_model, classname)
    datacls.__doc__ = desc
    return datacls


def create_enum(
    classname: str, fields: Dict[str, Any], desc: str = ""
) -> Any:  # noqa: ANN401
    """
    Create a Enum with the given fields.

    Args:
        classname (str): The name of the Enum class.
        fields (Dict[str, Any]): A dictionary containing the field names and values for the Enum.
        desc (str, optional): A description for the Enum. Defaults to "".

    Returns:
        Any: The created Enum object.
    """
    enum_obj = Enum(classname, fields)  # type: ignore
    enum_obj.__doc__ = desc
    return enum_obj


def typed(cls: Any) -> Any:  # noqa: ANN401
    """Decorator that converts a normal Python class or dataclass into a Pydantic model."""
    hints = get_type_hints(cls)

    field_definitions = {}
    for name, hint in hints.items():
        if name in cls.__dict__:
            field_definitions[name] = (hint, cls.__dict__[name])
        else:
            field_definitions[name] = (hint, ...)

    new_cls = create_model(f"{cls.__name__}", __base__=BaseModel, **field_definitions)
    new_cls.__doc__ = cls.__doc__

    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):
            setattr(new_cls, attr_name, attr_value)

    return new_cls
