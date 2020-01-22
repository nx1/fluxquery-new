#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:54:08 2020

@author: nk7g14
"""

import urllib
from pathlib import Path
import time
import sys
import logging

def reporthook(count, block_size, total_size):
    '''
    report hook used for urllib progress
    '''
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    if percent > 100 or percent < 0:
        sys.stdout.write("\r...%d MB, %d KB/s, %d seconds passed" %
                    (progress_size / (1024 * 1024), speed, duration))
    else:
        sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                        (percent, progress_size / (1024 * 1024), speed, duration))

def get_file(url, path):
    '''
    Retrieves the file from a given URL
    path: Save Location
    '''
    path_no_gz = path.replace('.gz', '')
    path_no_tar = path.replace('.tar', '')
    path_no_targz = path.replace('.tar.gz', '')

    path_is_file = Path(path).is_file()
    gz_is_file = Path(path_no_gz).is_file()
    tar_is_file = Path(path_no_tar).is_file()
    targz_is_file = Path(path_no_targz).is_file()
    
    if path_is_file or gz_is_file or tar_is_file or targz_is_file:
        logging.debug(f'{path} already exists, not downloading.')
        
    urllib.request.urlretrieve(url, path, reporthook)
