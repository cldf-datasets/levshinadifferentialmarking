# Releasing the dataset

## Requirements

Run
```shell
pip install .[test]
```
to install the dataset and the required curation software.

Make sure a local clone of https://github.com/glottolog/glottolog
is available. This can be done via [cldfbench](https://github.com/cldf/cldfbench/#catalogs).


## Release

- Recreate the CLDF data:
  ```shell
  cldfbench makecldf --with-cldfreadme --with-zenodo --glottolog-version v4.4 cldfbench_levshinadifferentialmarking.py
  ```
- and check the validity:
  ```shell
  pytest
  ```
- then recreate the README:
  ```shell
  cldfbench readme cldfbench_levshinadifferentialmarking.py
  ```
- Commit and tag the repos.
- Then create a matching release on GitHub.

