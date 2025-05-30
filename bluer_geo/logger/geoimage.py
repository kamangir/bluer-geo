from typing import List
import json
import numpy as np

from blueness import module
from bluer_options import string
from bluer_objects import file, objects
from bluer_objects.logger.matrix import log_matrix
from bluer_flow import fullname as bluer_flow_fullname

from bluer_geo import fullname
from bluer_geo.file.load import load_geoimage
from bluer_geo import NAME

NAME = module.name(__file__, NAME)


def log_geoimage(
    object_name: str,
    filename: str,
    header: List[str] = [],
    footer: List[str] = [],
    colormap: int = -1,  # example: cv2.COLORMAP_JET
    log: bool = True,
    verbose: bool = True,
    **kwargs,
) -> bool:
    full_filename = objects.path_of(
        filename=filename,
        object_name=object_name,
    )

    success, matrix, metadata = load_geoimage(
        full_filename,
        log=log,
    )
    if not success:
        return success

    matrix = np.transpose(matrix, (1, 2, 0))

    metadata_as_str: List[str] = []
    try:
        for keyword, value in metadata.items():
            try:
                metadata_as_str += [f"{keyword}={json.dumps(value)}"]
            except Exception:
                metadata_as_str += [f"{keyword}=..."]
    except Exception:
        pass

    if matrix.ndim == 2:
        matrix = np.expand_dims(matrix, axis=-1)

    if matrix.shape[2] == 1:
        matrix = np.repeat(matrix, 3, axis=2)

    if matrix.shape[2] > 3:
        matrix = matrix[:, :, :3]

    range_signature: List[str] = [string.pretty_shape_of_matrix(matrix)]
    if colormap == -1 and matrix.dtype != np.uint8:
        matrix = matrix.astype(np.float64)

        for index in range(matrix.shape[2]):
            min_value = np.min(matrix[:, :, index])
            max_value = np.max(matrix[:, :, index])

            matrix[:, :, index] = (
                255
                * (matrix[:, :, index] - min_value)
                / (max_value - min_value + np.finfo(np.float64).eps)
            )

            range_signature += [f"range[{index}]: {min_value:.3f} ... {max_value:.3f}"]

        matrix = matrix.astype(np.uint8)

    return log_matrix(
        matrix=matrix,
        filename=file.add_extension(full_filename, "png"),
        header=objects.signature(
            info=filename,
            object_name=object_name,
        )
        + metadata_as_str
        + range_signature
        + header,
        footer=[
            fullname(),
            bluer_flow_fullname(),
        ]
        + footer,
        colormap=colormap,
        log=log,
        verbose=verbose,
        log_shape_of_matrix=False,
        **kwargs,
    )
