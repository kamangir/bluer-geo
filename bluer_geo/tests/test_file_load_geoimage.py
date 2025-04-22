import pytest
from typing import Tuple
import numpy as np


from bluer_objects import objects, storage

from bluer_geo import env
from bluer_geo.file.load import load_geoimage


@pytest.mark.parametrize(
    [
        "object_name",
        "filename",
        "expected_success",
        "expected_shape",
    ],
    [
        [
            env.BLUE_GEO_FILE_LOAD_GEOIMAGE_TEST_OBJECT,
            env.BLUE_GEO_FILE_LOAD_GEOIMAGE_TEST_FILENAME,
            True,
            (4, 1150, 1274),
        ],
        [
            env.BLUE_GEO_FILE_LOAD_GEOIMAGE_TEST_OBJECT,
            "void",
            False,
            (),
        ],
    ],
)
def test_file_load_geoimage(
    object_name: str,
    filename: str,
    expected_success: bool,
    expected_shape: Tuple[int],
) -> None:
    if expected_success:
        assert storage.download(
            object_name=object_name,
            filename=filename,
        )

    success, image, metadata = load_geoimage(
        objects.path_of(
            object_name=object_name,
            filename=filename,
        )
    )
    assert success == expected_success

    if success:
        assert isinstance(image, np.ndarray)
        assert image.shape == expected_shape, image.shape
        assert "crs" in metadata
        assert "pixel_size" in metadata
