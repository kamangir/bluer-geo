# pylint: skip-file

if not QGIS_is_live:
    from ..logger import Q_log
    from ..application import BLUE_GEO_QGIS_APPLICATION
    from ..QGIS import QGIS


class BLUE_GEO_QGIS_APPLICATION_TEMPLATE(BLUE_GEO_QGIS_APPLICATION):
    def __init__(self):
        super().__init__("template", "🌀")

    def help_(self):
        Q_log(
            "template.func(var)",
            "func.",
            icon=self.icon,
        )

    def func(self, var: str = "🪄"):
        self.log(var)


template = BLUE_GEO_QGIS_APPLICATION_TEMPLATE()
QGIS.add_app(template)
