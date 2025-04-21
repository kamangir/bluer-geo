from typing import List

from bluer_ai.host import signature as abcli_signature
from bluerflow import fullname as bluerflow_fullname

from bluer_geo import fullname


def signature() -> List[str]:
    return [
        fullname(),
        bluerflow_fullname(),
    ] + abcli_signature()
