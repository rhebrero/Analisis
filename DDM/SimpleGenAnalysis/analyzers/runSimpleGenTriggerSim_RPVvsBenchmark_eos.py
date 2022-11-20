import os
import argparse
from SimpleTools import getSuffix

parser = argparse.ArgumentParser(description="creates submission scripts.")

parser.add_argument('--recent'    , dest='RECENT'   , action='store_true'     , default=False, help = 'submission script contains "recent" jobs')
parser.add_argument('--all'       , dest='ALL'      , action='store_true'     , default=False, help = 'submission script contains "all" jobs')
parser.add_argument('--nevents'   , dest='NEVENTS'  , default=-1              , help = 'number of processed events')
options = parser.parse_args()

jobs = []
f = open("jobs.sh", "w")
scriptName = "SimpleGenTriggerSim_RPVvsBenchmark.py"
nevents = options.NEVENTS
    
def appendScript(jobs, squark, chi, ctau, version, model, nevents):
    '''
    appends a job defined in command variable to a dictionary
    '''

    command = ""
    if model == "RPV":
        inputFileTemplate = "/eos/vbc/experiments/cms/store/user/escalant/SquarkToNeutralinoTo2LNu-MSquark_{MASS_SQUARK}_MChi_{MASS_CHI}_ctau_{CTAU}mm_TuneCP5_13p6TeV_pythia8/crab_SquarkToNeutralinoTo2LNu-MSquark_{MASS_SQUARK}_MChi_{MASS_CHI}_ctau_{CTAU}mm_TuneCP5_13p6TeV_pythia8_{VERSION}/"
        labelTemplate = "MSquark_{MASS_SQUARK}_MChi_{MASS_CHI}_ctau_{CTAU}mm"
        outFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"
        
        inputFile = inputFileTemplate.format(MASS_SQUARK = squark, MASS_CHI = chi, CTAU = ctau, VERSION = version)
        label = labelTemplate.format(MASS_SQUARK = squark, MASS_CHI = chi, CTAU = ctau)
        
    if model == "Benchmark":
        inputFileTemplate = "/eos/vbc/experiments/cms/store/user/escalant/HTo2LongLivedTo2mu2jets_MH-{MASS_SQUARK}_MFF-{MASS_CHI}_CTau-{CTAU}mm_TuneCP5_13p6TeV_pythia8/crab_HTo2LongLivedTo2mu2jets_MH-{MASS_SQUARK}_MFF-{MASS_CHI}_CTau-{CTAU}mm_TuneCP5_13p6TeV_pythia8_{VERSION}/"
        labelTemplate = "MH-{MASS_SQUARK}_MFF-{MASS_CHI}_CTau-{CTAU}mm"
        outFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"

        inputFile = inputFileTemplate.format(MASS_SQUARK = squark, MASS_CHI = chi, CTAU = ctau, VERSION = version)
        label = labelTemplate.format(MASS_SQUARK = squark, MASS_CHI = chi, CTAU = ctau)
        
    if model == "HAHM":
        inputFileTemplate = "/eos/vbc/experiments/cms/store/user/escalant/HTo2ZdTo2mu2x_MZd-{MASS_CHI}_Epsilon-{CTAU}_TuneCP5_13p6TeV_pythia8/crab_HTo2ZdTo2mu2x_MZd-{MASS_CHI}_Epsilon-{CTAU}_TuneCP5_13p6TeV_pythia8_{VERSION}/"
        labelTemplate = "MZd_{MASS_CHI}_Epsilon-{CTAU}"
        outFolder = "/users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/"
        
        inputFile = inputFileTemplate.format(MASS_CHI = chi, CTAU = ctau, VERSION = version)
        label = labelTemplate.format(MASS_CHI = chi, CTAU = ctau)
        
    inputFile = inputFile + getSuffix(inputFile)
    command = "python3 {SCRIPTNAME} --inputFile {INPUTFILETEMPLATE} --process RPV --trigger all --label {LABELTEMPLATE} --color 1 --triggerlabel SIM --outFolder {OUTFOLDER} --nevents {NEVENTS} \n".format(SCRIPTNAME = scriptName, INPUTFILETEMPLATE = inputFile, LABELTEMPLATE = label, OUTFOLDER = outFolder, NEVENTS = nevents)
        
    if len(command) > 0:
        jobs.append(command)
    else:
        print("ERROR: appendScript did not find a good job")
        exit()

    return jobs 


if options.RECENT == True or options.ALL == True:
    ## High priority task ##
    for lifetime in [1, 100, 10000]:
        appendScript(jobs, 120,  48,  lifetime, "GS-14_11", "RPV", nevents)
        appendScript(jobs, 200,  48,  lifetime, "GS-14_11", "RPV", nevents)
        appendScript(jobs, 110, 100,  lifetime, "GS-14_11", "RPV", nevents)
        appendScript(jobs, 220, 200,  lifetime, "GS-14_11", "RPV", nevents)
        appendScript(jobs, 330, 300,  lifetime, "GS-14_11", "RPV", nevents)
        appendScript(jobs, 440, 400,  lifetime, "GS-14_11", "RPV", nevents)
        appendScript(jobs, 550, 500,  lifetime, "GS-14_11", "RPV", nevents)

    appendScript(jobs, 125,  50,  500, "GS-November2022_500", "Benchmark", nevents)
    appendScript(jobs, 125,  20,  130, "GS-November2022_500", "Benchmark", nevents)

    appendScript(jobs, 125,  30,  7e-09, "GS-hahm_16_11", "HAHM", nevents)

    appendScript(jobs, 125,  20,  2e-07, "GS-hahm_16_11", "HAHM", nevents)
    appendScript(jobs, 125,  20,  5e-07, "GS-hahm_16_11", "HAHM", nevents)
    appendScript(jobs, 125,  20,  1e-08, "GS-hahm_16_11", "HAHM", nevents)
    appendScript(jobs, 125,  20,  5e-08, "GS-hahm_16_11", "HAHM", nevents)
    
if options.ALL == True:
    ## Already processed scripts ##
    appendScript(jobs,  350,  148,  100, "GS-November2022_500", "RPV", nevents)
    appendScript(jobs, 1000,  148,  100, "GS-November2022_50",  "RPV", nevents)
    appendScript(jobs, 1500,  494,  100, "GS-November2022_50",  "RPV", nevents)
    
    appendScript(jobs, 125,  50,  500, "GS-November2022_500",  "Benchmark", nevents)

for kjob in jobs:
    print(kjob)
    f.write(kjob)

print("jobs.sh written, happy submission")
f.close()

## to be ported... if needed...

## triggered (needs GEN SIM sample)
#python3 SimpleGenTriggerSim_RPVvsBenchmark.py --inputFile /eos/vbc/experiments/cms/store/user/escalant/SquarkToNeutralinoTo2LNu-MSquark_350_MChi_148_ctau_100mm_TuneCP5_13p6TeV_pythia8/crab_SquarkToNeutralinoTo2LNu-MSquark_350_MChi_148_ctau_100mm_TuneCP5_13p6TeV_pythia8_GS-November2022_500/221030_190707/0000/ --process RPV --trigger HLT_DoubleL2Mu23NoVtx_2Cha_v3,HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v3,HLT_DoubleL3Mu10NoVtx_Displaced_v1,HLT_DoubleL3Mu10NoVtx_CosmicSeed_Displaced_v1,HLT_DoubleL2Mu10NoVtx_2Cha_PromptL3Mu0Veto_Iter3_v1,HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_PromptL3Mu0Veto_v1 --label MSquark_350_MChi_148_ctau_100mm --color 1 --triggerlabel SIM --outFolder /users/alberto.escalante/private/Github/work/DDM/SimpleGenAnalysis/analyzers/plots_SimpleGenTriggerSim_RPVvsBenchmark/trigger/ --nevents -1
