import ROOT
from ROOT import gPad

def getTree(myFile, treeDir, treeName, label):
    
    f = ROOT.TFile.Open(myFile)
    tdir = f.Get(treeDir)
    t = tdir.Get(treeName)
    return f, t, label

def createPlots(variable, trees, labels, outputFolder):
    
    #variable configuration.
    variableName = variable["var_name"]
    selection = variable["selection"]
    nbins = variable["nbins"]
    inibin = variable["inibin"]
    endbin = variable["endbin"]
    norm = variable["norm"]

    c1=ROOT.TCanvas("c1")

    hist_dic = {}
    hist_index = 0
    colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen]
    legend = ROOT.TLegend (0.15 ,0.7 ,0.35 ,0.85)
    for ktree in trees:
        hist_dic["hist_"+str(hist_index)] = ROOT.TH1D(labels[hist_index], selection, nbins, inibin, endbin)        
        plotlabel = "hist SAME"
        if hist_index == 1 : plotlabel = "SAMES"
        ktree.Draw(variableName+" >> "+labels[hist_index], selection, "goff")
        if norm == True and hist_dic["hist_"+str(hist_index)].GetEntries()>0:
            hist_dic["hist_"+str(hist_index)].Scale(1/hist_dic["hist_"+str(hist_index)].GetEntries())
        hist_dic["hist_"+str(hist_index)].Draw(plotlabel)
        hist_dic["hist_"+str(hist_index)].SetLineColor(colors[hist_index])
        hist_dic["hist_"+str(hist_index)].GetXaxis().SetTitle(variableName)
        xlabel = "Events"
        if norm == True:
            xlabel = "Events. norm."
        hist_dic["hist_"+str(hist_index)].GetYaxis().SetTitle(xlabel)
        
        gPad.Update()
        stat = hist_dic["hist_"+str(hist_index)].FindObject("stats")
        stat.SetTextColor(colors[hist_index])        
        hist_dic["hist_"+str(hist_index)].FindObject("stats").SetX1NDC(0.80-0.2*hist_index)
        hist_dic["hist_"+str(hist_index)].FindObject("stats").SetX2NDC(0.99-0.2*hist_index)

        hist_index = hist_index +1

                
    #output files.
    formats = [".png", ".pdf", ".tex", ".C"]
    suffix = ""
    if norm == True:
        suffix = suffix + "_norm"
    for kformat in formats:
        c1.SaveAs(outputFolder+variableName+suffix+kformat)

