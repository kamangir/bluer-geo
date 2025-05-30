from typing import List

from bluer_options.terminal import show_usage


def help_pull(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "QGIS",
            "expressions",
            "pull",
        ],
        "pull QGIS expressions: git -> QGIS",
        {
            "from: $BLUE_GEO_QGIS_PATH_EXPRESSIONS_GIT": "",
            "to: $BLUE_GEO_QGIS_PATH_EXPRESSIONS": "",
            "https://docs.qgis.org/3.34/en/docs/user_manual/expressions": "",
        },
        mono=mono,
    )


def help_push(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "QGIS",
            "expressions",
            "push",
        ],
        "push QGIS expressions: QGIS -> git",
        {
            "from: $BLUE_GEO_QGIS_PATH_EXPRESSIONS": "",
            "to: $BLUE_GEO_QGIS_PATH_EXPRESSIONS_GIT": "",
            "https://docs.qgis.org/3.34/en/docs/user_manual/expressions": "",
        },
        mono=mono,
    )


help_functions = {
    "push": help_push,
    "pull": help_pull,
}
