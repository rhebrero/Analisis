import ROOT
from ROOT import gPad
from reader import getTree, createPlots

#inputFolder = "/home/aescalante/Desktop/toTry/"
inputFolder = "~/cernbox/lxplus/sandbox/files/Run2022C-PromptReco-v1_CMSSW_12_4_4/"
#f1, t1, l1 = getTree(inputFolder+"ntuple_106X_mcRun2_asymptotic_v13-v2.root", "SimpleNTupler", "DDTree", "nominal")
#f2, t2, l2 = getTree(inputFolder+"ntuple_106X_mcRun2_asymptotic_preVFP_v8.root", "SimpleNTupler", "DDTree", "preVFP")
#f1, t1, l1 = getTree(inputFolder+"test_mc.root", "SimpleNTupler", "DDTree", "simulation")
f1, t1, l1 = getTree(inputFolder+"test.root", "SimpleNTupler", "DDTree", "All")
f2, t2, l2 = getTree(inputFolder+"test.root", "SimpleNTupler",
                     "DDTree", "HLT_DoubleL2Mu23NoVtx_2Cha_v2")
f3, t3, l3 = getTree(inputFolder+"test.root", "SimpleNTupler", "DDTree",
                     "HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v1")
f4, t4, l4 = getTree(inputFolder+"test.root", "SimpleNTupler", "DDTree",
                     "HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v1")

# Create
trees = []
trees.append(t1)
trees.append(t2)
trees.append(t3)
trees.append(t4)

labels = []
labels.append(l1)
labels.append(l2)
labels.append(l3)
labels.append(l4)

selection = []
selection.append("trig_hlt_idx>=0")
selection.append('trig_hlt_path=="HLT_DoubleL2Mu23NoVtx_2Cha_v3"')
selection.append('trig_hlt_path=="HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v2"')
selection.append('trig_hlt_path=="HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v2"')
# selection.append("dim_pt>5")

variables = []
variables.append({"var_name": "dim_pt", "selection": selection,
                 "nbins": 50, "inibin": 0, "endbin": 100, "norm": False})
#variables.append({"var_name":"dim_pt", "selection": selection, "nbins": 50, "inibin": 0, "endbin": 100, "norm":True})
variables.append({"var_name": "patmu_nTrackerLayers", "selection": selection,
                 "nbins": 20, "inibin": 0, "endbin": 20, "norm": False})
variables.append({"var_name": "evt_run", "selection": selection, "nbins": 356386 -
                 352499, "inibin": 352499, "endbin": 356386, "norm": False})
variables.append({"var_name": "evt_lumi", "selection": selection,
                 "nbins": 250, "inibin": 0, "endbin": 250, "norm": False})
#variables.append({"var_name":"patmu_nTrackerLayers", "selection": selection, "nbins": 20, "inibin": 0, "endbin": 20, "norm":True})
variables.append({"var_name": "trig_hlt_path", "selection": selection,
                 "nbins": 20, "inibin": 0, "endbin": 20, "norm": False})
# other variables normalized

outputFolder = inputFolder+"plots/"

for kvariable in variables:
    createPlots(kvariable, trees, labels, outputFolder)
