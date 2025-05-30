#! /usr/bin/env bash

function test_bluer_geo_datacube_get_catalog() {
    local test_asset
    local datacube_id
    local expected_catalog
    for test_asset in \
        void:void \
        datacube-generic:generic \
        $BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2:copernicus \
        $BLUE_GEO_TEST_DATACUBE_FIRMS_AREA:firms \
        $BLUE_GEO_TEST_DATACUBE_MAXAR_OPEN_DATA:maxar_open_data \
        $BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP:ukraine_timemap; do

        datacube_id=$(python3 -c "print('$test_asset'.split(':',1)[0])")
        expected_catalog=$(python3 -c "print('$test_asset'.split(':',1)[1])")

        bluer_ai_assert \
            $(bluer_geo_datacube_get catalog $datacube_id) \
            $expected_catalog
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}

function test_bluer_geo_datacube_get_raw() {
    local datacube_id
    for datacube_id in \
        $BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2 \
        $BLUE_GEO_TEST_DATACUBE_FIRMS_AREA \
        $BLUE_GEO_TEST_DATACUBE_MAXAR_OPEN_DATA \
        $BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP; do

        # raw contains special characters; hard to test.
        bluer_geo_datacube_get raw $datacube_id
    done

    return 0
}

function test_bluer_geo_datacube_get_template() {
    local test_asset
    local datacube_id
    local expected_template

    for test_asset in \
        void:unknown-template \
        datacube-generic:unknown-template \
        $BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2:unknown-template \
        $BLUE_GEO_TEST_DATACUBE_FIRMS_AREA:$BLUE_GEO_QGIS_TEMPLATE_FIRMS_AREA \
        $BLUE_GEO_TEST_DATACUBE_MAXAR_OPEN_DATA:$BLUE_GEO_QGIS_TEMPLATE_MAXAR_OPEN_DATA \
        $BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP:$BLUE_GEO_QGIS_TEMPLATE_UKRAINE_TIMEMAP; do

        datacube_id=$(python3 -c "print('$test_asset'.split(':',1)[0])")
        expected_template=$(python3 -c "print('$test_asset'.split(':',1)[1])")

        bluer_ai_assert \
            $(bluer_geo_datacube_get template $datacube_id) \
            $expected_template
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}
