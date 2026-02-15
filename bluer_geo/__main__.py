from blueness.argparse.generic import main

from bluer_geo import NAME, VERSION, DESCRIPTION, ICON, README
from bluer_geo.logger import logger

main(
    ICON=ICON,
    NAME=NAME,
    DESCRIPTION=DESCRIPTION,
    VERSION=VERSION,
    main_filename=__file__,
    tasks={
        "build_README": README.build,
    },
    logger=logger,
)
