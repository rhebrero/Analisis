import ROOT
from ROOT import gPad
from reader import getTree, createPlots

inputFolder = "/home/aescalante/Desktop/toTry/"
f1, t1, l1 = getTree(inputFolder+"ntuple_106X_mcRun2_asymptotic_v13-v2.root", "SimpleNTupler", "DDTree", "nominal")
f2, t2, l2 = getTree(inputFolder+"ntuple_106X_mcRun2_asymptotic_preVFP_v8.root", "SimpleNTupler", "DDTree", "preVFP")

#Create                                                                                                                                                                 
trees = []
trees.append(t1)
trees.append(t2)

labels = []
labels.append(l1)
labels.append(l2)


variables  = []
selection = "gen_Lxy>10&&gen_Lxy<60"
variables.append({"var_name":"gen_Lxy", "selection": selection, "nbins": 50, "inibin": 0, "endbin": 100, "norm":False})
variables.append({"var_name":"gen_Lxy", "selection": selection, "nbins": 50, "inibin": 0, "endbin": 100, "norm":True})
variables.append({"var_name":"patmu_nTrackerLayers", "selection": selection, "nbins": 20, "inibin": 0, "endbin": 20, "norm":False})
outputFolder = "/home/aescalante/Desktop/toTry/plots/"


for kvariable in variables:
    createPlots(kvariable, trees, labels, outputFolder)


