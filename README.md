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

```Python
from matching.data import SiftAtlas
import matching.utils as ut

atlas =  SiftAtlas("atlas_celtics")

print(atlas.params)
print(len(atlas.descs))
print(atlas.descs[0].shape)
print(len(atlas.coords))
print(atlas.coords[0].shape)
```


## Notes

To import a new sift atlas from the Tracker monorepo, 
```bash
cd ${MATCHING_PATH}/data
dvc import git@github.com:awecom/tracker registries/nba22/data/sift_models/atlas_celtics.dat
```
