#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)
