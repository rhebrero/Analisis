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

#bash utils
import os

#configuration file
import argparse

#Updated Octobre 2022
parser = argparse.ArgumentParser(description="Simple gen analyzer, compatible with RPV, Benchmark and Darkphoton")

parser.add_argument('--inputFile'    , dest='INPUTFILE'    , default=''         , help='input file')
parser.add_argument('--process'      , dest='PROCESS'      , default=''         , help='process to be written in histograms')
parser.add_argument('--trigger'      , dest='TRIGGER'      , default=''         , help='input file (with scripts to run on)')
parser.add_argument('--label'        , dest='LABEL'        , default=''         , help='suffix for histograms and output folder')
parser.add_argument('--color'        , dest='COLOR'        , default=1          , help='color')
parser.add_argument('--triggerlabel' , dest='TRIGGERLABEL' , default='HLT'      , help='trigger process label')
parser.add_argument('--nevents'      , dest='NEVENTS'      , default=-1         , help='number of processed events')
parser.add_argument('--acceptance'   , dest='ACCEPTANCE'   , default=False      , help='apply basic acceptance cuts')
parser.add_argument('--outFolder'    , dest='OUTFOLDER'    , default=''         , help='output folder')

args = parser.parse_args()

if (len(args.INPUTFILE) == 0 or len(args.OUTFOLDER) == 0 or len(args.LABEL) == 0 or len(args.PROCESS) ==0 ):
    print ("provide minimum arguments: --inputFile, --process, --label, --outFolder")
    quit()

print ("running on jobs in {INPUTFILE}".format(INPUTFILE=args.INPUTFILE) )

outFolder = "{OUTFOLDER}/{LABEL}/".format(OUTFOLDER = args.OUTFOLDER, LABEL = args.LABEL)
print (outFolder)
if os.path.exists(outFolder) ==  False:
    print ("folder does not exist")
    os.makedirs(outFolder)
else: 
    print ("folder exists")

print ("will write output in {OUTFOLDERWITHLABEL}".format(OUTFOLDERWITHLABEL=outFolder))

samples = Sample()

import pdb
#samples.AddSample(args.INPUTFILE    , 'M_{H}=125, M_{X}=20, ALL'               , '125_20_CTau_130cm_ALL'         , 1)
samples.AddSample(args.INPUTFILE    , args.PROCESS + "_"+ args.LABEL           , args.PROCESS + "_"+ args.LABEL  , int(args.COLOR))
#samples.AddSample(samplesDir+ signal, 'L1'                                     , '125_20_CTau_130cm_L1'          , 14) # Gray
#samples.AddSample(samplesDir+ signal, 'L2'                                     , '125_20_CTau_130cm_L2'          , 2)  # Red
#samples.AddSample(samplesDir+ signal, 'L2VetoPrompt'                           , '125_20_CTau_130cm_L2VetoPrompt', 4)  # Blue
#samples.AddSample(samplesDir+ signal, 'L3Displaced'                            , '125_20_CTau_130cm_L3Displaced' , 8)  # Greed
#samples.AddSample(samplesDir+ signal, 'HLT'                                    , '125_20_CTau_130cm_HLT'         , 28) # Brown

sampleName = samples.GetSampleName()
legendName = samples.GetLegendName()
histName = samples.GetHistName()

#Type                                  Module                      Label     Process   
#--------------------------------------------------------------------------------------
#edm::TriggerResults                   "TriggerResults"            ""        "SIM"     
#edm::TriggerResults                   "TriggerResults"            ""        "HLT"     
#vector<reco::GenParticle>             "genParticles"              ""        "HLT"     
#trigger::TriggerEvent                 "hltTriggerSummaryAOD"      ""        "HLT"     
#edm::TriggerResults                   "TriggerResults"            ""        "HLTX"    
#trigger::TriggerEvent                 "hltTriggerSummaryAOD"      ""        "HLTX" 

# FOR GEN-SIM
handlePruned  = Handle ("std::vector<reco::GenParticle>")
labelPruned = ("genParticles")

# GEN PARTICLES
motherPdgID = getSignalPdgID()["mother"]
daughterPdgID = getSignalPdgID()["daughter"]

handleTriggerBits = Handle("edm::TriggerResults")        
labelTriggerBits  = ("TriggerResults","", args.TRIGGERLABEL) 

handleBeamspot  = Handle("reco::BeamSpot")
labelBeamspot  = ("hltOnlineBeamSpot","", args.TRIGGERLABEL) 

#1D Histograms Gen Level

h_massHiggs = createSimple1DPlot("h_massHiggs", "M_{H}", 200, 100., 1600., samples)
h_massX     = createSimple1DPlot("h_massX", "M_{X}"    , 200, 0., 500., samples)
h_muMulti   = createSimple1DPlot("", "h_muMulti"       , 4, 0., 4., samples)
h_lxy       = createSimple1DPlot("h_lxy", "lxy"        , 300,  0., 300., samples)
h_dxyMuons  = createSimple1DPlot("", "h_dxyMuons"      , 100,  0.,   50., samples)
h_dzMuons   = createSimple1DPlot("", "h_dzMuons"       , 100,  0.,  100., samples)
h_ptMuons   = createSimple1DPlot("", "h_ptMuons"       , 100,  0.,  250., samples)
h_mindxyMuons  = createSimple1DPlot("", "h_mindxyMuons", 100,  0.,   1., samples)
h_mindxygenMuons  = createSimple1DPlot("", "h_mindxygenMuons", 100,  0.,   1., samples)
h_mindzMuons   = createSimple1DPlot("", "h_mindzMuons" , 100,  0.,  30., samples)
h_minptMuons   = createSimple1DPlot("", "h_minptMuons" ,  60,  0.,  60., samples)
h_maxptMuons   = createSimple1DPlot("", "h_maxptMuons" ,  60,  0.,  60., samples)
h_etaMuons  = createSimple1DPlot("", "h_etaMuons"      , 100, -4.,    4., samples)
h_dRMuons   = createSimple1DPlot("", "h_dRMuons"       , 100,  0.,    3., samples)
h_cosalpha  = createSimple1DPlot("", "h_cosalpha"      , 100, -1.,    1., samples)
h_alpha     = createSimple1DPlot("", "h_alpha"         , 100,  0.,   6.3, samples)
h_dphi      = createSimple1DPlot("", "h_dphi"          , 100,  0.,   3.14, samples)
h_lxyVslz   = createSimple2DPlot("h_lxyVslz", "lxy vs lz", 350, 0, 1000, 200, 0, 700, samples)
h_dxyVsptrel = createSimple2DPlot("h_dxyVsptrel", "dxy vs pTrel", 100, 0., 50., 100, 0., 50., samples)

#1D Differential plots
doResolution = False
if doResolution == True:
    bins = {}
    h_dxyVspt_p = []
    h_dxyVspt = []
    h_lxyVspt = []
    h_lxyVspt_l =[]

    bins["pT"] = ["15", "30"]
    
    for pT in bins["pT"]:
        h_dxyVspt_p.append(createSimple1DPlot("h_dxyVspt_p_"+pT, "h_dxyVspt_p_"+pT, 100, 0., 0.1, samples))
        h_dxyVspt.append(createSimple1DPlot("h_dxyVspt_"+pT, "h_dxyVspt_"+pT, 100, 0., 10., samples))
        h_lxyVspt.append(createSimple1DPlot("h_lxyVspt_"+pT, "h_lxyVspt_"+pT, 50, 0., 100., samples))
        h_lxyVspt_l.append(createSimple1DPlot("h_lxyVspt_l_"+pT, "h_lxyVspt_l_"+pT, 60, 0., 300., samples))

    h_ptVsdxy     = []
    bins["threshold"] = ["0.015", "1.2"]
    for threshold in bins["threshold"]:
        h_ptVsdxy.append(createSimple1DPlot("h_ptVsdxy_"+threshold, "h_ptVsdxy_"+threshold, 60, 0., 60, samples))

    h_mindxyrange = []
    h_lxyrange    = [] 
    bins["distance"] = ["0.02", "0.1", "1", "10", "100", "300"]

    for distance in bins["distance"]:
        nbins = 100
        if distance in ["0.02", "0.1", "1", "10"]: nbins = 10
        if distance in ["100"]: nbins = 50
        if distance in ["300"]: nbins = 60

        h_mindxyrange.append(createSimple1DPlot("h_mindxyrange_"+distance, "h_mindxyrange_"+distance, nbins, 0., float(distance), samples))
        h_lxyrange.append(   createSimple1DPlot("h_lxyrange_"+distance   , "h_lxyrange_"+distance, nbins, 0., float(distance), samples))
    
nevents = int(args.NEVENTS)
triggerList = args.TRIGGER

if triggerList == "all": 
    triggerList = []
else:
    triggerList = triggerList.split(",")

print ("\n")
print ("Beging processing SimpleGenTriggerSim.py \n")
print ("N_EVENTS", nevents)
print ("TRIGGER LIST", triggerList)
print ("\n")

for index, ksample in enumerate(sampleName):
    print ("SAMPLE {INDEX}/{TOTAL}: {NAME}".format(INDEX=str(index+1), TOTAL=str(len(sampleName)), NAME=ksample))

    if isinstance(ksample, str):
        #if ksample is a string, convert to list
        ksample=ksample.split(" ")

    count_events = 0
    for indexSubsample, ksubsample in enumerate(ksample):## To debug 
        print ("   SUBSAMPLE {INDEXSUB}/{TOTALSUB}: {NAMESUB} ".format(INDEXSUB=indexSubsample+1, TOTALSUB=str(len(ksample)), NAMESUB=ksubsample.split('/')[-1] ))

        events = Events(ksubsample)    
        for i,event in enumerate(events):
            count_events = count_events + 1
            
            if (count_events % 1000 == 0 ): print("Event {COUNT_EVENTS}".format(COUNT_EVENTS=count_events))
            if count_events > nevents and nevents > 0: break

            #print("new event {I}, {INDEX}".format(I=i, INDEX=index))
            event.getByLabel(labelPruned, handlePruned)
            genParticles = handlePruned.product()

            beamspotInfo = False
            try:
                event.getByLabel(labelBeamspot, handleBeamspot)
                hltOnlineBeamSpot = handleBeamspot.product()
                #print ("BEAMSPOT ", hltOnlineBeamSpot.x0(), hltOnlineBeamSpot.y0(), hltOnlineBeamSpot.z0())
                beamspotInfo = True
            except:
                if count_events < 10: print ("WARNING: hltOnlineBeamSpot not found") #warnings are only shown for first 10 events

            triggerInfo = False
            try: 
                event.getByLabel(labelTriggerBits, handleTriggerBits)              
                triggerBits = handleTriggerBits.product()  
                HLTTriggerNames = events.object().triggerNames(triggerBits)
                triggerInfo = True
            except:
                print ("WARNING: HLTTriggerNames not found")
                
            #did the event trigger the event?
            triggered = False        
            if len(triggerList) > 0 and triggerInfo == True:
                for k in range(triggerBits.size()):
                    if triggerBits.accept(k) and triggered == False:
                        #print ("Triggers fired: ", HLTTriggerNames.triggerName(i))
                        for kTriggerList in triggerList:
                            if HLTTriggerNames.triggerName(i) == kTriggerList:
                                #print ("FIRED", index, triggerList, HLTTriggerNames.triggerName(i))
                                triggered = True
                                break
            else: 
                triggered = True
                #print ("Event {EVENT}/{NEVENTS}".format(EVENT=i, NEVENTS=events.size()))

            if triggered == True:
                for p in genParticles:
                    if p.isHardProcess() or abs(p.pdgId()) in daughterPdgID: #sometimes (e.g RPV, the daughter does not appear as hard process)
                        #tellMeMore(p)
                        if abs(p.pdgId()) in motherPdgID: #Plotting something from the Higgs, scalar Phi, or squark
                            h_massHiggs[index].Fill(p.mass())
                        if abs(p.pdgId()) in daughterPdgID: #Plotting something from the X, Zd, or chi_10 

                            alldaus = p.daughterRefVector()
                            if len(alldaus) == 1 and alldaus[0].pdgId() == p.pdgId(): continue # remove repeated gen particles (only appearing in RPV) 
                            h_massX[index].Fill(p.mass()) 

                            #lxy[index].Fill(abs(p.vertex().rho()))
                            #lzVslxy[index].Fill(abs(p.vertex().Z()), abs(p.vertex().rho()))
                            ## debug ##
                            #print(" len(alldaus)", len(alldaus))                            
                            #print(" p.mother(0).pdgId()", p.mother(0).pdgId())
                            #print(" p.pdgId()", p.pdgId())
                            ### loop over daughters for all daughters
                            #for k, kdau in enumerate(alldaus):
                            #    print(" alldaus[{INDEX}].pdgId() = {VALUE}".format(INDEX=k, VALUE= alldaus[k].pdgId()))
                            
                            daus = getDaughters(alldaus, mother = p.pdgId(), daughther = 13)                            
                            h_muMulti[index].Fill(len(daus))
                            ## loop over daughters for all muonic daughters
                            #for k, kdau in enumerate(daus):
                            #    print(" daus[{INDEX}].pdgId() = {VALUE}".format(INDEX=k, VALUE= daus[k].pdgId()))

                            if len(daus) != 2:
                                if len(daus)>0:
                                    print ("+++ LLP (", p.pdgId(),") decay involed", len(daus), "muons +++")
                                    print ("+++ PLEASE CHECK ... +++")
                            else:
                                #print ("INFO: LLP (", p.pdgId(),") decay involed", len(daus), "muons +++")
                                if (daus[0].pdgId() == 13 and daus[1].pdgId() == -13) or (daus[0].pdgId() == -13 and daus[1].pdgId() == 13):
                                    fsmuons = findFinalStateMuons(daus)
                                    if len(fsmuons) != 2:
                                        print ("+++ Wrong muon multiplicity +++")
                                        break;

                                    #print ("pTs of final state muons:", round(fsmuons[0].pt(),2), round(fsmuons[1].pt(),2))
                                    dimu_px = fsmuons[0].px() + fsmuons[1].px()
                                    dimu_py = fsmuons[0].py() + fsmuons[1].py()
                                    dimu_pt = sqrt(dimu_px**2 + dimu_py**2)

                                    #minimum
                                    min_pt = 999
                                    min_dxy = 999
                                    min_dxygen = 999
                                    min_dz = 999

                                    #maximum
                                    max_pt = 0

                                    if args.ACCEPTANCE == True:
                                        #basic acceptance cuts
                                        if abs(fsmuons[0].vertex().rho()) > 600: continue
                                        if abs(fsmuons[0].vertex().Z()) > 500: continue
                                        if abs(fsmuons[0].eta()) > 2.0 or abs(fsmuons[1].eta()) >2.0: continue

                                    for muon in fsmuons:
                                        h_ptMuons[index].Fill(muon.pt())
                                        h_etaMuons[index].Fill(muon.eta())

                                        # dxy and dz w.r.t. (0; 0)
                                        dxygen = (-muon.vx()*muon.py() + muon.vy()*muon.px())/muon.pt()
                                        dzgen = muon.vz() - (muon.vx()*muon.px() + muon.vy()*muon.py())/muon.pt()*muon.pz()/muon.pt()

                                        # dxy and dz w.r.t. beamspot (0.01075690; 0.0417208; -0.0316298)
                                        if beamspotInfo == True:
                                            ref_x = hltOnlineBeamSpot.x0()  - muon.vx()   
                                            ref_y = hltOnlineBeamSpot.y0()  - muon.vy() 
                                            ref_z =  hltOnlineBeamSpot.z0() - muon.vz()
                                        else:  #harcoded values only in case beampost information is not available
                                            ref_x = 0.01075690  - muon.vx()   
                                            ref_y = 0.0417208  - muon.vy() 
                                            ref_z = -0.0316298 - muon.vz()
                                            
                                        dxy = (-ref_x*muon.py() + ref_y*muon.px())/muon.pt()
                                        dz = ref_z - (muon.vx()*muon.px() + muon.vy()*muon.py())/muon.pt()*muon.pz()/muon.pt()

                                        #the differences between dxy wrt 0;0 or beamspot are not negligible
                                        #print (dxygen, dxy)

                                        h_dxyMuons[index].Fill(fabs(dxy))
                                        h_dzMuons[index].Fill(fabs(dz))

                                        # dxy vs relative pT of a muon in a pair
                                        px_rel = muon.px() - dimu_px
                                        py_rel = muon.py() - dimu_py
                                        pt_rel = sqrt(px_rel**2 + py_rel**2)
                                        h_dxyVsptrel[index].Fill(pt_rel, fabs(dxy))

                                        # minimum quantities of the pair
                                        min_pt     = min(muon.pt(), min_pt)
                                        max_pt     = max(muon.pt(), max_pt)
                                        min_dxygen = min(fabs(dxygen), fabs(min_dxygen))
                                        min_dxy    = min(fabs(dxy), fabs(min_dxy))
                                        min_dz     = min(fabs(dz), fabs(min_dz))

                                    h_minptMuons[index].Fill(min_pt)
                                    h_maxptMuons[index].Fill(max_pt)
                                    h_mindxygenMuons[index].Fill(min_dxygen)
                                    h_mindxyMuons[index].Fill(min_dxy)
                                    h_mindzMuons[index].Fill(min_dz)

                                    if doResolution == True:
                                        for ptIndex, pT in enumerate(bins["pT"]):
                                            if min_pt > float(pT):                                        
                                                h_dxyVspt[ptIndex][index].Fill(min_dxy)
                                                h_dxyVspt_p[ptIndex][index].Fill(min_dxy)

                                        for thresholdIndex, threshold in enumerate(bins["threshold"]):
                                            if min_dxy > float(threshold):
                                                h_ptVsdxy[thresholdIndex][index].Fill(min_pt)

                                    #if min_dxy < 0.001 and min_pt > 15:
                                    #    print ("new event", min_dxy, min_pt)
                                    #    for muon in fsmuons:
                                    #        # dxy and dz w.r.t. (0; 0)
                                    #        dxy = (-muon.vx()*muon.py() + muon.vy()*muon.px())/muon.pt()
                                    #        print ("   dxy, pt", dxy, muon.pt())
                                    #    for i in range(triggerBits.size()):
                                    #        if triggerBits.accept(i):
                                    #            #print ("Triggers fire: ", HLTTriggerNames.triggerName(i))
                                    #            if HLTTriggerNames.triggerName(i) in triggerList:
                                    #                print ("   FIRED", index, triggerList, HLTTriggerNames.triggerName(i))

                                        for distanceIndex, distance in enumerate(bins["distance"]):
                                            h_mindxyrange[distanceIndex][index].Fill(min_dxy)

                                    # delta R between two muons in a pair
                                    dphi = fabs(fsmuons[0].phi() - fsmuons[1].phi())
                                    deta = fabs(fsmuons[0].eta() - fsmuons[1].eta())
                                    dR = sqrt(dphi**2 + deta**2)
                                    h_dRMuons[index].Fill(dR)

                                    # 3D opening angle between two muons in a pair
                                    cosalpha = (fsmuons[0].px()*fsmuons[1].px() + fsmuons[0].py()*fsmuons[1].py() + fsmuons[0].pz()*fsmuons[1].pz())/fsmuons[0].p()/fsmuons[1].p()
                                    alpha = acos(cosalpha)
                                    h_cosalpha[index].Fill(cosalpha)
                                    h_alpha[index].Fill(alpha)

                                    if fabs(fsmuons[0].vx() - fsmuons[1].vx()) > 1e-3 or fabs(fsmuons[0].vy() - fsmuons[1].vy()) > 1e-3:
                                        print ("+++ two daughter muons are not produced at the same vertex +++")
                                    else:
                                        cosdphi = (fsmuons[0].vx()*dimu_px + fsmuons[0].vy()*dimu_py)/fsmuons[0].vertex().rho()/dimu_pt
                                        #print(cosdphi)
                                        #print(cosdphi, acos(cosdphi))
                                        if cosdphi > 1.0 : cosdphi  =  0.9999 #protection against rounding
                                        if cosdphi < -1.0: cosdphi  = -0.9999 #protection against rounding
                                            
                                        dphi = acos(cosdphi)
                                        #print ("dimu_pt =", dimu_pt, "cos(dphi) =", cosdphi, "dphi =", dphi)
                                        h_lxy[index].Fill(fsmuons[0].vertex().rho())
                                        h_lxyVslz[index].Fill(fabs(fsmuons[0].vertex().Z()), fsmuons[0].vertex().rho())
                                        h_dphi[index].Fill(dphi)

                                        if doResolution == True:
                                            for distanceIndex, distance in enumerate(bins["distance"]):
                                                h_lxyrange[distanceIndex][index].Fill(fsmuons[0].vertex().rho())

                                            for ptIndex, pT in enumerate(bins["pT"]):
                                                if min_pt > float(pT):                                        
                                                    h_lxyVspt[ptIndex][index].Fill(fsmuons[0].vertex().rho())
                                                    h_lxyVspt_l[ptIndex][index].Fill(fsmuons[0].vertex().rho())

                                else:
                                    print ("+++ X did not decay into two muons +++")
                                    print ("+++ id1:", daus[0].pdgId(), "id2:", daus[1].pdgId())

    print ("\n")
    print ("SUMMARY \n")
    print ("SAMPLE ", ksample)
    print ("PROCESSED ", count_events, "events")
    print ("\n")


#makeSimple1DPlot(var, canvas, samples, title, xtitle, ytitle, output, folder, logy=False, showOnly = []):

makeSimple1DPlot(h_massHiggs, 'h_massHiggs', samples, '', 'M_{Higgs}', 'events', 'h_massHiggs', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_massX, 'h_massX', samples, '', 'M_{X}', 'events', 'h_massX', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_muMulti, 'h_muMulti', samples, '', '#mu multiplicity', 'events', 'h_muMulti', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_lxy, 'h_lxy', samples, '', 'L_{xy}[cm]', 'events', 'h_lxy', outFolder, logy=True, norm=False)
makeSimple2DPlot(h_lxyVslz, 'h_lxyVslz', samples, 'Generated L_{xy}[cm] vs L_{z}[cm]', 'L_{z}[cm]', 'L_{xy}[cm]', 'h_LxyVsLz', outFolder)
makeSimple1DPlot(h_etaMuons, 'h_etaMuons', samples, '', 'eta', '', 'h_etaMuons', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_ptMuons, 'h_ptMuons', samples, '', 'pT [GeV]', '', 'h_ptMuons', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_dxyMuons, 'h_dxyMuons', samples, '', 'dxy [cm]', '', 'h_dxyMuons', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_dzMuons,  'h_dzMuons',  samples, '', 'dz [cm]',  '', 'h_dzMuons', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_minptMuons, 'h_minptMuons', samples, '', 'min pT [GeV]', '', 'h_minptMuons', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_maxptMuons, 'h_maxptMuons', samples, '', 'max pT [GeV]', '', 'h_maxptMuons', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_mindxyMuons, 'h_mindxyMuons', samples, '', 'min dxy [cm]', '', 'h_mindxyMuons', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_mindxygenMuons, 'h_mindxygenMuons', samples, '', 'min dxy [cm]', '', 'h_mindxygenMuons', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_mindzMuons,  'h_mindzMuons',  samples, '', 'min dz [cm]',  '', 'h_mindzMuons', outFolder, logy=True, norm=False)
makeSimple2DPlot(h_dxyVsptrel, 'h_dxyVsptrel', samples, 'dxy vs pT(mu,X)', 'pT(mu,X) [GeV]', 'dxy[cm]', 'h_dxyVsptrel', outFolder)
makeSimple1DPlot(h_dRMuons,  'h_dRMuons',  samples, '', 'dR',         '', 'h_dRMuons',  outFolder, logy=False, norm=False)
makeSimple1DPlot(h_cosalpha, 'h_cosalpha', samples, '', 'cos(alpha)', '', 'h_cosalpha', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_alpha,    'h_alpha',    samples, '', 'alpha',      '', 'h_alpha',    outFolder, logy=False, norm=False)
makeSimple1DPlot(h_dphi,     'h_dphi',     samples, '', 'dphi',       '', 'h_dphi',     outFolder, logy=False, norm=False)
#makeSimple2DPlot(h_mOverTau, 'h_mOverTau', samples,'', 'm/tau', 'L', 'E', 'h_mOverTau', outFolder)

#1D Histograms Gen Level, differential plots.
if doResolution == True:
    for index, pT in enumerate(bins["pT"]):
        makeSimple1DPlot(h_dxyVspt_p[index], "h_dxyVspt_p_"+pT, samples, 'pT>'+pT, 'dxy_'+pT,    'Events', 'h_dxyVspt_p_'+pT,     outFolder, logy=True, norm=False)
        makeSimple1DPlot(h_dxyVspt[index], "h_dxyVspt_"+pT, samples, 'pT>'+pT, 'dxy_'+pT,      'Events', 'h_dxyVspt_'+pT,     outFolder, logy=True, norm=False)
        makeSimple1DPlot(h_lxyVspt[index], "h_lxyVspt_"+pT, samples, 'pT>'+pT, 'lxy_'+pT,      'Events', 'h_lxyVspt_'+pT,     outFolder, logy=True, norm=False)
        makeSimple1DPlot(h_lxyVspt_l[index], "h_lxyVspt_l_"+pT, samples, 'pT>'+pT, 'lxy_'+pT,      'Events', 'h_lxyVspt_l_'+pT,     outFolder, logy=True, norm=False)

    for index, distance in enumerate(bins["distance"]):
        makeSimple1DPlot(h_mindxyrange[index], "h_mindxyrange_"+distance, samples, '', 'dxy [cm]', '', "h_mindxyrange_"+distance , outFolder, logy=True, norm=False)
        makeSimple1DPlot(h_lxyrange[index]   , "h_lxyrange_"+distance   , samples, '', 'Lxy [cm]', '', "h_lxyrange_"+distance    , outFolder, logy=True, norm=False)

    for index, threshold in enumerate(bins["threshold"]):
        makeSimple1DPlot(h_ptVsdxy[index]   , "h_ptVsdxy_"+threshold   , samples, '', 'pT [GeV]', '', "h_ptVsdxy_"+threshold    , outFolder, logy=True, norm=False)

