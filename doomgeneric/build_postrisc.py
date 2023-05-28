#!/usr/bin/env python3

import os
import shutil
import subprocess

# https://github.com/ozkl/doomgeneric
# git@github.com:ozkl/doomgeneric.git

# git remote add upstream git@github.com:ozkl/doomgeneric.git
# git remote -v
# git fetch upstream
# git rebase upstream/master

shutil.rmtree("./build", ignore_errors=True)

subprocess.run([
    "make", "-f", "Makefile.postrisc", "-j8"
])
