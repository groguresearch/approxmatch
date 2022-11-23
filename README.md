# matching

## Install

On your machine, install git, aws, dvc.
- See https://www.notion.so/awecom/New-Machines-3cf135449f5e485dbcb812ccdc058eeb
- Make sure you have the shared dvc-cache `/home/shared/dvc-cache`

On your user account, set up git, aws, dvc, mamba.
- See https://www.notion.so/awecom/New-Users-9817e400213e4fa7aea3312066e610ed

Git clone `tracker` repo. Add repo path and `.rc` to your `~/.bashrc` and source it. We need the tracker repo for its utilities and the mamba shortcuts.
```bash
cd ~/src
git clone --recursive git@github.com:awecom/tracker.git
echo '
export TRACKER_PATH="${HOME}/src/tracker"
source "${TRACKER_PATH}"/.rc
' >> ~/.bashrc
source ~/.bashrc
```

Git clone `matching` repo. Add repo path to your `~/.bashrc` and source it.
```bash
cd ~/src
git clone git@github.com:groguresearch/matching.git
echo 'export MATCHING_PATH="${HOME}/src/matching"' >> ~/.bashrc
source ~/.bashrc
```

Install matching as Python package (the mamba shortcut `add $ENV_NAME` installs the package and its dependencies in the `$ENV_NAME` environment)
```bash
cd ${MATCHING_PATH}
add matching
```

## Usage
The code. The data will be downloaded in the background if it is not yet on the machine.

```Python
from matching.data import SiftAtlas, SiftQuery

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
```
The output.
```
INFO:matching.data:Got atlas_celtics. Nothing to download.
atlas.params {'subsample': 0.0, 'threshold': 0.009999999776482582, 'edge': 50.0, 'match_max_ratio': 0.5, 'match_max_dist': 0.20000000298023224}
len(atlas.descs) 8400
atlas.descs[0].shape (128,)
len(atlas.coords) 8400
atlas.coords[0].shape (3,)
INFO:matching.data:Got query_500000. Nothing to download.
INFO:root:len(query.descs) 10815
INFO:root:query.descs[0].shape (128,)
INFO:root:query.descs[0]
[0.02780632 0.01143986 0.01076741 0.01244822 0.00994696 0.16006026
 0.25724468 0.04848445 0.16704617 0.08272785 0.00733572 0.00126691
 0.013832   0.20215379 0.13231426 0.07245468 0.15825371 0.08092273
 0.04651816 0.04548531 0.11434859 0.16133922 0.08783644 0.08591869
 0.00114933 0.00206406 0.01521663 0.02433823 0.09948147 0.12861416
 0.04122205 0.00491224 0.06167318 0.049609   0.17502598 0.16751148
 0.02944523 0.05302409 0.12308072 0.03771553 0.21643524 0.11682261
 0.05836961 0.06744396 0.03656355 0.04722667 0.06069295 0.06906815
 0.10383139 0.05358288 0.         0.         0.14084993 0.14363115
 0.04793772 0.04383607 0.         0.         0.         0.
 0.07295884 0.07717411 0.00726856 0.         0.06272227 0.05305695
 0.15168756 0.20846936 0.18709272 0.01956368 0.02291066 0.03454239
 0.11891917 0.05570934 0.07869437 0.13282201 0.16491579 0.05522606
 0.07010751 0.13741943 0.04845703 0.02644974 0.03479431 0.02882611
 0.08426031 0.13756539 0.08186147 0.07849246 0.         0.
 0.         0.00121324 0.03579413 0.04672759 0.02484115 0.
 0.06784992 0.04004632 0.06022728 0.11274634 0.14350928 0.03729729
 0.07101361 0.07942967 0.03058601 0.05692225 0.19535668 0.17256418
 0.1401725  0.03156943 0.02194773 0.04124083 0.01773757 0.0336997
 0.08431069 0.11749943 0.13537128 0.05770232 0.03118194 0.02711516
 0.         0.         0.         0.01307158 0.02625066 0.02046204
 0.01583879 0.        
```
## Notes

To import a new sift atlas from the Tracker monorepo, 
```bash
cd ${MATCHING_PATH}/data
dvc import git@github.com:awecom/tracker registries/nba22/data/sift_models/atlas_celtics.dat
```
