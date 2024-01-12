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


#Samples to process
samplesDir = '/pnfs/ciemat.es/data/cms/store/user/escalant/'

samples = Sample()

samples.AddSample(samplesDir+'HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8/crab_HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8_GS-October2023_ToDelete/231017_102029/0000/HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8_GS_1.root'  , 'M_{H}=125, M_{X}=20, c#tau=13cm'  , '125_20_CTau_13cm', 2)
samples.AddSample(samplesDir+'HTo2LongLivedTo2mu2jets_MH-125_MFF-50_CTau-500mm_TuneCP5_13p6TeV_pythia8/crab_HTo2LongLivedTo2mu2jets_MH-125_MFF-50_CTau-500mm_TuneCP5_13p6TeV_pythia8_GS-October2023_ToDelete/231017_102039/0000/HTo2LongLivedTo2mu2jets_MH-125_MFF-50_CTau-500mm_TuneCP5_13p6TeV_pythia8_GS_1.root' , 'M_{H}=125, M_{X}=50, c#tau=50cm'  , '125_50_CTau_50cm', 3)
# samples.AddSample(samplesDir+'TSG-Run3Summer21DRPremix-HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-13000mm_TuneCP5_13TeV_pythia8.root', 'M_{H}=125, M_{X}=20, c#tau=13000cm', '125_20_CTau_13000cm', 1) # last integer is the color

sampleName = samples.GetSampleName()
legendName = samples.GetLegendName()
histName = samples.GetHistName()

# FOR GEN-SIM
handlePruned  = Handle ("std::vector<reco::GenParticle>")
labelPruned = ("genParticles")

handleTriggerBits = Handle("edm::TriggerResults")                                                                                                                                                                                                                                                                                                                                                                          
#labelTriggerBits = ("TriggerResults","","HLT") set my label.
labelTriggerBits = ("TriggerResults", "", "HLT") 
TriggerFlags = ["HLT_TrkMu15_DoubleTrkMu5NoFiltersNoVtx_v2", "HLT_DoubleMu38NoFiltersNoVtx_v2", "HLT_L2DoubleMu28_NoVertex_2Cha_Angle2p5_Mass10_v2", "DST_DoubleMu3_Mass10_PFScouting_v1", "HLT_L2DoubleMu23_NoVertex_v2"]

#Histograms
massHiggs = createSimple1DPlot("massHiggs", "M_{H}", 100, 100, 600, samples)
massX = createSimple1DPlot("massX", "M_{X}", 300, 1, 180, samples)
lxy = createSimple1DPlot("lxy", "lxy", 100, 1, 100, samples)
lzVslxy = createSimple2DPlot("lzVslxy", "lz vs lxy", 350, 0, 1000, 200, 0, 700, samples)

for index, ksamples in enumerate(sampleName):
    print ("SAMPLE: "+ksamples+"\n")
    events = Events(ksamples)    
    for i,event in enumerate(events):   
        event.getByLabel (labelPruned, handlePruned)
        genParticles = handlePruned.product()
        
        event.getByLabel(labelTriggerBits, handleTriggerBits)                                                                                                                                                                                                                                                                                                                                                           
        triggerBits = handleTriggerBits.product()  
        
        HLTTriggerNames = event.object().triggerNames(triggerBits)
        for i in range(triggerBits.size()):
            if triggerBits.accept(i):        
                acceptedTrigger = HLTTriggerNames.triggerName(i) 
                if "HLT_" not in acceptedTrigger: continue # name does not follow usual HLT naming conventions (e.g this exlcudes AlCa, MC, Dataset etc.)
                print(acceptedTrigger)

        for p in genParticles:
            if p.isHardProcess():
                tellMeMore(p)
                if fabs(p.pdgId() == 35): #Plotting something from the Higgs
                    massHiggs[index].Fill(p.mass())
                if fabs(p.pdgId() == 6000113 ): #Plotting something from the X
                    massX[index].Fill(p.mass())
                if fabs(p.pdgId() == 13 ): #Plotting something from the displaced muons
                    lxy[index].Fill(abs(p.vertex().rho()))
                    lzVslxy[index].Fill(abs(p.vertex().Z()), abs(p.vertex().rho()))

        # Which fraction of events in the denominator that fullfill the triger                                                                                                                                                                                                                                                                                                                                       
        HLTTriggerNames = event.object().triggerNames(triggerBits)
        for TriggerIndex, kTrigger in enumerate(TriggerFlags):
            for i in range(triggerBits.size()):
                if triggerBits.accept(i):
                    print (HLTTriggerNames.triggerName(i))

plotsFolder = '/nfs/cms/rhebrero/plots_prueba'
#makeSimple1DPlot(var, canvas, samples, title, xtitle, ytitle, output, folder, logy=False, showOnly = []):

makeSimple1DPlot(massHiggs, 'massHiggs', samples, '', 'M_{Higgs}', 'norm.a.u', 'massHiggs', plotsFolder, logy=False)
makeSimple1DPlot(massX, 'massX', samples, '', 'M_{X}', 'norm.a.u', 'massX', plotsFolder, logy=False)
makeSimple1DPlot(lxy, 'lxy', samples, '', 'L_{xy}[cm]', 'norm.a.u', 'lxy', plotsFolder, logy=True)
makeSimple2DPlot(lzVslxy, 'lzVslxy', samples, 'Generated L_{z}[cm] vs L_{xy}[cm]', 'L_{z}[cm]', 'L_{xy}[cm]', 'GenLzVsLxy', plotsFolder)
