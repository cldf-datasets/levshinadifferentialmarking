# Releasing the dataset

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

