#! /usr/bin/env bash

function bluer_geo_gdal_get_crs() {
    gdalsrsinfo -o epsg ${1:-void} | tr -d '\n'
}
