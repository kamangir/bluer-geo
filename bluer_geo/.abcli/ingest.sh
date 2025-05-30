#! /usr/bin/env bash

function bluer_geo_ingest() {
    local options=$1
    local do_upload=$(bluer_ai_option_int "$options" upload 0)

    local object_name=${2:-void}

    local version=$(python3 -m bluer_geo.objects get \
        --what version \
        --object_name $object_name)
    version=$(bluer_ai_option "$options" version $version)

    local full_object_name=$object_name-$version

    local template_object_name=$(python3 -m bluer_geo.objects get \
        --what template_name \
        --object_name $object_name)
    [[ ! -z "$template_object_name" ]] &&
        bluer_objects_clone \
            - \
            $template_object_name \
            $full_object_name

    bluer_ai_log "ingesting $full_object_name ..."

    python3 -m bluer_geo.objects ingest \
        --object_name $object_name \
        --version $version \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - $full_object_name

    return $status
}
