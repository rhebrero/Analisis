from math import *
from RecoUtils import *

def deltaPhi(a,b):
    '''
    computes delta phi for two given gen particles
    '''
    dphi = abs(a.phi()-b.phi())
    if dphi > pi: dphi = 2*pi-dphi
    return dphi

def deltaR(a,b):
    '''
    computes dR for two given gen particles
    '''
    dphi = deltaPhi(a,b)
    return hypot(a.eta()-b.eta(),dphi)

def mass(a, b):
    '''
    computes the invariant mass for two given gen particles
    '''
    mass2 = 2*a.pt()*b.pt()*( cosh(a.eta()-b.eta()) - cos(deltaPhi(a,b)))
    mass = sqrt(mass2)
    return mass
