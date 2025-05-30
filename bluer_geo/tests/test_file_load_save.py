import pytest
from typing import Callable, Union, List

from blueness import module
from bluer_options import string
from bluer_objects import file, objects, storage

from bluer_geo.env import BLUE_GEO_TEST_OBJECT
from bluer_geo import NAME
from bluer_geo.file.load import (
    load_geodataframe,
    load_geojson,
)
from bluer_geo.file.save import (
    save_geojson,
)
from bluer_geo.logger import logger

NAME = module.name(__file__, NAME)


@pytest.fixture
def test_object():
    object_name = BLUE_GEO_TEST_OBJECT

    assert storage.download(object_name=object_name)

    yield object_name

    logger.info(f"deleting {NAME}.test_object ...")


@pytest.mark.skip(reason="test asset is missing")
@pytest.mark.parametrize(
    [
        "load_func",
        "filename",
        "save_func",
    ],
    [
        [
            load_geodataframe,
            "vancouver.geojson",
            save_geojson,
        ],
        [
            load_geojson,
            "vancouver.geojson",
            None,
        ],
    ],
)
def test_file_load_save(
    test_object,
    load_func: Callable,
    filename: str,
    save_func: Union[Callable, None],
):
    success, thing = load_func(
        objects.path_of(
            object_name=test_object,
            filename=filename,
        )
    )
    assert success

    if not save_func is None:
        assert save_func(
            file.add_suffix(
                objects.path_of(
                    object_name=test_object,
                    filename=filename,
                ),
                string.random(),
            ),
            thing,
        )
