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
from GenLongLivedUtils import *
from SimpleTools import *


#Samples to process
samplesDir = '/afs/hephy.at/work/a/aescalante/cmssw/SimpleGen/'

samples = Sample()

samples.AddSample(samplesDir+'EXO-RunIIFall17GS_HTo2LongLivedTo4mu_MH-200_MFF-50_CTau-200mm_TuneCUETP8M1_13TeV_pythia8_1.root', 'M_{H}=200, M_{X}=50, c#tau=20cm', '200_50_CTau_20cm', 2)
samples.AddSample(samplesDir+'EXO-RunIIFall17GS_HTo2LongLivedTo4mu_MH-125_MFF-20_CTau-1300mm_TuneCUETP8M1_13TeV_pythia8_1.root', 'M_{H}=125, M_{X}=20, c#tau=130cm', '125_20_CTau_130cm', 3)
samples.AddSample(samplesDir+'EXO-RunIIFall17GS_HTo2LongLivedTo4mu_MH-400_MFF-150_CTau-40mm_TuneCUETP8M1_13TeV_pythia8_1.root', 'M_{H}=400, M_{X}=150, c#tau=4cm', '400_150_CTau_4cm', 1) # last integer is the color

sampleName = samples.GetSampleName()
legendName = samples.GetLegendName()
histName = samples.GetHistName()

# FOR GEN-SIM
handlePruned  = Handle ("std::vector<reco::GenParticle>")
labelPruned = ("genParticles")


#Histograms
massHiggs = createSimple1DPlot("massHiggs", "M_{H}", 100, 100, 600, samples)
massX = createSimple1DPlot("massX", "M_{X}", 300, 1, 180, samples)
lxy = createSimple1DPlot("lxy", "lxy", 100, 1, 100, samples)
lzVslxy = createSimple2DPlot("lzVslxy", "lz vs lxy", 350, 0, 1000, 200, 0, 700, samples)

for index, ksamples in enumerate(sampleName):
    print "SAMPLE: "+ksamples+"\n"
    events = Events(ksamples)    
    for i,event in enumerate(events):   
        event.getByLabel (labelPruned, handlePruned)
        genParticles = handlePruned.product()
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



plotsFolder = '/afs/hephy.at/work/a/aescalante/cmssw/SimpleGen/plots/'
#makeSimple1DPlot(var, canvas, samples, title, xtitle, ytitle, output, folder, logy=False, showOnly = []):

makeSimple1DPlot(massHiggs, 'massHiggs', samples, '', 'M_{Higgs}', 'norm.a.u', 'massHiggs', plotsFolder, logy=False)
makeSimple1DPlot(massX, 'massX', samples, '', 'M_{X}', 'norm.a.u', 'massX', plotsFolder, logy=False)
makeSimple1DPlot(lxy, 'lxy', samples, '', 'L_{xy}[cm]', 'norm.a.u', 'lxy', plotsFolder, logy=True)
makeSimple2DPlot(lzVslxy, 'lzVslxy', samples, 'Generated L_{z}[cm] vs L_{xy}[cm]', 'L_{z}[cm]', 'L_{xy}[cm]', 'GenLzVsLxy', plotsFolder)
