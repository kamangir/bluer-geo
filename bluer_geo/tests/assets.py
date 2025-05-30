from bluer_geo.catalog.generic import GenericDatacube, VoidDatacube
from bluer_geo.catalog.copernicus import CopernicusSentinel2Datacube
from bluer_geo.catalog.firms.area import FirmsAreaDatacube
from bluer_geo.catalog.maxar_open_data import MaxarOpenDataDatacube
from bluer_geo.catalog.ukraine_timemap import UkraineTimemapDatacube
from bluer_geo import env


datacubes = {
    "void": VoidDatacube,
    "void-void-void-void-void-void-void-void": VoidDatacube,
    #
    "datacube-void-void-void": VoidDatacube,
    "datacube-generic": GenericDatacube,
    #
    "datacube-copernicus-void": VoidDatacube,
    env.BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2: CopernicusSentinel2Datacube,
    #
    "datacube-firms_void-void-void-void-void": VoidDatacube,
    "datacube-firms_area-void-void-void-void": VoidDatacube,
    "datacube-firms-area-void-void-void-void": VoidDatacube,
    "datacube-firms-area-world-void-2024-07-20-1": VoidDatacube,
    "datacube-firms-area-void-MODIS_NRT-2024-09-20-1": VoidDatacube,
    env.BLUE_GEO_TEST_DATACUBE_FIRMS_AREA: FirmsAreaDatacube,
    #
    env.BLUE_GEO_TEST_DATACUBE_MAXAR_OPEN_DATA: MaxarOpenDataDatacube,
    #
    "datacube-ukraine": VoidDatacube,
    env.BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP: UkraineTimemapDatacube,
}
