# Examples about how to do a private production in Run 3 

This is usally done in three steps, for this you need a valid grid certificate

0. identify whats the correct release, in 2022 I tested this in `CMSSW_12_4_5`

1. create the PYTHIA fragments for a given model, see [link to Gitlab Repo](https://gitlab.cern.ch/DisplacedDimuons/DisplacedDimuons/-/tree/master/SignalSamples?ref_type=heads)

2. create the CMSSW fragmenets for a given release using, `createGENFragments.py`, 

```bash
# this needs to be done inside CMSSW, after linking scripts (e.g in /nfs/cms/escalante/Displaced2023/CMSSW_12_4_5/src/Production)

# generic example
python createGENFragments.py -m BENCHMARK

# for stop and sleptons (with fragments in Fragments2022_XX folder)
python createGENFragments.py -m STOP
python createGENFragments.py -m SLEPTON

```

3. submit the jobs via crab, `crabGenerationGenProd.py`

```bash
1. put all the pythia fragments, output of cmsDriver
```

submit: 
```bash
python crabGenerationGenProd.py -f submission -v GS-October2023_ToDelete -s 100 -n 1000 -d
```

