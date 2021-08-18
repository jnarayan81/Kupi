#!/usr/bin/env python

# Author: Jitendra Narayan (jnarayan@igib.res.in)
# Genomics lab http://igib.in
# Description: python script for NEW SARC-CoV-2 variants detection
###############################################################################

import sys
import argparse
import os
import subprocess
import os.path
import fileinput

from KAPP.introduce import *
from KAPP.greet import SayHello as SH
from KAPP.cleaner import *
from KAPP.alignment import *

intro(0.01)
usage()
who()
