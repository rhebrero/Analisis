# Examples about how to do a private production in Run 3 

This is usally done in three steps, for this you need a valid grid certificate

0. identify whats the correct release, in 2022 I tested this in `CMSSW_12_4_5`

1. create the PYTHIA fragments for a given model, see [link to Gitlab Repo](https://gitlab.cern.ch/DisplacedDimuons/DisplacedDimuons/-/tree/master/SignalSamples?ref_type=heads)

2. create the CMSSW fragmenets for a given release using, `createGENFragments.py` 

3. submit the jobs via crab, `crabGenerationGenProd.py`