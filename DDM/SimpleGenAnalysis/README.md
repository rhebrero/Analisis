# SimpleGenAnalysis

This folder contains basic, general scripts, used by the plotter and analyzer,

1. `GenLongLivedUtils.py` includes tools to use gen level information
2. `RecoUtils.py` general functions to be used when running on a AOD, reconstructe sample. 
3. `ResolutionUtils.py` unused (?). *TBC*.
4. `myMathUtils.py` basic math operations.
5. `SimpleTools.py` plotter and ratio plotter.
6. `SamplesDatabase.py` database of all signal samples.

These scripts are liked to `plotters` and `analyzer` via:

`python linkUtils.py`

*update*: linking is not needed anymore, now packages are loaded via `utils/getLibraries.py`. 