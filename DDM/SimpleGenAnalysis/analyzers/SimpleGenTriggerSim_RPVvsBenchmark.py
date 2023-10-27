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

# Utils for Longlived Generator Level studies.
from utils import getLibraries
from GenLongLivedUtils import *
from SimpleTools import *
from myMathUtils import *

# debug tools 
import pdb

# bash utils
import os

#configuration file
import argparse                                    

#Updated Octobre 2023
parser = argparse.ArgumentParser(description="Simple gen analyzer, compatible with RPV, Benchmark and Darkphoton, SMUON, STOP")
parser.add_argument('--inputFile'    , dest='INPUTFILE'    , default=''         , help='input file')
parser.add_argument('--trigger'      , dest='TRIGGER'      , default=''         , help='input file (with scripts to run on)')
parser.add_argument('--label'        , dest='LABEL'        , default=''         , help='suffix for histograms and output folder')
parser.add_argument('--color'        , dest='COLOR'        , default=1          , help='color')
parser.add_argument('--triggerlabel' , dest='TRIGGERLABEL' , default='HLT'      , help='trigger process label')
parser.add_argument('--nevents'      , dest='NEVENTS'      , default=-1         , help='number of processed events')
parser.add_argument('--acceptance'   , dest='ACCEPTANCE'   , default=False      , help='apply basic acceptance cuts')
parser.add_argument('--outFolder'    , dest='OUTFOLDER'    , default=''         , help='output folder')
parser.add_argument('--LHE'          , dest='LHE'          , default=False      , help='run on LHE root file')
parser.add_argument('--model'        , dest='model'        , default=""         , help='model (BENCHMARK, HAHM, RPV, STOP, SMUON)', required = True)
parser.add_argument('--verbose'      , dest='verbose'      , default=0          , help='increase verbosity (levels 0, 1, 2)')
args = parser.parse_args()

if (len(args.INPUTFILE) == 0 or len(args.OUTFOLDER) == 0 or len(args.LABEL) == 0):
    print ("provide minimum arguments: --inputFile, --label, --outFolder")
    quit()

print ("running on jobs in {INPUTFILE}".format(INPUTFILE=args.INPUTFILE) )

# create output folder, if it does not exist
outFolder = "{OUTFOLDER}/{LABEL}/".format(OUTFOLDER = args.OUTFOLDER, LABEL = args.LABEL)
print (outFolder)
if os.path.exists(outFolder) ==  False:
    print ("folder does not exist")
    os.makedirs(outFolder)
else: 
    print ("folder exists")

print ("will write output in {OUTFOLDERWITHLABEL}".format(OUTFOLDERWITHLABEL=outFolder))

# add the sample to process 
samples = Sample()
samples.AddSample(args.INPUTFILE    , args.LABEL           , args.LABEL  , int(args.COLOR))
# other samples could be added (to be implemented as argument value). In practice this is not recommended as it less efficient for batch production)

# get vectors for samples, legends and histograms
sampleName = samples.GetSampleName()
legendName = samples.GetLegendName()
histName = samples.GetHistName()

# Gen sim collections
handlePruned  = Handle ("std::vector<reco::GenParticle>")
labelPruned = ("genParticles")

# Other collections 
handleTriggerBits = Handle("edm::TriggerResults")        
labelTriggerBits  = ("TriggerResults","", args.TRIGGERLABEL) 

handleBeamspot  = Handle("reco::BeamSpot")
labelBeamspot  = ("hltOnlineBeamSpot","", args.TRIGGERLABEL) 

# Getting information of model (HAHM, RPV, BENCHMARK, STAU, STOP)
motherPdgID = getSignalPdgID(args.model)["mother"]
longlivedPdgID = getSignalPdgID(args.model)["LLP"]
otherPdgID = getSignalPdgID(args.model)["otherBSM"]

# 1D Histograms Gen Level
h_pzProton       = createSimple1DPlot("", "h_pzProton", 150, 6000, 7500., samples)
h_massHiggs      = createSimple1DPlot("", "h_massHiggs", 200, 100., 1600., samples)
h_massX          = createSimple1DPlot("", "h_massX", 200, 0., 500., samples)
h_ptX            = createSimple1DPlot("", "h_ptX", 200, 0., 500., samples)
h_ptOvermassX    = createSimple1DPlot("", "h_ptOvermass", 100, 0., 10., samples)
h_betaX          = createSimple1DPlot("", "h_beta", 100, 0., 1., samples)
h_muMulti        = createSimple1DPlot("", "h_muMulti"       , 4, 0., 4., samples)
h_genTriggerDiff = createSimple1DPlot("", "h_genTriggerDiff"    , 6, 0., 6., samples)
h_genTrigger     = createSimple1DPlot("", "h_genTrigger"    , 2, 0., 2., samples)
h_lxy_s          = createSimple1DPlot("", "lxy_s"      , 300,  0., 100., samples)
h_lxy            = createSimple1DPlot("", "lxy"       , 300,  0., 300., samples)
h_distance_x     = createSimple1DPlot("", "distance_x" , 300,  0., 300., samples)
h_distance_y     = createSimple1DPlot("", "distance_y" , 300,  0., 300., samples)
h_distance_z     = createSimple1DPlot("", "distance_z" , 300,  0., 300., samples)
h_distance       = createSimple1DPlot("", "distance"   , 300,  0., 300., samples)
h_dxyMuons       = createSimple1DPlot("", "h_dxyMuons"      , 100,  0.,   50., samples)
h_dzMuons        = createSimple1DPlot("", "h_dzMuons"       , 100,  0.,  100., samples)
h_ptMuons        = createSimple1DPlot("", "h_ptMuons"       , 100,  0.,  250., samples)
h_mindxyMuons    = createSimple1DPlot("", "h_mindxyMuons", 100,  0.,   1., samples)
h_mindxygenMuons = createSimple1DPlot("", "h_mindxygenMuons", 100,  0.,   1., samples)
h_mindzMuons     = createSimple1DPlot("", "h_mindzMuons" , 100,  0.,  30., samples)
h_minptMuons     = createSimple1DPlot("", "h_minptMuons" ,  60,  0.,  60., samples)
h_minptMuons_l   = createSimple1DPlot("", "h_minptMuons_l" , 200,  0., 200., samples)
h_maxptMuons     = createSimple1DPlot("", "h_maxptMuons" ,  60,  0.,  60., samples)
h_dimumass       = createSimple1DPlot("", "h_dimumass"    , 120, 0., 120., samples)
h_corrdimumass   = createSimple1DPlot("", "h_corrdimumass"    , 120, 0., 120., samples)
h_corrdimumass_2d = createSimple1DPlot("", "h_corrdimumass_2d"    , 120, 0., 120., samples)
h_dimumass_l     = createSimple1DPlot("", "h_dimumass_l"  , 500, 0., 500., samples)
h_corrdimumass_l = createSimple1DPlot("", "h_corrdimumass_l"  , 500, 0., 500., samples)
h_corrdimumass_2d_l = createSimple1DPlot("", "h_corrdimumass_2d_l"  , 500, 0., 500., samples)
h_dimupt         = createSimple1DPlot("", "h_dimupt"       , 120, 0., 120., samples)
h_proptime       = createSimple1DPlot("", "h_proptime"     , 120, 0., 120., samples)
h_proptime_l     = createSimple1DPlot("", "h_proptime_l"   , 500, 0., 500., samples)
h_etaMuons       = createSimple1DPlot("", "h_etaMuons"      , 100, -4.,    4., samples)
h_dRMuons        = createSimple1DPlot("", "h_dRMuons"       , 100,  0.,    3., samples)
h_cosalpha       = createSimple1DPlot("", "h_cosalpha"      , 100, -1.,    1., samples)
h_alpha          = createSimple1DPlot("", "h_alpha"         , 100,  0.,   6.3, samples)
h_dphi           = createSimple1DPlot("", "h_dphi"          , 100,  0.,   3.14, samples)
h_lxyVslz        = createSimple2DPlot("h_lxyVslz", "lxy vs lz", 350, 0, 1000, 200, 0, 700, samples)
h_dxyVsptrel     = createSimple2DPlot("h_dxyVsptrel", "dxy vs pTrel", 100, 0., 50., 100, 0., 50., samples)

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

# end of definition of the histograms

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
        if (args.LHE == False and "_inLHE_" in ksubsample.split('/')[-1]):
            print ("   INFO: This is a LHE file -> Skip")
            continue
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
                if int(args.verbose) >= 1:
                    print("len(triggerBits)", len(triggerBits))
                    for k in range(triggerBits.size()):
                        if triggerBits.accept(k):
                            print ("Triggers fired: ", HLTTriggerNames.triggerName(k))
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
                                #print ("FIRED", index, triggerList, HLTTriggerNames.triggerName(k))
                                triggered = True
                                break
            else: 
                triggered = True
                #print ("Event {EVENT}/{NEVENTS}".format(EVENT=i, NEVENTS=events.size()))

            if triggered == True:
                # set LLP daugthers (all daus) and final state muons (daus) to zero
                alldaus = []
                daus = []

                for p in genParticles:
                    # tellMeMore(p)
                    if abs(p.pdgId()) == 2212:
                        h_pzProton[index].Fill(abs(p.pz()))
                    if p.isHardProcess() or abs(p.pdgId()) in longlivedPdgID: #sometimes (e.g RPV, the daughter does not appear as hard process)
                        #tellMeMore(p)

                        if abs(p.pdgId()) in motherPdgID: 
                            # fill information for LLP mother
                            h_massHiggs[index].Fill(p.mass())

                        if abs(p.pdgId()) in longlivedPdgID: 
                            alldaus = p.daughterRefVector()                            
                            if isLastCopyOfLLP(alldaus, p) == False:
                                continue
                        
                            # fill information for LLP
                            massX = p.mass()
                            h_massX[index].Fill(massX)
                            ptX = p.pt()
                            h_ptX[index].Fill(ptX)

                            if massX == 0:
                                print("ERROR: LLP is massless")
                                exit()
                            
                            # fill kinematics of LLP
                            h_ptOvermassX[index].Fill(ptX/massX)
                            genBeta = sqrt(p.energy()*p.energy() - p.mass()*p.mass())/p.energy()
                            h_betaX[index].Fill(genBeta) 

                            # get LLP decay producuts (note that this is model dependent)
                            if len(daus) == 0:
                                # daughters of first LLP with pdgID = 13
                                daus = getDaughters(alldaus, mother = p.pdgId(), daughther = 13)
                            else:
                                # daughters of second LLP with pdgID = 13 if the first LLP had decays to pdgID = 13
                                exdaus = getDaughters(alldaus, mother = p.pdgId(), daughther = 13)
                                if args.model == "STOP" or args.model == "SMUON":
                                    # combine muons from two decays
                                    daus = daus + exdaus
                                if args.model == "BENCHMARK" or args.model == "RPV":
                                    # replace muons from the decays (e.g in 4mu samples)
                                    daus = exdaus
                            
                            # Multiplicity for debugging                            
                            h_muMulti[index].Fill(len(daus))
                            
                            # After this point work only with events with at least two dimuons (for SMUON and STOP, they must come from different mother)
                            if len(daus) < 2: continue

                            # check correct multiplicity
                            if len(daus) != 2:
                                if len(daus)>0:
                                    print ("+++ LLP (", p.pdgId(),") decay involed", len(daus), "muons +++")
                                    print ("+++ PLEASE CHECK ... +++")
                            else:
                                if (daus[0].pdgId() == 13 and daus[1].pdgId() == -13) or (daus[0].pdgId() == -13 and daus[1].pdgId() == 13):
                                    fsmuons = findFinalStateMuons(daus)
                                    if len(fsmuons) != 2:
                                        print ("+++ Wrong muon multiplicity +++")
                                        break

                                    # select events with two muons in a given acceptance
                                    if args.ACCEPTANCE == True:
                                        if abs(fsmuons[0].vertex().rho()) > 600 or abs(fsmuons[1].vertex().rho()) > 600: continue
                                        if abs(fsmuons[0].vertex().Z()) > 500 or abs(fsmuons[1].vertex().Z()) > 500: continue
                                        if abs(fsmuons[0].eta()) > 2.0 or abs(fsmuons[1].eta()) >2.0: continue

                                    dimu_px = fsmuons[0].px() + fsmuons[1].px()
                                    dimu_py = fsmuons[0].py() + fsmuons[1].py()
                                    dimu_pz = fsmuons[0].pz() + fsmuons[1].pz()
                                    dimu_pt = sqrt(dimu_px**2 + dimu_py**2)
                                    dimu_p = sqrt(dimu_px**2 + dimu_py**2 + dimu_pz**2)
                                    dimu_mass = mass(fsmuons[0], fsmuons[1])

                                    # minimum and maximum
                                    min_pt = 999
                                    min_dxy = 999
                                    min_dxygen = 999
                                    min_dz = 999
                                    max_pt = 0
                                    max_eta = 0

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
                                        else:  #harcoded values only in case beamspot information is not available
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
                                        min_dxygen = min(fabs(dxygen), fabs(min_dxygen))
                                        min_dxy    = min(fabs(dxy), fabs(min_dxy))
                                        min_dz     = min(fabs(dz), fabs(min_dz))
                                        max_pt     = max(muon.pt(), max_pt)
                                        max_eta    = max(fabs(muon.eta()), max_eta)

                                    h_minptMuons[index].Fill(min_pt)
                                    h_minptMuons_l[index].Fill(min_pt)
                                    h_maxptMuons[index].Fill(max_pt)
                                    h_mindxygenMuons[index].Fill(min_dxygen)
                                    h_mindxyMuons[index].Fill(min_dxy)
                                    h_mindzMuons[index].Fill(min_dz)

                                    # check if events would pass a pseudotrigger defined at gen level
                                    genTriggerBit = getGenTrigger(min_pt, max_pt, min_dxy, max_eta, fsmuons[0].vertex().rho(), abs(fsmuons[0].vertex().Z()))
                                    h_genTriggerDiff[index].Fill(genTriggerBit)
                                    if genTriggerBit > 2:
                                        h_genTrigger[index].Fill(1)
                                    else:
                                        h_genTrigger[index].Fill(0)

                                    # do a study of the resolution (deprecated?)
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
                                    # end of resolution study

                                    # delta R between two muons in a pair
                                    dphi = fabs(deltaPhi(fsmuons[0], fsmuons[1]))
                                    deta = fabs(fsmuons[0].eta() - fsmuons[1].eta())
                                    dR = sqrt(dphi**2 + deta**2)
                                    h_dRMuons[index].Fill(dR)

                                    # 3D opening angle between two muons in a pair
                                    cosalpha = (fsmuons[0].px()*fsmuons[1].px() + fsmuons[0].py()*fsmuons[1].py() + fsmuons[0].pz()*fsmuons[1].pz())/fsmuons[0].p()/fsmuons[1].p()
                                    alpha = acos(cosalpha)
                                    h_cosalpha[index].Fill(cosalpha)
                                    h_alpha[index].Fill(alpha)

                                    # distance between the two muons in x, y, z and total
                                    distance_x = fabs(fsmuons[0].vx() - fsmuons[1].vx())
                                    distance_y = fabs(fsmuons[0].vy() - fsmuons[1].vy())
                                    distance_z = fabs(fsmuons[0].vz() - fsmuons[1].vz())
                                    distance = sqrt(distance_x*distance_x + distance_y*distance_y + distance_z*distance_z)

                                    h_distance_x[index].Fill(distance_x)
                                    h_distance_y[index].Fill(distance_y)
                                    h_distance_z[index].Fill(distance_z)
                                    h_distance[index].Fill(distance)

                                    if distance_x > 1e-3 or distance_y > 1e-3:
                                        print ("+++ INFO: two daughter muons are not produced at the same vertex +++")

                                    if distance_x < 1e-3 and distance_y < 1e-3 or args.model == "SMUON" or args.model == "STOP":
                                        
                                        # note: for SMUON and STOP models, currently the dphi, dtheta, lxy, lz... are only implemented for first muon (one of the decay)

                                        cosdphi = (fsmuons[0].vx()*dimu_px + fsmuons[0].vy()*dimu_py)/fsmuons[0].vertex().rho()/dimu_pt
                                        cosdtheta = (fsmuons[0].vx()*dimu_px + fsmuons[0].vy()*dimu_py + fsmuons[0].vz()*dimu_pz)/sqrt(fsmuons[0].vertex().rho()**2+fsmuons[0].vertex().Z()**2)/dimu_p
                                        #print(cosdphi, cosdtheta)
                                        #print(cosdphi, acos(cosdphi))
                                        
                                        # protection against rounding
                                        if cosdphi > 1.0 : cosdphi  =  0.9999     
                                        if cosdphi < -1.0: cosdphi  = -0.9999     
                                        if cosdtheta > 1.0 : cosdtheta  =  0.9999 
                                        if cosdtheta < -1.0: cosdtheta  = -0.9999 
                                            
                                        dphi = acos(cosdphi)
                                        dtheta = acos(cosdtheta)
                                        
                                        #print ("dimu_pt =", dimu_pt, "cos(dphi) =", cosdphi, "dphi =", dphi)
                                        h_lxy_s[index].Fill(fsmuons[0].vertex().rho())
                                        h_lxy[index].Fill(fsmuons[0].vertex().rho())
                                        h_lxyVslz[index].Fill(fabs(fsmuons[0].vertex().Z()), fsmuons[0].vertex().rho())
                                        h_dphi[index].Fill(dphi)

                                        # mass
                                        h_dimumass[index].Fill(dimu_mass)
                                        h_dimumass_l[index].Fill(dimu_mass)
                                        h_dimupt[index].Fill(dimu_pt)

                                        # corrected mass (in 2D and 3D)                                       
                                        corr_mass_2d = sqrt(dimu_mass**2+sin(dphi)*sin(dphi)*dimu_pt**2)+dimu_pt*sin(dphi)
                                        corr_mass = sqrt(dimu_mass**2+sin(dtheta)*sin(dtheta)*dimu_p**2)+dimu_p*sin(dtheta)
                                        h_corrdimumass_2d[index].Fill(corr_mass_2d)
                                        h_corrdimumass_2d_l[index].Fill(corr_mass_2d)
                                        h_corrdimumass[index].Fill(corr_mass)
                                        h_corrdimumass_l[index].Fill(corr_mass)
                                        
                                        # proper time, to recover the lifetime
                                        h_proptime[index].Fill(fsmuons[0].vertex().rho()*10*massX/ptX) #convert lxy from cm to mm
                                        h_proptime_l[index].Fill(fsmuons[0].vertex().rho()*10*massX/ptX) #convert lxy from cm to mm

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

# getting labels for x and y-axis labels
motherLatex = getSignalPdgID(args.model)["mother_latex"][0]
longlivedLatex = getSignalPdgID(args.model)["LLP_latex"][0]
if len(otherPdgID)>0:
    otherLatex = getSignalPdgID(args.model)["otherBSM_latex"][0]

# 1D distributions
# makeSimple1DPlot(var, canvas, samples, title, xtitle, ytitle, output, folder, logy=False, showOnly = []):
makeSimple1DPlot(h_pzProton, 'h_pzProton', samples, '', 'p_{Z} proton', 'events', 'h_pzProton', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_massHiggs, 'h_massHiggs', samples, '', 'M({MOTHER})'.format(MOTHER=motherLatex), 'events', 'h_massHiggs', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_massX, 'h_massX', samples, '', 'M({LLP})'.format(LLP = longlivedLatex), 'events', 'h_massX', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_ptX, 'h_ptX', samples, '', 'p_{T}({LLP})'.format(T="{T}", LLP = longlivedLatex), 'events', 'h_ptX', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_betaX, 'h_betaX', samples, '', '#beta({LLP})'.format(LLP = longlivedLatex), 'events', 'h_betaX', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_ptOvermassX, 'h_ptOvermassX', samples, '', 'p_{T}({LLP})/M({LLP})'.format(T="{T}", LLP=longlivedLatex), 'events', 'h_ptOvermassX', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_muMulti, 'h_muMulti', samples, '', '#mu multiplicity', 'events', 'h_muMulti', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_genTriggerDiff, 'h_genTriggerDiff', samples, '', 'gen level trigger', 'events', 'h_genTriggerDiff', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_genTrigger, 'h_genTrigger', samples, '', 'gen level trigger', 'events', 'h_genTrigger', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_lxy_s, 'h_lxy_s', samples, '', 'L_{xy}[cm]', 'events', 'h_lxy_s', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_lxy, 'h_lxy', samples, '', 'L_{xy}[cm]', 'events', 'h_lxy', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_distance_x, 'h_distance_x', samples, '', '|#mu_{1}.vx - #mu_{2}.vx| [cm]', 'events', 'h_distance_x', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_distance_y, 'h_distance_y', samples, '', '|#mu_{1}.vy - #mu_{2}.vy| [cm]', 'events', 'h_distance_y', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_distance_z, 'h_distance_z', samples, '', '|#mu_{1}.vz - #mu_{2}.vz| [cm]', 'events', 'h_distance_z', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_distance, 'h_distance', samples, '', '|#mu_{1}- #mu_{2}| [cm]', 'events', 'h_distance', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_etaMuons, 'h_etaMuons', samples, '', '#eta', 'events', 'h_etaMuons', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_ptMuons, 'h_ptMuons', samples, '', 'p_{T} [GeV]', 'events', 'h_ptMuons', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_dxyMuons, 'h_dxyMuons', samples, '', 'dxy [cm]', 'events', 'h_dxyMuons', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_dzMuons,  'h_dzMuons',  samples, '', 'dz [cm]', 'events', 'h_dzMuons', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_minptMuons, 'h_minptMuons', samples, '', 'min(p_{T}) [GeV]', 'events', 'h_minptMuons', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_minptMuons_l, 'h_minptMuons_l', samples, '', 'min(p_{T}) [GeV]', 'events', 'h_minptMuons_l', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_maxptMuons, 'h_maxptMuons', samples, '', 'max(p_{T}) [GeV]', 'events', 'h_maxptMuons', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_dimumass, 'h_dimumass', samples, '', 'm_{#mu#mu} [GeV]', 'events', 'h_dimumass', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_corrdimumass, 'h_corrdimumass', samples, '', 'corr. m_{#mu#mu} [GeV]', 'events', 'h_corrdimumas', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_corrdimumass_2d, 'h_corrdimumass_2d', samples, '', 'corr. m_{#mu#mu} 2d [GeV]', 'events', 'h_corrdimumas_2d', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_dimumass_l, 'h_dimumass_l', samples, '', 'm_{#mu#mu} [GeV]', 'events', 'h_dimumass_l', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_corrdimumass_l, 'h_corrdimumass_l', samples, '', 'corr. m_{#mu#mu} [GeV]', 'events', 'h_corrdimumass_l', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_corrdimumass_2d_l, 'h_corrdimumass_2d_l', samples, '', 'corr. m_{#mu#mu} 2d [GeV]', 'events', 'h_corrdimumass_2d_l', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_dimupt, 'h_dimupt', samples, '', 'dim p_{T} [GeV]', 'events', 'h_dimupt', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_proptime, 'h_proptime', samples, '', 'prop.time', 'events', 'h_proptime', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_proptime_l, 'h_proptime_l', samples, '', 'prop.time', 'events', 'h_proptime_l', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_mindxyMuons, 'h_mindxyMuons', samples, '', 'min dxy [cm]', 'events', 'h_mindxyMuons', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_mindxygenMuons, 'h_mindxygenMuons', samples, '', 'min dxy [cm]', 'events', 'h_mindxygenMuons', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_mindzMuons,  'h_mindzMuons',  samples, '', 'min dz [cm]',  'events', 'h_mindzMuons', outFolder, logy=True, norm=False)
makeSimple1DPlot(h_dRMuons,  'h_dRMuons',  samples, '', '#Delta R', 'events', 'h_dRMuons',  outFolder, logy=False, norm=False)
makeSimple1DPlot(h_cosalpha, 'h_cosalpha', samples, '', 'cos(#alpha)', 'events', 'h_cosalpha', outFolder, logy=False, norm=False)
makeSimple1DPlot(h_alpha,    'h_alpha',    samples, '', '#alpha', 'events', 'h_alpha',    outFolder, logy=False, norm=False)
makeSimple1DPlot(h_dphi,     'h_dphi',     samples, '', '$Delta #Phi', 'events', 'h_dphi',     outFolder, logy=False, norm=False)

# 2D histograms
makeSimple2DPlot(h_dxyVsptrel, 'h_dxyVsptrel', samples, 'dxy vs #Delta p_{T}(#mu,{LLP})', '#Delta p_{T}(#mu,{LLP}) [GeV]'.format(T="T", LLP= longlivedLatex), 'dxy[cm]', 'h_dxyVsptrel', outFolder)
makeSimple2DPlot(h_lxyVslz, 'h_lxyVslz', samples, 'Generated L_{xy}[cm] vs L_{z}[cm]', 'L_{z}[cm]', 'L_{xy}[cm]', 'h_LxyVsLz', outFolder)

# 1D Histograms Gen Level, differential plots.
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