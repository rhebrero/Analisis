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

plots = addVariable(plots, var = "h_massHiggs", xtitle = "M_{H} [GeV]", show_more = True)
plots = addVariable(plots, "h_massX"    ,   "M_{X} [GeV]", show_more = True)
plots = addVariable(plots, var = "h_massHiggs", xtitle = "M_{H} [GeV]")
plots = addVariable(plots, "h_massX"    ,   "M_{X} [GeV]")

plots = addVariable(plots, "h_etaMuons"    ,  "#eta", rebin = 3)
plots = addVariable(plots, "h_dRMuons"    ,  "#Delta R", rebin = 3)
plots = addVariable(plots, "h_cosalpha"    ,  "cos #alpha", rebin = 2, legend_offsetx = 0.1)
plots = addVariable(plots, "h_dphi"    ,  "#Delta #phi (coll)", rebin = 2)
plots = addVariable(plots, "h_dphi"    ,  "#Delta #phi (coll)", rebin = 2, logy=True)
plots = addVariable(plots, "h_dphi"    ,  "#Delta #phi (coll)", rebin = 2, logy=True, show_more = True)

#pt inclusive displacement
plots = addVariable(plots, "h_lxy"       ,   "Lxy [cm]", logy=True, show_more = True)
plots = addVariable(plots, "h_lxy"       ,   "Lxy [cm]", logy=True)
plots = addVariable(plots, "h_dxyMuons", "min(d_{xy})[cm] ", logy=True)
plots = addVariable(plots, "h_mindxyMuons", "min(d_{xy})[cm] ", )
plots = addVariable(plots, "h_mindxygenMuons", "min(d_{xy})[cm] wrt (0;0)")

#dxy inclusive pT
plots = addVariable(plots, "h_minptMuons",  "min(p_{T}) [GeV]", rebin = 2)
plots = addVariable(plots, "h_minptMuons",  "min(p_{T}) [GeV]", rebin = 2, logy = True, show_more = True)
plots = addVariable(plots, "h_maxptMuons",  "max(p_{T}) [GeV]", rebin = 2)

# What to plot
inputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#color =
#1: black, 2: red, 3: green, 4: blue, 14:gray, 11:light brown, 12: dark gray, 2:red, 8:green]
inputs = []
inputs = addInput(inputs, inputFolder + "MSquark_350_MChi_148_ctau_100mm/",  "RPV_MSquark_350_MChi_148_ctau_100mm",   "#tilde{q}(350), #chi(148), 100 mm", 2) 
inputs = addInput(inputs, inputFolder + "MSquark_1000_MChi_148_ctau_100mm/",  "RPV_MSquark_1000_MChi_148_ctau_100mm","#tilde{q}(1000), #chi(148), 100 mm", 4) 
inputs = addInput(inputs, inputFolder + "MSquark_1500_MChi_494_ctau_100mm/", "RPV_MSquark_1500_MChi_494_ctau_100mm", "#tilde{q}(1500), #chi(494), 100 mm", 8)

inputs = addInput(inputs, inputFolder + "MH-125_MFF-50_CTau-500mm/", "RPV_MH-125_MFF-50_CTau-500mm", "h(125), X(50), 500 mm", 1)
inputs = addInput(inputs, inputFolder + "MH-125_MFF-20_CTau-130mm/", "RPV_MH-125_MFF-20_CTau-130mm", "h(125), X(20), 130 mm", 39)

## where to plot it
outputFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/plotters/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

#for var, axis, title in zip(plots["var"], plots["axis"], plots["title"]):
for plot in plots:
    makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)
