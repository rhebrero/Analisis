#simple ratio plot
from ddm_tools import plot_ratio, plot_overlay

inputFolder = "/Users/escalante/Downloads/"
plotsFolder = inputFolder

root_FG = inputFolder + "pat_2022FG_mind0pv_REP_LXYE_ONEORMORENONISO_CHI2_COSA_DCA_PXL_DPHI_HB4V_NTRKLAYSLXY_OS_JPSIMASSTIGHT_PT23_HLTRun2PP_add_HLTDisplacedL3_Jpsi_eff.root"
root_CD = inputFolder + "pat_2022CD_mind0pv_REP_LXYE_ONEORMORENONISO_CHI2_COSA_DCA_PXL_DPHI_HB4V_NTRKLAYSLXY_OS_JPSIMASSTIGHT_PT23_HLTRun2PP_add_HLTDisplacedL3_Jpsi_eff.root"

histogram = "HData2022postHLTDisplacedL3_copy"

legend_FG = "FG"
legend_CD = "CD PromptReco"

#plot_ratio(root_FG, histogram, legend_FG, root_CD, histogram, legend_CD, "d_{0}", "#epsilon", "#epsilon_{FG}/#epsilon_{CD}", selection= "CMS Work in progress", output_file = plotsFolder + "combinedTrigger_ratio", new_title = "(13.6 TeV)", options = ["linear", "br"])
plot_overlay(root_FG, histogram, legend_FG, root_CD, histogram, legend_CD, "d_{0}", "Trigger efficiency", selection= "CMS #it{internal}", new_title = "(13.6 TeV)", output_file = plotsFolder + "combinedTrigger", options = ["linear", "br"])
