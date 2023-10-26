import os

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-m", "--model", dest="model", help="specify model, supported values: Benchmark, HAHM, RPV, STOP, SLEPTON", required=True)
parser.add_argument("-n", "--nevents", dest="nevents", help="number of events, default is 100", required=False, default = 100)

options = parser.parse_args()

SUSY = "Configuration/GenProduction/python/ThirteenPointSixTeV/Fragments2022_RPV/"
BENCHMARK = "Configuration/GenProduction/python/ThirteenPointSixTeV/Fragments2022_Benchmark/"
HAHM = "Configuration/GenProduction/python/ThirteenPointSixTeV/Fragments2022_HAHM/"
STOP = "Configuration/GenProduction/python/ThirteenPointSixTeV/Fragments2022_Stop/"
SLEPTON = "Configuration/GenProduction/python/ThirteenPointSixTeV/Fragments2022_Slepton/"

samples = []

# Stop samples
if options.model == "STOP":
    samples.append(STOP + "StopToMuB-M_700_ctau_50mm_TuneCP5_13p6TeV_pythia8_cff.py" )
    samples.append(STOP + "StopToMuD-M_700_ctau_50mm_TuneCP5_13p6TeV_pythia8_cff.py" )

# Slepton samples
if options.model == "SLEPTON":
    samples.append(SLEPTON + "SMuonToMuGravitino-MSmuon_300_ctau_100mm_TuneCP5_13p6TeV_pythia8_cff.py" )

#RPV SUSY
if options.model == "RPV":
    #lifetimeGrid = [1, 10, 100, 1000, 10000]
    #lifetimeGrid = [1, 100, 10000]  # to be adjusted

    fragments = []
    fragments.append({"massSquark": 125, "massChi":  50, "ctauChi":[20, 200, 2000]})
    fragments.append({"massSquark": 125, "massChi": 100, "ctauChi":[35, 350, 3500]})

    fragments.append({"massSquark": 200, "massChi":  50, "ctauChi":[15, 150, 1500]})
    fragments.append({"massSquark": 200, "massChi": 175, "ctauChi":[40, 400, 4000]})

    fragments.append({"massSquark": 350, "massChi":  50, "ctauChi":[8, 80, 800]})
    fragments.append({"massSquark": 350, "massChi": 150, "ctauChi":[25, 250, 2500]})
    fragments.append({"massSquark": 350, "massChi": 325, "ctauChi":[45, 450, 4500]})

    fragments.append({"massSquark": 700, "massChi":  50, "ctauChi":[5, 50, 500]})
    fragments.append({"massSquark": 700, "massChi": 500, "ctauChi":[40, 400, 4000]})
    fragments.append({"massSquark": 700, "massChi": 675, "ctauChi":[50, 500, 5000]})

    fragments.append({"massSquark": 1150, "massChi":   50, "ctauChi":[3,  30, 300]})
    fragments.append({"massSquark": 1150, "massChi":  500, "ctauChi":[30, 300, 3000]})
    fragments.append({"massSquark": 1150, "massChi":  950, "ctauChi":[50, 500, 5000]})
    fragments.append({"massSquark": 1150, "massChi": 1125, "ctauChi":[60, 600, 6000]})

    fragments.append({"massSquark": 1600, "massChi":   50, "ctauChi":[2, 20, 200]})
    fragments.append({"massSquark": 1600, "massChi":  500, "ctauChi":[20, 200, 2000]})
    fragments.append({"massSquark": 1600, "massChi":  950, "ctauChi":[40, 400, 4000]})
    fragments.append({"massSquark": 1600, "massChi": 1400, "ctauChi":[60, 600, 6000]})
    fragments.append({"massSquark": 1600, "massChi": 1575, "ctauChi":[70, 700, 7000]})

    for fragment in fragments:
        massSquark = fragment["massSquark"]
        massChi = fragment["massChi"]
        ctauChi = fragment["ctauChi"]
        for kLifetime in ctauChi:
            samples.append(SUSY +  "SquarkToNeutralinoTo2LNu-MSquark_{MASSSQUARK}_MChi_{MASSCHI}_ctau_{CTAUCHI}mm_TuneCP5_13p6TeV_pythia8_cff.py".format(MASSSQUARK=massSquark, MASSCHI=massChi, CTAUCHI=kLifetime))
        
#Benchmark samples
if options.model == "BENCHMARK":
    samples.append(BENCHMARK + "HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8_cff.py" )
    samples.append(BENCHMARK + "HTo2LongLivedTo2mu2jets_MH-125_MFF-50_CTau-500mm_TuneCP5_13p6TeV_pythia8_cff.py" )

#HAHM (needs gridpacks)
if options.model == "HAHM":
    #HAHM samples
    samples.append(HAHM + "HTo2ZdTo2mu2x_MZd-20_Epsilon-1e-08_TuneCP5_13p6TeV_pythia8_cff.py" )
    samples.append(HAHM + "HTo2ZdTo2mu2x_MZd-20_Epsilon-2e-07_TuneCP5_13p6TeV_pythia8_cff.py" )
    samples.append(HAHM + "HTo2ZdTo2mu2x_MZd-20_Epsilon-5e-07_TuneCP5_13p6TeV_pythia8_cff.py" )
    samples.append(HAHM + "HTo2ZdTo2mu2x_MZd-20_Epsilon-5e-08_TuneCP5_13p6TeV_pythia8_cff.py" )
    samples.append(HAHM + "HTo2ZdTo2mu2x_MZd-30_Epsilon-7e-09_TuneCP5_13p6TeV_pythia8_cff.py" )

outfolder = ""
for kSample in samples:
    pythia_fragment = kSample
    kSample_short = kSample.split("/")[-1]
    gen_fragment = kSample_short.replace("_cff.py", "_1_cfg_GS.py")
    out_file = outfolder + kSample_short.replace("_cff.py", "_GS.root")

    if options.model == "HAHM":
        #HAHM needs LHE file and uses gridpack
        command = "cmsDriver.py {PYTHIA_FRAGMENT} --python_filename {GEN_FRAGMENT} --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --fileout file:{OUT_FILE} --conditions 124X_mcRun3_2022_realistic_v10 --beamspot Realistic25ns13p6TeVEarly2022Collision --step LHE,GEN,SIM --geometry DB:Extended --era Run3 --mc -n {NEVENTS} --no_exec".format(PYTHIA_FRAGMENT=pythia_fragment, GEN_FRAGMENT=gen_fragment, OUT_FILE=out_file, NEVENTS=options.nevents)
    else:
        command = "cmsDriver.py {PYTHIA_FRAGMENT} --python_filename {GEN_FRAGMENT} --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:{OUT_FILE} --conditions 124X_mcRun3_2022_realistic_v10 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --mc -n {NEVENTS} --no_exec".format(PYTHIA_FRAGMENT=pythia_fragment, GEN_FRAGMENT=gen_fragment, OUT_FILE=out_file, NEVENTS=options.nevents)

    os.system(command)
