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

def test3():
    atlas =  SiftAtlas("atlas_celtics")

    print(f"atlas.params {atlas.params}")
    print(f"len(atlas.descs) {len(atlas.descs)}")
    print(f"atlas.descs[0].shape {atlas.descs[0].shape}")
    print(f"len(atlas.coords) {len(atlas.coords)}")
    print(f"atlas.coords[0].shape {atlas.coords[0].shape}")

    query = SiftQuery("query_500000")
        
    logging.info(f"len(query.descs) {len(query.descs)}")
    logging.info(f"query.descs[0].shape {query.descs[0].shape}")
    logging.info(f"query.descs[0]\n{query.descs[0]}")

def test4():
    atlas_name = "atlas_celtics"
    atlas =  SiftAtlas(atlas_name)
    print(np.array(atlas.descs).shape)

    atlas_file = ut.package_path()/f"data/{atlas_name}.npy"
    np.save(atlas_file, np.array(atlas.descs))

    query_name = "query_500000"
    query = SiftQuery(query_name)
    print(np.array(query.descs).shape)

    query_file = ut.package_path()/f"data/{query_name}.npy"
    np.save(query_file, np.array(query.descs))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test4()