import pytest

from bluer_objects import objects, storage
from bluer_objects.env import ABCLI_OBJECT_ROOT

from bluer_geo.env import BLUE_GEO_WATCH_TARGET_LIST
from bluer_geo.QGIS.dependency import list_of_dependencies


@pytest.mark.parametrize(
    ["object_name"],
    [[BLUE_GEO_WATCH_TARGET_LIST]],
)
def test_parse_datacube_id(
    object_name: str,
):
    assert storage.download(
        object_name=object_name,
        filename=f"{object_name}.qgz",
    )

    output = list_of_dependencies(
        objects.path_of(
            filename=f"{object_name}.qgz",
            object_name=object_name,
        ),
        ABCLI_OBJECT_ROOT,
    )

    assert isinstance(output, list)
    assert output
    assert object_name in output
