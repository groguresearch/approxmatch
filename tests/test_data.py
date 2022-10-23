import logging

import matching.data as dt
import matching.utils as ut

def test1():
    atlas_descriptors, atlas_wcs, sift_parameters = dt.Sift.load_sift_atlas_from_file(ut.package_path()/"data/atlas_celtics.dat")

    desc = [d.tolist() for d in atlas_descriptors]

    logging.info("----------")
    logging.info(sift_parameters)
    logging.info(len(atlas_descriptors))
    logging.info(atlas_descriptors[0].shape)
    logging.info(len(atlas_wcs))
    logging.info(atlas_wcs[0].shape)
    logging.info(desc[0])
    ut.dump(desc,ut.package_path()/"data/atlas_celtics.json")

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()