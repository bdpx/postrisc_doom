#!/usr/bin/env python3

import os
import subprocess
import platform

# ../../llvm-build-debug/bin/llvm-objdump -d --reloc ./doomgeneric.postrisc > doomgeneric.postrisc.s
# sudo perf stat -a --
# os.environ['QT_QPA_PLATFORM'] = 'xcb'

# On Windows we may build only using gcc
if platform.system() == 'Windows':
    POSTRISC_APP = "../../postrisc_release_gcc/bin/postrisc.exe"
else:
    POSTRISC_APP = "../../postrisc_release/bin/postrisc"

subprocess.run([
    POSTRISC_APP,
    "--gui",
    "--log-file=../../postrisc/docs/doom-log.html",
    "--video-capture=doom-video.mp4",
    "--profiling",
    "--timing-info",
    "--instruction-limit=10000000000", # 10 billion instructions
    "--env=LS_COLORS=ow=1;105;30:di=1;34",
    "--env=USER=user",
    "--env=LOGNAME=user",
    "--env=HOME=/home/user",
    "--env=NAME=DESKTOP",
    "--env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "--env=HOSTTYPE=postrisc",
    "--exeapp",
    "--param=doomgeneric.postrisc"
])
