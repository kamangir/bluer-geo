import pytest
from shapely.geometry import Polygon

from bluer_objects import file, objects

from bluer_geo.tests.test_target_list import target_list
from bluer_geo.watch.targets import TargetList, Target


@pytest.mark.parametrize(
    ["target_name"],
    [["Miduk"]],
)
def test_target(
    target_list: TargetList,
    target_name: str,
):
    target = target_list.list_of_targets[target_name]

    assert isinstance(target, Target)

    assert target.one_liner

    polygon = target.polygon
    assert isinstance(polygon, Polygon)

    object_name = objects.unique_object()

    assert target.save(object_name)

    assert file.exists(
        objects.path_of(
            filename="target/shape.geojson",
            object_name=object_name,
        )
    )
