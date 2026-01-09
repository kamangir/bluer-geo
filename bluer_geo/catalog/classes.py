from typing import List, Type

from bluer_options import env

from bluer_geo.env import BLUE_GEO_DISABLED_CATALOGS
from bluer_geo.catalog.generic import (
    GenericCatalog,
    VoidCatalog,
    GenericDatacube,
    VoidDatacube,
)

from bluer_geo.catalog.copernicus import CopernicusCatalog, CopernicusSentinel2Datacube
from bluer_geo.catalog.firms import FirmsCatalog
from bluer_geo.catalog.firms.area import FirmsAreaDatacube

if not env.INTERNET_IS_NATIONAL:
    from bluer_geo.catalog.maxar_open_data import (
        MaxarOpenDataCatalog,
        MaxarOpenDataDatacube,
    )
    from bluer_geo.catalog.ukraine_timemap import (
        UkraineTimemapCatalog,
        UkraineTimemapDatacube,
    )

list_of_catalog_classes: List[Type[GenericCatalog]] = [GenericCatalog, FirmsCatalog] + (
    []
    if env.INTERNET_IS_NATIONAL
    else [
        CopernicusCatalog,
        MaxarOpenDataCatalog,
        UkraineTimemapCatalog,
    ]
)

list_of_catalogs: List[str] = sorted(
    [
        catalog_name
        for catalog_name in [
            catalog_class.name for catalog_class in list_of_catalog_classes
        ]
        if catalog_name not in BLUE_GEO_DISABLED_CATALOGS.split(",")
    ]
)

list_of_datacube_classes: List[Type[GenericDatacube]] = [
    GenericDatacube,
    FirmsAreaDatacube,
] + (
    []
    if env.INTERNET_IS_NATIONAL
    else [
        UkraineTimemapDatacube,
        CopernicusSentinel2Datacube,
        MaxarOpenDataDatacube,
    ]
)
