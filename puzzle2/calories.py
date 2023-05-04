from pathlib import Path
from typing import List


def read_input(file: Path) -> List[List[str]]:
    lstvalues = []
    with open(file, "r") as f:
        value = f.read()
    values = value.split("\n\n")
    for v in values:
        lstvalues.append(v.split("\n"))
    return lstvalues


def get_max(lst: List[List[str]]) -> List[int]:
    new_lst = [list(map(int, i)) for i in lst]
    max_values = list(map(sum, new_lst))
    return max_values


def get_top3_max(lst: List[int]) -> int:
    top_1 = lst.pop(lst.index(max(lst)))
    top_2 = lst.pop(lst.index(max(lst)))
    top_3 = lst.pop(lst.index(max(lst)))

    lst_result = [top_1, top_2, top_3]
    return sum(lst_result)


if __name__ == "__main__":
    filename = Path(__file__).parent / "calorie_input.txt"
    result = read_input(filename)
    print(result)
    print(type(result))
    print(get_max(result))
    print(max(get_max(result)))
    print(get_top3_max(get_max(result)))
