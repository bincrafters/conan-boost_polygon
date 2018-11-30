#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostPolygonConan(base.BoostBaseConan):
    name = "boost_polygon"
    url = "https://github.com/bincrafters/conan-boost_polygon"
    lib_short_names = ["polygon"]
    header_only_libs = ["polygon"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_mpl"
    ]
