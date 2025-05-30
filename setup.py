from blueness.pypi import setup

from bluer_geo import NAME, VERSION, DESCRIPTION, REPO_NAME


setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.catalog",
        f"{NAME}.catalog.copernicus",
        f"{NAME}.catalog.copernicus.sentinel_2",
        f"{NAME}.catalog.firms",
        f"{NAME}.catalog.firms.area",
        f"{NAME}.catalog.generic",
        f"{NAME}.catalog.generic.stac",
        f"{NAME}.catalog.generic.generic",
        f"{NAME}.catalog.maxar_open_data",
        f"{NAME}.catalog.maxar_open_data.collection",
        f"{NAME}.catalog.ukraine_timemap",
        f"{NAME}.catalog.ukraine_timemap.ukraine_timemap",
        #
        f"{NAME}.doc",
        #
        f"{NAME}.datacube",
        f"{NAME}.datacube.label",
        #
        f"{NAME}.file",
        #
        f"{NAME}.help",
        f"{NAME}.help.catalog",
        f"{NAME}.help.datacube",
        f"{NAME}.help.watch",
        f"{NAME}.help.QGIS",
        #
        f"{NAME}.logger",
        #
        f"{NAME}.QGIS",
        f"{NAME}.QGIS.console",
        f"{NAME}.QGIS.console.apps",
        f"{NAME}.QGIS.expressions",
        #
        f"{NAME}.objects",
        f"{NAME}.objects.md",
        #
        f"{NAME}.watch",
        f"{NAME}.watch.algo",
        f"{NAME}.watch.algo.diff",
        f"{NAME}.watch.algo.modality",
        f"{NAME}.watch.targets",
        f"{NAME}.watch.targets.md",
        f"{NAME}.watch.workflow",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            "sample.env",
            ".abcli/**/*.sh",
            "**/*.md",
        ],
    },
)
