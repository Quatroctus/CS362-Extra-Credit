import typing


def accuire_target_sum(array: typing.List[int], target: int):
    lookup = set()
    for v in array:
        if v in lookup:
            return [v, target - v]
        else:
            lookup.add(target - v)
    return None
