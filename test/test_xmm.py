#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:53:34 2020

@author: Norman Khan

Test file for fluxquery/xmm/xmm.py
"""

import pytest
from fluxquery import xmm
import astroquery

from auxil.fetchfile import get_file

@pytest.fixture
def test_query_master_catalogue():
    result = xmm.query_master_catalogue('NGC1313')
    assert len(result) >= 35
    return result


def test_bad_query_master_catalogue():
    with pytest.raises(astroquery.exceptions.InvalidQueryError):
        result = xmm.query_master_catalogue('monkey')
    
def test_get_observation_IDs(test_query_master_catalogue):
    cat = test_query_master_catalogue
    obsids = xmm.get_observation_IDs(cat)
    assert '0150281101' in obsids
    assert len(obsids) == len(cat)
    
def test_bad_type_get_observation_IDs():
    with pytest.raises(TypeError, match='catalogue must be astropy.table.table.Table'):
        obsids = xmm.get_observation_IDs(7)

def test_download_observations():
    xmm.download_single_observation('0150281101')
