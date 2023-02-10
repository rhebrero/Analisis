# import ROOT in batch mode
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT

ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events
from math import *

#Utils for Longlived Generator Level studies.
from GenLongLivedUtils import *
from SimpleTools import *

#bash utils
import os

## Variables to be plotted

plots = []

plots = addImportantVariable(plots, var = "h_massHiggs", xtitle = "M_{H} [GeV]", show_more = True)
plots = addImportantVariable(plots, "h_massX"    ,   "M_{X} [GeV]", show_more = True)

plots = addImportantVariable(plots, "h_ptX"    ,   "p^{X}_{T} [GeV]")
plots = addImportantVariable(plots, "h_ptOvermassX"    ,   "p^{X}_{T}/M_{X}")
plots = addImportantVariable(plots, "h_betaX"    ,   "#beta_{X}")
plots = addImportantVariable(plots, "h_genTrigger"   ,   "gen.Trigger bit")
plots = addImportantVariable(plots, "h_genTriggerDiff"   ,   "gen.Trigger bit")

plots = addImportantVariable(plots, "h_etaMuons"    ,  "#eta", rebin = 2)
plots = addImportantVariable(plots, "h_dRMuons"    ,  "#Delta R", rebin = 2)

plots = addVariable(plots, "h_cosalpha"    ,  "cos #alpha", rebin = 2, legend_offsetx = 0.1)
plots = addImportantVariable(plots, "h_dphi"    ,  "#Delta #phi (coll)", rebin = 2)

#pt inclusive displacement
plots = addImportantVariable(plots, "h_lxy"       ,   "Lxy [cm]", fit = True, show_more = True)
plots = addImportantVariable(plots, "h_mindxyMuons", "min(d_{xy})[cm] ")

plots = addVariable(plots, "h_dxyMuons", "min(d_{xy})[cm] ", logy=True)
plots = addVariable(plots, "h_mindxygenMuons", "min(d_{xy})[cm] wrt (0;0)")

#dxy inclusive pT
plots = addImportantVariable(plots, "h_minptMuons_l",  "min(p_{T}) [GeV]", rebin = 2)
plots = addImportantVariable(plots, "h_minptMuons",  "min(p_{T}) [GeV]", rebin = 2)
plots = addVariable(plots, "h_maxptMuons",  "max(p_{T}) [GeV]")

#mass
plots = addImportantVariable(plots, "h_dimumass",  "m_{#mu#mu} [GeV]")
plots = addImportantVariable(plots, "h_dimumass_l",  "m_{#mu#mu} [GeV]")
plots = addImportantVariable(plots, "h_dimupt",    "dim p_{T} [GeV]")
plots = addImportantVariable(plots, "h_proptime",    "#tau", rebin = 2, fit = True)
plots = addImportantVariable(plots, "h_proptime_l",    "#tau", rebin = 2, fit = True) 


colors = {"black":1, "red":2, "light-green":3, "blue":4, "green": 8, "light-brown":11, "dark-gray":12, "gray":14}

def makePlots(plots, inputs, studyName, outputFolder):
    outputFolder = outputFolder.format(STUDYNAME=studyName)    
    os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))

    for plot in plots:
        makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)

# input and outputs
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/"

studyName = "Overview"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_1500_MChi_494_ctau_100mm/", "RPV_MSquark_1500_MChi_494_ctau_100mm", "#tilde{q}(1500), #chi(494), 100 mm", 8)
inputs = addInput(inputs, inputFolder + "MSquark_1000_MChi_148_ctau_100mm/",  "RPV_MSquark_1000_MChi_148_ctau_100mm","#tilde{q}(1000), #chi(148), 100 mm", 4) 
makePlots(plots, inputs, studyName, outputFolder)

studyName = "RPV-RunI"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_1500_MChi_494_ctau_100mm/", "RPV_MSquark_1500_MChi_494_ctau_100mm", "#tilde{q}(1500), #chi(494), 100 mm", 8)
inputs = addInput(inputs, inputFolder + "MSquark_1000_MChi_148_ctau_100mm/",  "RPV_MSquark_1000_MChi_148_ctau_100mm","#tilde{q}(1000), #chi(148), 100 mm", 4) 
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_148_ctau_100mm/",  "RPV_MSquark_350_MChi_148_ctau_100mm",   "#tilde{q}(350), #chi(148), 100 mm", 2) 
inputs = addInput(inputs, inputFolder + "MSquark_120_MChi_48_ctau_100mm/", "RPV_MSquark_120_MChi_48_ctau_100mm", "#tilde{q}(120), #chi(48), 100 mm", 1)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "Compressed"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/", "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 8)
inputs = addInput(inputs, inputFolder + "MSquark_220_MChi_200_ctau_100mm/", "RPV_MSquark_220_MChi_200_ctau_100mm", "#tilde{q}(220), #chi(200), 100 mm", 4) 
inputs = addInput(inputs, inputFolder + "MSquark_330_MChi_300_ctau_100mm/", "RPV_MSquark_330_MChi_300_ctau_100mm", "#tilde{q}(330), #chi(300), 100 mm", 2) 
inputs = addInput(inputs, inputFolder + "MSquark_440_MChi_400_ctau_100mm/", "RPV_MSquark_440_MChi_400_ctau_100mm", "#tilde{q}(440), #chi(400), 100 mm", 1)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "Low-pT"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_120_MChi_48_ctau_100mm/", "RPV_MSquark_120_MChi_48_ctau_100mm", "#tilde{q}(120), #chi(48), 100 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/", "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 2)
inputs = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 4)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "RPV-All"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_1500_MChi_494_ctau_100mm/", "RPV_MSquark_1500_MChi_494_ctau_100mm", "#tilde{q}(1500), #chi(494), 100 mm", 8)
inputs = addInput(inputs, inputFolder + "MSquark_1000_MChi_148_ctau_100mm/",  "RPV_MSquark_1000_MChi_148_ctau_100mm","#tilde{q}(1000), #chi(148), 100 mm", 4) 
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_148_ctau_100mm/",  "RPV_MSquark_350_MChi_148_ctau_100mm",   "#tilde{q}(350), #chi(148), 100 mm", 2) 
inputs = addInput(inputs, inputFolder + "MSquark_120_MChi_48_ctau_100mm/", "RPV_MSquark_120_MChi_48_ctau_100mm", "#tilde{q}(120), #chi(48), 100 mm", 1)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_110_100"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_1mm/",     "RPV_MSquark_110_MChi_100_ctau_1mm", "#tilde{q}(110), #chi(100), 1 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/",   "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_10000mm/", "RPV_MSquark_110_MChi_100_ctau_10000mm", "#tilde{q}(110), #chi(100), 10000 mm", 4)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "HtoXX"
inputs = []
inputs = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 1)
inputs = addInput(inputs, inputFolder + "MH-125_MFF-20_CTau-130mm/", "RPV_MH-125_MFF-20_CTau-130mm", "h(125), X(20), 130 mm", 39)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "HtoZd_HtoXX"
inputs = []
inputs = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 1)
inputs = addInput(inputs, inputFolder + "MH-125_MFF-20_CTau-130mm/", "RPV_MH-125_MFF-20_CTau-130mm", "h(125), X(20), 130 mm", 39)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-07/", "RPV_MZd_20_Epsilon-5e-07", "Z_{D}(20), #epsilon = 5e-07", 3)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-2e-07/", "RPV_MZd_20_Epsilon-2e-07", "Z_{D}(20), #epsilon = 2e-07", 2)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-08/", "RPV_MZd_20_Epsilon-5e-08", "Z_{D}(20), #epsilon = 5e-08", 11)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-1e-08/", "RPV_MZd_20_Epsilon-1e-08", "Z_{D}(20), #epsilon = 1e-08", 4)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "HtoZd"
inputs = []
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-07/", "RPV_MZd_20_Epsilon-5e-07", "Z_{D}(20), #epsilon = 5e-07 (  2.1 mm)", 3)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-2e-07/", "RPV_MZd_20_Epsilon-2e-07", "Z_{D}(20), #epsilon = 2e-07 ( 13.5 mm)", 2)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-08/", "RPV_MZd_20_Epsilon-5e-08", "Z_{D}(20), #epsilon = 5e-08 ( 217  mm)", 1)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-1e-08/", "RPV_MZd_20_Epsilon-1e-08", "Z_{D}(20), #epsilon = 1e-08 (5424  mm)", 4)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "HtoZd_HtoXX_simple"
inputs = []
inputs = addInput(inputs, inputFolder + "MH-125_MFF-20_CTau-130mm/", "RPV_MH-125_MFF-20_CTau-130mm", "h(125), X(20), 130 mm", 1)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-08/", "RPV_MZd_20_Epsilon-5e-08", "Z_{D}(20), #epsilon = 5e-08 (217 mm)", 2)
makePlots(plots, inputs, studyName, outputFolder)

plots = addImportantVariable(plots, "h_lxy_s"       ,   "Lxy [cm]", show_more = True)

studyName = "MSquark_deltaM_25"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_125_MChi_100_ctau_100mm/",  "RPV_MSquark_125_MChi_100_ctau_100mm", "#tilde{q}(125), #chi(100), 100 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_200_MChi_175_ctau_100mm/",  "RPV_MSquark_200_MChi_175_ctau_100mm", "#tilde{q}(200), #chi(175), 100 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_325_ctau_100mm/",  "RPV_MSquark_350_MChi_325_ctau_100mm", "#tilde{q}(350), #chi(325), 100 mm", 3)
inputs = addInput(inputs, inputFolder + "MSquark_700_MChi_675_ctau_100mm/",  "RPV_MSquark_700_MChi_675_ctau_100mm", "#tilde{q}(700), #chi(675), 100 mm", 4)
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_1575_ctau_100mm/",  "RPV_MSquark_1600_MChi_1575_ctau_100mm", "#tilde{q}(1600), #chi(1575), 100 mm", 12)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_deltaM_75"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_125_MChi_50_ctau_100mm/",  "RPV_MSquark_125_MChi_50_ctau_100mm", "#tilde{q}(125), #chi(50), 100 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_200_MChi_125_ctau_100mm/",  "RPV_MSquark_200_MChi_125_ctau_100mm", "#tilde{q}(200), #chi(125), 100 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_275_ctau_100mm/",  "RPV_MSquark_350_MChi_275_ctau_100mm", "#tilde{q}(350), #chi(275), 100 mm", 3)
inputs = addInput(inputs, inputFolder + "MSquark_700_MChi_625_ctau_100mm/",  "RPV_MSquark_700_MChi_625_ctau_100mm", "#tilde{q}(700), #chi(625), 100 mm", 4)
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_1525_ctau_100mm/",  "RPV_MSquark_1600_MChi_1525_ctau_100mm", "#tilde{q}(1600), #chi(1525), 100 mm", 12)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_deltaM_200"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_150_ctau_100mm/",  "RPV_MSquark_350_MChi_150_ctau_100mm", "#tilde{q}(350), #chi(150), 100 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_700_MChi_500_ctau_100mm/",   "RPV_MSquark_700_MChi_500_ctau_100mm", "#tilde{q}(700), #chi(500), 100 mm", 4)
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_1400_ctau_100mm/",  "RPV_MSquark_1600_MChi_1400_ctau_100mm", "#tilde{q}(1600), #chi(1400), 100 mm", 3)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_1600"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_50_ctau_100mm/",  "RPV_MSquark_1600_MChi_50_ctau_100mm", "#tilde{q}(1600), #chi(50), 100 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_500_ctau_100mm/",  "RPV_MSquark_1600_MChi_500_ctau_100mm", "#tilde{q}(1600), #chi(500), 100 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_1400_ctau_100mm/",  "RPV_MSquark_1600_MChi_1400_ctau_100mm", "#tilde{q}(1600), #chi(1400), 100 mm", 3)
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_1525_ctau_100mm/",  "RPV_MSquark_1600_MChi_1525_ctau_100mm", "#tilde{q}(1600), #chi(1525), 100 mm", 4)
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_1575_ctau_100mm/",  "RPV_MSquark_1600_MChi_1575_ctau_100mm", "#tilde{q}(1600), #chi(1575), 100 mm", 12)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_700"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_700_MChi_50_ctau_100mm/",  "RPV_MSquark_700_MChi_50_ctau_100mm", "#tilde{q}(700), #chi(50), 100 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_700_MChi_500_ctau_100mm/",  "RPV_MSquark_700_MChi_500_ctau_100mm", "#tilde{q}(700), #chi(500), 100 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_700_MChi_625_ctau_100mm/",  "RPV_MSquark_700_MChi_625_ctau_100mm", "#tilde{q}(700), #chi(625), 100 mm", 3)
inputs = addInput(inputs, inputFolder + "MSquark_700_MChi_675_ctau_100mm/",  "RPV_MSquark_700_MChi_675_ctau_100mm", "#tilde{q}(700), #chi(675), 100 mm", 4)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_350"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_50_ctau_100mm/",  "RPV_MSquark_350_MChi_50_ctau_100mm", "#tilde{q}(350), #chi(50), 100 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_150_ctau_100mm/",  "RPV_MSquark_350_MChi_150_ctau_100mm", "#tilde{q}(350), #chi(150), 100 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_275_ctau_100mm/",  "RPV_MSquark_350_MChi_275_ctau_100mm", "#tilde{q}(350), #chi(275), 100 mm", 3)
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_325_ctau_100mm/",  "RPV_MSquark_350_MChi_325_ctau_100mm", "#tilde{q}(350), #chi(325), 100 mm", 4)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_200"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_200_MChi_50_ctau_100mm/",  "RPV_MSquark_200_MChi_50_ctau_100mm", "#tilde{q}(200), #chi(50), 100 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_200_MChi_125_ctau_100mm/",  "RPV_MSquark_200_MChi_125_ctau_100mm", "#tilde{q}(200), #chi(125), 100 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_200_MChi_175_ctau_100mm/",  "RPV_MSquark_200_MChi_175_ctau_100mm", "#tilde{q}(200), #chi(175), 100 mm", 3)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_125"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_125_MChi_50_ctau_100mm/",  "RPV_MSquark_125_MChi_50_ctau_100mm", "#tilde{q}(125), #chi(50), 100 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_125_MChi_100_ctau_100mm/",  "RPV_MSquark_125_MChi_100_ctau_100mm", "#tilde{q}(125), #chi(100), 100 mm", 2)
makePlots(plots, inputs, studyName, outputFolder)


######################################
studyName = "MSquark_1600"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_50_ctau_30mm/",  "RPV_MSquark_1600_MChi_50_ctau_30mm", "#tilde{q}(1600), #chi(50), 30 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_500_ctau_200mm/",  "RPV_MSquark_1600_MChi_500_ctau_200mm", "#tilde{q}(1600), #chi(500), 200 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_950_ctau_300mm/",  "RPV_MSquark_1600_MChi_950_ctau_300mm", "#tilde{q}(1600), #chi(950), 300 mm", 3)
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_1400_ctau_600mm/",  "RPV_MSquark_1600_MChi_1400_ctau_600mm", "#tilde{q}(1600), #chi(1400), 600 mm", 11)
inputs = addInput(inputs, inputFolder + "MSquark_1600_MChi_1575_ctau_700mm/",  "RPV_MSquark_1600_MChi_1575_ctau_700mm", "#tilde{q}(1600), #chi(1575), 700 mm", 12)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_1150"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_1150_MChi_50_ctau_40mm/",  "RPV_MSquark_1150_MChi_50_ctau_40mm", "#tilde{q}(1150), #chi(50), 40 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_1150_MChi_500_ctau_300mm/",  "RPV_MSquark_1150_MChi_500_ctau_300mm", "#tilde{q}(1150), #chi(500), 300 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_1150_MChi_950_ctau_400mm/",  "RPV_MSquark_1150_MChi_950_ctau_400mm", "#tilde{q}(1150), #chi(950), 400 mm", 3)
inputs = addInput(inputs, inputFolder + "MSquark_1150_MChi_1125_ctau_500mm/",  "RPV_MSquark_1150_MChi_1125_ctau_500mm", "#tilde{q}(1150), #chi(1125), 500 mm", 4)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_700"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_700_MChi_50_ctau_50mm/",  "RPV_MSquark_700_MChi_50_ctau_50mm", "#tilde{q}(700), #chi(50), 50 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_700_MChi_500_ctau_400mm/",  "RPV_MSquark_700_MChi_500_ctau_400mm", "#tilde{q}(700), #chi(500), 400 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_700_MChi_675_ctau_500mm/",  "RPV_MSquark_700_MChi_675_ctau_500mm", "#tilde{q}(700), #chi(675), 500 mm", 4)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_350"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_50_ctau_70mm/",  "RPV_MSquark_350_MChi_50_ctau_70mm", "#tilde{q}(350), #chi(50), 70 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_150_ctau_250mm/",  "RPV_MSquark_350_MChi_150_ctau_250mm", "#tilde{q}(350), #chi(150), 250 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_325_ctau_450mm/",  "RPV_MSquark_350_MChi_325_ctau_450mm", "#tilde{q}(350), #chi(325), 450 mm", 4)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_200"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_200_MChi_50_ctau_150mm/",  "RPV_MSquark_200_MChi_50_ctau_150mm", "#tilde{q}(200), #chi(50), 150 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_200_MChi_175_ctau_400mm/",  "RPV_MSquark_200_MChi_175_ctau_400mm", "#tilde{q}(200), #chi(175), 400 mm", 3)
makePlots(plots, inputs, studyName, outputFolder)

studyName = "MSquark_125"
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_125_MChi_50_ctau_200mm/",  "RPV_MSquark_125_MChi_50_ctau_200mm", "#tilde{q}(125), #chi(50), 200 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_125_MChi_100_ctau_350mm/",  "RPV_MSquark_125_MChi_100_ctau_350mm", "#tilde{q}(125), #chi(100), 350 mm", 2)
makePlots(plots, inputs, studyName, outputFolder)
