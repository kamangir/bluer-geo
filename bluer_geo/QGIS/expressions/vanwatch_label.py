import math
from qgis.core import *
from qgis.gui import *


@qgsfunction(args="auto", group="Custom", referenced_columns=[])
def vanwatch_label(row, webdings, feature, parent):
    """
    Produce label text for a vanwatch mapid.

    vanwatch_label(row)
    """
    # version 8.1.1

    row = {
        keyword: value
        for keyword, value in row.items()
        if isinstance(value, int) and value != 0
    }

    symbol = {
        "bicycle": "",
        "car": "",
        "person": "",
    }
    scale = 10

    if webdings:
        output = "".join(
            [
                thing
                for thing in [
                    "".join(
                        math.ceil(row.get(thing, 0) / scale) * [symbol.get(thing, "x")]
                    )
                    for thing in symbol.keys()
                ]
                if thing
            ]
        )
        if not output:
            return "µ"

        side = math.ceil(math.sqrt(len(output)))
        matrix = {0: []}
        j = 0
        for i in range(len(output)):
            matrix[j] += [output[i]]
            if len(matrix[j]) >= side:
                j += 1
                matrix[j] = []
        return "\n".join(["".join(thing) for thing in matrix.values()])

    return ", ".join(
        sorted(["{}:{}".format(keyword, value) for keyword, value in row.items()])
    )
