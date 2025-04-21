#! /usr/bin/env bash

function bluer_geo_watch_targets_download() {
    local options=$1

    abcli_download - \
        $BLUE_GEO_WATCH_TARGET_LIST \
        "$@"

    abcli_list_log $(python3 -m bluer_geo.watch.targets \
        list \
        --log 0) \
        --before "downloaded" \
        --after "target(s)"
}
