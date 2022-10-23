import logging

from matching.data import SiftAtlas
import matching.utils as ut

def test1():
    atlas =  SiftAtlas(ut.package_path()/"data/atlas_celtics.dat")

    logging.info("----------")
    logging.info(atlas.params)
    logging.info(len(atlas.descs))
    logging.info(atlas.descs[0].shape)
    logging.info(len(atlas.coords))
    logging.info(atlas.coords[0].shape)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()