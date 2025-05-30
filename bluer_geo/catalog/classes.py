from typing import List, Type

from bluer_geo import env
from bluer_geo.catalog.generic import (
    GenericCatalog,
    VoidCatalog,
    GenericDatacube,
    VoidDatacube,
)
from bluer_geo.catalog.copernicus import CopernicusCatalog, CopernicusSentinel2Datacube
from bluer_geo.catalog.firms import FirmsCatalog
from bluer_geo.catalog.firms.area import FirmsAreaDatacube
from bluer_geo.catalog.maxar_open_data import (
    MaxarOpenDataCatalog,
    MaxarOpenDataDatacube,
)
from bluer_geo.catalog.ukraine_timemap import (
    UkraineTimemapCatalog,
    UkraineTimemapDatacube,
)

list_of_catalog_classes: List[Type[GenericCatalog]] = [
    GenericCatalog,
    CopernicusCatalog,
    FirmsCatalog,
    MaxarOpenDataCatalog,
    UkraineTimemapCatalog,
]

list_of_catalogs: List[str] = sorted(
    [
        catalog_name
        for catalog_name in [
            catalog_class.name for catalog_class in list_of_catalog_classes
        ]
        if catalog_name not in env.BLUE_GEO_DISABLED_CATALOGS.split(",")
    ]
)

list_of_datacube_classes: List[Type[GenericDatacube]] = [
    GenericDatacube,
    FirmsAreaDatacube,
    UkraineTimemapDatacube,
    CopernicusSentinel2Datacube,
    MaxarOpenDataDatacube,
]
