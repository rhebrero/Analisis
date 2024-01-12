# import ROOT in batch mode
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT

ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events
from math import *

#Utils for Longlived Generator Level studies.
from utils import getLibraries
from GenLongLivedUtils import *
from SimpleTools import *

import pdb

#Samples to process
samplesDir = '/pnfs/ciemat.es/data/cms/store/user/escalant/'

samples = Sample()

# samples.AddSample(samplesDir+'SMuonToMuGravitino-M_200_ctau_6000mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_200_ctau_6000mm_TuneCP5_13p6TeV_pythia8_GS-October2023_ToDelete/231027_172449/0000/SMuonToMuGravitino-M_200_ctau_6000mm_TuneCP5_13p6TeV_pythia8_GS_11.root'  , 'M_{l}=200, c#tau=600 cm'  , '200_6000', 2)
#samples.AddSample(samplesDir+'TSG-Run3Summer21DRPremix-HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-1300mm_TuneCP5_13TeV_pythia8.root' , 'M_{H}=125, M_{X}=20, c#tau=130cm'  , '125_20_CTau_1300cm', 3)
#samples.AddSample(samplesDir+'TSG-Run3Summer21DRPremix-HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-13000mm_TuneCP5_13TeV_pythia8.root', 'M_{H}=125, M_{X}=20, c#tau=13000cm', '125_20_CTau_13000cm', 1) # last integer is the color
# samples.AddSample(samplesDir+'SMuonToMuGravitino-M_400_ctau_2000mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_400_ctau_2000mm_TuneCP5_13p6TeV_pythia8_GS-October2023_ToDelete/231027_172511/0000/'  , 'M_{l}=400, c#tau=200 cm'  , '400_2000', 4)
# samples.AddSample(samplesDir+'SMuonToMuGravitino-M_200_ctau_6000mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_200_ctau_6000mm_TuneCP5_13p6TeV_pythia8_GS-October2023_ToDelete/231027_172449/0000/'  , 'M_{l}=200, c#tau=600 cm'  , '200_6000', 2)

samples.AddSample(samplesDir+'SMuonToMuGravitino-M_100_ctau_10mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_100_ctau_10mm_TuneCP5_13p6TeV_pythia8_GS-November2023_ctau/231110_181915/0000/'  , 'M_{l}=100, c#tau=1 cm'  , '100_10', 2)
samples.AddSample(samplesDir+'SMuonToMuGravitino-M_100_ctau_1000mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_100_ctau_1000mm_TuneCP5_13p6TeV_pythia8_GS-November2023_ctau/231110_181846/0000/'  , 'M_{l}=100, c#tau=100 cm'  , '100_1000', 4)

sampleName = samples.GetSampleName()
legendName = samples.GetLegendName()
histName = samples.GetHistName()

# FOR GEN-SIM
handlePruned  = Handle ("std::vector<reco::GenParticle>")
labelPruned = ("genParticles")

#handleTriggerBits = Handle("edm::TriggerResults")                                                                                                                                                                                                                                                                                                                                                                          
#labelTriggerBits = ("TriggerResults","","HLT") set my label.
#labelTriggerBits = ("TriggerResults","","HLT") 
#TriggerFlags = ["HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v2", "HLT_DoubleMu38NoFiltersNoVtx_v2", "HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v2", "DST_DoubleMu3_Mass10_PFScouting_v1", "HLT_L2DoubleMu23_NoVertex_v2"]

#Histograms
massHiggs = createSimple1DPlot("massHiggs", "M_{H}", 100, 100, 600, samples)
massX = createSimple1DPlot("massX", "M_{X}", 400, 1, 900, samples)
lxy = createSimple1DPlot("lxy", "lxy", 100, 1, 100, samples)
lzVslxy = createSimple2DPlot("lzVslxy", "lz vs lxy", 350, 0, 1000, 200, 0, 700, samples)


# ksamples es una matrix n_lotesXn_archivos_en_lote, el primer for divide los lotes y el segundo analiza los archivos de cada lote

for index, ksamples in enumerate(sampleName):
    #print ("SAMPLE: "+str(ksamples)+"\n")
    #pdb.set_trace()
    # print ("SAMPLE: "+sampleName[index][0]+"\n")
    events = Events(ksamples)    
    for i,event in enumerate(events):   
        event.getByLabel (labelPruned, handlePruned)
        genParticles = handlePruned.product()

        #event.getByLabel(labelTriggerBits, handleTriggerBits)                                                                                                                                                                                                                                                                                                                                                           
        #triggerBits = handleTriggerBits.product()  

        #print("Event: "+str(i)+"\n")
        #print("--------------------")

        # pdb.set_trace()
        for p in genParticles:
            # tellMeMore(p)
            if abs(p.pdgId()) == 1000013 or abs(p.pdgId()) == 2000013 or abs(p.pdgId()) == 1000015 or abs(p.pdgId()) == 2000015:
                # no esta considerando los electrones supersimetricos
                # tellMeMore(p)
                massX[index].Fill(p.mass())

            if abs(p.pdgId()) == 1000039:

                lxy[index].Fill(abs(p.vertex().rho()))
                lzVslxy[index].Fill(abs(p.vertex().Z()), abs(p.vertex().rho()))

            #    tellMeMore(p)
            # if fabs(p.pdgId() == 35): #Plotting something from the Higgs
            #     massHiggs[index].Fill(p.mass())
            #    if fabs(p.pdgId() == 6000113 ): #Plotting something from the X
            #        massX[index].Fill(p.mass())
            #    if fabs(p.pdgId() == 13 ): #Plotting something from the displaced muons
            #        lxy[index].Fill(abs(p.vertex().rho()))
            #        lzVslxy[index].Fill(abs(p.vertex().Z()), abs(p.vertex().rho()))

        # Which fraction of events in the denominator that fullfill the triger                                                                                                                                                                                                                                                                                                                                       
        # HLTTriggerNames = event.object().triggerNames(triggerBits)
        # for TriggerIndex, kTrigger in enumerate(TriggerFlags):
        #    for i in range(triggerBits.size()):
        #        if triggerBits.accept(i):        
        #            print (HLTTriggerNames.triggerName(i))

plotsFolder = '/nfs/cms/rhebrero/tfm_rh/plots/sandbox/'
#makeSimple1DPlot(var, canvas, samples, title, xtitle, ytitle, output, folder, logy=False, showOnly = []):

makeSimple1DPlot(massHiggs, 'massHiggs', samples, '', 'M_{Higgs}', 'norm.a.u', 'massHiggs', plotsFolder, logy=True, norm = False)
makeSimple1DPlot(massX, 'massX', samples, '', 'M_{X}', 'norm.a.u', 'massX', plotsFolder, logy=True, norm = False)
# makeSimple1DPlot(lxy, 'lxy', samples, '', 'L_{xy}[cm]', 'norm.a.u', 'lxy', plotsFolder, logy=True)
makeSimple1DPlot(lxy, 'lxy', samples, '', 'L_{xy}[cm]', 'norm.a.u', 'lxy', plotsFolder, logy=True, norm = False)
makeSimple2DPlot(lzVslxy, 'lzVslxy', samples, 'Generated L_{z}[cm] vs L_{xy}[cm]', 'L_{z}[cm]', 'L_{xy}[cm]', 'GenLzVsLxy', plotsFolder)
