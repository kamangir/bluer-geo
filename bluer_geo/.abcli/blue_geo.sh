#! /usr/bin/env bash

function bluer_geo() {
    local task=$(abcli_unpack_keyword $1 version)

    if [ "$task" == "pylint" ]; then
        abcli_${task} ignore=bluer_geo/QGIS,plugin=bluer_geo,$2 \
            "${@:3}"
        return
    fi

    abcli_generic_task \
        plugin=bluer_geo,task=$task \
        "${@:2}"
}

abcli_log $(bluer_geo version --show_icon 1)

gdalinfo --version
