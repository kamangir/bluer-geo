#! /usr/bin/env bash

function test_bluer_geo_README() {
    local options=$1

    abcli_eval ,$options \
        bluer_geo build_README
}
