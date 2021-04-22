from homework11.hw1 import SimplifiedEnum


def test_simplified_enum():
    keys = ("RED", "BLUE", "ORANGE", "BLACK")

    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = keys

    colors_enum = ColorsEnum()

    for key in keys:
        assert getattr(colors_enum, key) == key


def test_defining_enum_without_keys():
    class SomeEnum(metaclass=SimplifiedEnum):
        ...

    assert SomeEnum()


def test_defining_some_enums():
    colors = ("RED", "BLUE", "ORANGE", "BLACK")
    sizes = ("XL", "L", "M", "S", "XS")

    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = colors

    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = sizes

    colors_enum = ColorsEnum()
    sizes_enum = SizesEnum()

    for color in colors:
        assert getattr(colors_enum, color) == color

    for size in sizes:
        assert getattr(sizes_enum, size) == size
