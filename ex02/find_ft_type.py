def all_thing_is_obj(object: any) -> int:
    if type(object) == str:
        print(f"{object} is in the kitchen : {type(object)}")
    if type(object) == int:
        print("Type not found")

    elif type(object) == list or type(object) == tuple or type(object) == set or type(object) == dict:
        obj = type(object);
        print(f"{obj.__name__.capitalize()} : {obj}")

    return 42

#Write a function that prints the object types and returns 42.