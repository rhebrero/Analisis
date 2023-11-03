import os
import json

def get_xsec_pb(filename, mass):
    """
    Given a filename.json and the SUSY mass, return the "xsec_pb" field in [pb] from one of the json files in json/*
    matching the filename.
    """
    xsec_pb = None
    for file in os.listdir('json'):
        if file.endswith('.json') and file.startswith(filename):
            with open(os.path.join('json', file)) as f:
                data = json.load(f)
                xsec_pb = data['data'][str(mass)]['xsec_pb']
    return xsec_pb

def get_weight(filename, mass, nevents, luminosity):
    """
    Given a signal model determined by the json filename and the mass, it returns the corresponding weight given a number of
    generated events and an integrated luminosity in pb
    """
    weight = 0 
    xsec_pb = get_xsec_pb(filename, mass)
    weight = luminosity * xsec_pb /nevents  # corresponding weight for the given signal model
    return weight

if __name__ == "__main__":
    # testing the function
    mass = 500
    nevents = 20000
    filename = "pp13_snuM-slep_NLO+NLL_PDF4LHC.json"
    xsec_pb = get_xsec_pb(filename, mass)
    luminosity = 64 # [fb^-1]
    luminosity = 64*1000 # [pb^-1]
    weight = get_weight(filename, mass, nevents, luminosity)
    print("Cross section for {filename} and {mass}: {xsec_pb} pb".format(**locals()))
    print("weight for nevents {nevents} and luminosity {luminosity}: {weight} ".format(**locals()))



