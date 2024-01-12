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

handleTriggerBits = Handle("edm::TriggerResults")                                                                                                                                                                                                                                                                                                                                                                          
labelTriggerBits = ("TriggerResults","","HLT") #set my label.
labelTriggerBits = ("TriggerResults", "", "HLT") 
TriggerFlags = ["HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v2", "HLT_DoubleMu38NoFiltersNoVtx_v2", "HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v2", "DST_DoubleMu3_Mass10_PFScouting_v1", "HLT_L2DoubleMu23_NoVertex_v2"]


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
eff_tS1 = []
eff_tS2 = []
eff_tS3 = []

def CheckTrigger(triggerlist, triggerBits):
    fired = False
    HLTTriggerNames = event.object().triggerNames(triggerBits)

    for ktriggerlist in triggerlist:
        for i in range(triggerBits.size()):
            if ktriggerlist == HLTTriggerNames.triggerName(i) and triggerBits.accept(i) == True:
                fired = True
                break
            else:
                continue
    return fired

Triggerlist_S2 = ["HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v2", "HLT_DoubleL2Mu23NoVtx_2Cha_v3", "HLT_DoubleL2Mu23NoVtx_2Cha_v2", "HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v1", "HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v1"]
Triggerlist_S1 = ["HLT_DoubleMu40NoFiltersNoVtxDisplaced_v1"]
Triggerlist_S3 = ["HLT_IsoMu24_v13"]

# Triggerlist_S3 = ["HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v2"]



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

        event.getByLabel(labelTriggerBits, handleTriggerBits)                                                                                                                                                                                                                                                                                                                                                           
        triggerBits = handleTriggerBits.product()  



        HLTTriggerNames = event.object().triggerNames(triggerBits)
        
        # if N < 10:
        #     print(" \n")
        #     print("[printAlltriggers] Existing triggers in sample:")
        #     for i in range(triggerBits.size()):
        #         acceptedTrigger = HLTTriggerNames.triggerName(i) 
        #         # if "HLT_" not in acceptedTrigger: continue # name does not follow usual HLT naming conventions (e.g this exlcudes AlCa, MC, Dataset etc.)
        #         if triggerBits.accept(i) == False:
        #             print(HLTTriggerNames.triggerName(i), i)
        #         if triggerBits.accept(i) == True:
        #             print(HLTTriggerNames.triggerName(i), i,  " -> PASS!! ")
        #     print("[printAlltriggers] END \n")
        # else:
        #     pdb.set_trace()

        for p in genParticles:

            if (p.pdgId() == 13 or p.pdgId() == 15) and (abs(p.mother().pdgId()) == 1000013 or abs(p.mother().pdgId()) == 2000013 or abs(p.mother().pdgId()) == 1000015 or abs(p.mother().pdgId()) == 2000015): #solo tengo en cuenta mu y tau

                dxy_p = abs((p.py()*p.vertex().x()-p.px()*p.vertex().y())/p.pt())
                lxy_p = abs(p.vertex().rho())
            
            if (p.pdgId() == -13 or p.pdgId() == -15) and (abs(p.mother().pdgId()) == 1000013 or abs(p.mother().pdgId()) == 2000013 or abs(p.mother().pdgId()) == 1000015 or abs(p.mother().pdgId()) == 2000015): #solo tengo en cuenta mu y tau

                dxy_n = abs((p.py()*p.vertex().x()-p.px()*p.vertex().y())/p.pt()) 
                lxy_n = abs(p.vertex().rho())
        
        # pdb.set_trace()

        if dxy_p * dxy_n < 0 or lxy_p * lxy_n <0:
            
            pdb.set_trace()



        if CheckTrigger(Triggerlist_S1, triggerBits): 
            N_trigger_S1 += 1
            
            if dxy_p < 10 and dxy_n < 10 and dxy_n > 0.1 and dxy_p > 0.1:

                dxy[index].Fill(max(dxy_n, dxy_p))

        if CheckTrigger(Triggerlist_S2, triggerBits): 
            N_trigger_S2 += 1
            
            if lxy_p < 400 and lxy_n < 400 and dxy_n > 0.1 and dxy_p > 0.1:
                
                lxy_menor[index].Fill(max(dxy_p, dxy_n))
        
        if CheckTrigger(Triggerlist_S3, triggerBits): 
            N_trigger_S3 += 1

            if lxy_p > 400 and lxy_n > 400:
                
                lxy_mayor[index].Fill(min(lxy_n, lxy_p)) 


        # if dxy_p < 10 and dxy_n < 10 and dxy_n > 0.1 and dxy_p > 0.1 and triggerBits.accept(394) == True:

        #     dxy[index].Fill(max(dxy_n, dxy_p))
                                      
        # if lxy_p < 400 and lxy_n < 400 and dxy_n > 0.1 and dxy_p > 0.1 and triggerBits.accept(105) == True:
            
        #     lxy_menor[index].Fill(max(dxy_p, dxy_n))

        # if lxy_p > 400 and lxy_n > 400 and triggerBits.accept(83) == True:
            
        #     lxy_mayor[index].Fill(min(lxy_n, lxy_p)) 

        
    N_dxy.append(dxy[index].Integral())
    N_menor.append(lxy_menor[index].Integral())
    N_mayor.append(lxy_mayor[index].Integral())
    

    if N_dxy[index] == 0.0:
        
        eficiencia_dxy.append("infinita")
        
    else:
        eficiencia_dxy.append(50*N/N_dxy[index]/Luminosity/CrossSection)

    if N_mayor[index] == 0.0:
        
        eficiencia_mayor.append("infinita")
        
    else:
        eficiencia_mayor.append(10*N/N_mayor[index]/Luminosity/CrossSection)
    
    if N_menor[index] == 0.0:
        eficiencia_menor.append("infinita")
    else:
        eficiencia_menor.append(10*N/N_menor[index]/Luminosity/CrossSection)
    
    vidas_medias.append(ksamples[0].split('_')[3])

    eff_tS1.append(N_trigger_S1/N)
    eff_tS2.append(N_trigger_S2/N)
    eff_tS3.append(N_trigger_S3/N) 

    print("Para M = 500Gev y c#tau = ", ksamples[0].split('_')[3], ":") #hace algo raro, ksamples no es una lista si solo analizo un root

    print("EFICIENCIA DEL TRIGGER S1", eff_tS1[index], ", aceptancia =")
    print("EFICIENCIA DEL TRIGGER S2", eff_tS2[index], ", aceptancia =")
    print("EFICIENCIA DEL TRIGGER S3", eff_tS3[index], ", aceptancia =")
    


# pdb.set_trace()

with open('eficiencias_necesarias_500GeV_con_trigger.txt', 'w') as text:

    text.write("{:<20} {:<25} {:<25} {:<25} {:<30} {:<25} {:<25}\n".format("Vida media", "Aceptancia S1", "Acepatancia S2", "Aceptancia S3", "Eff trigger S1", "Eff trigger S2", "Eff trigger S3" ))
    
    for i in range(len(vidas_medias)):

        text.write(f"{vidas_medias[i]:<20}\t{N_dxy[i]/N:<25}\t{N_menor[i]/N:<25}\t{N_mayor[i]/N:<25}\t{eff_tS1[i]:<25}\t{eff_tS2[i]:<25}\t{eff_tS3[i]:<25}\n")



plotsFolder = '/nfs/cms/rhebrero/plots_prueba/trigger_500Gev/'

makeSimple1DPlot(lxy_menor, 'lxy_menor', samples, '', 'L_{xy}[cm]', 'n eventos', 'lxy_menor', plotsFolder, logy = True, norm = False)
makeSimple1DPlot(dxy, 'dxy', samples, '', 'd_{xy}[cm]', 'n eventos', 'dxy', plotsFolder, logy = True, norm = False)
makeSimple1DPlot(lxy_mayor, 'lxy_mayor', samples, '', 'L_{xy}[cm]', 'n eventos', 'lxy_mayor', plotsFolder, logy = True, norm = False)

