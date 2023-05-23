#!/usr/bin/env python

"""Tests for `addana` package."""


import sys

sys.path.append('..')
import  addana

def test_addana():
    print(addana.transform(["吉林：吉林"]))
test_addana()
