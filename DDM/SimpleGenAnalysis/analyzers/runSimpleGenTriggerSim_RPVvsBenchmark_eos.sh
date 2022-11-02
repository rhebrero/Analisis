## LL SUSY RPV
python3 SimpleGenTriggerSim_RPVvsBenchmark.py --inputFile /eos/vbc/experiments/cms/store/user/escalant/SquarkToNeutralinoTo2LNu-MSquark_350_MChi_148_ctau_100mm_TuneCP5_13p6TeV_pythia8/crab_SquarkToNeutralinoTo2LNu-MSquark_350_MChi_148_ctau_100mm_TuneCP5_13p6TeV_pythia8_GS-November2022_500/221030_190707/0000/ --process RPV --trigger all --label MSquark_350_MChi_148_ctau_100mm --color 1 --triggerlabel SIM --outFolder /users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/ --nevents -1

python3 SimpleGenTriggerSim_RPVvsBenchmark.py --inputFile /eos/vbc/experiments/cms/store/user/escalant/SquarkToNeutralinoTo2LNu-MSquark_1000_MChi_148_ctau_100mm_TuneCP5_13p6TeV_pythia8/crab_SquarkToNeutralinoTo2LNu-MSquark_1000_MChi_148_ctau_100mm_TuneCP5_13p6TeV_pythia8_GS-November2022_50/221030_190649/0000/  --process RPV --trigger all --label MSquark_1000_MChi_148_ctau_100mm --color 1 --triggerlabel SIM --outFolder /users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/ --nevents -1

python3 SimpleGenTriggerSim_RPVvsBenchmark.py --inputFile /eos/vbc/experiments/cms/store/user/escalant/SquarkToNeutralinoTo2LNu-MSquark_1500_MChi_494_ctau_100mm_TuneCP5_13p6TeV_pythia8/crab_SquarkToNeutralinoTo2LNu-MSquark_1500_MChi_494_ctau_100mm_TuneCP5_13p6TeV_pythia8_GS-November2022_50/221030_190701/0000/ --process RPV --trigger all --label MSquark_1500_MChi_494_ctau_100mm --color 1 --triggerlabel SIM --outFolder /users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/ --nevents -1

## Wmu2Jets
python3 SimpleGenTriggerSim_RPVvsBenchmark.py --inputFile /eos/vbc/experiments/cms/store/user/escalant/HTo2LongLivedToWmu2jets_MH-125_MFF-50_CTau-500mm_TuneCP5_13p6TeV_pythia8/crab_HTo2LongLivedToWmu2jets_MH-125_MFF-50_CTau-500mm_TuneCP5_13p6TeV_pythia8_GS-November2022_500/221030_190643/0000/ --process RPV --trigger all --label MH-125_MFW-50_CTau-500mm --color 1 --triggerlabel SIM --outFolder /users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/ --nevents -1

python3 SimpleGenTriggerSim_RPVvsBenchmark.py --inputFile /eos/vbc/experiments/cms/store/user/escalant/HTo2LongLivedToWmu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8/crab_HTo2LongLivedToWmu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8_GS-November2022_500/221030_190636/0000/ --process RPV --trigger all --label MH-125_MFW-20_CTau-130mm --color 1 --triggerlabel SIM --outFolder /users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/ --nevents -1

## 2mu2jets
python3 SimpleGenTriggerSim_RPVvsBenchmark.py --inputFile /eos/vbc/experiments/cms/store/user/escalant/HTo2LongLivedTo2mu2jets_MH-125_MFF-50_CTau-500mm_TuneCP5_13p6TeV_pythia8/crab_HTo2LongLivedTo2mu2jets_MH-125_MFF-50_CTau-500mm_TuneCP5_13p6TeV_pythia8_GS-November2022_500/221030_190630/0000/ --process RPV --trigger all --label MH-125_MFF-50_CTau-500mm --color 1 --triggerlabel SIM --outFolder /users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/ --nevents -1

python3 SimpleGenTriggerSim_RPVvsBenchmark.py --inputFile /eos/vbc/experiments/cms/store/user/escalant/HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8/crab_HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8_GS-November2022_500/221030_190624/0000/ --process RPV --trigger all --label MH-125_MFF-20_CTau-130mm --color 1 --triggerlabel SIM --outFolder /users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/ --nevents -1

## triggered (needs GEN SIM sample)
#python3 SimpleGenTriggerSim_RPVvsBenchmark.py --inputFile /eos/vbc/experiments/cms/store/user/escalant/SquarkToNeutralinoTo2LNu-MSquark_350_MChi_148_ctau_100mm_TuneCP5_13p6TeV_pythia8/crab_SquarkToNeutralinoTo2LNu-MSquark_350_MChi_148_ctau_100mm_TuneCP5_13p6TeV_pythia8_GS-November2022_500/221030_190707/0000/ --process RPV --trigger HLT_DoubleL2Mu23NoVtx_2Cha_v3,HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v3,HLT_DoubleL3Mu10NoVtx_Displaced_v1,HLT_DoubleL3Mu10NoVtx_CosmicSeed_Displaced_v1,HLT_DoubleL2Mu10NoVtx_2Cha_PromptL3Mu0Veto_Iter3_v1,HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_PromptL3Mu0Veto_v1 --label MSquark_350_MChi_148_ctau_100mm --color 1 --triggerlabel SIM --outFolder /users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/trigger/ --nevents -1
