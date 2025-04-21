#! /usr/bin/env bash

function bluer_geo_datacube_ingest() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local scope=$(abcli_option "$options" scope metadata)
    local do_overwrite=$(abcli_option_int "$options" overwrite 0)
    local do_upload=$(abcli_option_int "$options" upload 0)

    local datacube_id=$(abcli_clarify_object $2 .)

    abcli_log "🧊 ingesting $datacube_id ..."

    local template_object_name=$(bluer_geo_datacube get template $datacube_id)
    local do_copy_template=1
    [[ "$template_object_name" == "unknown-template" ]] &&
        do_copy_template=0
    do_copy_template=$(abcli_option_int "$options" copy_template $do_copy_template)

    [[ "$do_copy_template" == 1 ]] &&
        abcli_clone \
            - \
            $template_object_name \
            $datacube_id

    abcli_eval - \
        python3 -m bluer_geo.datacube \
        ingest \
        --datacube_id $datacube_id \
        --dryrun $do_dryrun \
        --overwrite $do_overwrite \
        --scope $scope \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $datacube_id

    return $status
}
