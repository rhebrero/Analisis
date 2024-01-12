import sys 
oldargv = sys.argv[:]
sys.arg = [ '-b-' ]
import ROOT 

ROOT.gROOT.SetBatch(True)
sys.argv = oldargv


ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable() #habilita el entorno FWLite

from math import *
import numpy as np
from array import array


from utils import getLibraries
from GenLongLivedUtils import *
from SimpleTools import *

import pdb



def readFile(dictionary, filename, lumi, sigma, bckg):
    
    with open(filename, "r") as f:
        for x in f:
            if '#' in x[0]: continue
                
            x_split = x.split(",") 
            ae_1 = x_split[1]
            ae_2 = x_split[2]
            ae_3 = x_split[3]
            
            dictionary["AE1"].append(float(ae_1))
            dictionary["AE2"].append(float(ae_2))
            dictionary["AE3"].append(float(ae_3))

            dictionary["EV1"].append((float(ae_1)) *118* sigma)
            dictionary["EV2"].append((float(ae_2)) *lumi * sigma)
            dictionary["EV3"].append((float(ae_3)) *lumi * sigma)

            dictionary["S1"].append((float(ae_1)) *lumi * sigma/sqrt(bckg))
            dictionary["S2"].append((float(ae_2)) *lumi * sigma/sqrt(bckg))
            dictionary["S3"].append((float(ae_3)) *lumi * sigma/sqrt(bckg))

    return dictionary

ae_100 = {"labels": ["Aceptancia", "Eventos", "Significancia", "100"], "AE1": [], "AE2": [], "AE3":[], "EV1": [], "EV2": [], "EV3": [], "S1": [], "S2": [], "S3": []}
ae_500 = {"labels": ["Aceptancia", "Eventos", "Significancia", "500"], "AE1": [], "AE2": [], "AE3":[], "EV1": [], "EV2": [], "EV3": [], "S1": [], "S2": [], "S3": []}

ae_100 = readFile(ae_100, "datos_eficiencias_100GeV.txt", 64, 0.3*1000, 20)
ae_500 = readFile(ae_500, "datos_eficiencias_500GeV.txt", 64, 0.5, 3)

# for i in ae_100: 
#     pdb.set_trace()

# pdb.set_trace()

vidas_medias = [0.1, 1, 10, 100, 1000, 10000]

# 100 GeV con AE1, AE2, AE3 (efficiencia vs lifetime)
# 100 GeV con EV1, EV2, EV (numero sucesos vs lifetime para un dado ctau) -> comparamos con mapa exclusion

# 500 GeV con AE1, AE2, AE3 (efficiencia vs lifetime)
# 500 GeV con EV1, EV2, EV (numero sucesos vs lifetime para un dado ctau) -> comparamos con mapa exclusion



# para hacer el plot, al parecer ROOT espera arreglos de tipo double, y conviene convertir las listas con array('d', lista)
def make_plot(ae, ctau):

    canvas = ROOT.TCanvas("canvas", "plot aceptancias")
    canvas.SetLogx()
    # canvas.SetLogy()

    graficoAE1 = ROOT.TGraph(len(ae["AE1"]), array('d', ctau), array('d', ae["AE1"]))
    graficoAE2 = ROOT.TGraph(len(ae["AE2"]), array('d', ctau), array('d', ae["AE2"]))
    graficoAE3 = ROOT.TGraph(len(ae["AE3"]), array('d', ctau), array('d', ae["AE3"]))

    graficoAE1.SetLineWidth(2)
    graficoAE2.SetLineWidth(2)
    graficoAE3.SetLineWidth(2)

    legend = ROOT.TLegend(0.25, 0.90, 0.75, 0.85)
    legend.AddEntry(graficoAE1, "Escenario 1")
    legend.AddEntry(graficoAE2, "Escenario 2")
    legend.AddEntry(graficoAE3, "Escenario 3")
    legend.SetNColumns(3)

    y_max = max(ROOT.TMath.MaxElement(graficoAE2.GetN(), graficoAE2.GetY()), ROOT.TMath.MaxElement(graficoAE1.GetN(), graficoAE1.GetY()), ROOT.TMath.MaxElement(graficoAE3.GetN(), graficoAE3.GetY()))
    
    graficoAE2.GetXaxis().SetTitle("c#tau [cm]")
    graficoAE2.GetYaxis().SetTitle("Aceptancia")
    graficoAE2.SetTitle("Curvas vida media - {nombre}".format(nombre = ae["labels"][0]))
    
    
    graficoAE2.Draw("AC")
    graficoAE3.Draw("C same")
    graficoAE1.Draw("C same")
    
    graficoAE2.SetMaximum(y_max * 1.5)
    legend.Draw()

    graficoAE1.SetLineColor(ROOT.kRed)
    graficoAE2.SetLineColor(ROOT.kBlue)
    graficoAE3.SetLineColor(ROOT.kGreen)

    canvas.SaveAs('/nfs/cms/rhebrero/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_Neventos/' + ae["labels"][0] + ae["labels"][3] + '.png')

    canvas.Close()



    canvas2 = ROOT.TCanvas("canvas2", "plot eventos")
    
    canvas2.SetLogx()
    # canvas2.SetLogy()

    graficoEV1 = ROOT.TGraph(len(ae["EV1"]), array('d', ctau), array('d', ae["EV1"]))
    graficoEV2 = ROOT.TGraph(len(ae["EV2"]), array('d', ctau), array('d', ae["EV2"]))
    graficoEV3 = ROOT.TGraph(len(ae["EV3"]), array('d', ctau), array('d', ae["EV3"]))

    graficoEV1.SetLineWidth(2)
    graficoEV2.SetLineWidth(2)
    graficoEV3.SetLineWidth(2)

    legend = ROOT.TLegend(0.25, 0.90, 0.75, 0.85)
    legend.AddEntry(graficoEV1, "Escenario 1")
    legend.AddEntry(graficoEV2, "Escenario 2")
    legend.AddEntry(graficoEV3, "Escenario 3")
    legend.SetNColumns(3)

    y_max = max(ROOT.TMath.MaxElement(graficoEV2.GetN(), graficoEV2.GetY()), ROOT.TMath.MaxElement(graficoEV1.GetN(), graficoEV1.GetY()), ROOT.TMath.MaxElement(graficoEV3.GetN(), graficoEV3.GetY()))

    graficoEV2.GetXaxis().SetTitle("c#tau [cm]")
    graficoEV2.GetYaxis().SetTitle("N de sucesos")
    graficoEV2.SetTitle("Curvas vida media - {nombre}".format(nombre = ae["labels"][1]))
    
    graficoEV2.Draw("AC")
    graficoEV3.Draw("C same")
    graficoEV1.Draw("C same")
    graficoEV2.SetMaximum(y_max * 1.5)
    legend.Draw()


    graficoEV1.SetLineColor(ROOT.kRed)
    graficoEV2.SetLineColor(ROOT.kBlue)
    graficoEV3.SetLineColor(ROOT.kGreen)

    canvas2.SaveAs('/nfs/cms/rhebrero/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_Neventos/' + ae["labels"][1] + ae["labels"][3] + '.png')

    canvas2.Close()


    canvas3 = ROOT.TCanvas("canvas", "plot significancias")
    canvas3.SetLogx()
    # canvas3.SetLogy()

    graficoS1 = ROOT.TGraph(len(ae["S1"]), array('d', ctau), array('d', ae["S1"]))
    graficoS2 = ROOT.TGraph(len(ae["S2"]), array('d', ctau), array('d', ae["S2"]))
    graficoS3 = ROOT.TGraph(len(ae["S3"]), array('d', ctau), array('d', ae["S3"]))
    Significancia_minima = ROOT.TF1("sucesos necesarios 100", "3", ctau[0], ctau[-1])#aqui habria que poner algun criterio para 

    y_max = max(ROOT.TMath.MaxElement(graficoS2.GetN(), graficoS2.GetY()), ROOT.TMath.MaxElement(graficoS1.GetN(), graficoS1.GetY()), ROOT.TMath.MaxElement(graficoS3.GetN(), graficoS3.GetY()))
    # y_max = 17/1.3

    graficoS2.GetXaxis().SetTitle("c#tau [cm]")
    graficoS2.GetYaxis().SetTitle("Significancia")
    graficoS2.SetTitle("Curvas vida media - {nombre}".format(nombre = ae["labels"][2]))

    legend = ROOT.TLegend(0.25, 0.90, 0.75, 0.85)
    legend.AddEntry(graficoS1, "Escenario 1")
    legend.AddEntry(graficoS2, "Escenario 2")
    legend.AddEntry(graficoS3, "Escenario 3")
    legend.SetNColumns(3)

    graficoS2.Draw("AC")
    graficoS3.Draw("C same")
    graficoS1.Draw("C same")
    Significancia_minima.Draw("same")
    graficoS2.SetMaximum(y_max * 1.3)
    graficoS2.SetMinimum(0)
    graficoS2.GetXaxis().SetRangeUser(0.1, 10000)
    
    legend.Draw()

    graficoS1.SetLineWidth(2)
    graficoS2.SetLineWidth(2)
    graficoS3.SetLineWidth(2)

    Significancia_minima.SetLineColor(ROOT.kBlack)
    graficoS1.SetLineColor(ROOT.kRed)
    graficoS2.SetLineColor(ROOT.kBlue)
    graficoS3.SetLineColor(ROOT.kGreen)

    canvas3.SaveAs('/nfs/cms/rhebrero/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_Neventos/' + ae["labels"][2] + ae["labels"][3] + '.png')

    canvas3.Close()
    

make_plot(ae_100, vidas_medias)
make_plot(ae_500, vidas_medias)


