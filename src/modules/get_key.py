from random import choice

def get_key(d : dict, length=4) -> str:
    letters = list(range(65,65+26))
    key = "".join(
        [chr(choice(letters)) for i in range(length)]
    )
    while key in d:
        key = "".join(
            [chr(choice(letters)) for i in range(length)]
        )
    return key
