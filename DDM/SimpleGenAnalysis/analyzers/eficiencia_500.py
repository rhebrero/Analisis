import sys 
oldargv = sys.argv[:]
sys.arg = [ '-b-' ]
import ROOT 

ROOT.gROOT.SetBatch(True)
sys.argv = oldargv


ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable() #habilita el entorno FWLite

from DataFormats.FWLite import Handle, Events
from math import *

from utils import getLibraries
from GenLongLivedUtils import *
from SimpleTools import *

import pdb


samplesDir = '/pnfs/ciemat.es/data/cms/store/user/escalant/'
samples = Sample()

# samples.AddSample(samplesDir+'SMuonToMuGravitino-M_500_ctau_1mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_500_ctau_1mm_TuneCP5_13p6TeV_pythia8_GS-November2023_ctau/231110_181803/0000/'  , 'M_{l}=500, c#tau=0.1 cm'  , '500_1', 1)
# samples.AddSample(samplesDir+'SMuonToMuGravitino-M_500_ctau_10mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_500_ctau_10mm_TuneCP5_13p6TeV_pythia8_GS-November2023_ctau/231110_181749/0000/'  , 'M_{l}=500, c#tau=1 cm'  , '500_10', 2)
# samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_100mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_500_ctau_100mm_TuneCP5_13p6TeV_pythia8_GS-November2023_ctau/231110_181734/0000/'  , 'M_{l}=500, c#tau=10 cm'  , '500_100', 3) 
# samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_1000mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_500_ctau_1000mm_TuneCP5_13p6TeV_pythia8_GS-November2023_ctau/231110_181720/0000/'  , 'M_{l}=500, c#tau=100 cm'  , '500_1000', 4) 
# samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_10000mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_500_ctau_10000mm_TuneCP5_13p6TeV_pythia8_GS-November2023_ctau/231110_181705/0000/'  , 'M_{l}=500, c#tau=1000 cm'  , '500_10000', 5) 
# samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_100000mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_500_ctau_100000mm_TuneCP5_13p6TeV_pythia8_GS-November2023_ctau/231110_181651/0000/'  , 'M_{l}=500, c#tau=10000 cm'  , '500_10000', 6) 

samples.AddSample(samplesDir+'SMuonToMuGravitino-M_500_ctau_1mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095357/0000/'  , 'M_{l}=500, c#tau=0.1 cm'  , '500_1', 1)
samples.AddSample(samplesDir+'SMuonToMuGravitino-M_500_ctau_10mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095334/0000/'  , 'M_{l}=500, c#tau=1 cm'  , '500_10', 2)
samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_100mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095312/0000/'  , 'M_{l}=500, c#tau=10 cm'  , '500_100', 3) 
samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_1000mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095248/0000/'  , 'M_{l}=500, c#tau=100 cm'  , '500_1000', 4) 
samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_10000mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095227/0000/'  , 'M_{l}=500, c#tau=1000 cm'  , '500_10000', 5) 
samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_100000mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095203/0000/'  , 'M_{l}=500, c#tau=10000 cm'  , '500_10000', 6) 


sampleName = samples.GetSampleName()
legenName = samples.GetLegendName()
histName = samples.GetHistName()

handle = Handle("std::vector<reco::GenParticle>")
label = ("genParticles")


lxy_mayor = createSimple1DPlot("lxy_mayor", "lxy_mayor", 100, 60, 1000, samples) 
lxy_menor = createSimple1DPlot("lxy_menor", "lxy_menor", 100, 0, 50, samples) 
dxy = createSimple1DPlot("dxy", "dxy", 100, 0, 11, samples)
lz = createSimple1DPlot("lz", "lz", 100, 0, 5, samples)

N_mayor = []
N_menor = []
N_dxy = []

CrossSection = 0.5
Luminosity = 64000
eficiencia_menor = []
eficiencia_mayor = []
vidas_medias = []
eficiencia_dxy = []


for index, ksamples in enumerate(sampleName): #recorre los batch del sampleName
    
    events = Events(ksamples) #asigna la clase Events a los .root para poder iterar sobre ellos
    
    N = 0

    for i, event in enumerate(events): #recorre los .root en cada bacth
        
        N += 1
        event.getByLabel(label, handle) #"abre" la coleccion correspondiente a la etiqueta del .root
        genParticles = handle.product() #el product() accede a los datos de la coleccion
        
        dxy_p = -1
        lxy_p = -1
        dxy_n = -1
        lxy_n = -1


        for p in genParticles:

            if (p.pdgId() == 13 or p.pdgId() == 15) and (abs(p.mother().pdgId()) == 1000013 or abs(p.mother().pdgId()) == 2000013 or abs(p.mother().pdgId()) == 1000015 or abs(p.mother().pdgId()) == 2000015): #solo tengo en cuenta mu y tau

                dxy_p = abs((p.py()*p.vertex().x()-p.px()*p.vertex().y())/p.pt())
                lxy_p = abs(p.vertex().rho())
            
            if (p.pdgId() == -13 or p.pdgId() == -15) and (abs(p.mother().pdgId()) == 1000013 or abs(p.mother().pdgId()) == 2000013 or abs(p.mother().pdgId()) == 1000015 or abs(p.mother().pdgId()) == 2000015): #solo tengo en cuenta mu y tau

                dxy_n = abs((p.py()*p.vertex().x()-p.px()*p.vertex().y())/p.pt()) 
                lxy_n = abs(p.vertex().rho())
        
        # pdb.set_trace()

        if dxy_p*dxy_n < 0 or lxy_p*lxy_n < 0:
            
            pdb.set_trace()
             

        if dxy_p < 10 and dxy_n < 10 and dxy_n > 0.1 and dxy_p > 0.1:

            dxy[index].Fill(max(dxy_n, dxy_p))
                                      
        if lxy_p < 400 and lxy_n < 400 and dxy_n > 0.1 and dxy_p > 0.1:
            
            lxy_menor[index].Fill(max(dxy_p, dxy_n))

        if lxy_p > 700 and lxy_n > 700:
            
            lxy_mayor[index].Fill(min(lxy_n, lxy_p)) 
        
    N_dxy.append(dxy[index].Integral())
    N_menor.append(lxy_menor[index].Integral())
    N_mayor.append(lxy_mayor[index].Integral())
    

    if N_dxy[index] == 0.0:
        eficiencia_dxy.append("infinita")
        
    else:
        eficiencia_dxy.append(10*N/N_dxy[index]/Luminosity/CrossSection)

    if N_mayor[index] == 0.0:
        eficiencia_mayor.append("infinita")
        
    else:
        eficiencia_mayor.append(10*N/N_mayor[index]/Luminosity/CrossSection)
    
    if N_menor[index] == 0.0:
        eficiencia_menor.append("infinita")
    
    else:
        eficiencia_menor.append(10*N/N_menor[index]/Luminosity/CrossSection)
    
    vidas_medias.append(ksamples[0].split('_')[3])

    # print("Para M = 500Gev y c#tau = ", ksamples[0].split('_')[3], ":") #hace algo raro, ksamples no es una lista si solo analizo un root

    # print("En el rango Lxy < 4m se dan", N_menor[index], "eventos y la eficiencia es ", eficiencia_menor[index], ", aceptancia =", N_menor[index]/N)
    # print("En el rango Lxy > 7m se dan", N_mayor[index], "eventos y la eficiencia es ", eficiencia_mayor[index], ", aceptancia =", N_mayor[index]/N)
    # print("En el rango dxy < 10cm se dan", N_dxy[index], "eventos y la eficiencia es ", eficiencia_dxy[index], ", aceptancia =", N_dxy[index]/N)




with open('eficiencias_necesarias_500.txt', 'w') as text:

    text.write("{:<20} {:<25} {:<25} {:<25} {:<25} {:<25} {:<25}\n".format("Vida media", "eficiencia S1", "eficiencia S2", "eficiencia S3", "Aceptancia S1", "Acepatancia S2", "Aceptancia S3"))
    
    for i in range(len(vidas_medias)):

        text.write(f"{vidas_medias[i]:<20}\t{eficiencia_menor[i]:<20}\t{eficiencia_mayor[i]:<20}\t{eficiencia_dxy[i]:<20}\t{N_dxy[i]/N:<25}\t{N_menor[i]/N:<25}\t{N_mayor[i]/N:<25}\n")



plotsFolder = '/nfs/cms/rhebrero/plots_prueba/500GeV/'

makeSimple1DPlot(lxy_menor, 'lxy_menor', samples, '', 'L_{xy}[cm]', 'n eventos', 'lxy_menor', plotsFolder, logy = True, norm = False)
makeSimple1DPlot(dxy, 'dxy', samples, '', 'd_{xy}[cm]', 'n eventos', 'dxy', plotsFolder, logy = True, norm = False)
makeSimple1DPlot(lxy_mayor, 'lxy_mayor', samples, '', 'L_{xy}[cm]', 'n eventos', 'lxy_mayor', plotsFolder, logy = True, norm = False)

