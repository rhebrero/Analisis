# Utils for Longlived Generator Level studies.
from utils import getLibraries
from GenLongLivedUtils import *
from SimpleTools import *

# colors that have been defined in SimpleTools.py
#  {"black":1, "red":2, "light-green":3, "blue":4, "green": 8, "light-brown":11, "dark-gray":12, "gray":14}

# input and outputs - CIEMAT
inputFolder = "/nfs/cms/escalante/plots/plots_SimpleGenTriggerSim_RPVvsBenchmark/"
outputFolder = "/nfs/cms/escalante/plots/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/"

# smuon
studies_SMUON = {}
studies_SMUON["Overview"] = []
studies_SMUON["Overview"] = addInput(studies_SMUON["Overview"], inputFolder + "MSMuon_100_ctau-8000/", "MSMuon_100_ctau-8000", "#tilde{l}(100)  800 cm", 8)
studies_SMUON["Overview"] = addInput(studies_SMUON["Overview"], inputFolder + "MSMuon_200_ctau-6000/", "MSMuon_200_ctau-6000", "#tilde{l}(200)  600 cm", 4)
studies_SMUON["Overview"] = addInput(studies_SMUON["Overview"], inputFolder + "MSMuon_400_ctau-2000/", "MSMuon_400_ctau-2000", "#tilde{l}(400), 200 cm", 2)
studies_SMUON["Overview"] = addInput(studies_SMUON["Overview"], inputFolder + "MSMuon_700_ctau-700/", "MSMuon_700_ctau-700", "#tilde{l}(700), 70 cm", 1)
studies_SMUON["Overview"] = addInput(studies_SMUON["Overview"], inputFolder + "MSMuon_400_ctau-2000/", "MSMuon_400_ctau-2000", "#tilde{l}(400), 200 cm", 2)

studies_SMUON["Overview_simple"] = []
studies_SMUON["Overview_simple"] = addInput(studies_SMUON["Overview_simple"], inputFolder + "MSMuon_100_ctau-8000/", "MSMuon_100_ctau-8000", "#tilde{l}(100)  800 cm", 8)
studies_SMUON["Overview_simple"] = addInput(studies_SMUON["Overview_simple"], inputFolder + "MSMuon_200_ctau-6000/", "MSMuon_200_ctau-6000", "#tilde{l}(200)  600 cm", 4)

# interesting studies for smuons
do_studies_SMUON  = ["Overview", "Overview_simple"]

# input and outputs - HEPHY
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/"

# RPV
studies_RPV = {}
studies_RPV["Overview"] = []
studies_RPV["Overview"] = addInput(inputs, inputFolder + "MSquark_1500_MChi_494_ctau_100mm/", "RPV_MSquark_1500_MChi_494_ctau_100mm", "#tilde{q}(1500), #chi(494), 100 mm", 8)
studies_RPV["Overview"] = addInput(inputs, inputFolder + "MSquark_1000_MChi_148_ctau_100mm/",  "RPV_MSquark_1000_MChi_148_ctau_100mm","#tilde{q}(1000), #chi(148), 100 mm", 4)

studies_RPV["RPV-RunI"] = []
studies_RPV["RPV-RunI"] = addInput(inputs, inputFolder + "MSquark_1500_MChi_494_ctau_100mm/", "RPV_MSquark_1500_MChi_494_ctau_100mm", "#tilde{q}(1500), #chi(494), 100 mm", 8)
studies_RPV["RPV-RunI"] = addInput(inputs, inputFolder + "MSquark_1000_MChi_148_ctau_100mm", "RPV_MSquark_1000_MChi_148_ctau_100mm", "#tilde{q}(1000), #chi(148), 100 mm", 4) 
studies_RPV["RPV-RunI"] = addInput(inputs, inputFolder + "MSquark_350_MChi_148_ctau_100mm/", "RPV_MSquark_350_MChi_148_ctau_100mm", "#tilde{q}(350), #chi(148), 100 mm", 2)
studies_RPV["RPV-RunI"] = addInput(inputs, inputFolder + "MSquark_120_MChi_48_ctau_100mm/", "RPV_MSquark_120_MChi_48_ctau_100mm", "#tilde{q}(120), #chi(48), 100 mm", 1)

studies_RPV["Compressed"] = []
studies_RPV["Compressed"] = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/", "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 8)
studies_RPV["Compressed"] = addInput(inputs, inputFolder + "MSquark_220_MChi_200_ctau_100mm/", "RPV_MSquark_220_MChi_200_ctau_100mm", "#tilde{q}(220), #chi(200), 100 mm", 4) 
studies_RPV["Compressed"] = addInput(inputs, inputFolder + "MSquark_330_MChi_300_ctau_100mm/", "RPV_MSquark_330_MChi_300_ctau_100mm", "#tilde{q}(330), #chi(300), 100 mm", 2) 
studies_RPV["Compressed"] = addInput(inputs, inputFolder + "MSquark_440_MChi_400_ctau_100mm/", "RPV_MSquark_440_MChi_400_ctau_100mm", "#tilde{q}(440), #chi(400), 100 mm", 1)

studies_RPV["Low-pT"] = []
studies_RPV["Low-pT"] = addInput(inputs, inputFolder + "MSquark_120_MChi_48_ctau_100mm/", "RPV_MSquark_120_MChi_48_ctau_100mm", "#tilde{q}(120), #chi(48), 100 mm", 1)
studies_RPV["Low-pT"] = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/", "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 2)
studies_RPV["Low-pT"] = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 4)

studies_RPV["RPV-All"] = []
studies_RPV["RPV-All"] = addInput(inputs, inputFolder + "MSquark_1500_MChi_494_ctau_100mm/", "RPV_MSquark_1500_MChi_494_ctau_100mm", "#tilde{q}(1500), #chi(494), 100 mm", 8)
studies_RPV["RPV-All"] = addInput(inputs, inputFolder + "MSquark_1000_MChi_148_ctau_100mm/",  "RPV_MSquark_1000_MChi_148_ctau_100mm","#tilde{q}(1000), #chi(148), 100 mm", 4) 
studies_RPV["RPV-All"] = addInput(inputs, inputFolder + "MSquark_350_MChi_148_ctau_100mm/",  "RPV_MSquark_350_MChi_148_ctau_100mm",   "#tilde{q}(350), #chi(148), 100 mm", 2) 
studies_RPV["RPV-All"] = addInput(inputs, inputFolder + "MSquark_120_MChi_48_ctau_100mm/", "RPV_MSquark_120_MChi_48_ctau_100mm", "#tilde{q}(120), #chi(48), 100 mm", 1)

studies_RPV["MSquark_110_100"] = []
studies_RPV["MSquark_110_100"] = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_1mm/",     "RPV_MSquark_110_MChi_100_ctau_1mm", "#tilde{q}(110), #chi(100), 1 mm", 1)
studies_RPV["MSquark_110_100"] = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/",   "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 2)
studies_RPV["MSquark_110_100"] = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_10000mm/", "RPV_MSquark_110_MChi_100_ctau_10000mm", "#tilde{q}(110), #chi(100), 10000 mm", 4)
studies_RPV["MSquark_110_100"] = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 1)
studies_RPV["MSquark_110_100"] = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 1)
studies_RPV["MSquark_110_100"] = addInput(inputs, inputFolder + "MH-125_MFF-20_CTau-130mm/", "RPV_MH-125_MFF-20_CTau-130mm", "h(125), X(20), 130 mm", 39)

studies_RPV["HtoZd_HtoXX"] = []
studies_RPV["HtoZd_HtoXX"] = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 1)
studies_RPV["HtoZd_HtoXX"] = addInput(inputs, inputFolder + "MH-125_MFF-20_CTau-130mm/", "RPV_MH-125_MFF-20_CTau-130mm", "h(125), X(20), 130 mm", 39)
studies_RPV["HtoZd_HtoXX"] = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-07/", "RPV_MZd_20_Epsilon-5e-07", "Z_{D}(20), #epsilon = 5e-07", 3)
studies_RPV["HtoZd_HtoXX"] = addInput(inputs, inputFolder + "MZd_20_Epsilon-2e-07/", "RPV_MZd_20_Epsilon-2e-07", "Z_{D}(20), #epsilon = 2e-07", 2)
studies_RPV["HtoZd_HtoXX"] = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-08/", "RPV_MZd_20_Epsilon-5e-08", "Z_{D}(20), #epsilon = 5e-08", 11)
studies_RPV["HtoZd_HtoXX"] = addInput(inputs, inputFolder + "MZd_20_Epsilon-1e-08/", "RPV_MZd_20_Epsilon-1e-08", "Z_{D}(20), #epsilon = 1e-08", 4)

studies_RPV["HtoZd"] = []
studies_RPV["HtoZd"] = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-07/", "RPV_MZd_20_Epsilon-5e-07", "Z_{D}(20), #epsilon = 5e-07 (  2.1 mm)", 3)
studies_RPV["HtoZd"] = addInput(inputs, inputFolder + "MZd_20_Epsilon-2e-07/", "RPV_MZd_20_Epsilon-2e-07", "Z_{D}(20), #epsilon = 2e-07 ( 13.5 mm)", 2)
studies_RPV["HtoZd"] = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-08/", "RPV_MZd_20_Epsilon-5e-08", "Z_{D}(20), #epsilon = 5e-08 ( 217  mm)", 1)
studies_RPV["HtoZd"] = addInput(inputs, inputFolder + "MZd_20_Epsilon-1e-08/", "RPV_MZd_20_Epsilon-1e-08", "Z_{D}(20), #epsilon = 1e-08 (5424  mm)", 4)

studies_RPV["HtoZd_HtoXX_simple"] = []
studies_RPV["HtoZd_HtoXX_simple"] = addInput(inputs, inputFolder + "MH-125_MFF-20_CTau-130mm/", "RPV_MH-125_MFF-20_CTau-130mm", "h(125), X(20), 130 mm", 1)
studies_RPV["HtoZd_HtoXX_simple"] = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-08/", "RPV_MZd_20_Epsilon-5e-08", "Z_{D}(20), #epsilon = 5e-08 (217 mm)", 2)

studies_RPV["MSquark_deltaM_25"] = []
studies_RPV["MSquark_deltaM_25"] = addInput(inputs, inputFolder + "MSquark_125_MChi_100_ctau_100mm/",  "RPV_MSquark_125_MChi_100_ctau_100mm", "#tilde{q}(125), #chi(100), 100 mm", 1)
studies_RPV["MSquark_deltaM_25"] = addInput(inputs, inputFolder + "MSquark_200_MChi_175_ctau_100mm/",  "RPV_MSquark_200_MChi_175_ctau_100mm", "#tilde{q}(200), #chi(175), 100 mm", 2)
studies_RPV["MSquark_deltaM_25"] = addInput(inputs, inputFolder + "MSquark_350_MChi_325_ctau_100mm/",  "RPV_MSquark_350_MChi_325_ctau_100mm", "#tilde{q}(350), #chi(325), 100 mm", 3)
studies_RPV["MSquark_deltaM_25"] = addInput(inputs, inputFolder + "MSquark_700_MChi_675_ctau_100mm/",  "RPV_MSquark_700_MChi_675_ctau_100mm", "#tilde{q}(700), #chi(675), 100 mm", 4)
studies_RPV["MSquark_deltaM_25"] = addInput(inputs, inputFolder + "MSquark_1600_MChi_1575_ctau_100mm/",  "RPV_MSquark_1600_MChi_1575_ctau_100mm", "#tilde{q}(1600), #chi(1575), 100 mm", 12)

studies_RPV["MSquark_deltaM_75"] = []
studies_RPV["MSquark_deltaM_75"] = addInput(inputs, inputFolder + "MSquark_125_MChi_50_ctau_100mm/",  "RPV_MSquark_125_MChi_50_ctau_100mm", "#tilde{q}(125), #chi(50), 100 mm", 1)
studies_RPV["MSquark_deltaM_75"] = addInput(inputs, inputFolder + "MSquark_200_MChi_125_ctau_100mm/",  "RPV_MSquark_200_MChi_125_ctau_100mm", "#tilde{q}(200), #chi(125), 100 mm", 2)
studies_RPV["MSquark_deltaM_75"] = addInput(inputs, inputFolder + "MSquark_350_MChi_275_ctau_100mm/",  "RPV_MSquark_350_MChi_275_ctau_100mm", "#tilde{q}(350), #chi(275), 100 mm", 3)
studies_RPV["MSquark_deltaM_75"] = addInput(inputs, inputFolder + "MSquark_700_MChi_625_ctau_100mm/",  "RPV_MSquark_700_MChi_625_ctau_100mm", "#tilde{q}(700), #chi(625), 100 mm", 4)
studies_RPV["MSquark_deltaM_75"] = addInput(inputs, inputFolder + "MSquark_1600_MChi_1525_ctau_100mm/",  "RPV_MSquark_1600_MChi_1525_ctau_100mm", "#tilde{q}(1600), #chi(1525), 100 mm", 12)

studies_RPV["MSquark_deltaM_200"] = []
studies_RPV["MSquark_deltaM_200"] = addInput(inputs, inputFolder + "MSquark_350_MChi_150_ctau_100mm/",  "RPV_MSquark_350_MChi_150_ctau_100mm", "#tilde{q}(350), #chi(150), 100 mm", 2)
studies_RPV["MSquark_deltaM_200"] = addInput(inputs, inputFolder + "MSquark_700_MChi_500_ctau_100mm/",   "RPV_MSquark_700_MChi_500_ctau_100mm", "#tilde{q}(700), #chi(500), 100 mm", 4)
studies_RPV["MSquark_deltaM_200"] = addInput(inputs, inputFolder + "MSquark_1600_MChi_1400_ctau_100mm/",  "RPV_MSquark_1600_MChi_1400_ctau_100mm", "#tilde{q}(1600), #chi(1400), 100 mm", 3)

studies_RPV["MSquark_1600"] = []
studies_RPV["MSquark_1600"] = addInput(inputs, inputFolder + "MSquark_1600_MChi_50_ctau_100mm/",  "RPV_MSquark_1600_MChi_50_ctau_100mm", "#tilde{q}(1600), #chi(50), 100 mm", 1)
studies_RPV["MSquark_1600"] = addInput(inputs, inputFolder + "MSquark_1600_MChi_500_ctau_100mm/",  "RPV_MSquark_1600_MChi_500_ctau_100mm", "#tilde{q}(1600), #chi(500), 100 mm", 2)
studies_RPV["MSquark_1600"] = addInput(inputs, inputFolder + "MSquark_1600_MChi_1400_ctau_100mm/",  "RPV_MSquark_1600_MChi_1400_ctau_100mm", "#tilde{q}(1600), #chi(1400), 100 mm", 3)
studies_RPV["MSquark_1600"] = addInput(inputs, inputFolder + "MSquark_1600_MChi_1525_ctau_100mm/",  "RPV_MSquark_1600_MChi_1525_ctau_100mm", "#tilde{q}(1600), #chi(1525), 100 mm", 4)
studies_RPV["MSquark_1600"] = addInput(inputs, inputFolder + "MSquark_1600_MChi_1575_ctau_100mm/",  "RPV_MSquark_1600_MChi_1575_ctau_100mm", "#tilde{q}(1600), #chi(1575), 100 mm", 12)

studies_RPV["MSquark_700"] = [] 
studies_RPV["MSquark_700"] = addInput(inputs, inputFolder + "MSquark_700_MChi_50_ctau_100mm/",  "RPV_MSquark_700_MChi_50_ctau_100mm", "#tilde{q}(700), #chi(50), 100 mm", 1)
studies_RPV["MSquark_700"] = addInput(inputs, inputFolder + "MSquark_700_MChi_500_ctau_100mm/",  "RPV_MSquark_700_MChi_500_ctau_100mm", "#tilde{q}(700), #chi(500), 100 mm", 2)
studies_RPV["MSquark_700"] = addInput(inputs, inputFolder + "MSquark_700_MChi_625_ctau_100mm/",  "RPV_MSquark_700_MChi_625_ctau_100mm", "#tilde{q}(700), #chi(625), 100 mm", 3)
studies_RPV["MSquark_700"] = addInput(inputs, inputFolder + "MSquark_700_MChi_675_ctau_100mm/",  "RPV_MSquark_700_MChi_675_ctau_100mm", "#tilde{q}(700), #chi(675), 100 mm", 4)

studies_RPV["MSquark_350"] = []
studies_RPV["MSquark_350"] = addInput(inputs, inputFolder + "MSquark_350_MChi_50_ctau_100mm/",  "RPV_MSquark_350_MChi_50_ctau_100mm", "#tilde{q}(350), #chi(50), 100 mm", 1)
studies_RPV["MSquark_350"] = addInput(inputs, inputFolder + "MSquark_350_MChi_150_ctau_100mm/",  "RPV_MSquark_350_MChi_150_ctau_100mm", "#tilde{q}(350), #chi(150), 100 mm", 2)
studies_RPV["MSquark_350"] = addInput(inputs, inputFolder + "MSquark_350_MChi_275_ctau_100mm/",  "RPV_MSquark_350_MChi_275_ctau_100mm", "#tilde{q}(350), #chi(275), 100 mm", 3)
studies_RPV["MSquark_350"] = addInput(inputs, inputFolder + "MSquark_350_MChi_325_ctau_100mm/",  "RPV_MSquark_350_MChi_325_ctau_100mm", "#tilde{q}(350), #chi(325), 100 mm", 4)

studies_RPV["MSquark_200"] = []
studies_RPV["MSquark_200"] = addInput(inputs, inputFolder + "MSquark_200_MChi_50_ctau_100mm/",  "RPV_MSquark_200_MChi_50_ctau_100mm", "#tilde{q}(200), #chi(50), 100 mm", 1)
studies_RPV["MSquark_200"] = addInput(inputs, inputFolder + "MSquark_200_MChi_125_ctau_100mm/",  "RPV_MSquark_200_MChi_125_ctau_100mm", "#tilde{q}(200), #chi(125), 100 mm", 2)
studies_RPV["MSquark_200"] = addInput(inputs, inputFolder + "MSquark_200_MChi_175_ctau_100mm/",  "RPV_MSquark_200_MChi_175_ctau_100mm", "#tilde{q}(200), #chi(175), 100 mm", 3)

studies_RPV["MSquark_125"] = []
studies_RPV["MSquark_125"] = addInput(inputs, inputFolder + "MSquark_125_MChi_50_ctau_100mm/",  "RPV_MSquark_125_MChi_50_ctau_100mm", "#tilde{q}(125), #chi(50), 100 mm", 1)
studies_RPV["MSquark_125"] = addInput(inputs, inputFolder + "MSquark_125_MChi_100_ctau_100mm/",  "RPV_MSquark_125_MChi_100_ctau_100mm", "#tilde{q}(125), #chi(100), 100 mm", 2)

studies_RPV["MSquark_1150"] = []
studies_RPV["MSquark_1150"] = addInput(inputs, inputFolder + "MSquark_1150_MChi_50_ctau_40mm/",  "RPV_MSquark_1150_MChi_50_ctau_40mm", "#tilde{q}(1150), #chi(50), 40 mm", 1)
studies_RPV["MSquark_1150"] = addInput(inputs, inputFolder + "MSquark_1150_MChi_500_ctau_300mm/",  "RPV_MSquark_1150_MChi_500_ctau_300mm", "#tilde{q}(1150), #chi(500), 300 mm", 2)
studies_RPV["MSquark_1150"] = addInput(inputs, inputFolder + "MSquark_1150_MChi_950_ctau_400mm/",  "RPV_MSquark_1150_MChi_950_ctau_400mm", "#tilde{q}(1150), #chi(950), 400 mm", 3)
studies_RPV["MSquark_1150"] = addInput(inputs, inputFolder + "MSquark_1150_MChi_1125_ctau_500mm/",  "RPV_MSquark_1150_MChi_1125_ctau_500mm", "#tilde{q}(1150), #chi(1125), 500 mm", 4)