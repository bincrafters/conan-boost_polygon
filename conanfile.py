#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostPolygonConan(base.BoostBaseConan):
    name = "boost_polygon"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_polygon"
    lib_short_names = ["polygon"]
    header_only_libs = ["polygon"]
    b2_requires = ["boost_config"]
