from os import system as bash
import subprocess
import argparse

parser = argparse.ArgumentParser(description="Tool for running trigger efficiencies")
parser.add_argument('--trigger'      , dest='TRIGGER'       , default=''     , help='trigger label')
parser.add_argument('--label'        , dest='LABEL'         , default=''     , help='label')
parser.add_argument('--color'        , dest='COLOR'         , default=''     , help='color')
args = parser.parse_args()


def parseFiles(inputFile):
    #this function is needed to convert a list into
    #long string of files, comma separated, to be 
    #processed in a CLI.

    stringFiles = ""
    for inputFile in inputFile:
        if len(stringFiles) == 0: 
            stringFiles = inputFile
        else:
            stringFiles = stringFiles + "," + inputFile
    return stringFiles

#inputFiles    = "/afs/cern.ch/work/e/escalant/private/Displaced2021/Trigger_V2/CMSSW_12_3_0_pre5/src/test/logs_debug_V14/root/output_Trigger_v14_all.root" #test with local file instead of a folder
#access files from lxplus stored in Vienna. 
#gfal-ls gsiftp://se.grid.vbc.ac.at:2811//eos/vbc/experiments/cms/store/user/escalant/HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-1mm_TuneCP5_13TeV_pythia8/crab_DR_HLT_V14_HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-1mm_TuneCP5_13TeV_pythia8/220325_191907/0000/

#add files to process

myeos = "/eos/vbc/experiments/cms/store/user/escalant/"

samples = []
samples.append({"mass":["20"], "lifetimes":["0p1","1", "13", "130", "1300", "13000"] })
samples.append({"mass":["50"], "lifetimes":["0p5","5", "50", "500", "5000", "50000"] })
#samples.append({"mass":["50"], "lifetimes":["0p5","5", "50", "50000"] })
#samples.append({"mass":["20"], "lifetimes":["1", "13", "130", "1300", "13000"] })
#samples.append({"mass":["50"], "lifetimes":["5", "50", "500", "5000", "50000"] })
#samples.append({"mass":["20"], "lifetimes":["1", "13000"] })
##samples.append({"mass":["50"], "lifetimes":["50000"] })

inputFiles    = [] 
for sample in samples:
    for mass in sample["mass"]:
        for lifetime in sample["lifetimes"]:
            #get the identifier
            label = myeos + "HTo2LongLivedTo2mu2jets_MH-125_MFF-{MASS}_CTau-{LIFETIME}mm_TuneCP5_13TeV_pythia8/crab_DR_HLT_V14_HTo2LongLivedTo2mu2jets_MH-125_MFF-{MASS}_CTau-{LIFETIME}mm_TuneCP5_13TeV_pythia8/".format(MASS=mass, LIFETIME=lifetime)
            #get label
            idx_command = 'gfal-ls gsiftp://se.grid.vbc.ac.at:2811{LABEL}'.format(LABEL=label)
            if len(idx_command)>0:
                idx   = subprocess.getoutput(idx_command)

                if ("Error" or "error" or "No" or "no" or "gfal-ls") in idx: 
                    print(" ERROR: lifetime {MASS} GeV, {LIFETIME} mm directory not found, SKIP sample".format(MASS=mass, LIFETIME=lifetime))
                    continue

                label = label + "/" + idx + "/0000/"            
                inputFiles.append(label.replace("//", "/"))

#print(inputFiles)

#local files
#inputFiles.append("/afs/cern.ch/work/e/escalant/private/Displaced2021/Trigger_V2/CMSSW_12_3_0_pre5/src/test/logs_debug_V14/root/output_Trigger_v14_all.root")

inputFiles = parseFiles(inputFiles)

outFolder    = "/eos/user/e/escalant/lxplus/displaced2022/plotsTriggerV6/"
process      = "125_XX"
triggerLabel = "HLTX"
triggerFlags = {"trigger":[], "label":[], "color":[]}

def addTrigger (triggerFlags, trigger, label, color):
    triggerFlags["trigger"].append(trigger)
    triggerFlags["label"].append(label)
    triggerFlags["color"].append(color)
    return triggerFlags

#Available triggers
#--path 
#HLT_L1Seeds_v3,HLT_L1Seeds_cpt_v3,HLT_L1Seeds_upt_v3,
#HLT_DoubleL2Mu23NoVtx_2Cha_v3,HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v3,
#HLT_DoubleL3Mu10NoVtx_Displaced_v1,HLT_DoubleL3Mu10NoVtx_CosmicSeed_Displaced_v1,
#HLT_DoubleL2Mu10NoVtx_2Cha_PromptL3Mu0Veto_Iter3_v1,HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_PromptL3Mu0Veto_v1

#triggerFlags = addTrigger(triggerFlags, "HLT_L1Seeds_sct_v3", "L1sct", 13 ) # TO DEBUG
    
triggerFlags = addTrigger(triggerFlags, args.TRIGGER, args.LABEL, args.COLOR ) #keyword for any trigger

#triggerFlags = addTrigger(triggerFlags, "all", "ALL", 1 ) #keyword for any trigger
#triggerFlags = addTrigger(triggerFlags, "HLT_L1Seeds_v3", "L1", 14 )
#triggerFlags = addTrigger(triggerFlags, "HLT_L1Seeds_cpt_v3", "L1cpt", 11 )
#triggerFlags = addTrigger(triggerFlags, "HLT_L1Seeds_upt_v3", "L1upt", 12 )
#triggerFlags = addTrigger(triggerFlags, "HLT_DoubleL2Mu23NoVtx_2Cha_v3,HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v3", "L2", 2)
#triggerFlags = addTrigger(triggerFlags, "HLT_DoubleL2Mu10NoVtx_2Cha_PromptL3Mu0Veto_Iter3_v1,HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_PromptL3Mu0Veto_v1", "L2VetoPrompt", 4)
#triggerFlags = addTrigger(triggerFlags, "HLT_DoubleL3Mu10NoVtx_Displaced_v1,HLT_DoubleL3Mu10NoVtx_CosmicSeed_Displaced_v1", "L3", 8)
#triggerFlags = addTrigger(triggerFlags, "HLT_DoubleL2Mu23NoVtx_2Cha_v3,HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v3,HLT_DoubleL3Mu10NoVtx_Displaced_v1,HLT_DoubleL3Mu10NoVtx_CosmicSeed_Displaced_v1,HLT_DoubleL2Mu10NoVtx_2Cha_PromptL3Mu0Veto_Iter3_v1,HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_PromptL3Mu0Veto_v1", "HLT", 28)

for trigger, label, color in zip(triggerFlags["trigger"], triggerFlags["label"], triggerFlags["color"]):
    command = "python3 SimpleGenTriggerSim.py --inputFile {INPUTFILES} --process {PROCESS} --trigger {TRIGGER} --label {LABEL} --color {COLOR} --outFolder {OUTFOLDER} --triggerlabel {TRIGGERLABEL}".format(INPUTFILES=inputFiles, PROCESS=process, TRIGGER=trigger, LABEL=label, COLOR=str(color), OUTFOLDER=outFolder, TRIGGERLABEL=triggerLabel) 
    print (command)
    bash(command)

