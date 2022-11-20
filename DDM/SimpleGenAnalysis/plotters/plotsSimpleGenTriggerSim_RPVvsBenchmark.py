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

###
studyName = "Overview"
# What to plot
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#colors,  1: black, 2: red, 3: green, 4: blue, 14:gray, 11:light brown, 12: dark gray, 2:red, 8:green
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_1500_MChi_494_ctau_100mm/", "RPV_MSquark_1500_MChi_494_ctau_100mm", "#tilde{q}(1500), #chi(494), 100 mm", 8)
#inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/", "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 4)
inputs = addInput(inputs, inputFolder + "MSquark_1000_MChi_148_ctau_100mm/",  "RPV_MSquark_1000_MChi_148_ctau_100mm","#tilde{q}(1000), #chi(148), 100 mm", 4) 
#inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_148_ctau_100mm/",  "RPV_MSquark_350_MChi_148_ctau_100mm",   "#tilde{q}(350), #chi(148), 100 mm", 2) 

#inputs = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 1)
#inputs = addInput(inputs, inputFolder + "MH-125_MFF-20_CTau-130mm/", "RPV_MH-125_MFF-20_CTau-130mm", "h(125), X(20), 130 mm", 39)

# Where to plot it
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/".format(STUDYNAME=studyName)
os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))

for plot in plots:
    makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)
###

###
studyName = "RPV-RunI"
# What to plot
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#colors,  1: black, 2: red, 3: green, 4: blue, 14:gray, 11:light brown, 12: dark gray, 2:red, 8:green
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_1500_MChi_494_ctau_100mm/", "RPV_MSquark_1500_MChi_494_ctau_100mm", "#tilde{q}(1500), #chi(494), 100 mm", 8)
inputs = addInput(inputs, inputFolder + "MSquark_1000_MChi_148_ctau_100mm/",  "RPV_MSquark_1000_MChi_148_ctau_100mm","#tilde{q}(1000), #chi(148), 100 mm", 4) 
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_148_ctau_100mm/",  "RPV_MSquark_350_MChi_148_ctau_100mm",   "#tilde{q}(350), #chi(148), 100 mm", 2) 
inputs = addInput(inputs, inputFolder + "MSquark_120_MChi_48_ctau_100mm/", "RPV_MSquark_120_MChi_48_ctau_100mm", "#tilde{q}(120), #chi(48), 100 mm", 1)
#inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/", "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 8)
#inputs = addInput(inputs, inputFolder + "MSquark_440_MChi_400_ctau_100mm/", "RPV_MSquark_440_MChi_400_ctau_100mm", "#tilde{q}(440), #chi(400), 100 mm", 1)

# Where to plot it
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/".format(STUDYNAME=studyName)
os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))

for plot in plots:
    makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)
###

###
studyName = "Compressed"
# What to plot
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#colors,  1: black, 2: red, 3: green, 4: blue, 14:gray, 11:light brown, 12: dark gray, 2:red, 8:green
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/", "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 8)
inputs = addInput(inputs, inputFolder + "MSquark_220_MChi_200_ctau_100mm/", "RPV_MSquark_220_MChi_200_ctau_100mm", "#tilde{q}(220), #chi(200), 100 mm", 4) 
inputs = addInput(inputs, inputFolder + "MSquark_330_MChi_300_ctau_100mm/", "RPV_MSquark_330_MChi_300_ctau_100mm", "#tilde{q}(330), #chi(300), 100 mm", 2) 
inputs = addInput(inputs, inputFolder + "MSquark_440_MChi_400_ctau_100mm/", "RPV_MSquark_440_MChi_400_ctau_100mm", "#tilde{q}(440), #chi(400), 100 mm", 1)

# Where to plot it
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/".format(STUDYNAME=studyName)
os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))

for plot in plots:
    makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)
###


###
studyName = "Low-pT"
# What to plot
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#colors,  1: black, 2: red, 3: green, 4: blue, 14:gray, 11:light brown, 12: dark gray, 2:red, 8:green
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_120_MChi_48_ctau_100mm/", "RPV_MSquark_120_MChi_48_ctau_100mm", "#tilde{q}(120), #chi(48), 100 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/", "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 2)
inputs = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 4)

# Where to plot it
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/".format(STUDYNAME=studyName)
os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))

for plot in plots:
    makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)
###

###
studyName = "RPV-All"
# What to plot
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#colors,  1: black, 2: red, 3: green, 4: blue, 14:gray, 11:light brown, 12: dark gray, 2:red, 8:green
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_1500_MChi_494_ctau_100mm/", "RPV_MSquark_1500_MChi_494_ctau_100mm", "#tilde{q}(1500), #chi(494), 100 mm", 8)
inputs = addInput(inputs, inputFolder + "MSquark_1000_MChi_148_ctau_100mm/",  "RPV_MSquark_1000_MChi_148_ctau_100mm","#tilde{q}(1000), #chi(148), 100 mm", 4) 
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_148_ctau_100mm/",  "RPV_MSquark_350_MChi_148_ctau_100mm",   "#tilde{q}(350), #chi(148), 100 mm", 2) 
inputs = addInput(inputs, inputFolder + "MSquark_120_MChi_48_ctau_100mm/", "RPV_MSquark_120_MChi_48_ctau_100mm", "#tilde{q}(120), #chi(48), 100 mm", 1)
#inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/", "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 3)
#inputs = addInput(inputs, inputFolder + "MSquark_440_MChi_400_ctau_100mm/", "RPV_MSquark_440_MChi_400_ctau_100mm", "#tilde{q}(440), #chi(400), 100 mm", 3)

# Where to plot it
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/".format(STUDYNAME=studyName)
os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))

for plot in plots:
    makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)
###

##lifetime scan
###
studyName = "MSquark_110_100"
# What to plot
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#colors,  1: black, 2: red, 3: green, 4: blue, 14:gray, 11:light brown, 12: dark gray, 2:red, 8:green
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_1mm/",     "RPV_MSquark_110_MChi_100_ctau_1mm", "#tilde{q}(110), #chi(100), 1 mm", 1)
inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/",   "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 2)
inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_10000mm/", "RPV_MSquark_110_MChi_100_ctau_10000mm", "#tilde{q}(110), #chi(100), 10000 mm", 4)

# Where to plot it
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/".format(STUDYNAME=studyName)
os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))
for plot in plots:
    makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)
###

studyName = "HtoXX"
# What to plot
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#colors,  1: black, 2: red, 3: green, 4: blue, 14:gray, 11:light brown, 12: dark gray, 2:red, 8:green
inputs = []
#inputs = addInput(inputs, inputFolder + "MSquark_1500_MChi_494_ctau_100mm/", "RPV_MSquark_1500_MChi_494_ctau_100mm", "#tilde{q}(1500), #chi(494), 100 mm", 8)
#inputs = addInput(inputs, inputFolder + "MSquark_110_MChi_100_ctau_100mm/", "RPV_MSquark_110_MChi_100_ctau_100mm", "#tilde{q}(110), #chi(100), 100 mm", 4)
#inputs = addInput(inputs, inputFolder + "MSquark_1000_MChi_148_ctau_100mm/",  "RPV_MSquark_1000_MChi_148_ctau_100mm","#tilde{q}(1000), #chi(148), 100 mm", 4) 
#inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_148_ctau_100mm/",  "RPV_MSquark_350_MChi_148_ctau_100mm",   "#tilde{q}(350), #chi(148), 100 mm", 2) 

inputs = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 1)
inputs = addInput(inputs, inputFolder + "MH-125_MFF-20_CTau-130mm/", "RPV_MH-125_MFF-20_CTau-130mm", "h(125), X(20), 130 mm", 39)

# Where to plot it
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/".format(STUDYNAME=studyName)
os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))

for plot in plots:
    makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)
###

studyName = "HtoZd_HtoXX"
# What to plot
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#colors,  1: black, 2: red, 3: green, 4: blue, 14:gray, 11:light brown, 12: dark gray, 2:red, 8:green
inputs = []

inputs = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 1)
inputs = addInput(inputs, inputFolder + "MH-125_MFF-20_CTau-130mm/", "RPV_MH-125_MFF-20_CTau-130mm", "h(125), X(20), 130 mm", 39)

inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-07/", "RPV_MZd_20_Epsilon-5e-07", "Z_{D}(20), #epsilon = 5e-07", 3)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-2e-07/", "RPV_MZd_20_Epsilon-2e-07", "Z_{D}(20), #epsilon = 2e-07", 2)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-08/", "RPV_MZd_20_Epsilon-5e-08", "Z_{D}(20), #epsilon = 5e-08", 11)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-1e-08/", "RPV_MZd_20_Epsilon-1e-08", "Z_{D}(20), #epsilon = 1e-08", 4)


# Where to plot it
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/".format(STUDYNAME=studyName)
os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))

for plot in plots:
    makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)

###
studyName = "HtoZd"
# What to plot
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#colors,  1: black, 2: red, 3: green, 4: blue, 14:gray, 11:light brown, 12: dark gray, 2:red, 8:green
inputs = []

inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-07/", "RPV_MZd_20_Epsilon-5e-07", "Z_{D}(20), #epsilon = 5e-07 (  2.1 mm)", 3)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-2e-07/", "RPV_MZd_20_Epsilon-2e-07", "Z_{D}(20), #epsilon = 2e-07 ( 13.5 mm)", 2)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-08/", "RPV_MZd_20_Epsilon-5e-08", "Z_{D}(20), #epsilon = 5e-08 ( 217  mm)", 1)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-1e-08/", "RPV_MZd_20_Epsilon-1e-08", "Z_{D}(20), #epsilon = 1e-08 (5424  mm)", 4)


# Where to plot it
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/".format(STUDYNAME=studyName)
os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))

for plot in plots:
    makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)
###

studyName = "HtoZd_HtoXX_simple"
# What to plot
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#colors,  1: black, 2: red, 3: green, 4: blue, 14:gray, 11:light brown, 12: dark gray, 2:red, 8:green
inputs = []

inputs = addInput(inputs, inputFolder + "MH-125_MFF-20_CTau-130mm/", "RPV_MH-125_MFF-20_CTau-130mm", "h(125), X(20), 130 mm", 1)
inputs = addInput(inputs, inputFolder + "MZd_20_Epsilon-5e-08/", "RPV_MZd_20_Epsilon-5e-08", "Z_{D}(20), #epsilon = 5e-08 (217 mm)", 2)

# Where to plot it
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/{STUDYNAME}/".format(STUDYNAME=studyName)
os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))

for plot in plots:
    makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)

