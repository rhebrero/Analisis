import ROOT
import subprocess
import os
class Sample:
    'Sample information class'
    def __init__(self):
        self.sampleName = []
        self.sampleLegendName = []
        self.histName = []
        self.histColor = []

    def AddSample(self, sampleName, legendName, histName, histColor):
        if ".root" not in sampleName: sampleName = GetFilesFromSampleName(sampleName) # Useful in case the diretory is given instead of a file
        self.sampleName.append(sampleName)
        self.sampleLegendName.append(legendName)
        self.histName.append(histName)
        self.histColor.append(histColor)

    def GetSampleName(self):
        return self.sampleName

    def GetLegendName(self):
        return self.sampleLegendName

    def GetHistName(self):
        return self.histName

    def GetHistColor(self):
        return self.histColor

    def nSamples(self):
        return len(self.sampleName)

def GetFilesFromSampleName(folderList):
    #import pdb
    outputCleaned = []
    folderList = folderList.split(",")
    print ("Input:")
    print (folderList)
    #if sampleName[-1] != "/":
    #    print ("provide a folder")
    #    return outputCleaned

    #access to folders/wildcards is not implemented (yet)
    hostname = os.getenv('HOSTNAME')

    prefix = "ls "
    samplePrefix = ""

    if "/store/" in folderList[0]:
        prefix = "gfal-ls gsiftp://se.grid.vbc.ac.at:2811"
        samplePrefix = "root://eos.grid.vbc.ac.at/"

    #get all samples
    output = []
    for folder in folderList:
        if len(folder) == 0: continue
        depth  = 0
        command   = prefix + folder
        rootFiles = subprocess.getoutput(command)
        rootFiles = rootFiles.split('/n')
        print (rootFiles)
        #adding folder to directory
        for index, rootFile in enumerate(rootFiles):
            if ".root" in rootFile: output.append(samplePrefix+folder+rootFile)

    print ("Summary")
    print ("nfiles", len(output))
    print (output)
    #pdb.set_trace()
    return output


def createSimple1DPlot(var, title, nbins, inibin, endbin, samples):
    hist1D = []
    colors = [1,2,3,4,6,7,8,9,28,30,38,49,46]
    for index, ksamples in enumerate(samples.GetSampleName()):
        hist1D.append(ROOT.TH1F(var, title, nbins, inibin, endbin))
        hist1D[index].SetDirectory(0)
        hist1D[index].Sumw2()
        hist1D[index].SetLineColor(samples.GetHistColor()[index])

    return hist1D

def createSimple2DPlot(var, title, nbinsX, inibinX, endbinX, nbinsY, inibinY, endbinY, samples):
    hist2D = []
    colors = [1,2,3,4,6,7,8,9,28,30,38,49,46]
    for index, ksamples in enumerate(samples.GetSampleName()):
        hist2D.append(ROOT.TH2F(var, title, nbinsX, inibinX, endbinX, nbinsY, inibinY, endbinY))
        hist2D[index].SetDirectory(0)
        hist2D[index].SetMarkerColor(samples.GetHistColor()[index])
        hist2D[index].SetLineColor(samples.GetHistColor()[index])
        hist2D[index].SetMarkerStyle(20)
        hist2D[index].SetMarkerSize(0.6)

    return hist2D

def makeSimple1DPlot(var, canvas, samples, title, xtitle, ytitle, output, folder, logy=False, showOnly = [], norm = True):

    file = ROOT.TFile(folder+output+"-hist.root","recreate")
    file.cd()
    template = []

    ROOT.gStyle.SetOptStat(0)

#    leg = ROOT.TLegend(0.65,0.55,.90,.90)
    leg = ROOT.TLegend(0.55,0.65,.90,.90)
    leg.SetFillColor(0)

    Canvas = ROOT.TCanvas(canvas, title, 10, 10, 700, 500 )
    Canvas.cd()

    plotted = False
    for index, hist in enumerate(var):
        #needed to store the templates
        template.append(hist.Clone())
        template[index].SetName(samples.GetHistName()[index])

        ##hist
        normHist = 1
        if hist.Integral()> 0 and norm == True:
            hist.Scale(normHist/hist.Integral())
        if len(showOnly) >0:
            if samples.GetHistName()[index] not in showOnly:
                continue

        if plotted == True:
            hist.Draw("hist same")

        if plotted == False:
            Minimum = hist.GetMinimum()
            Maximum = hist.GetMaximum()

            if (Minimum >0.) and logy==False: hist.SetMinimum(.0)
            if (Minimum >0.01) and logy==True: hist.SetMinimum(0.01)
            if (Maximum >0.) and logy==False: hist.SetMaximum(1.3*hist.GetMaximum())
#            if (Maximum >0.) and logy==True: hist.SetMaximum(1.3*hist.GetMaximum())
#if (Maximum >0.) and logy==False: hist.SetMaximum(1.)
            if (Maximum >0.) and logy==True and norm == True: hist.SetMaximum(1.3)
            if (Maximum >0.) and logy==True and norm == False: hist.SetMaximum(1.3*hist.GetMaximum())

            hist.Draw("hist")
            hist.SetTitle(title)
#            var[index].GetXaxis()
            Xaxis = hist.GetXaxis()
            Xaxis.SetTitle(xtitle)
            Yaxis = hist.GetYaxis()
            Yaxis.SetTitle(ytitle)
            plotted = True

        leg.AddEntry(var[index], samples.GetLegendName()[index], "l")

    leg.Draw()
    if logy == True:
        Canvas.SetLogy(1)

    Canvas.SaveAs(folder+output+".pdf")
    Canvas.SaveAs(folder+output+".png")
    Canvas.SaveAs(folder+output+".eps")
    Canvas.SaveAs(folder+output+".root")
    file.Write()
    file.Close()

def makeSimple2DPlot(var, canvas, samples, title, xtitle, ytitle, output, folder, showOnly = [], showReversed= True):

    file = ROOT.TFile(folder+output+"-2Dhist.root","recreate")
    file.cd()
    template = []

    ROOT.gStyle.SetOptStat(0)

#    leg = ROOT.TLegend(0.65,0.55,.90,.90)
    leg = ROOT.TLegend(0.50,0.65,.90,.90)
    leg.SetFillColor(0)

    Canvas = ROOT.TCanvas(canvas, title, 10, 10, 700, 500 )
    Canvas.cd()

    plotted = False
    for index, hist in enumerate(var):
        #needed to store the templates
        template.append(hist.Clone())
        template[index].SetName(samples.GetHistName()[index])
        if len(showOnly) >0:
            if samples.GetHistName()[index] not in showOnly:
                continue

        if plotted == True:
            hist.Draw("hist same")

        if plotted == False:
            hist.Draw("hist")
            hist.SetTitle(title)

            Xaxis = hist.GetXaxis()
            Xaxis.SetTitle(xtitle)
            Yaxis = hist.GetYaxis()
            Yaxis.SetTitle(ytitle)
            plotted = True

        leg.AddEntry(var[index], samples.GetLegendName()[index], "p")


    ## Make plot cleaner. Illustration only.
    if showReversed==True:
        for index in range(samples.nSamples()-1, -1, -1):
            if len(showOnly) >0:
                if samples.GetHistName()[index] not in showOnly:
                    continue
                var[index].Draw("hist same")

    ########################
    leg.Draw()

    Canvas.SaveAs(folder+output+".pdf")
    Canvas.SaveAs(folder+output+".png")
    Canvas.SaveAs(folder+output+".eps")
    Canvas.SaveAs(folder+output+".root")
    file.Write()
    file.Close()

def makeRatio(RootFileNumName, RootFileDenName, HistNumName, HistDenName, NumTagName, DenTagName, xAxisName, yAxisName, Output, LogScale=True, ColorNum = 2, ColorDen = 1, ColorRatio = 1, Title = "", Rebin = 1, UncMode = "cp"):

    print("Input folder: \n")
    print("\t Num   {ROOTFILENUMNAME} \n".format(ROOTFILENUMNAME = RootFileNumName))
    print("\t Den   {ROOTFILEDENNAME} \n".format(ROOTFILEDENNAME = RootFileDenName))
    print("Input Histogram: \n")
    print("\t Num   {HISTNUMNAME} \n".format(HISTNUMNAME = HistNumName))
    print("\t Den   {HISTDENNAME} \n".format(HISTDENNAME = HistDenName))
    print("Output       {OUTPUT}".format(OUTPUT = Output))

    print (RootFileNumName, HistNumName)
    RootFileNum = ROOT.TFile.Open(RootFileNumName)
    RootFileDen = ROOT.TFile.Open(RootFileDenName)

    HistoNum = RootFileNum.Get(HistNumName)
    HistoDen = RootFileDen.Get(HistDenName)

    print("\t Numerator   Name ", HistoNum.GetName())
    print("\t Numerator   bins ", HistoDen.GetNbinsX())

    print("\t Denominator Name ", HistoDen.GetName())
    print("\t Denominator bins ", HistoNum.GetNbinsX())

    #Rebinning:
    if (Rebin!=1):
        print("HistoNum GetNbinsX()", HistoNum.GetNbinsX())
        print("HistoDen GetNbinsX()", HistoDen.GetNbinsX())

        HistoDen = HistoDen.Rebin(Rebin)
        HistoNum = HistoNum.Rebin(Rebin)

        print("New HistoNum GetNbinsX()", HistoNum.GetNbinsX())
        print("New HistoDen GetNbinsX()", HistoDen.GetNbinsX())

    #if (HistoNum.GetNbinsX() != HistoDen.GetNbinsX()):
    #    print("WARINIG!: Different binning in Reference %d and Validation %d \n")

    YieldsNum = HistoDen.Integral(1,HistoDen.GetNbinsX())
    YieldsDen = HistoNum.Integral(1,HistoNum.GetNbinsX())

    print("Integral Reference  {YIELDSNUM} \n".format(YIELDSNUM=YieldsNum))
    print("Integral Validation {YIELDSDEN} \n".format(YIELDSDEN=YieldsDen))

    if (YieldsNum ==0 or YieldsDen == 0):
        return 0

    HistoNumForRatio = HistoNum.Clone()
    HistoNumForRatio.Sumw2()

    HistoDenForRatio = HistoDen.Clone()
    HistoDenForRatio.Sumw2()

    print("Pre divide \n")
    HistoNumForRatioAsym = ROOT.TGraphAsymmErrors(HistoNumForRatio, HistoDenForRatio, UncMode) #asym uncertainties
    HistoNumForRatio.Divide(HistoDenForRatio) # dummy histogram.
    print("after divide \n")

    Canvas = ROOT.TCanvas("", "", 10, 10, 700, 800 )
    #Canvas = ROOT.TCanvas("", "", 10, 10, 700, 700 )

    ROOT.gStyle.SetOptTitle(0)
    ROOT.gStyle.SetOptStat(0)
    Canvas.SetFillColor(0)
    Canvas.SetFillStyle(4000)
    Canvas.SetTitle("")
    Canvas.cd()

    HistoNum.SetLineColor(ColorNum)
    HistoDen.SetMarkerColor(ColorNum)
    HistoNum.SetLineWidth(2)
    HistoNum.SetFillColor(0)
    HistoNum.SetMarkerSize(0)

    HistoDen.SetLineColor(ColorDen)
    HistoDen.SetMarkerColor(ColorDen)
    HistoDen.SetLineWidth(2)
    HistoDen.SetFillColor(0)

    HistoNumForRatioAsym.SetLineColor(ColorRatio)
    HistoNumForRatioAsym.SetMarkerSize(0.5)
    HistoNumForRatioAsym.SetMarkerStyle(34)
    HistoNumForRatioAsym.SetMarkerColor(ColorRatio)

    #dummy histogram, just for plotting
    HistoNumForRatio.SetLineColor(0)
    HistoNumForRatio.SetMarkerSize(0.5)
    HistoNumForRatio.SetMarkerStyle(34)
    HistoNumForRatio.SetMarkerColor(0)

    #remove all titles
    HistoNum.SetTitle("")
    HistoDen.SetTitle("")
    HistoNumForRatio.SetTitle("")

    pad1 = ROOT.TPad("pad1","top pad",0,0.3,1,1)
    pad1.SetBottomMargin(0.038)
    pad1.Draw()

    pad2 = ROOT.TPad("pad2","bottom pad",0,0.0,1,0.3)
    pad2.SetBottomMargin(0)
    pad2.SetBottomMargin(0.22)
    pad2.Draw()

    pad1.cd()
    pad1.SetLogy(0)
    if (LogScale==True):
        pad1.SetLogy(1)

    #adjust the maximum of the histogram that the plots looks nice.
    Maximum = HistoDen.GetMaximum()

    minimum = 0.0

    if LogScale==True:
        minimum = 1.0

    HistoNum.SetMinimum(minimum)
    HistoDen.SetMinimum(minimum)

    if (HistoDen.GetMaximum() > HistoNum.GetMaximum()):
        if LogScale==True: HistoDen.SetMaximum(HistoDen.GetMaximum()*10)
        HistoDen.Draw("h")
        HistoNum.Draw("p same")
    else:
        if LogScale==True: HistoNum.SetMaximum(HistoNum.GetMaximum()*10)
        HistoNum.Draw("p")
        HistoDen.Draw("h same")

    leg = ROOT.TLegend(0.60,0.70,0.80,0.85)
    leg.SetFillColor(0)
    leg.SetTextSize(0.042)
    leg.SetBorderSize(0)
    leg.SetTextFont(42)
    leg.AddEntry(HistoDen , DenTagName, "l")
    leg.AddEntry(HistoNum , NumTagName, "pe")
    leg.Draw()

    #TString title=""
    text = ROOT.TLatex(0.12, 0.93, Title)
    text.SetNDC()
    text.SetTextFont(42)
    text.SetTextSize(0.045)
    if len(Title) > 0: text.Draw()
    #if (ChiAndKolmogorov == true) preliminary->Draw()

    xax = HistoNum.GetXaxis()
    yax = HistoDen.GetYaxis()
    xax.SetTitle("")
    yax.SetTitle(yAxisName)
    yax.SetTitleSize(0.05)
    yax.SetTitleOffset(0.85)
    yax.SetLabelSize(0.05)

    #Ratio PAD
    pad2.cd()

    RatioMax = 1.0
    if UncMode == "cp":   RatioMax   = 1.0
    if UncMode == "pois": RatioMax = 3.0

    HistoNumForRatio.SetMaximum(RatioMax)
    HistoNumForRatio.SetMinimum(0.)

    HistoNumForRatio.Draw("P") # dummy histogram, just for plotting
    HistoNumForRatioAsym.Draw("pe")

    xax = HistoNumForRatio.GetXaxis()
    yax = HistoNumForRatio.GetYaxis()
    xax.SetTitleSize(0.10)
    xax.SetLabelSize(0.09)
    xax.SetTitleOffset(0.9)
    xax.SetTitle(xAxisName)
    yax.SetTitleSize(0.10)
    yax.SetTitleOffset(0.9)
    yax.SetTitle("Ratio")

    yax.SetLabelSize(0.09)
    yax.SetTitleOffset(0.4)
    yax.SetNdivisions(405)
    minxaxis = xax.GetXmin()
    maxxaxis = xax.GetXmax()

    line = True
    if line == True:
        l = ROOT.TLine(minxaxis,1.0,maxxaxis,1.0)
        l.SetLineColor(2)
        l.SetLineWidth(2)
        l.Draw("same")

    Canvas.SaveAs(Output+".pdf")
    Canvas.SaveAs(Output+".png")
    Canvas.SaveAs(Output+".jpg")
