#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015 Yann Lanthony
# Copyright (c) 2017-2018 Spyder Project Contributors
#
# Licensed under the terms of the MIT License
# (See LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""qtsass command line interface."""

# Standard library imports
from __future__ import absolute_import
import sys

# Local imports
from qtsass import cli


if __name__ == '__main__':
    cli.main(sys.argv[1:])
