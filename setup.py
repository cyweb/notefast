#!/usr/bin/python3

import sys
if sys.version_info < (3, 2):
    sys.exit('NoteFast requires Python 3.2 or newer')

from distutils.core import setup
from DistUtilsExtra.command import *

import re
import glob
from subprocess import Popen, PIPE



VERSION="1.0.0"

setup(name="notefast",
      version=VERSION,
      description="Writing note fast witout save button.",
      author="Can Yalçın",
      author_email="onetoy@gmail.com",
      long_description= ( open('README.md').read() + '\n'),
      classifiers=[
        "Development Status :: 1 - Beta",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Editor",
       ],
      keywords='note notefast editor edit write save note it fast',
      url='https://github.com/cyweb/notefast',
      license='GPLv3',
      scripts=["bin/notefast"
               ],
      packages = ['notefast',
                 ],
      data_files=[
                  ('share/notefast/images/', glob.glob("data/images/*png")),
                  ('share/notefast/icons/', glob.glob("data/icons/*png")),
                  ('share/applications/', glob.glob("data/*desktop")),
                  ],
      cmdclass = { "build" : build_extra.build_extra,
                   "build_i18n" :  build_i18n.build_i18n,
                   "build_help" : build_help.build_help,
                   "build_icons" : build_icons.build_icons}
      )

