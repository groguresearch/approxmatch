import logging

from matching.data import download, SiftAtlas
import matching.utils as ut

def test1():
    atlas = SiftAtlas("atlas_celtics")

    logging.info("----------")
    logging.info(atlas.params)
    logging.info(len(atlas.descs))
    logging.info(atlas.descs[0].shape)
    logging.info(len(atlas.coords))
    logging.info(atlas.coords[0].shape)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()