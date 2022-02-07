object1 = {"a": { "b": { "c": "d" }}}

object2 = {"x": { "y": { "z": "a" }}}

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

for key, value in recursive_items(object1):
    print(value)

for key, value in recursive_items(object2):
    print(value)
