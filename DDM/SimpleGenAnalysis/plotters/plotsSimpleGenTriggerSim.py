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

#1D efficiencies.

def addVariable(plots, var, axis, title): 
    
    plots["var"].append(var)
    plots["axis"].append(axis)
    plots["title"].append(title)

    return plots

#Efficiencies as ratios of produced 1 Histograms.

plots ={"var":[], "axis":[], "title":[]}

plots = addVariable(plots, "h_massHiggs",   "M_{H} [GeV]", "")
plots = addVariable(plots, "h_massX"    ,   "M_{X} [GeV]", "")

plots = addVariable(plots, "h_etaMuons"    ,  "#eta", "")
plots = addVariable(plots, "h_dRMuons"    ,  "#Delta R", "")
plots = addVariable(plots, "h_cosalpha"    ,  "cos #alpha", "")


#pt inclusive displacement
plots = addVariable(plots, "h_lxy"       ,   "Lxy [cm]", "")
plots = addVariable(plots, "h_mindxyMuons", "min(dxy)[cm] ", "")
plots = addVariable(plots, "h_mindxygenMuons", "min(dxy)[cm] wrt (0;0)", "")

#dxy inclusive pT
plots = addVariable(plots, "h_minptMuons",  "min(pT) [GeV]", "")
plots = addVariable(plots, "h_maxptMuons",  "max(pT) [GeV]", "")

#differential measurements
#from SimpleGenTriggerSim import bins
bins = {}
bins["pT"] = ["15", "30"]
bins["distance"] = ["0.02", "0.1", "1", "10", "100", "400"]

for pT in bins["pT"]:
    addVariable(plots, "h_dxyVspt_p_{pT}".format(pT=pT), "min(dxy)[cm]", "pT > {pT} GeV".format(pT=pT))
    addVariable(plots, "h_dxyVspt_{pT}".format(pT=pT)  , "min(dxy)[cm]", "pT > {pT} GeV".format(pT=pT))

    addVariable(plots, "h_lxyVspt_l_{pT}".format(pT=pT)  , "Lxy [cm]", "pT > {pT} GeV".format(pT=pT))
    addVariable(plots, "h_lxyVspt_{pT}".format(pT=pT)    , "Lxy [cm]", "pT > {pT} GeV".format(pT=pT))

#for distance in bins["distance"]:
#    print (distance, "TO BE IMPLEMENTED")

bins["threshold"] = ["0.015", "1.2"]
for threshold in bins["threshold"]:   
    addVariable(plots, "h_ptVsdxy_{THRESHOLD}".format(THRESHOLD=threshold)    , "pT [GeV]", "dxy > {THRESHOLD} [cm]".format(THRESHOLD=threshold))

## numerators
#histName = "125_20_CTau_130cm"
histName = "125_XX"

nums = {
    "histName": [histName + "_L1", histName + "_L1cpt", histName + "_L1upt", histName + "_L2", histName + "_L2VetoPrompt", histName + "_L3", histName + "_HLT"], 
    "label"   : [            "L1",             "L1cpt",             "L1upt",             "L2",             "L2VetoPrompt",             "L3",             "HLT"], 
    "color"   : [              14,                  11,                  12,                2,                          4,                8,                28]
}

# denominator
dens = {
    "histName": [histName + "_ALL", histName + "_HLT", histName + "_L1", histName + "_L2", histName + "_L1cpt"], 
    "label"   : [            "ALL",             "HLT",             "L1",             "L2",             "L1cpt"]
}

baseOutFolder = "/eos/user/e/escalant/lxplus/displaced2022/plotsTriggerV6/"
#output follows the following: /Eff/{NUM}_{DEN}/Eff_{VAR}_{NUMLABEL}_{DENLABEL}

for var, axis, title in zip(plots["var"], plots["axis"], plots["title"]):
    for numlist, denlist in zip(nums, dens):            
        for numindex in range(len(nums["histName"])):
            for denindex in range(len(dens["histName"])):
                if dens["label"][denindex] == nums["label"][numindex]: continue                              # leads to effficiencies eq 1

                uncmode = "cp"
                if dens["label"][denindex] == "HLT" and nums["label"][numindex] == "L1"           : uncmode = "pois"     # eff > 1
                if dens["label"][denindex] == "L1"  and nums["label"][numindex] in ["ALL"] : uncmode = "pois"     # eff > 1
                if dens["label"][denindex] == "L2": 
                    uncmode = "pois"
                    if nums["label"][numindex] not in ["L2VetoPrompt", "L3", "HLT"]: continue     # eff > 1
                if dens["label"][denindex] == "L1cpt": 
                    uncmode = "pois"
                    if nums["label"][numindex] not in ["L1upt", "L1"]: continue     # eff > 1

                #open/read/write files
                # create Folder.
                outFolder = "{BASEOUTFOLDER}EFF/{NUMLABEL}_{DENLABEL}/".format(BASEOUTFOLDER=baseOutFolder, NUMLABEL=nums["label"][numindex], DENLABEL=dens["label"][denindex])
                print (outFolder) 
                if os.path.exists(outFolder) ==  False:
                    print ("folder does not exist")
                    os.makedirs(outFolder)
                else:
                    print ("folder exists")

                outFilename = outFolder + "Eff_{VAR}_{NUMLABEL}_{DENLABEL}_test".format(VAR=var, NUMLABEL=nums["label"][numindex], DENLABEL=dens["label"][denindex])
                numFilename = baseOutFolder + "{NUMLABEL}/{VAR}-hist.root".format(NUMLABEL = nums["label"][numindex], VAR=var)
                denFilename = baseOutFolder + "{DENLABEL}/{VAR}-hist.root".format(DENLABEL = dens["label"][denindex], VAR=var)

                rebin = 1
                if "15" in outFilename:
                    rebin = 2
                if "30" in outFilename:
                    rebin = 10
                if "_h_lxy_" in outFilename:
                    rebin = 3

                makeRatio(numFilename, denFilename, nums["histName"][numindex], dens["histName"][denindex], nums["label"][numindex], dens["label"][denindex], axis, "Events", outFilename, ColorNum = nums["color"][numindex], Title = title, Rebin = rebin, UncMode = uncmode)
