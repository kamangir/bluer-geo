#! /usr/bin/env bash

function test_bluer_geo_version() {
    local options=$1

    abcli_eval ,$options \
        "bluer_geo version ${@:2}"

    return 0
}
