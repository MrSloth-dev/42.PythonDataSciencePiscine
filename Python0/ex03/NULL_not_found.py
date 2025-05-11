from types import NoneType


def NULL_not_found(object: any) -> int:
    if (isinstance(object, str) and object.__len__() == 0):
        print("Empty :", type(object))
        return 0
    elif (isinstance(object, NoneType)):
        print("Nothing :", object, type(object))
        return 0
    elif (isinstance(object, float)):
        print("Cheese :", object, type(object))
        return 0
    elif (isinstance(object, bool) and object is False):
        print("Fake :", object, type(object))
        return 0
    elif (isinstance(object, int) and object == 0):
        print("Zero :", object, type(object))
        return 0
    else:
        print("Type not Found!")
        return 1
