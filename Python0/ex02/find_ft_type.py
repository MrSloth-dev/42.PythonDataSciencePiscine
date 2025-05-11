def all_thing_is_obj(object: any) -> int:
    types_str = ["list", "tuple", "set", "dict", "str"]

    if (isinstance(object, str)):
        print(object, "is in the kitchen :", type(object))
        return 42
    for typ in types_str:
        if (isinstance(object, eval(typ))):
            print(typ.capitalize(), ":", type(object))
            return 42
    else:
        print("Type not Found!")
    return 42
