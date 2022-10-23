import numpy as np
import struct

from . import utils as ut

# from tracker/src/popsift/load_sift_atlas_from_file
class Sift:

    @classmethod
    def read_int32(cls, fp):
        the_bytes = fp.read(4)
        int_value = struct.unpack("<L", the_bytes)[0]
        return int_value

    @classmethod
    def read_float32(cls, fp):
        the_bytes = fp.read(4)
        float_value = struct.unpack("<f", the_bytes)[0]
        return float_value

    @classmethod
    def read_3(cls, fp):
        v = np.zeros(shape=(3,), dtype=np.float32)
        for i in range(3):
            v[i] = cls.read_float32(fp)
        return v

    @classmethod
    def read_128_float32s(cls, fp):
        v = np.zeros(shape=(128,), dtype=np.float32)
        for i in range(128):
            v[i] = cls.read_float32(fp)
        return v

    @classmethod
    def load_sift_atlas_from_file(cls, altas_file_name):

        print(f"opening  atlas-file {altas_file_name}")

        # open the altas-file:
        fh = open(altas_file_name, "rb")

        SIFT_SUBSAMPLE = cls.read_float32(fh)
        print(f"apparently {SIFT_SUBSAMPLE=}")

        SIFT_THRESH = cls.read_float32(fh)
        print(f"apparently {SIFT_THRESH=}")

        SIFT_EDGE = cls.read_float32(fh)
        print(f"apparently {SIFT_EDGE=}")

        SIFT_MATCH_RATIO_MAX = cls.read_float32(fh)
        print(f"apparently {SIFT_MATCH_RATIO_MAX=}")

        SIFT_MATCH_MAXDIST = cls.read_float32(fh)
        print(f"apparently {SIFT_MATCH_MAXDIST=}")

        n_regions = cls.read_int32(fh)
        print(f"apparently {n_regions=}")

        atlas_descriptors = []
        atlas_wcs = []

        for region_idx in range(n_regions):
            print(f"for region {region_idx}")
            mask_id = cls.read_int32(fh)
            print(f"{mask_id=}")
            num_descriptors = cls.read_int32(fh)
            print(f"{num_descriptors=}")
            for descriptor_id in range(num_descriptors):
                world_position = cls.read_3(fh)
                descriptor = cls.read_128_float32s(fh)
                atlas_descriptors.append(descriptor)
                atlas_wcs.append(world_position)

        fh.close()
        num_atlas_descriptors = len(atlas_descriptors)
        print(f"Apparently there are {num_atlas_descriptors=}")

        sift_parameters = dict(
            SIFT_SUBSAMPLE=SIFT_SUBSAMPLE,
            SIFT_THRESH=SIFT_THRESH,
            SIFT_EDGE=SIFT_EDGE,
            SIFT_MATCH_RATIO_MAX=SIFT_MATCH_RATIO_MAX,
            SIFT_MATCH_MAXDIST=SIFT_MATCH_MAXDIST,
        )
        return atlas_descriptors, atlas_wcs, sift_parameters
