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
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mass', dest = 'MASS', required = True, help = "La masa del muon a analizar, seleccional 100 ó 500" )

args = parser.parse_args()



samplesDir = '/pnfs/ciemat.es/data/cms/store/user/escalant/'
samples = Sample()



if float(args.MASS) == 100:

    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_100_ctau_1mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095140/0000/'  , 'M_{l}=100, c#tau=0.1 cm'  , '100_1', 1)
    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_100_ctau_10mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095118/0000/'  , 'M_{l}=100, c#tau=1 cm'  , '100_10', 2)
    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_100_ctau_100mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095057/0000/'  , 'M_{l}=100, c#tau=10 cm'  , '100_100', 3) 
    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_100_ctau_1000mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095034/0000/'  , 'M_{l}=100, c#tau=100 cm'  , '100_1000', 4) 
    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_100_ctau_10000mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095012/0000/'  , 'M_{l}=100, c#tau=1000 cm'  , '100_10000', 5) 
    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_100_ctau_100000mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_094950/0000/'  , 'M_{l}=100, c#tau=10000 cm'  , '100_10000', 6) 

elif float(args.MASS) == 500:

    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_1mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095357/0000/'  , 'M_{l}=500, c#tau=0.1 cm'  , '500_1', 1)
    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_10mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095334/0000/'  , 'M_{l}=500, c#tau=1 cm'  , '500_10', 2)
    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_100mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095312/0000/'  , 'M_{l}=500, c#tau=10 cm'  , '500_100', 3) 
    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_1000mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095248/0000/'  , 'M_{l}=500, c#tau=100 cm'  , '500_1000', 4) 
    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_10000mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095227/0000/'  , 'M_{l}=500, c#tau=1000 cm'  , '500_10000', 5) 
    samples.AddSample(samplesDir + 'SMuonToMuGravitino-M_500_ctau_100000mm_TuneCP5_13p6TeV_pythia8/AODSIM-November2023_v1/231122_095203/0000/'  , 'M_{l}=500, c#tau=10000 cm'  , '500_10000', 6) 
else:
    print("No hay datos para esa masa")
    quit()

sampleName = samples.GetSampleName()
legenName = samples.GetLegendName()
histName = samples.GetHistName()

handle = Handle("std::vector<reco::GenParticle>")
label = ("genParticles")

handleTriggerBits = Handle("edm::TriggerResults")                                                                                                                                                                                                                                                                                                                                                                          
labelTriggerBits = ("TriggerResults","","HLT") #set my label.

TriggerFlags = ["HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v2", "HLT_DoubleMu38NoFiltersNoVtx_v2", "HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v2", "DST_DoubleMu3_Mass10_PFScouting_v1", "HLT_L2DoubleMu23_NoVertex_v2"]


lxy_mayor = createSimple1DPlot("lxy_mayor", "lxy_mayor", 100, 400, 100000, samples) 
lxy_menor = createSimple1DPlot("lxy_menor", "lxy_menor", 100, 0, 400, samples) 
dxy = createSimple1DPlot("dxy", "dxy", 100, 0, 10, samples)
# lz = createSimple1DPlot("lz", "lz", 100, 0, 5, samples)

N_mayor = []
N_menor = []
N_dxy = []

# CrossSection = 0.3
# Luminosity = 64000
# eficiencia_menor = []
# eficiencia_mayor = []
vidas_medias = []
# eficiencia_dxy = []
eff_tS1 = []
eff_tS2 = []
eff_tS3 = []
N_tot =[]

# def CheckTrigger(triggerlist, triggerBits):
#     fired = False
#     HLTTriggerNames = event.object().triggerNames(triggerBits)

#     for ktriggerlist in triggerlist:
#         for i in range(triggerBits.size()):
#             if ktriggerlist == HLTTriggerNames.triggerName(i) and triggerBits.accept(i) == True:
#                 fired = True
#                 break
#             else:
#                 continue
#     return fired



# cambio la forma de checkear los trigger
def CheckTrigger(triggerIdlist, triggerBits):
    fired = False

    for ktriggerIdlist in triggerIdlist:
        if triggerBits.accept(ktriggerIdlist) == True:
            fired = True
            break
        else:
            continue
    return fired


def GetTriggerId(triggerlist, HLTTriggerNames):
    triggerIdlist = []

    for ktriggerlist in triggerlist:
        for i in range(HLTTriggerNames.size()):
            if ktriggerlist == HLTTriggerNames.triggerName(i):
                triggerIdlist.append(i)
    
    return triggerIdlist


Triggerlist_S2 = ["HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v2", "HLT_DoubleL2Mu23NoVtx_2Cha_v3", "HLT_DoubleL2Mu23NoVtx_2Cha_v2", "HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v1", "HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v1"]
Triggerlist_S1 = ["HLT_DoubleMu40NoFiltersNoVtxDisplaced_v1"]
Triggerlist_S3 = ["HLT_IsoMu24_v13"]


for index, ksamples in enumerate(sampleName): #recorre los batch del sampleName
    
    events = Events(ksamples) #asigna la clase Events a los .root para poder iterar sobre ellos
    
    N = 0
    N_trigger_S1 = 0
    N_trigger_S2 = 0
    N_trigger_S3 = 0

    for i, event in enumerate(events): #recorre los .root en cada bacth
        # pdb.set_trace()
        N += 1
        event.getByLabel(label, handle) #"abre" la coleccion correspondiente a la etiqueta del .root
        genParticles = handle.product() #el product() accede a los datos de la coleccion
        
        dxy_p = -1
        lxy_p = -1
        dxy_n = -1
        lxy_n = -1

        event.getByLabel(labelTriggerBits, handleTriggerBits)#cada evento hay que abrir el handle para luego sacar el triggerBits? porque? si no, se podria sacar el id de cada trigger antes del bucle y ya                                                                                                                                                                                                                                                                                                                                                            
        triggerBits = handleTriggerBits.product()  



        HLTTriggerNames = event.object().triggerNames(triggerBits)
        TriggerIdlist_S1 = GetTriggerId(Triggerlist_S1, HLTTriggerNames)
        TriggerIdlist_S2 = GetTriggerId(Triggerlist_S2, HLTTriggerNames)
        TriggerIdlist_S3 = GetTriggerId(Triggerlist_S3, HLTTriggerNames)

        #cambiarlo para que no se meta en el bucle a no ser que se haya activado algun trigger
        for p in genParticles:
            # quito los pdgId = +-15 y voy a quitar también el que vengan de staus
            if (p.pdgId() == 13) and (abs(p.mother().pdgId()) == 1000013 or abs(p.mother().pdgId()) == 2000013): 

                dxy_p = abs((p.py()*p.vertex().x()-p.px()*p.vertex().y())/p.pt())
                lxy_p = abs(p.vertex().rho())
            
            if (p.pdgId() == -13) and (abs(p.mother().pdgId()) == 1000013 or abs(p.mother().pdgId()) == 2000013): 

                dxy_n = abs((p.py()*p.vertex().x()-p.px()*p.vertex().y())/p.pt()) 
                lxy_n = abs(p.vertex().rho())
        
        # pdb.set_trace()

        if dxy_p * dxy_n < 0 or lxy_p * lxy_n <0:
            
            pdb.set_trace()



        if CheckTrigger(TriggerIdlist_S1, triggerBits): 
            N_trigger_S1 += 1
            
            if max(dxy_n, dxy_p) < 10 and min(dxy_n, dxy_p) > 0.1: #en el paper creo que lo hacian con dxy>0.01cm

                dxy[index].Fill(max(dxy_n, dxy_p))

        if CheckTrigger(TriggerIdlist_S2, triggerBits): 
            N_trigger_S2 += 1
            
            if max(lxy_p, lxy_n) < 400 and min(lxy_n, lxy_p) > 0.1 and min(dxy_n, dxy_p) > 0.1: #and min(lxy_n, lxy_p) > 0.1 se lo añado nuevo que lo acabo de ver en las diapositivas que me mando
                
                lxy_menor[index].Fill(max(lxy_p, lxy_n))
        
        if CheckTrigger(TriggerIdlist_S3, triggerBits): 
            N_trigger_S3 += 1

            if min(lxy_n, lxy_p) > 400:
                
                lxy_mayor[index].Fill(min(lxy_n, lxy_p)) 

        
    N_dxy.append(dxy[index].Integral())
    N_menor.append(lxy_menor[index].Integral())
    N_mayor.append(lxy_mayor[index].Integral())
    N_tot.append(N)


    
    vidas_medias.append(ksamples[0].split('_')[3])

    eff_tS1.append(N_trigger_S1/N)
    eff_tS2.append(N_trigger_S2/N)
    eff_tS3.append(N_trigger_S3/N) 

    print("Para M = 100Gev y c#tau = ", ksamples[0].split('_')[3], ":") #hace algo raro, ksamples no es una lista si solo analizo un root

    print("EFICIENCIA DEL TRIGGER S1", eff_tS1[index], ", aceptancia =", N_dxy[index]/N_tot[index])
    print("EFICIENCIA DEL TRIGGER S2", eff_tS2[index], ", aceptancia =", N_menor[index]/N_tot[index])
    print("EFICIENCIA DEL TRIGGER S3", eff_tS3[index], ", aceptancia =", N_mayor[index]/N_tot[index])
    


# pdb.set_trace()

# seria conveniente guardar los datos en un TTree si voy a hacer luego otras cosas con ellos?
with open('eficiencias_necesarias_{MASS}GeV_con_trigger.txt'.format(MASS = args.MASS), 'w') as text:

    text.write("{:<20} {:<30} {:<30} {:<30} {:<30} {:<25} {:<25} {:<25} {:<25} {:<25}\n".format("Vida media", "Aceptancia S1(N total)", "Acepatancia S2(N total)", "Aceptancia S3(N total)", "Eff trigger S1", "Eff trigger S2", "Eff trigger S3", "N tot S1", "N tot S2", "N tot S3" ))
    
    for i in range(len(vidas_medias)):

        text.write(f"{vidas_medias[i]:<20}\t{N_dxy[i]/N_tot[i]:<25}\t{N_menor[i]/N_tot[i]:<25}\t{N_mayor[i]/N_tot[i]:<25}\t{eff_tS1[i]:<25}\t{eff_tS2[i]:<25}\t{eff_tS3[i]:<25}\t{N_dxy[i]:<25}\t{N_menor[i]:<25}\t{N_mayor[i]:<25}\n")

with open('datos_eficiencias_{MASS}GeV.txt'.format(MASS = args.MASS), 'w') as text:

    for i in range(len(vidas_medias)):
        
        text.write(f"{vidas_medias[i].split('m')[0]},{N_dxy[i]/N_tot[i]},{N_menor[i]/N_tot[i]},{N_mayor[i]/N_tot[i]},{eff_tS1[i]},{eff_tS2[i]},{eff_tS3[i]},{N_dxy[i]},{N_menor[i]},{N_mayor[i]}\n")



# plotsFolder = '/nfs/cms/rhebrero/plots_prueba/trigger_{MASS}Gev/'.format(MASS = args.MASS)

# makeSimple1DPlot(lxy_menor, 'lxy_menor', samples, '', 'L_{xy}[cm]', 'n eventos', 'lxy_menor', plotsFolder, logy = True, norm = False)
# makeSimple1DPlot(dxy, 'dxy', samples, '', 'd_{xy}[cm]', 'n eventos', 'dxy', plotsFolder, logy = True, norm = False)
# makeSimple1DPlot(lxy_mayor, 'lxy_mayor', samples, '', 'L_{xy}[cm]', 'n eventos', 'lxy_mayor', plotsFolder, logy = True, norm = False)

