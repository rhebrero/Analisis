# Analyzers

This folder contains simple scripts to run directoy over GEN-SIM samples, AOD and MiniAOD samples. Useful for quick checks (but not well suited for analysis).
The output is usually simple plots and histograms. To make more involved plots (and comparisons), use the `plotters` folder.

## Existing scripts

Analyzers have have .py and run*.py, the run script creates batch compatible script

1. `SimpleGenSim.py` is a simple and self contained scripts that serves an example of an analyzer, `python simpleGenSim.py` 
2. `SimpleGenTriggerSim.py` is an analyzer that is configured via `runSimpleGenTriggerSim.py`, it can be run with many configurable arguments (and it was used for trigger efficiencies).

```bash
# Examples from submit_runSimpleGenTriggerSim.sh
python3 runSimpleGenTriggerSim.py --trigger all --label ALL --color 1

python3 runSimpleGenTriggerSim.py --trigger HLT_L1Seeds_v3 --label L1 --color 14

python3 runSimpleGenTriggerSim.py --trigger HLT_L1Seeds_cpt_v3 --label L1cpt --color 11

python3 runSimpleGenTriggerSim.py --trigger HLT_L1Seeds_upt_v3 --label L1upt --color 12

python3 runSimpleGenTriggerSim.py --trigger HLT_DoubleL2Mu23NoVtx_2Cha_v3,HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v3 --label L2 --color 2

python3 runSimpleGenTriggerSim.py --trigger HLT_DoubleL2Mu10NoVtx_2Cha_PromptL3Mu0Veto_Iter3_v1,HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_PromptL3Mu0Veto_v1 --label L2VetoPrompt --color 4

python3 runSimpleGenTriggerSim.py --trigger HLT_DoubleL3Mu10NoVtx_Displaced_v1,HLT_DoubleL3Mu10NoVtx_CosmicSeed_Displaced_v1 --label L3 --color 8

python3 runSimpleGenTriggerSim.py --trigger HLT_DoubleL2Mu23NoVtx_2Cha_v3,HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v3,HLT_DoubleL3Mu10NoVtx_Displaced_v1,HLT_DoubleL3Mu10NoVtx_CosmicSeed_Displaced_v1,HLT_DoubleL2Mu10NoVtx_2Cha_PromptL3Mu0Veto_Iter3_v1,HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_PromptL3Mu0Veto_v1 --label HLT --color 28    
```

3.  `SimpleGenTriggerSim_RPVvsBenchmark.py` is a more complex analyzer that also supports RPV SUSY samples. It is configured via `runSimpleGenTriggerSim_RPVvsBenchmark_eos.py` and it was tested with files
store in `T2_AT_Vienna`.

```bash
# Example of running on single file stored in pnfs
python3 SimpleGenTriggerSim_RPVvsBenchmark.py \
--inputFile /pnfs/ciemat.es/data/cms/store/user/escalant/HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8/crab_HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8_GS-October2023_ToDelete/231017_102029/0000/HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8_GS_1.root \
--trigger all \
--label 125_20_130 \
--color 1 \
--triggerlabel SIM \
--outFolder /nfs/cms/escalante/plots/sandbox/ \
/
```

4. `ValidateMiniAOD.py` this is an example to run on MiniAOD, it is now deprecated.

## To-do

Most scripts here have been tested in Vienna, porting to other sites would be needed. 
