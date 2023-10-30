import os
import argparse
import socket

from utils import getLibraries
from SimpleTools import getSuffix
from SamplesDatabase import samples_Benchmark, samples_HAHM, samples_RPV, samples_SMUON, samples_2022

parser = argparse.ArgumentParser(description="creates submission scripts.")

parser.add_argument('--nevents'   , dest='NEVENTS'     , default=-1           , help = 'number of processed events')
parser.add_argument('--folderEOS' , dest='FOLDER_EOS'  , default=''           , help = 'overrides eos folder where samples are stored')
parser.add_argument('--scriptname', dest='SCRIPTNAME'  , default='SimpleGenTriggerSim_RPVvsBenchmark.py'   , help = 'scriptName, default: SimpleGenTriggerSim_RPVvsBenchmark.py')
parser.add_argument('--jobsname'  , dest='JOBSNAMES'   , default='jobs.sh'    , help = 'jobs output filename, default: jobs.sh')

#RPV
parser.add_argument('--rpv'         , dest='RPV'      , action='store_true'     , default=False, help = 'run on RPV samples')
parser.add_argument('--massChi'     , dest='MASS_CHI' , default=-1              , help = 'chi mass')
parser.add_argument('--massSquark'  , dest='MASS_SQUARK' , default=-1           , help = 'squark mass')

#Benchmark
parser.add_argument('--benchmark' , dest='BENCHMARK', action='store_true'     , default=False, help = 'run on Benchmark samples')
parser.add_argument('--massH'     , dest='MASS_H' , default=-1                , help = 'H mass')
parser.add_argument('--massX'     , dest='MASS_X'   , default=-1              , help = 'X mass')

#Darkphoton
parser.add_argument('--hahm'      , dest='HAHM'    , action='store_true'      , default=False, help = 'run on HAHM')
parser.add_argument('--massZd'    , dest='MASS_ZD' , default=-1               , help = 'Dark photon mass')

#SMuon
parser.add_argument('--smuon'     , dest='SMUON'    , action='store_true'      , default=False, help = 'run on SMUON')
parser.add_argument('--massSmuon' , dest='MASS_SMUON'  , default=-1            , help = 'Smuon Mass')

#lifetimes
parser.add_argument('--lifetime'  , dest='LIFETIME' , default=-1               , help = 'lifetime point. Valid arguments: 0, 1, 2, and 3 (only for dark photon)')

#Data
parser.add_argument('--data'      , dest='DATA', action='store_true'            , default=False, help = 'run on data samples')
parser.add_argument('--era'       , dest='ERA' , default=-1                     , help = 'Data Taking Era (E.g MuonRun2022F)')

options = parser.parse_args()

scriptName = options.SCRIPTNAME

def configureHistograms(grid, ctau):
    '''
    configures the input file and label for the histograms
    '''

    if "vbc.at" in socket.gethostname():
        eosFolder = "/eos/vbc/experiments/cms/store/user/escalant/"
    elif "ciemat.es" in socket.gethostname():
        eosFolder = "/pnfs/ciemat.es/data/cms/store/user/escalant/"
    else:
        print("ERROR: eosFolder not configured")
        exit()
        
    #deafult samples
    if options.HAHM == True:          version = "GS-hahm_16_11"       # at CLIP
    if options.RPV == True:           version = "GS-27_11"            # at CLIP
    if options.BENCHMARK == True:     version = "GS-November2022_500" # at CLIP
    if options.SMUON == True:         version = "GS-October2023_ToDelete" # at CIEMAT

    if options.DATA == True:
        eosFolder = "/eos/vbc/experiments/cms/store/user/sonawane/"
        if grid["era"] == "MuonRun2022F":  version = "PromptReco-v1_012023-v01"
        
    if len(options.FOLDER_EOS) > 0:
        version = options.FOLDER_EOS
        print("Configured EOS samples: {FOLDER_EOS} \n".format(FOLDER_EOS=options.FOLDER_EOS))

    if options.RPV == True:
        inputFileTemplate = "{EOS_FOLDER}SquarkToNeutralinoTo2LNu-MSquark_{MASS_SQUARK}_MChi_{MASS_CHI}_ctau_{CTAU}mm_TuneCP5_13p6TeV_pythia8/crab_SquarkToNeutralinoTo2LNu-MSquark_{MASS_SQUARK}_MChi_{MASS_CHI}_ctau_{CTAU}mm_TuneCP5_13p6TeV_pythia8_{VERSION}/"
        labelTemplate = "MSquark_{MASS_SQUARK}_MChi_{MASS_CHI}_ctau_{CTAU}mm"
        
        inputFile = inputFileTemplate.format(EOS_FOLDER = eosFolder, MASS_SQUARK = grid['massSquark'], MASS_CHI = grid['massChi'], CTAU = ctau, VERSION = version)
        label = labelTemplate.format(MASS_SQUARK = grid['massSquark'], MASS_CHI = grid['massChi'], CTAU = ctau)
        
    if options.BENCHMARK == True:
        inputFileTemplate = "{EOS_FOLDER}HTo2LongLivedTo2mu2jets_MH-{MASS_H}_MFF-{MASS_X}_CTau-{CTAU}mm_TuneCP5_13p6TeV_pythia8/crab_HTo2LongLivedTo2mu2jets_MH-{MASS_H}_MFF-{MASS_X}_CTau-{CTAU}mm_TuneCP5_13p6TeV_pythia8_{VERSION}/"
        labelTemplate = "MH-{MASS_H}_MFF-{MASS_X}_CTau-{CTAU}mm"

        inputFile = inputFileTemplate.format(EOS_FOLDER = eosFolder, MASS_H = grid['massH'], MASS_X = grid['massX'], CTAU = ctau, VERSION = version)
        label = labelTemplate.format(MASS_H = grid['massH'], MASS_X = grid['massX'], CTAU = ctau)
        
    if options.HAHM == True:
        inputFileTemplate = "{EOS_FOLDER}/HTo2ZdTo2mu2x_MZd-{MASS_ZD}_Epsilon-{CTAU}_TuneCP5_13p6TeV_pythia8/crab_HTo2ZdTo2mu2x_MZd-{MASS_ZD}_Epsilon-{CTAU}_TuneCP5_13p6TeV_pythia8_{VERSION}/"
        labelTemplate = "MZd_{MASS_ZD}_Epsilon-{CTAU}"
        
        inputFile = inputFileTemplate.format(EOS_FOLDER = eosFolder, MASS_ZD = grid['massZd'], CTAU = ctau, VERSION = version)
        label = labelTemplate.format(MASS_ZD = grid['massZd'], CTAU = ctau)

    if options.SMUON == True:
        inputFileTemplate = "{EOS_FOLDER}/SMuonToMuGravitino-M_{MASS_SMUON}_ctau_{CTAU}mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-M_{MASS_SMUON}_ctau_{CTAU}mm_TuneCP5_13p6TeV_pythia8_{VERSION}/"
        labelTemplate = "MSMuon_{MASS_SMUON}_ctau-{CTAU}"
        
        inputFile = inputFileTemplate.format(EOS_FOLDER = eosFolder, MASS_SMUON = grid['massSMuon'], CTAU = ctau, VERSION = version)
        label = labelTemplate.format(MASS_SMUON = grid['massSMuon'], CTAU = ctau)

    if options.DATA == True:
        inputFileTemplate = "{EOS_FOLDER}Muon/PATFilter_{ERA}-{VERSION}/"
        labelTemplate = "{ERA}"
        
        inputFile = inputFileTemplate.format(EOS_FOLDER = eosFolder, ERA = grid['era'], VERSION = version)
        label = labelTemplate.format(ERA = grid['era'])

    if len(inputFile)*len(label) == 0:
        print("ERROR: Histograms have not been configured correctly")
        exit()
        
    return inputFile, label 

def appendScript(jobs, grid, ctau = []):
    '''
    appends a job defined in command variable to a dictionary
    '''
    inputFile, label = configureHistograms(grid, ctau)
    inputFile = inputFile + getSuffix(inputFile)
    outFolder = "/users/alberto.escalante/plots/plots_{SCRIPTNAME}/".format(SCRIPTNAME = options.SCRIPTNAME.replace(".py", ""))
    
    if "vbc.at" in socket.gethostname():
        outFolder = "/users/alberto.escalante/plots/plots_{SCRIPTNAME}/".format(SCRIPTNAME = options.SCRIPTNAME.replace(".py", ""))
    elif "ciemat.es" in socket.gethostname():
        outFolder = "/nfs/cms/escalante/plots/plots_{SCRIPTNAME}/".format(SCRIPTNAME = options.SCRIPTNAME.replace(".py", ""))
    else:
        print("ERROR: outFolder not configured")
        exit()

    # it could be implemented more nicely
    model = ""
    if options.RPV: model = "RPV"
    if options.HAHM: model = "HAHM"
    if options.BENCHMARK: model = "BENCHMARK"
    if options.SMUON: model = "SMUON"

    command = "python3 {SCRIPTNAME} --inputFile {INPUTFILETEMPLATE} --model {MODEL} --trigger all --label {LABELTEMPLATE} --color 1 --triggerlabel SIM --outFolder {OUTFOLDER} --nevents {NEVENTS} \n".format(SCRIPTNAME = options.SCRIPTNAME, INPUTFILETEMPLATE = inputFile, MODEL = model, LABELTEMPLATE = label, OUTFOLDER = outFolder, NEVENTS = options.NEVENTS)
    command.format(OUTFOLDER = outFolder)
    
    if len(command) > 0:
        jobs.append(command)
    else:
        print("ERROR: appendScript did not find a good job")
        exit()

    return jobs 

## creation of submission scripts ##

jobs = []
grid = {}

if options.RPV == True:
    for kSample in samples_RPV:
        grid['massSquark'] = kSample["massSquark"]
        grid['massChi'] = kSample["massChi"]
        grid['ctauChi'] = kSample["ctauChi"]

        if int(options.MASS_SQUARK) > 0 and  int(options.MASS_SQUARK) != int(grid['massSquark']): continue #select specific mass_squark
        if int(options.MASS_CHI) > 0 and int(options.MASS_CHI) != int(grid['massChi']): continue           #select specific mass_chi

        for index, kLifetime in enumerate(grid['ctauChi']):
            if int(options.LIFETIME) > 0 and int(options.LIFETIME) != kLifetime: continue                  #select specific lifetime
            appendScript(jobs, grid, ctau = kLifetime)

if options.BENCHMARK == True:
    for kSample in samples_Benchmark:
        grid['massH'] = kSample["massH"]
        grid['massX'] = kSample["massX"]
        grid['ctauX'] = kSample["ctauX"]

        if int(options.MASS_H) > 0 and int(options.MASS_H) != int(grid['massH']): continue #select specific mass_squark
        if int(options.MASS_X) > 0 and int(options.MASS_X) != int(grid['massX']): continue #select specific mass_chi

        for index, kLifetime in enumerate(grid['ctauX']):
            if int(options.LIFETIME) > 0 and int(options.LIFETIME) != kLifetime: continue  #select specific lifetime
            appendScript(jobs, grid, ctau = kLifetime)

if options.HAHM == True:
    for kSample in samples_HAHM:
        grid['massZd'] = kSample["DP"]
        grid['epsilon'] = kSample["EPSILON"]
        if int(options.MASS_ZD) > 0 and  int(options.MASS_ZD) != int(grid['massZd']): continue #select specific dark photon mass

        for index, kLifetime in enumerate(grid['epsilon']):
            if options.LIFETIME != kLifetime: continue #select specific lifetime
            appendScript(jobs, grid, ctau = kLifetime)

if options.SMUON == True:
    for kSample in samples_SMUON:
        grid['massSMuon'] = kSample["massSMuon"]
        grid['ctauSMuon'] = kSample["ctauSMuon"]
        print(grid['ctauSMuon'], grid['massSMuon'])
        if int(options.MASS_SMUON) > 0 and int(options.MASS_SMUON) != int(grid['massSMuon']): continue #select specific SMUON mass

        for index, kLifetime in enumerate(grid['ctauSMuon']):
            if options.LIFETIME != kLifetime and options.LIFETIME > 0: continue #select specific lifetime
            print(jobs, grid, kLifetime)
            appendScript(jobs, grid, ctau = kLifetime)

if options.DATA == True:
    for kSample in samples_2022:
        grid['era'] = kSample["era"]
        appendScript(jobs, grid)

# write all tasks saved in vector jobs in an a text file that can be submitted to the grid
if len(jobs) == 0:
    print("please specify a model type --rpv, --hahm, --Benchmark, --smuon, --data")
    exit()
else:
    f = open(options.JOBSNAMES, "w")
    for kjob in jobs:
        print(kjob)
        f.write(kjob)
    print("jobs.sh written, happy submission")
    f.close()

