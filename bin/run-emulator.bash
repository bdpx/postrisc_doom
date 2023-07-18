#!/usr/bin/env bash

ROOT_DIR=../..

# ${ROOT_DIR}/llvm-build/bin/llvm-objdump -d --reloc ./doomgeneric.postrisc > doomgeneric.postrisc.s

# sudo perf stat -a --
# QT_QPA_PLATFORM=xcb
${ROOT_DIR}/postrisc_release/bin/qtpostrisc \
    --exeapp \
    --log-file "doom-log.txt" \
    -- \
    doomgeneric.postrisc

# console
# ${ROOT_DIR}/postrisc_release/bin/postrisc \
#    --exeapp \
#    --log-file "doom-log.txt" \
#    -- \
#    doomgeneric.postrisc
