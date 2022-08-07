import ROOT
# import pdb to DEBUG


def getTree(myFile, treeDir, treeName, label):

    f = ROOT.TFile.Open(myFile)
    tdir = f.Get(treeDir)
    t = tdir.Get(treeName)
    return f, t, label


def createPlots(variable, trees, labels, outputFolder):

    # variable configuration.
    variableName = variable["var_name"]
    selection = variable["selection"]
    nbins = variable["nbins"]
    inibin = variable["inibin"]
    endbin = variable["endbin"]
    norm = variable["norm"]

    c1 = ROOT.TCanvas("c1")

    hist_dic = {}
    colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange]
    legend = ROOT.TLegend(0.15, 0.7, 0.35, 0.85)
    for index, ktree in enumerate(trees):
        if index > 3:
            print("reader.py only allows up to 4 histograms")
            break
        hist_dic["hist_"+str(index)] = ROOT.TH1D(labels[index],
                                                 selection[index], nbins, inibin, endbin)
        plotlabel = "hist"
        if index > 0:
            plotlabel = "SAMES"
        ktree.Draw(variableName+" >> "+labels[index], selection[index], "goff")
        if norm == True and hist_dic["hist_"+str(index)].GetEntries() > 0:
            hist_dic["hist_"+str(index)].Scale(1/hist_dic["hist_"+str(index)].GetEntries())
        hist_dic["hist_"+str(index)].Draw(plotlabel)
        hist_dic["hist_"+str(index)].SetLineColor(colors[index])
        hist_dic["hist_"+str(index)].GetXaxis().SetTitle(variableName)
        xlabel = "Events"
        if norm == True:
            xlabel = "Events. norm."
        hist_dic["hist_"+str(index)].GetYaxis().SetTitle(xlabel)

        ROOT.gPad.Update()
        stat = hist_dic["hist_"+str(index)].FindObject("stats")
        stat.SetTextColor(colors[index])
        hist_dic["hist_"+str(index)].FindObject("stats").SetX1NDC(0.80-0.2*index)
        hist_dic["hist_"+str(index)].FindObject("stats").SetX2NDC(0.99-0.2*index)

    # output files.
    formats = [".png", ".pdf", ".tex", ".C"]
    suffix = ""
    if norm == True:
        suffix = suffix + "_norm"
    for kformat in formats:
        filename = outputFolder+variableName+suffix
        filename = filename.replace("()", "")  # cleanup the filename
        filename = filename.replace(".", "_")  # cleantup the filename
        filename = filename+kformat
        c1.SaveAs(filename)
