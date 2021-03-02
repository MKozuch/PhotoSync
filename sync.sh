#!/usr/bin/env bash

if [[ $# -ne 2 ]]; then
    echo "Usage: [sourcedir, destdir]"
    exit -1
fi

sourcedir=$1
destdir=$2

python3 sync_helper.py <(find "$1"  -type f -exec md5sum {} \; | sort) <(find "$2" -type f -exec md5sum {} \; | sort) | xargs cp -v -t $2

