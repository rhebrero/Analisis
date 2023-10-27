from math import *
from RecoUtils import *
from myMathUtils import *
from ResolutionUtils import *

def getSignalPdgID(model):
    """
    List with all PDG IDs for Benchmark, HAHM, RPV, STOP, SMUON.
    """
    pdgID = {"mother":[], "mother_latex":[], "LLP":[], "LLP_latex":[], "otherBSM":[], "otherBSM_latex":[]}

    if model == "HAHM":
        pdgID["mother"].append(25) # SM h
        pdgID["LLP"].append(1023) # X
        pdgID["mother_latex"].append("h(125)") # SM h
        pdgID["LLP_latex"].append("Z_{D}") # X

    if model == "BENCHMARK":
        pdgID["mother"].append(35) # Phi
        pdgID["LLP"].append(6000113) # X
        pdgID["mother_latex"].append("H") # Phi
        pdgID["LLP_latex"].append("X") # X

    if model == "RPV":
        pdgID["mother"].append(1000001) # ~d_L
        pdgID["mother"].append(2000001) # ~d_R  
        pdgID["mother"].append(1000002) # ~u_L
        pdgID["mother"].append(2000002) # ~u_R
        pdgID["mother"].append(1000003) # ~s_L
        pdgID["mother"].append(2000003) # ~s_R
        pdgID["mother"].append(1000004) # ~c_L
        pdgID["mother"].append(2000004) # ~c_R
        pdgID["mother"].append(1000005) # ~b_1
        pdgID["mother"].append(2000005) # ~b_2
        pdgID["mother"].append(1000006) # ~t_1
        pdgID["mother_latex"].append("#tilde{q}") # ~t_1

        pdgID["LLP"].append(1000022) # ~chi_10
        pdgID["LLP_latex"].append("\chi") # ~chi_10

    if model == "SMUON":
        #to be improved mothers for SMUON
        pdgID["mother"].append(1) # d
        pdgID["mother"].append(2) # u
        pdgID["mother"].append(3) # s
        pdgID["mother"].append(4) # c
        pdgID["mother"].append(5) # b
        pdgID["mother"].append(6) # t
        pdgID["mother_latex"].append("q") 

        pdgID["LLP"].append(1000011) # ~selectron_L
        pdgID["LLP"].append(2000011) # ~selectron_R
        pdgID["LLP"].append(1000013) # ~muon_L
        pdgID["LLP"].append(2000013) # ~muon_R
        pdgID["LLP"].append(1000015) # ~stau_L
        pdgID["LLP"].append(2000015) # ~stau_R
        pdgID["LLP_latex"].append("#tilde{l}") # ~stau_R

        pdgID["otherBSM"].append(1000039) # Gravitino
        pdgID["otherBSM_latex"].append("#tilde{G}") # Gravitino

    return pdgID

def getMotherPdgID(p):
    pdgID = []

    return pdgID
    
def tellMeMore(p):
    print("pdgID: ", p.pdgId(), "mass:", round(p.mass(), 2), "pt:", round(p.pt(),2), "pz:", round(p.pz(),2), "hardProcess:", p.isHardProcess())
    ndaughters = len(p.daughterRefVector())
    if p.pdgId() != 21 and p.pdgId() != 2212:
        #skip gluons and protons
        print("  mother id : "+str(round(p.mother(0).pdgId(),2)), " mother mass: "+str(round(p.mother(0).mass(),2)), "ndaughters: " + str(ndaughters))
        

# Finds the last muons in a decay chain of a given list of muons.
def findFinalStateMuons(prunedParticles):
    fsmuons = []

    for mu in prunedParticles:
        muon = mu
        #print ("Last copy?", muon.isLastCopy())
        while (muon.isLastCopy() == False):
            for dau in muon.daughterRefVector():
                # Assume that there is always only one muon in the decay chain
                if dau.pdgId() == muon.pdgId():
                    muon = dau;
                    break;

        if muon.isLastCopy() == False:
            print ("+++ Final state muon is not found +++")
            break;
        else:
            fsmuons.append(muon)

    return fsmuons

def getDaughters(prunedParticles, mother = 35, daughther = 13):
    """
    Given a list of particles, returns the daughters of a given mother 
    """
    daughtersMother = []
    for p in prunedParticles:
        if abs(p.pdgId()) > 0 and abs(p.pdgId()) < 1000:
            if p.isHardProcess():
                if p.mother(0).pdgId() == mother:
                    if abs(p.pdgId()) == daughther:
                        daughtersMother.append(p)
                    

    #Returns a list with 0 - 2 muons(depending on the model/daughter/mother)
    return daughtersMother

def getMothers(prunedParticles, mother1 =-1, mother2=-1):
    mothers = []
    for p in prunedParticles:
        if abs(p.pdgId()) > 0 and abs(p.pdgId()) < 1000:
            if p.isHardProcess():
                tellMeMore(p)
                if p.pdgId() == mother1 or p.pdgId() == mother2:

                    #Check if mother is already in mothers.
                    isNewMother = True
                    for kCandidate in mothers:
                        if kCandidate.pdgId() == p.pdgId():
                            isNewMother = False

                    if isNewMother == True:
                        mothers.append(p)                                    
                    
    if len(mothers) == 1 or len(mothers) == 2:        
        return mothers
    else:
        print ("WTF!! \n")


def getMotherMass(prunedParticles, mother):
    mothers = getMothers(prunedParticles, mother)
    return mothers[0].mass()

def getMotherLorentzBoost(prunedParticles, mother):
    mothers = getMothers(prunedParticles, mother)
    
    E_Over_m = mothers[0].energy()/mothers[0].mass()
    gammaV2 = sqrt( mothers[0].pt()*mothers[0].pt()+mothers[0].pz()*mothers[0].pz()+mothers[0].mass()*mothers[0].mass() )/mothers[0].mass()
    
    #print "E_Over_m = "+str(E_Over_m)+"  ,  "+"gammaV2 "+str(gammaV2)
    return mothers[0].energy()/mothers[0].mass()

def getMotherEtaPhi(prunedParticles, mother):
    mothers = getMothers(prunedParticles, mother)
    return mothers[0].eta(), mothers[0].phi()
    
#    dau1 = daughtersMother[0]
#    dau2 = daughtersMother[1]
#    print dau1.phi(), dau2.phi()
#    print deltaPhi(dau1, dau2)
    #    print dau1.pt()*dau2.pt()
#    print cosh(dau1.eta()-dau2.eta())-cos(deltaPhi(dau1, dau2))
#    zMass2 = 2*dau1.pt()*dau2.pt()*(cosh(dau1.eta()-dau2.eta())-cos(deltaPhi(dau1, dau2)))
#    if sqrt(zMass2)<51:
#        print sqrt(zMass2)
#    return sqrt(zMass2)


#def getMotherMass(prunedParticles, mother1=35, mother2=36):
#    mother1Mass = []
#    mother2Mass = [] 
#    for p in :
#        if abs(p.pdgId()) > 0 and abs(p.pdgId()) < 1000:
#            if p.isHardProcess():
#                if p.mother(0).pdgId() == mother1:
#                    mother1Mass.append(p.mother(0).mass())
#                if p.mother(0).pdgId() == mother2:
#                    mother2Mass.append(p.mother(0).mass())
#
#    return mother1Mass, mother2Mass


def getMotherMomentum(prunedParticles, mother1=35, mother2=36):
    ptMother = []
    pzMother = [] 
    for p in prunedParticles:
        if abs(p.pdgId()) > 0 and abs(p.pdgId()) < 1000:
            if p.isHardProcess():
                if p.mother(0).pdgId() == mother1 or p.mother(0).pdgId() == mother2:
                    ptMother.append(p.mother(0).pt())
                    pzMother.append(p.mother(0).pz())
                    
    return ptMother, pzMother

def getGenDaughters(prunedParticles, mother1=35, mother2=36, daughter1=-1, daughter2=-1, Inclusive = False):
    daughters = []
    for p in prunedParticles:
        if abs(p.pdgId()) > 0 and abs(p.pdgId()) < 1000:
            if p.isHardProcess():

                if Inclusive == False:
                    if (abs(p.pdgId()) == daughter1 or abs(p.pdgId()) == daughter2) and abs(p.eta())<2.4:
                        daughters.append(p)

                if Inclusive == True:
                    if (abs(p.pdgId()) == daughter1 or abs(p.pdgId()) == daughter2):
                        daughters.append(p)

                    
    return daughters



def getDauDeltaR(prunedParticles, mother1=35, mother2=36):
    dauDeltaR = []
    dau1 = []
    dau2 = []

    for p in prunedParticles:
        if abs(p.pdgId()) > 0 and abs(p.pdgId()) < 1000:
            if p.isHardProcess():
                if p.mother(0).pdgId() == mother1 and p.mother(0).pt()< 50:
                    dau1.append(p)                    
                if p.mother(0).pdgId() == mother2 and p.mother(0).pt()< 50:
                    dau2.append(p)                    


    if len(dau1)>0:    
        dauDeltaR.append(deltaR(dau1[0], dau1[1]))

    if len(dau2)>0:
        dauDeltaR.append(deltaR(dau2[0], dau2[1]))
#    print dauDeltaR
    return dauDeltaR


def getDauLastCopy(prunedParticles, EtaRange = [0, 2.4],  PtRange=[5,1000], LxyRange=[0,1000], LzRange=[0,1000], DrRange = [0, 10] ):

    minDeltaRGenThreshold = 10
    minDeltaRMatchedThreshold = 0.20
    DauPdgId = 13
    
    dauLastCopies = [] 

    for p in prunedParticles:        
        if abs(p.pdgId()) != DauPdgId or p.isLastCopy()!= True:
            continue
        if abs(p.eta()) < EtaRange[0] or abs(p.eta()) > EtaRange[1]:
            continue
        if abs(p.pt()) < PtRange[0] or abs(p.pt())> PtRange[1]:            
            continue
        if abs(p.vertex().Rho()) < LxyRange[0] or abs(p.vertex().Rho()) > LxyRange[1]:            
            continue
        if abs(p.vertex().Z()) < LzRange[0] or abs(p.vertex().Z()) > LzRange[1]:            
            continue

        for k in prunedParticles:
            if k.pdgId() == -p.pdgId() and k.isLastCopy():
                if deltaR(p, k) < minDeltaRGenThreshold:
                    minDeltaRGenThreshold = deltaR(p, k)

        if minDeltaRGenThreshold < DrRange[0] or minDeltaRGenThreshold > DrRange[1]:
            continue

        dauLastCopies.append(p)

    return dauLastCopies


def motherParticle(p):
    return p.mother(0)

def getTrueMother(p):
    motherPdgId = p.pdgId()
    while p.mother(0).pdgId() == motherPdgId:
        p = motherParticle(p)
        motherPdgId = p.pdgId()
    return p.mother(0)
    

def getResolution(RecoMuon, prunedParticles, EtaRange = [0, 2.4],  PtRange=[5,1000], LxyRange=[0,1000], LzRange=[0,1000], DrRange = [0.5, 10], TrackType = 'STA'):
    minDeltaRGenThreshold = 10
    minDeltaRMatchedThreshold = 0.30
    DauPdgId = 13
    verbose = False

    resolutionParam = ResolutionParam()
    
    if verbose == True: print ('Looking for Gen Muon')
    if verbose == True: print((EtaRange, PtRange, LxyRange, LzRange, DrRange))
    if verbose == True: print((RecoMuon.pt(), RecoMuon.eta(), RecoMuon.phi()))

    pairReco = []
    pairGen = []
    
    for kRecoMuon in RecoMuon:
        matchedGenMu=[]
        if isTrackType(kRecoMuon, TrackType) == False:
            continue

        if TrackType == 'STA':
            RecoTrack = kRecoMuon.standAloneMuon()
        if TrackType == 'PFTrack':
            RecoTrack = kRecoMuon.muonBestTrack()
                        
        for p in prunedParticles:
            if abs(p.pdgId()) != DauPdgId or p.isLastCopy()!= True:
                continue
            if abs(p.eta()) < EtaRange[0] or abs(p.eta()) > EtaRange[1]:
                continue
            if abs(p.pt()) < PtRange[0] or abs(p.pt())> PtRange[1]:            
                continue
            if abs(p.vertex().Rho()) < LxyRange[0] or abs(p.vertex().Rho()) > LxyRange[1]:            
                continue
            if abs(p.vertex().Z()) < LzRange[0] or abs(p.vertex().Z()) > LzRange[1]:            
                continue
            if p.charge() != RecoTrack.charge():            
                continue
        
            for k in prunedParticles:
                if k.pdgId() == -p.pdgId() and k.isLastCopy():
                    if deltaR(p, k) < minDeltaRGenThreshold:
                        minDeltaRGenThreshold = deltaR(p, k)

            if verbose == True: print("Delta R "+str(minDeltaRGenThreshold))
            if minDeltaRGenThreshold < DrRange[0] or minDeltaRGenThreshold > DrRange[1]:
                continue

            if verbose == True: print("#PdgId : %s  status: %s  pt : %.4s  eta : %.4s   phi : %.4s  " %(p.pdgId(),p.status(),p.pt(),p.eta(),p.phi()))
            if verbose == True: print("    -> Delta R %f"%(deltaR(RecoTrack, p)))

            if deltaR(RecoTrack, p) <minDeltaRMatchedThreshold:
                minDeltaR = deltaR(RecoTrack, p)
                matchedGenMu.append(p)
                    

        if len(matchedGenMu) > 0:
            pairReco.append(RecoTrack)
            pairGen.append(matchedGenMu[-1])
                
    if verbose == True: print('found matched muons '+str(len(pairReco)))


    if len(pairGen)> 1:
#        print 'test ----- nmuons '+str(len(pairGen))
        for kIndex in range(0, len(pairGen)):
            for jIndex in range(kIndex, len(pairGen)):
                if verbose == True: print(kIndex, jIndex)
                if getTrueMother(pairGen[kIndex]).pdgId() == getTrueMother(pairGen[jIndex]).pdgId() and pairGen[kIndex].pdgId() !=  pairGen[jIndex].pdgId():
                    if verbose == True: print(kIndex, pairGen[kIndex].charge(), pairGen[kIndex].pdgId(), getTrueMother(pairGen[kIndex]).pdgId(), pairGen[kIndex].eta(), pairGen[kIndex].phi())
                    if verbose == True: print(jIndex, pairGen[jIndex].charge(), pairGen[jIndex].pdgId(), getTrueMother(pairGen[jIndex]).pdgId(), pairGen[jIndex].eta(), pairGen[jIndex].phi())

                    recoMass = sqrt( 2*pairReco[jIndex].pt()*pairReco[kIndex].pt()*(cosh(pairReco[jIndex].eta()-pairReco[kIndex].eta())-cos(deltaPhi(pairReco[jIndex], pairReco[kIndex]))))
                    recoDeltaR = deltaR(pairReco[jIndex], pairReco[kIndex])

                    if getTrueMother(pairGen[kIndex]).pdgId() == getTrueMother(pairGen[jIndex]).pdgId() == 35:
                        resolutionParam.matchedRecoMassMother1.append(recoMass)
                    if getTrueMother(pairGen[kIndex]).pdgId() == getTrueMother(pairGen[jIndex]).pdgId() == 36:                        
                        resolutionParam.matchedRecoMassMother2.append(recoMass)

                    genMass = getTrueMother(pairGen[kIndex]).mass()                                                            
                    resolutionParam.matchedMassResolution.append((recoMass-genMass)/genMass)

                    deltaPhiReco = deltaPhi(pairReco[jIndex],pairReco[kIndex])
                    deltaEtaReco = abs(pairReco[jIndex].eta()-pairReco[kIndex].eta())

                    deltaPhiGen = deltaPhi(pairGen[jIndex],pairGen[kIndex])
                    deltaEtaGen = abs(pairGen[jIndex].eta()-pairGen[kIndex].eta())

                    genDeltaR = deltaR(pairGen[jIndex], pairGen[kIndex])
                    if genDeltaR > 0.5:
                        resolutionParam.matchedDeltaPhiResolution.append(deltaPhiReco-deltaPhiGen)
                        resolutionParam.matchedDeltaEtaResolution.append(deltaEtaReco-deltaEtaGen)                        
                        resolutionParam.matchedDeltaRResolution.append(recoDeltaR-genDeltaR)

                    if recoDeltaR-genDeltaR < 0.2 and verbose == True:
                        print('-----------mother %s ---------' % pairGen[kIndex].pdgId())
                        print('RECO: pt1:%s pt2:%s eta1: %s, eta2: %s , phi1: %s, phi2: %s, mass: %s deltaR: %s '%  (pairReco[jIndex].pt(), pairReco[kIndex].pt(), pairReco[jIndex].eta(), pairReco[kIndex].eta(), pairReco[jIndex].phi(), pairReco[kIndex].phi(), recoMass, recoDeltaR))
                        print('GENE: pt1:%s pt2:%s eta1: %s, eta2: %s , phi1: %s, phi2: %s, mass: %s, deltaR: %s, lxy: %s, lz:%s '%  (pairGen[jIndex].pt(), pairGen[kIndex].pt(), pairGen[jIndex].eta(), pairGen[kIndex].eta(), pairGen[jIndex].phi(), pairGen[kIndex].phi(), genMass, genDeltaR, pairGen[kIndex].vertex().Rho(), pairGen[kIndex].vertex().Z()))
                        #print 'Global:    Deta-Rec: %s, DPhi-Rec: %s' %  (pairReco[jIndex].eta()-pairReco[kIndex].eta(), deltaPhi(pairReco[jIndex],pairReco[kIndex]) )
                        #print 'Global:    Deta-Rec: %s, DPhi-Rec: %s' %  (pairGen[jIndex].eta()-pairGen[kIndex].eta(), deltaPhi(pairGen[jIndex],pairGen[kIndex]) )
                        #print 'Global:    Diff: %s, Diff: %s' %  ( pairReco[jIndex].eta()-pairReco[kIndex].eta()-pairGen[jIndex].eta()+pairGen[kIndex].eta(), deltaPhi(pairGen[jIndex],pairGen[kIndex])- deltaPhi(pairReco[jIndex],pairReco[kIndex]) )
                        print('Global:    Deta-Rec: %s, DPhi-Rec: %s' %  (deltaEtaReco, deltaPhiReco ))
                        print('Global:    Deta-Rec: %s, DPhi-Rec: %s' %  (deltaEtaGen, deltaPhiGen ))
                        print('Global:    Diff: %s, Diff: %s DeltaR %s' %  ( deltaEtaReco-deltaEtaGen, deltaPhiReco-deltaPhiGen, recoDeltaR-genDeltaR))
                        
                    
                    
    for kMatchedReco, kMatchedGen in zip(pairReco, pairGen):
        if len(pairGen) >0:
            resolutionParam.matchedEtaResolution.append(kMatchedReco.eta()-kMatchedGen.eta())
            resolutionParam.matchedPhiResolution.append(kMatchedReco.phi()-kMatchedGen.phi())
            resolutionParam.matchedPtResolution.append((kMatchedReco.pt()-kMatchedGen.pt())/kMatchedGen.pt())
                
    return resolutionParam 


def getGenTrigger(min_pT, max_pT, min_dxy, max_eta, lxy, lz):
    """
    returns a flag corresponding to a trigger at gen level. 
    Triggers implemented correspond to 2022.
    """
    #print(min_pT, max_pT, min_dxy, max_eta, lxy, lz)
    triggerID = 0 #no trigger
    if lxy < 600 and lz < 500:
        if max_eta>2.0:
            triggerID = 2 #decays in CMS but outside eta acceptance
        else:
            if min_pT > 10 and max_pT > 16 and min_dxy > 0.01:
                triggerID = 5 #HLT_DoubleL3Mu16_10 MinDxy0p01cm
            if min_pT > 10 and min_dxy > 1:
                triggerID = 4 #HLT_DoubleL2Mu10 PromptVetoMinDxy1cm
            if min_pT > 23:
                triggerID = 3 #HLT_DoubleL2Mu23
    else:
        triggerID = 1 #decays outisde CMS

    return triggerID
