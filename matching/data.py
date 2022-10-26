import numpy as np
import struct
import sh
import logging

from . import utils as ut

logger = logging.getLogger(__name__)
shlog = {
    "_err": lambda x: logger.error(x.strip()),
    "_out": lambda x: logger.info(x.strip()),
    "_cwd": ut.get_posix(ut.package_path())}

DAT_PATH = f"data/{{dat_file}}.dat"


def download(dat_file):
    dat_path = ut.package_path()/DAT_PATH.format(dat_file=dat_file)
    if not dat_path.is_file():
        logger.info(f"Downloading {dat_file}...")
        sh.dvc("pull",ut.get_posix(dat_path), **shlog)
    else:
        logger.info(f"Got {dat_file}. Nothing to download.")

class SiftQuery:

    def __init__(self, query_name):

        download(query_name)
        
        query_path = ut.package_path()/DAT_PATH.format(dat_file=query_name)

        with open(query_path, "rb") as fh:

            desc_count = struct.unpack("<L", fh.read(4))[0]

            self.descs = []
            for _ in range(desc_count):
                self.descs.append(np.array(struct.unpack("<128f", fh.read(512))))




class SiftAtlas:

    # adapted from tracker/src/popsift/load_sift_atlas_from_file
    def __init__(self, atlas_name):

        download(atlas_name)
        
        atlas_path = ut.package_path()/DAT_PATH.format(atlas_name=atlas_name)

        with open(atlas_path, "rb") as fh:

            s = struct.unpack("<fffffL", fh.read(24))
            self.params = dict(
                subsample=s[0],
                threshold=s[1],
                edge=s[2],
                match_max_ratio=s[3],
                match_max_dist=s[4],
            )
            region_count = s[5]

            self.descs = []
            self.coords = []
            for _ in range(region_count):
                s = struct.unpack("<LL", fh.read(8))
                # mask_id = s[0]
                desc_count = s[1]
                for _ in range(desc_count):
                    self.coords.append(np.array(struct.unpack("<3f", fh.read(12))))
                    self.descs.append(np.array(struct.unpack("<128f", fh.read(512))))
