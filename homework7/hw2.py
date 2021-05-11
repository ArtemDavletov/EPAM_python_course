"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def pop_item(arr: list):
    try:
        return arr.pop()
    except IndexError:
        ...


def simplify_input_string(string: str):
    ans = []

    for i in string:
        if i == "#":
            pop_item(ans)
        else:
            ans.append(i)
    return "".join(ans)


def backspace_compare(first: str, second: str):
    simplified_first = simplify_input_string(first)
    simplified_second = simplify_input_string(second)
    return hash(simplified_first) == hash(simplified_second)
