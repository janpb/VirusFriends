#  magicblast.py
#
#  Author: Jan Piotr Buchmann <jan.buchmann@sydney.edu.au>
#  Description:
#
#  Version: 0.0

import os
import sys
import subprocess

sys.path.insert(1, os.path.join(sys.path[0], '../../'))
import lib.vdbdump.vdbdump
from . import magicblast_parser


class Magicblast:



  def __init__(self, path='magicblast', outdir='analysis'):
    self.path = path
    self.out = os.path.join(outdir,"magicblast.sam")
    self.num_threads = 4
    self.outfmt = 'sam'

  def run(self, srr, db):
    cmd = [self.path, '-db',  db,
                      '-sra', srr,
                      '-no_unaligned',
                      '-num_threads', str(self.num_threads),
                      '-outfmt', self.outfmt,
                      '-out', self.out,
                      '-splice', 'F']
    print(cmd)
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
    return proc.stdout
