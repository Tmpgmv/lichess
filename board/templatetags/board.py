from django import template

register = template.Library()

@register.filter
def letter(number):
    # Get a column letter by a given number.

    map = {1:"A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}

    result = map.get(number, "")

    return result


@register.filter
def colour(row, column):

    # Margins on the board.
    if column in [0, 9] or row in [0, 9]:
        result = "white-square"
        return result

    if (row + column) % 2 == 0:
        result = "white-square"
    else:
        result = "black-square"
    return result