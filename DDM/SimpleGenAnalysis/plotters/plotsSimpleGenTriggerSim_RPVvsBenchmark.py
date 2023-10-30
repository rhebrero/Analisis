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
from utils import getLibraries
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
plots = addImportantVariable(plots, "h_lxy_l"     ,   "Lxy [cm]", fit = False, show_more = True)
plots = addImportantVariable(plots, "h_distance_l"     ,   "distance [cm]", fit = False, show_more = True)
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

def makePlots(plots, inputs, studyName, outputFolder):
    outputFolder = outputFolder.format(STUDYNAME=studyName)    
    os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = outputFolder))

    for plot in plots:
        makeSimple1DPlotFromDic(plot = plot, inputs = inputs, folder = outputFolder)

from studies import studies_SMUON, do_studies_SMUON

for key in studies_SMUON.keys():
    inputs = studies_SMUON[key]
    studyName = key
    if len(do_studies_SMUON) > 0:
        if key in do_studies_SMUON: 
           makePlots(plots, inputs, studyName, outputFolder)