import pytest

from bluer_objects.objects import unique_object

from bluer_geo.tests import assets
from bluer_geo.catalog.copernicus import CopernicusCatalog
from bluer_geo.catalog.copernicus.sentinel_2 import CopernicusSentinel2Datacube


def test_get_list_of_collections():
    catalog = CopernicusCatalog()
    assert catalog.get_list_of_collections()


def test_query():
    object_name = unique_object()

    success = CopernicusSentinel2Datacube.query(
        object_name,
        datetime="2024-07-30/2024-08-09",
        bbox=[-122.88, 51.73, -122.68, 51.93],
        count=5,
        verbose=True,
    )
    assert success


@pytest.mark.parametrize(
    ["datacube_id"],
    [
        [
            [datacube_id]
            for datacube_id, datacube_class in assets.datacubes.items()
            if datacube_class == CopernicusSentinel2Datacube
        ][-1]
    ],
)
def test_datacube_from_datacube_id(datacube_id: str):
    datacube = CopernicusSentinel2Datacube(datacube_id)

    success, _ = datacube.ingest()
    assert success

    assert datacube.list_of_files()


@pytest.mark.parametrize(
    ["datacube_id", "expected_success"],
    [
        [datacube_id, datacube_class == CopernicusSentinel2Datacube]
        for datacube_id, datacube_class in assets.datacubes.items()
    ],
)
def test_parse_datacube_id(
    datacube_id: str,
    expected_success: bool,
):
    success, _ = CopernicusSentinel2Datacube.parse_datacube_id(datacube_id)
    assert success == expected_success
