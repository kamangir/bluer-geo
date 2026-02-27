# pylint: skip-file

if not QGIS_is_live:
    from .QGIS import QGIS


QGIS.intro()
