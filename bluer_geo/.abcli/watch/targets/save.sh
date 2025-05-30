#! /usr/bin/env bash

function bluer_geo_watch_targets_save() {
    local options=$1
    local target_name=$(bluer_ai_option "$options" target all)

    local object_name=$(bluer_ai_clarify_object $2 .)

    bluer_objects_clone \
        ~relate \
        $BLUE_GEO_QGIS_TEMPLATE_WATCH \
        $object_name

    python3 -m bluer_geo.watch.targets save \
        --target_name $target_name \
        --object_name $object_name \
        "${@:3}"
}
