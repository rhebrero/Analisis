from ddm_tools import plot_ratio
import pdb
def makePlotRatio(years, selections, xtitle, ytitle, ratiotitle, variable, variable_suffix):
    for year in years:
        for selection in selections:
            histogram1 = selection["dataset"] + selection["histogram1"]
            legend1 = selection["legend1"]

            histogram2 = selection["dataset"] + selection["histogram2"]
            legend2 = selection["legend2"]

            root_file1 = selection["root_file1"].format(INPUTFOLDER = inputFolder, SELECTION = selection["selection"], YEAR = year, DATASET = selection["dataset"], CUT = selection["cut"], HISTOGRAM1 = selection["histogram1"], HISTOGRAM2 = selection["histogram2"], VARIABLE=variable, VARIABLE_SUFFIX=variable_suffix)
            root_file2 = root_file1

            outfile = "{PLOTSFOLDER}/TF_{YEAR}_{VARIABLE}_{DATASET}{HISTOGRAM1}_{DATASET}{HISTOGRAM2}_{SELECTION}_{VARIABLE_SUFFIX}".format(PLOTSFOLDER = plotsFolder, YEAR=year, DATASET = selection["dataset"], HISTOGRAM1 = histogram1, HISTOGRAM2 = histogram2, SELECTION=selection["selection"], VARIABLE=variable, VARIABLE_SUFFIX = variable_suffix)

            plot_ratio(root_file1, histogram1, legend1, root_file2, histogram2, legend2, xtitle, ytitle, ratiotitle, selection["selection"], outfile)
            #print(root_file1, histogram1, legend1, root_file2, histogram2, legend2, xtitle, ytitle, ratiotitle, selection["selection"], outfile)

#general configuration
years = ["2016", "2018", "2022"]
#label = "Feb12" #obsolete due to bugs in mass bins (underflow)
label = "Feb16"

inputFolder = "/Users/escalante/cernbox/www/protected/ddm/run3data/Run3/TF_QCD_{LABEL}/".format(LABEL=label)
plotsFolder = "{INPUTFOLDER}/TF_plots/".format(INPUTFOLDER = inputFolder)

selections_QCD = []
selections_QCD.append(
    {
        "selection":"IDETANDTIDETASEG_SS",
        "cut": "REP_LXYE_CHI2_COSA_LXYS_DCA_IDETANDTIDETASEG_SEG_DSATIME_DIR_BBDSATIMEDIFF_DPHI_SS",

        "histogram1":"DSAISO0P1",
        "legend1":"Iso.",
        "histogram2":"IDSAISO0P1",

        "legend2":"Non Iso.",
        "dataset": "DoubleMuon",
        "root_file1": "{INPUTFOLDER}/base_overlay_qcd_{SELECTION}_{HISTOGRAM1}_{HISTOGRAM2}/dsa_{YEAR}_{VARIABLE}_{DATASET}_{CUT}_dcuts_{HISTOGRAM1}_{HISTOGRAM2}{VARIABLE_SUFFIX}.root",
        "root_file2": "", #not needed
    }
)

selections_QCD.append(
    {
        "selection":"IDETANDTIDETASEG_OS",
        "cut": "REP_LXYE_CHI2_COSA_LXYS_DCA_IDETANDTIDETASEG_SEG_DSATIME_DIR_BBDSATIMEDIFF_DPHI_OS",

        "histogram1":"DSAISO0P1",
        "legend1":"Iso.",
        "histogram2":"IDSAISO0P1",

        "legend2":"Non Iso.",
        "dataset": "DoubleMuon",
        "root_file1": "{INPUTFOLDER}/base_overlay_qcd_{SELECTION}_{HISTOGRAM1}_{HISTOGRAM2}/dsa_{YEAR}_{VARIABLE}_{DATASET}_{CUT}_dcuts_{HISTOGRAM1}_{HISTOGRAM2}{VARIABLE_SUFFIX}.root",
        "root_file2": "", #not needed
    }
)

selections_QCD.append(
    {
        "selection":"IDETANDTIDETASEG_noSEG_SS",
        "cut": "REP_LXYE_CHI2_COSA_LXYS_DCA_IDETANDTIDETASEG_DSATIME_DIR_BBDSATIMEDIFF_DPHI_SS",

        "histogram1":"DSAISO0P1",
        "legend1":"Iso.",
        "histogram2":"IDSAISO0P1",

        "legend2":"Non Iso.",
        "dataset": "DoubleMuon",
        "root_file1": "{INPUTFOLDER}/base_overlay_qcd_{SELECTION}_{HISTOGRAM1}_{HISTOGRAM2}/dsa_{YEAR}_{VARIABLE}_{DATASET}_{CUT}_dcuts_{HISTOGRAM1}_{HISTOGRAM2}{VARIABLE_SUFFIX}.root",
        "root_file2": "", #not needed
    }
)

selections_QCD.append(
    {
        "selection":"IDETANDTIDETASEG_noSEG_OS",
        "cut": "REP_LXYE_CHI2_COSA_LXYS_DCA_IDETANDTIDETASEG_DSATIME_DIR_BBDSATIMEDIFF_DPHI_OS",

        "histogram1":"DSAISO0P1",
        "legend1":"Iso.",
        "histogram2":"IDSAISO0P1",

        "legend2":"Non Iso.",
        "dataset": "DoubleMuon",
        "root_file1": "{INPUTFOLDER}/base_overlay_qcd_{SELECTION}_{HISTOGRAM1}_{HISTOGRAM2}/dsa_{YEAR}_{VARIABLE}_{DATASET}_{CUT}_dcuts_{HISTOGRAM1}_{HISTOGRAM2}{VARIABLE_SUFFIX}.root",
        "root_file2": "", #not needed
    }
)

selections_QCD.append(
    {
        "selection":"IMASS_OS",
        "cut": "REP_LXYE_IMASS_CHI2_COSA_LXYS_DCA_DETANDT_DETASEG_SEG_DSATIME_DIR_BBDSATIMEDIFF_DPHI_OS",
        "histogram1":"DSAISO0P1",
        "legend1":"Iso.",
        "histogram2":"IDSAISO0P1",

        "legend2":"Non Iso.",
        "dataset": "DoubleMuon",
        "root_file1": "{INPUTFOLDER}/base_overlay_qcd_{SELECTION}_{HISTOGRAM1}_{HISTOGRAM2}/dsa_{YEAR}_{VARIABLE}_{DATASET}_{CUT}_dcuts_{HISTOGRAM1}_{HISTOGRAM2}{VARIABLE_SUFFIX}.root",
        "root_file2": "", #not needed
    }
)

selections_QCD.append(
    {
        "selection":"IMASS_SS",
        "cut": "REP_LXYE_CHI2_COSA_LXYS_DCA_DETANDT_DETASEG_SEG_DSATIME_DIR_BBDSATIMEDIFF_DPHI_SS",

        "histogram1":"DSAISO0P1",
        "legend1":"Iso.",
        "histogram2":"IDSAISO0P1",

        "legend2":"Non Iso.",
        "dataset": "DoubleMuon",
        "root_file1": "{INPUTFOLDER}/base_overlay_qcd_{SELECTION}_{HISTOGRAM1}_{HISTOGRAM2}/dsa_{YEAR}_{VARIABLE}_{DATASET}_{CUT}_dcuts_{HISTOGRAM1}_{HISTOGRAM2}{VARIABLE_SUFFIX}.root",
        "root_file2": "", #not needed
    }
)

#QCD
#makePlotRatio(years, selections_QCD, xtitle = "m_{#mu#mu}", ytitle = "Events", ratiotitle = "TF_{QCD}", variable = "mass", variable_suffix = "_extra-xe_6_10_30_60_80")
makePlotRatio(years, selections_QCD, xtitle = "m_{#mu#mu}", ytitle = "Events", ratiotitle = "TF_{QCD}", variable = "mass", variable_suffix = "_extra-xe_0_2_4_6_10_30_40_50")
makePlotRatio(years, selections_QCD, xtitle = "m_{#mu#mu}", ytitle = "Events", ratiotitle = "TF_{QCD}", variable = "mass", variable_suffix = "_extra-x1_0_x2_60_nx_6")
makePlotRatio(years, selections_QCD, xtitle = "min(p_{T})", ytitle = "Events", ratiotitle = "TF_{QCD}", variable = "minpt", variable_suffix = "_extra-x1_0_x2_60_nx_12")
makePlotRatio(years, selections_QCD, xtitle = "#eta", ytitle = "Events", ratiotitle = "TF_{QCD}", variable = "eta", variable_suffix = "")
makePlotRatio(years, selections_QCD, xtitle = "L_{xy}/#sigma_{L_{xy}}", ytitle = "Events", ratiotitle = "TF_{QCD}", variable = "lxysigpv", variable_suffix = "_extra-x1_0_x2_60_nx_20")
makePlotRatio(years, selections_QCD, xtitle = "#Delta R_{#mu#mu}", ytitle = "Events", ratiotitle = "TF_{QCD}", variable = "deltar", variable_suffix = "_extra-x1_0_x2_0.5_nx_20")
makePlotRatio(years, selections_QCD, xtitle = "vtx. norm #chi^{2}", ytitle = "Events", ratiotitle = "TF_{QCD}", variable = "vtxnormchi2", variable_suffix = "")
makePlotRatio(years, selections_QCD, xtitle = "#Delta #phi", ytitle = "Events", ratiotitle = "TF_{QCD}", variable = "deltaphi", variable_suffix = "")
makePlotRatio(years, selections_QCD, xtitle = "D.C.A", ytitle = "Events", ratiotitle = "TF_{QCD}", variable = "dca", variable_suffix = "")


inputFolder = "/Users/escalante/cernbox/www/protected/ddm/run3data/Run3/TF_DY_{LABEL}/".format(LABEL=label)
plotsFolder = "{INPUTFOLDER}/TF_plots/".format(INPUTFOLDER = inputFolder)

selections_DY = []
selections_DY.append(
    {
        "selection":"ILXYS",
        "cut": "REP_LXYE_MASS_CHI2_COSA_ILXYS_DCA_DETANDT_DETASEG_SEG_DSATIME_DIR_BBDSATIMEDIFF_DSAISO0P1",

        "histogram1":"DPHI",
        "legend1":"|#Delta#Phi| < #pi/4",

        "histogram2":"IDPHI3",
        "legend2":"|#Delta#Phi| > 3#pi/4",

        "dataset": "DoubleMuon",
        "root_file1": "{INPUTFOLDER}/base_overlay_dy_{SELECTION}_{HISTOGRAM1}_{HISTOGRAM2}/dsa_{YEAR}_{VARIABLE}_{DATASET}_{CUT}_dcuts_{HISTOGRAM1}_{HISTOGRAM2}{VARIABLE_SUFFIX}.root",
        "root_file2": "", #not needed
    }
)

selections_DY.append(
    {
        "selection":"PATPAT",
        "cut": "DSA3_LXYE_MASS_CHI2_COSA_DCA_DETANDT_DETASEG_SEG_DSATIME_DIR_BBDSATIMEDIFF_OS_DYTFPATCUTS_DSAISO0P1",

        "histogram1":"DPHI",
        "legend1":"|#Delta#Phi| < #pi/4",

        "histogram2":"IDPHI3",
        "legend2":"|#Delta#Phi| > 3#pi/4",

        "dataset": "DoubleMuon",
        "root_file1": "{INPUTFOLDER}/base_overlay_dy_{SELECTION}_{HISTOGRAM1}_{HISTOGRAM2}/dsa_{YEAR}_{VARIABLE}_{DATASET}_{CUT}_dcuts_{HISTOGRAM1}_{HISTOGRAM2}{VARIABLE_SUFFIX}.root",
        "root_file2": "", #not needed
    }
)

selections_DY.append(
    {
        "selection":"HYB",
        "cut": "DSA11_LXYE_MASS_CHI2_COSA_DCA_DETANDT_DETASEG_SEG_DSATIME_DIR_BBDSATIMEDIFF_OS_DYTFHYBCUTS_DSAISO0P1",

        "histogram1":"DPHI",
        "legend1":"|#Delta#Phi| < #pi/4",

        "histogram2":"IDPHI3",
        "legend2":"|#Delta#Phi| > 3#pi/4",

        "dataset": "DoubleMuon",
        "root_file1": "{INPUTFOLDER}/base_overlay_dy_{SELECTION}_{HISTOGRAM1}_{HISTOGRAM2}/dsa_{YEAR}_{VARIABLE}_{DATASET}_{CUT}_dcuts_{HISTOGRAM1}_{HISTOGRAM2}{VARIABLE_SUFFIX}.root",
        "root_file2": "", #not needed
    }
)

#DY
makePlotRatio(years, selections_DY, xtitle = "m_{#mu#mu}", ytitle = "Events", ratiotitle = "TF_{DY}", variable = "mass", variable_suffix = "_extra-xe_6_10_30_60_80")
makePlotRatio(years, selections_DY, xtitle = "L_{xy}/#sigma_{L_{xy}}", ytitle = "Events", ratiotitle = "TF_{DY}", variable = "lxysigpv", variable_suffix = "_extra-x1_0_x2_6_nx_6")


selections_DY = []
selections_DY.append(
    {
        "selection":"ILXYS",
        "cut": "REP_LXYE_MASS_CHI2_COSA_ILXYS_DCA_DETANDT_DETASEG_SEG_DSATIME_DIR_BBDSATIMEDIFF_DSAISO0P1",

        "histogram1":"DPHI",
        "legend1":"|#Delta#Phi| < #pi/4",

        "histogram2":"IDPHI3",
        "legend2":"|#Delta#Phi| > 3#pi/4",

        "dataset": "DoubleMuon",
        "root_file1": "{INPUTFOLDER}/base_overlay_dy_{SELECTION}_{HISTOGRAM1}_{HISTOGRAM2}/dsa_{YEAR}_{VARIABLE}_{DATASET}_{CUT}_dcuts_{HISTOGRAM1}_{HISTOGRAM2}{VARIABLE_SUFFIX}.root",
        "root_file2": "", #not needed
    }
)

#makePlotRatio(["2016"], selections_DY, xtitle = "m_{#mu#mu}", ytitle = "Events", ratiotitle = "TF_{DY}", variable = "mass", variable_suffix = "_extra-xe_6_10_30_60_80")
