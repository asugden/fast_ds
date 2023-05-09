str1 = 'Janssen Pharmaceuticals Inc.'
str2 = 'JANSSEN INC'


def set_overlap(a: str, b: str) -> float:
    set1 = set(str1.lower().split(' '))
    set2 = set(str2.lower().split(' '))
    # Perhaps delete unnecessary words, e.g. "INC"
    # Perhaps delete unnecessary characters, e.g. "."
    return len(set1.intersection(set2))/min(len(set1), len(set2))
