from random import choice

def get_key(d : dict, length=4) -> str:
    letters = list(range(65,65+26))
    key = "".join(
        [chr(l) for l in random.choice(letters)]
    )
    while key in d:
        key = "".join(
            [chr(l) for l in random.choice(letters)]
        )
    return key
