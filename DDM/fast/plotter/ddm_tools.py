import ROOT
import argparse
import pdb

def configureOptions(options):
    """
    supported pltting options, e.g ["logy", "br"]
    scale  = "logy", "linear" 
    legpos = "tr", "br"
    """
    
    extra_option = {}
    if "logy" in options:
        extra_option["scale"] = "logy"
    else:
        extra_option["scale"] = "linear"

    if "br" in options:
        extra_option["pos"] = "br"
    else:
        extra_option["pos"] = "tr"

    return extra_option

def plot_ratio(root_file1, histogram1, legend1, root_file2, histogram2, legend2, xtitle, ytitle, ratiotitle, selection, output_file, tlist = "main", new_title = "", options = ""):
    """
    Makes a ratio from two input .C files produced with DDM framework 
    """
    # Open the root files
    f1 = ROOT.TFile.Open(root_file1)
    f2 = ROOT.TFile.Open(root_file2)

    # Retrieve the histograms from the canvas
    canvas1 = f1.Get("c")
    canvas2 = f2.Get("c")
    #optional, if histograms are inside a list
    if len(tlist)>0:
        tpad1 = canvas1.GetListOfPrimitives().FindObject("main")
        tpad2 = canvas2.GetListOfPrimitives().FindObject("main")
        # Get the histograms in the canvas
        h1 = tpad1.GetPrimitive(histogram1)
        h2 = tpad2.GetPrimitive(histogram2)
        # Get all the text in the canvas
        TLatexList = []
        tlist1 = tpad1.GetListOfPrimitives()
        for i in range(tlist1.GetSize()):
            obj = tlist1.At(i)
            # Check if the object is a TText object
            if obj.InheritsFrom("TText"):
                TLatexList.append(obj)
    else:
        h1 = canvas1.GetPrimitive(histogram1)
        h2 = canvas2.GetPrimitive(histogram2)

    print(h1.GetName(), h2.GetName())
    print(h1.GetTitle(), h2.GetTitle())

    # configure dynamically plotting options
    extra_option = configureOptions(options)

    # Create a new canvas
    c = ROOT.TCanvas("c", "c", 800, 800)
    #c.Divide(1, 2, 0, 0.1)
    c.Divide(1, 2)

    # Plot h1 and h2 in the first subplot
    c.cd(1)
    h1.Draw("E1")
    h2.Draw("SAME E1")
    h1.SetTitle("")
    h2.SetTitle("")
    h1.GetXaxis().SetTitle("")
    h1.GetYaxis().SetTitle(ytitle)
    h1.GetYaxis().SetTitleOffset(0.8)
    h1.SetLineColor(ROOT.kBlue)
    h1.SetMarkerColor(ROOT.kBlue)
    h2.SetLineColor(ROOT.kRed)
    h2.SetMarkerColor(ROOT.kRed)
    if extra_option["scale"] == "logy":
        ROOT.gPad.SetLogy(1)
    elif extra_option["scale"] == "linear":
        ROOT.gPad.SetLogy(0)
    else:
        ROOT.gPad.SetLogy(1)

    c.GetPad(1).SetBottomMargin(0.07)
    c.GetPad(1).SetTopMargin(0.09)
    c.GetPad(1).SetLeftMargin(0.12)

    # Draw the legend on the canvas
    legend = ROOT.TLegend(0.67, 0.67, 0.85, 0.85)
    if extra_option["pos"] == "br":
        legend = ROOT.TLegend(0.67, 0.2, 0.85, 0.35)

    legend.AddEntry(h1, legend1, "l")
    legend.AddEntry(h2, legend2, "l")
    legend.SetBorderSize(0)
    legend.Draw()

    #retrieve from canvas
    if len(tlist)>0 and len(TLatexList)>0:
        for kTLatex in TLatexList:
            if len(new_title) and "TeV)" in kTLatex.GetTitle(): kTLatex.SetTitle(new_title)
            if "CMS" in kTLatex.GetTitle():
                kTLatex.SetTitle(selection)
                offset_X = 0.02
            else:
                #    kTLatex.SetText(kTLatex.GetTitle() + " Internal")
                offset_X = 0.05

            offset_Y = 0.03
            kTLatex.SetTextSize(0.06)
            kTLatex.SetY(kTLatex.GetY()-offset_Y)
            kTLatex.SetX(kTLatex.GetX()-offset_X)
            kTLatex.Draw()

    # Plot the ratio of h1 and h2 in the second subplot
    c.cd(2)
    ratio = h1.Clone("ratio")
    ratio.Divide(h2)
    ratio.Draw("E1")
    ratio.SetTitle("")
    ratio.GetXaxis().SetTitle(xtitle)
    ratio.GetYaxis().SetTitle(ratiotitle)
    ratio.SetMarkerStyle(21)
    ratio.SetMarkerColor(ROOT.kBlack)
    ratio.SetLineColor(ROOT.kBlack)
    ratio.SetMinimum(0.0)
    ratio.SetMaximum(2)
    c.GetPad(2).SetTopMargin(0.02)
    c.GetPad(2).SetBottomMargin(0.2)
    c.GetPad(2).SetLeftMargin(0.12)

    # Calculate and plot the statistical uncertainty on h1, h2, and ratio
    line_for_text_ratio = []
    line_for_text_yield = []

    for i in range(h1.GetNbinsX()+1):
        ratio_value = ratio.GetBinContent(i)
        h1_value = h1.GetBinContent(i)
        h2_value = h2.GetBinContent(i)
        print("h1", i, h1.GetBinLowEdge(i), h1.GetBinLowEdge(i+1), h1_value, ratio_value)
        print("h2", i, h2.GetBinLowEdge(i), h2.GetBinLowEdge(i+1), h2_value, ratio_value)
        if h2_value != 0:
            uncertainty = ROOT.TMath.Sqrt( h1_value / h2_value**2 + h1_value**2 / h2_value**4 )
            print("Divide", i, ratio.GetBinError(i))
            #ratio.SetBinError(i, ratio_value * uncertainty)
            ##internal check
            #print("Chat GPT ", i, ratio_value*uncertainty)
            #my_uncertainty = ratio_value*ratio_value * (1/h1_value + 1/h2_value)
            my_uncertainty = ratio_value * (1/h2_value + h1_value/h2_value**2)
            my_uncertainty = ROOT.TMath.Sqrt(my_uncertainty)
            #print("Alberto GPT ", i, my_uncertainty)
            #ratio.SetBinError(i, uncertainty)
            #ratio.SetBinError(i, my_uncertainty)
            line_for_text_ratio.append(" {LOW_EDGE} < {XTITLE} < {UP_EDGE}, ratio = {VALUE}+-{ERROR} \n".format(LOW_EDGE = ratio.GetBinLowEdge(i), XTITLE = xtitle, UP_EDGE = ratio.GetBinLowEdge(i+1), VALUE = round(ratio_value, 3), ERROR = round(my_uncertainty,3)))
            line_for_text_yield.append(" {LOW_EDGE} < {XTITLE} < {UP_EDGE}, num   = {VALUE_NUM}, den = {VALUE_DEN} \n".format(LOW_EDGE = h1.GetBinLowEdge(i), XTITLE = xtitle, UP_EDGE = h1.GetBinLowEdge(i+1), VALUE_NUM = round(h1_value, 3), VALUE_DEN = round(h2_value, 3)))
        else:
            ratio.SetBinError(i, 0)

    line = ROOT.TLine(ratio.GetXaxis().GetXmin(), 1, ratio.GetXaxis().GetXmax(), 1)
    line.SetLineColor(ROOT.kRed)
    line.SetLineStyle(2)
    line.Draw()

    #line2 = ROOT.TLine(ratio.GetXaxis().GetXmin(), 0.5, ratio.GetXaxis().GetXmax(), 0.5)
    #line2.SetLineColor(ROOT.kBlue)
    #line2.SetLineStyle(2)
    #line2.Draw()

    # Save the plot
    #c.Update()
    for extension in [".png",".pdf",".C", ".root"]:
        c.SaveAs(output_file+extension)

    # Save the yields
    f = open(output_file+".txt", "w")
    f.write("yields for: {FILE} \n".format(FILE = output_file))
    f.write("TOP PAD \n")
    for kline in line_for_text_yield:
        f.write(kline)

    f.write("BOTTOM PAD \n")
    for kline in line_for_text_ratio:
        f.write(kline)
    f.close()

def plot_overlay(root_file1, histogram1, legend1, root_file2, histogram2, legend2, xtitle, ytitle, selection, output_file, tlist = "main", new_title = "", options = ""):
    """
    Makes an overlay of two histograms from two .C files produced with DDM framework
    """
    
    # Open the root files
    f1 = ROOT.TFile.Open(root_file1)
    f2 = ROOT.TFile.Open(root_file2)

    # Retrieve the histograms from the canvas
    canvas1 = f1.Get("c")
    canvas2 = f2.Get("c")
    #optional, if histograms are inside a list
    if len(tlist)>0:
        tpad1 = canvas1.GetListOfPrimitives().FindObject("main")
        tpad2 = canvas2.GetListOfPrimitives().FindObject("main")
        # Get the histograms in the canvas
        h1 = tpad1.GetPrimitive(histogram1)
        h2 = tpad2.GetPrimitive(histogram2)
        # Get all the text in the canvas
        TLatexList = []
        tlist1 = tpad1.GetListOfPrimitives()
        for i in range(tlist1.GetSize()):
            obj = tlist1.At(i)
            # Check if the object is a TText object
            if obj.InheritsFrom("TText"):
                TLatexList.append(obj)
    else:
        h1 = canvas1.GetPrimitive(histogram1)
        h2 = canvas2.GetPrimitive(histogram2)

    print(h1.GetName(), h2.GetName())
    print(h1.GetTitle(), h2.GetTitle())

    # Create a new canvas
    c = ROOT.TCanvas("c", "c", 800, 800)

    # configure dynamically plotting options
    extra_option = configureOptions(options)

    # Plot h1 and h2 in the first subplot
    h1.Draw("E1")
    h2.Draw("SAME E1")
    h1.SetTitle("")
    h2.SetTitle("")

    h1.GetXaxis().SetTitle(xtitle)
    h1.GetYaxis().SetTitle(ytitle)
    h1.GetXaxis().SetTitleSize(0.05)
    h1.GetXaxis().SetTitleOffset(0.95)
    h1.GetXaxis().SetLabelSize(0.030)
    h1.GetYaxis().SetTitleSize(0.05)
    h1.GetYaxis().SetTitleOffset(1.0)
    h1.GetYaxis().SetLabelSize(0.030)

    h1.SetLineColor(ROOT.kBlue)
    h1.SetMarkerColor(ROOT.kBlue)
    h2.SetLineColor(ROOT.kRed)
    h2.SetMarkerColor(ROOT.kRed)

    if extra_option["scale"] == "logy":
        ROOT.gPad.SetLogy(1)
    elif extra_option["scale"] == "linear":
        ROOT.gPad.SetLogy(0)
    else:
        ROOT.gPad.SetLogy(1)
    
    c.SetBottomMargin(0.13)
    c.SetTopMargin(0.09)
    c.SetLeftMargin(0.12)

    # Draw the legend on the canvas
    legend = ROOT.TLegend(0.67, 0.67, 0.85, 0.85)
    if extra_option["pos"] == "br":
        legend = ROOT.TLegend(0.47, 0.2, 0.85, 0.35)

    legend.AddEntry(h1, legend1, "l")
    legend.AddEntry(h2, legend2, "l")
    legend.SetBorderSize(0)
    legend.Draw()

    #retrieve from canvas
    if len(tlist)>0 and len(TLatexList)>0:
        for kTLatex in TLatexList:
            if len(new_title) and "TeV)" in kTLatex.GetTitle(): kTLatex.SetTitle(new_title)
            if "CMS" in kTLatex.GetTitle():
                kTLatex.SetTitle(selection)
                offset_X = 0.02
            else:
                #    kTLatex.SetText(kTLatex.GetTitle() + " Internal")
                offset_X = 0.05

            offset_Y = 0.03
            kTLatex.SetTextSize(0.04)
            kTLatex.SetY(kTLatex.GetY()-offset_Y)
            kTLatex.SetX(kTLatex.GetX()-offset_X)
            kTLatex.Draw()

    # Save the plot
    #c.Update()
    for extension in [".png",".pdf",".C", ".root"]:
        c.SaveAs(output_file+extension)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot the ratio of two histograms")
    parser.add_argument("--root_file1", type=str, required=True, help="The name of the first root file")
    parser.add_argument("--histogram1", type=str, required=True, help="The name of the first histogram")
    parser.add_argument("--legend1"   , type=str, required=True, help="The name of the first legend")

    parser.add_argument("--root_file2", type=str, required=True, help="The name of the second root file")
    parser.add_argument("--histogram2", type=str, required=True, help="The name of the second histogram")
    parser.add_argument("--legend2"   , type=str, required=True, help="The name of the second legend")

    parser.add_argument("--xtitle"     , type=str, required=True,  help="X axis title")
    parser.add_argument("--ytitle"     , type=str, required=True,  help="Y axis title")
    parser.add_argument("--ratiotitle" , type=str, required=True, help="Ratio axis title")
    parser.add_argument("--selection"  , type=str, required=False,  default = "", help="Selection label")

    parser.add_argument("--output_file", type=str, required=True, help="The name of the output PDF file")
    args = parser.parse_args()

    plot_ratio(args.root_file1, args.histogram1, args.legend1, args.root_file2, args.histogram2, args.legend2, args.xtitle, args.ytitle, args.ratiotitle, args.selection, args.args.output_file)
