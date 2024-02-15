import sys 
oldargv = sys.argv[:]
sys.arg = [ '-b-' ]
import ROOT 

ROOT.gROOT.SetBatch(True)
sys.argv = oldargv
import time

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
parser.add_argument('--mass', dest = 'MASS', required = True, help = "La masa del muon a analizar: 100 ó 500" )

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


histogram_S3 = createSimple1DPlot("histogram_S3", "histogram_S3", 100, 400, 100000, samples) 
histogram_S2 = createSimple1DPlot("histogram_S2", "histogram_S2", 100, 0, 400, samples) 
histogram_S1 = createSimple1DPlot("histogram_S1", "histogram_S1", 100, 0, 10, samples)
histogram_S2_tracker = createSimple1DPlot("histogram_S2_tracker", "histogram_S2_tracker", 100, 0, 400, samples)

# lz = createSimple1DPlot("lz", "lz", 100, 0, 5, samples)

N_S3 = []
N_S2 = []
N_S1 = []
N_S2_tracker = []


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
                break 
    
    return triggerIdlist


Triggerlist_S2 = ["HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v2", "HLT_DoubleL2Mu23NoVtx_2Cha_v3", "HLT_DoubleL2Mu23NoVtx_2Cha_v2", "HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v1", "HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v1"]
Triggerlist_S1 = ["HLT_DoubleMu40NoFiltersNoVtxDisplaced_v1"]
# Triggerlist_S3 = ["HLT_IsoMu24_v13"]
Triggerlist_S3 = ["HLT_Mu50_v15"]

start_time = time.time()

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
                smuon_pt_p = abs(p.mother().pt())
                smuon_R_p = abs(p.mother().vertex().r())
                smuon_eta_p = abs(p.mother().eta())#se debe coger este eta o el del vertex?
                # diferencia entre la eta del vertex y no vertex? porque r solo esta en el vertex?
            
            if (p.pdgId() == -13) and (abs(p.mother().pdgId()) == 1000013 or abs(p.mother().pdgId()) == 2000013): 

                dxy_n = abs((p.py()*p.vertex().x()-p.px()*p.vertex().y())/p.pt()) 
                lxy_n = abs(p.vertex().rho())
                smuon_pt_n = abs(p.mother().pt())
                smuon_R_n = abs(p.mother().vertex().r())
                smuon_eta_n = abs(p.mother().eta())        
        # pdb.set_trace()

        if dxy_p * dxy_n < 0 or lxy_p * lxy_n <0:
            
            pdb.set_trace()

        # para despues imponer que uno de ellos al menos cumpla las caracteristicas 
        smuon_eta = min(smuon_eta_p, smuon_eta_n)
        smuon_pt = max(smuon_pt_n, smuon_pt_p)
        smuon_R = min(smuon_R_n, smuon_R_p)

        if CheckTrigger(TriggerIdlist_S1, triggerBits): 
            N_trigger_S1 += 1
            
            if max(dxy_n, dxy_p) < 10 and min(dxy_n, dxy_p) > 0.1: #en el paper creo que lo hacian con dxy>0.01cm

                histogram_S1[index].Fill(max(dxy_n, dxy_p))

        if CheckTrigger(TriggerIdlist_S2, triggerBits): 
            N_trigger_S2 += 1
            tracker = False

            # aqui pido tambien que Lxy sea mayor que 0.1, que no se si debo
            if (max(lxy_p, lxy_n) < 100 and min(lxy_n, lxy_p) > 0.1 and min(dxy_n, dxy_p) > 0.1):
                histogram_S2_tracker[index].Fill(max(lxy_n, lxy_p)) 
                tracker = True
            
            if (100 < max(lxy_p, lxy_n) < 400 and min(lxy_n, lxy_p) > 0.1 and min(dxy_n, dxy_p) > 10) or tracker: #and min(lxy_n, lxy_p) > 0.1 se lo añado nuevo que lo acabo de ver en las diapositivas que me mando
                histogram_S2[index].Fill(max(lxy_p, lxy_n))
        
        if CheckTrigger(TriggerIdlist_S3, triggerBits): 
            N_trigger_S3 += 1
            # no habria que hacer que la condicion en el parametro de impacto se imponga al muon cuyo smuon madre cumple tambien las demas imposiciones?
            if ((smuon_eta_n < 1.0 and smuon_pt_n > 200) and (min(lxy_n, lxy_p) > 400 or (min(lxy_n, lxy_p) > 100 and smuon_R_n < 0.3))) or (smuon_eta_p < 1.0 and smuon_pt_p > 200) and (min(lxy_n, lxy_p) > 400 or (min(lxy_n, lxy_p) > 100 and smuon_R_p < 0.3)):
                
                histogram_S3[index].Fill(min(lxy_n, lxy_p)) 

        
    N_S1.append(histogram_S1[index].Integral())
    N_S2.append(histogram_S2[index].Integral())
    N_S3.append(histogram_S3[index].Integral())
    N_tot.append(N)

    N_S2_tracker.append(histogram_S2_tracker[index].Integral())


    
    vidas_medias.append(ksamples[0].split('_')[3])

    eff_tS1.append(N_trigger_S1/N)
    eff_tS2.append(N_trigger_S2/N)
    eff_tS3.append(N_trigger_S3/N) 

    print("Para M = 100Gev y c#tau = ", ksamples[0].split('_')[3], ":") #hace algo raro, ksamples no es una lista si solo analizo un root

    print("EFICIENCIA DEL TRIGGER S1", eff_tS1[index], ", eficiencia =", N_S1[index]/N_tot[index])
    print("EFICIENCIA DEL TRIGGER S2", eff_tS2[index], ", eficiencia =", N_S2[index]/N_tot[index], "eff tracker only =", N_S2_tracker[index]/N_tot[index])
    print("EFICIENCIA DEL TRIGGER S3", eff_tS3[index], ", eficiencia =", N_S3[index]/N_tot[index])
    
end_time = time.time()
total_time = end_time - start_time

# pdb.set_trace()

# seria conveniente guardar los datos en un TTree si voy a hacer luego otras cosas con ellos?
with open('eficiencias_necesarias_{MASS}GeV_con_trigger_2.txt'.format(MASS = args.MASS), 'w') as text:

    text.write("{:<20} {:<30} {:<30} {:<30} {:<30} {:<25} {:<25} {:<25} \n".format("Vida media", "Eficiencia S1", "Eficiencia S2", "Eficiencia S3", "Eff trigger S1", "Eff trigger S2", "Eff trigger S3", "Eficiencia S2 tracker"))
    
    for i in range(len(vidas_medias)):

        text.write(f"{vidas_medias[i]:<20}\t{N_S1[i]/N_tot[i]:<25}\t{N_S2[i]/N_tot[i]:<25}\t{N_S3[i]/N_tot[i]:<25}\t{eff_tS1[i]:<25}\t{eff_tS2[i]:<25}\t{eff_tS3[i]:<25}\t{N_S2_tracker[i]/N_tot[i]:<25}\n")

with open('datos_eficiencias_{MASS}GeV_2.txt'.format(MASS = args.MASS), 'w') as text:

    for i in range(len(vidas_medias)):
        
        text.write(f"{vidas_medias[i].split('m')[0]},{N_S1[i]/N_tot[i]},{N_S2[i]/N_tot[i]},{N_S3[i]/N_tot[i]},{eff_tS1[i]},{eff_tS2[i]},{eff_tS3[i]},{N_S2_tracker[i]/N_tot[i]}\n")


print(total_time)

# plotsFolder = '/nfs/cms/rhebrero/plots_prueba/trigger_{MASS}Gev/'.format(MASS = args.MASS)

# makeSimple1DPlot(histogram_S2, 'histogram_S2', samples, '', 'L_{xy}[cm]', 'n eventos', 'histogram_S2', plotsFolder, logy = True, norm = False)
# makeSimple1DPlot(dxy, 'dxy', samples, '', 'd_{xy}[cm]', 'n eventos', 'dxy', plotsFolder, logy = True, norm = False)
# makeSimple1DPlot(histogram_S3, 'histogram_S3', samples, '', 'L_{xy}[cm]', 'n eventos', 'histogram_S3', plotsFolder, logy = True, norm = False)

