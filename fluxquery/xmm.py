#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:16:00 2020

@author: nk7g14
"""

from astroquery.heasarc import Heasarc
import astropy

from auxil import get_file

def query_master_catalogue(source_name):
    h = Heasarc()
    catalogue = h.query_object(source_name, mission='xmmmaster')
    return catalogue

def get_observation_IDs(catalogue):
    if not isinstance(catalogue, astropy.table.table.Table):
        raise TypeError('catalogue must be astropy.table.table.Table')
    return list(catalogue['OBSID'])

def download_single_observation(obsID, ODF=True, PPS=True):
    url = f'http://nxsa.esac.esa.int/nxsa-sl/servlet/data-action-aio?obsno={obsID}'
    if ODF and PPS==False:
        url = url + '&level=ODF'
    elif PPS and ODF==False:
        url = url + '&level=PPS'
        #TODO change path
    get_file(url, f'{obsID}.tar')
    
def download_multiple_observations(obsIDs, ODF=True, PPS=True):
    for obsID in obsIDs:
        download_single_observation(obsID, ODF, PPS)
    