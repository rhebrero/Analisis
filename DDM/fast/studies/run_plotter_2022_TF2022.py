from os import system as bash
import argparse

def submitPlotter(selection, variable, label, webpage = "/users/alberto.escalante/plots/Run3/", extra = "-debug", myselection = "all"):
    command = "python3 plotter_2022.py -s {SELECTION} -v {VARIABLE} -y all -pf {PLOTSFOLDER} {EXTRA}"
    command = command.format(SELECTION = selection, VARIABLE = variable, PLOTSFOLDER = webpage + label, EXTRA=extra.replace("_", "-"))
    if myselection in selection:
        print(command)
        bash(command)
    elif myselection == "all":
        print(command)
        bash(command)

parser = argparse.ArgumentParser(description="runs plotter_2022.py in the context of a TF 2022 plots")
parser.add_argument("--label", type=str, required=True, help="label to be used in output folder (e.g Feb12)")
parser.add_argument("--extra", type=str, required=False, default =  "-debug", help="extra options to append to plotter_2022.py (e.g -sub for submission)")
parser.add_argument("--selection", type=str, required=False, default =  "all", help="only process jobs with the selection label (e.g base_overlay_dy_ILXYS_DPHI_IDPHI3)")
args = parser.parse_args()

#label = "TF_DY_Feb12"
label = "TF_DY_{LABEL}".format(LABEL = args.label)
selections_DY = []
selections_DY.append("base_overlay_dy_ILXYS_DPHI_IDPHI3")
selections_DY.append("base_overlay_dy_ILXYS_DPHI1_IDPHI2")
#REP-PAT
selections_DY.append("base_overlay_dy_PATPAT_DPHI_IDPHI3")
selections_DY.append("base_overlay_dy_PATPAT_DPH1_IDPHI2")
#REP-HYB
selections_DY.append("base_overlay_dy_HYB_DPHI_IDPHI3")
selections_DY.append("base_overlay_dy_HYB_DPHI1_IDPHI2")

variables_DY = ["mass_v5", "lxysigpv_v2"]

for selection_DY in selections_DY:
    for variable_DY in variables_DY:
#        submitPlotter(selection_DY, variable_DY, label, extra = args.extra, myselection = args.selection)
        print("")

#label = "TF_QCD_Feb12"
label = "TF_QCD_{LABEL}".format(LABEL = args.label)
selections_QCD = []
#SS
selections_QCD.append("base_overlay_qcd_IDETANDTIDETASEG_SS_DSAISO0P1_IDSAISO0P1")
selections_QCD.append("base_overlay_qcd_IDETANDTIDETASEG_noSEG_SS_DSAISO0P1_IDSAISO0P1")
selections_QCD.append("base_overlay_qcd_IMASS_SS_DSAISO0P1_IDSAISO0P1")
#OS
selections_QCD.append("base_overlay_qcd_IDETANDTIDETASEG_OS_DSAISO0P1_IDSAISO0P1")
selections_QCD.append("base_overlay_qcd_IDETANDTIDETASEG_noSEG_OS_DSAISO0P1_IDSAISO0P1")
selections_QCD.append("base_overlay_qcd_IMASS_OS_DSAISO0P1_IDSAISO0P1")

## do not split by isolation
selections_QCD.append("base_selection_qcd_IDETANDTIDETASEG")
selections_QCD.append("base_selection_qcd_IDETANDTIDETASEG_noSEG")
selections_QCD.append("base_selection_qcd_IMASS")

#variables_QCD = ["mass_v3", "mass_v5", "mass_v6", "mass_v7", "mass_v8", "mass_v9", "mass_v10", "dimdeltaeta,dimnseg", "dimdeltaeta,dthitscschits0", "dimdeltaeta,mindthitscschits0","minpt_v2", "eta", "lxysigpv_v3", "deltaphi", "dca_v1", "vtxnormchi2", "deltar_v2"]
variables_QCD = ["dca_v1"]

for selection_QCD in selections_QCD:
    for variable_QCD in variables_QCD:
        submitPlotter(selection_QCD, variable_QCD, label, extra = args.extra, myselection = args.selection)
