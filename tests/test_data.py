import logging
import struct
import numpy as np

from matching.data import SiftAtlas, SiftQuery
import matching.utils as ut

def test1():
    atlas = SiftAtlas("atlas_celtics")

    logging.info("----------")
    logging.info(atlas.params)
    logging.info(len(atlas.descs))
    logging.info(atlas.descs[0].shape)
    logging.info(len(atlas.coords))
    logging.info(atlas.coords[0].shape)

def test2():
    query = SiftQuery("query_120000")
    
    logging.info("----------")
    logging.info(len(query.descs))
    logging.info(query.descs[0].shape)
    logging.info(query.descs[0])


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test2()