from os import system as bash
import argparse
'''
script to test SimpleGenTriggerSim_RPVvsBenchmark.py for different signal models
'''
parser = argparse.ArgumentParser(description="runs locally SimpleGenTriggerSim_RPVvsBenchmark.py with a set of given samples (from different models)")
parser.add_argument('--batch'      , dest='BATCH'      , default=False        , action = 'store_true', help='run test in batch')
args = parser.parse_args()

def runSample(sample, label, model):
    command = "python3 SimpleGenTriggerSim_RPVvsBenchmark.py --inputFile {SAMPLE} --trigger all --label {LABEL} --color 1 --triggerlabel SIM --model {MODEL} --nevents 1000 --outFolder /nfs/cms/escalante/plots/sandbox/ "
    command = command.format(SAMPLE = sample, LABEL = label, MODEL = model)
    
    # create submission script
    if args.BATCH == True:
        bash("echo {COMMAND} > test.sh".format(COMMAND = command))
        bash("cat  test.sh")
    else:
        bash(command)


pnfs = "/pnfs/ciemat.es/data/cms/store/user/escalant/{FOLDER}"

runSample(pnfs.format(FOLDER = "StopToMuB-M_700_ctau_50mm_TuneCP5_13p6TeV_pythia8/crab_StopToMuB-M_700_ctau_50mm_TuneCP5_13p6TeV_pythia8_GS-October2023_ToDelete/231026_133157/0000/"), "test_StopToMuB", "STOP")
runSample(pnfs.format(FOLDER = "StopToMuD-M_700_ctau_50mm_TuneCP5_13p6TeV_pythia8/crab_StopToMuD-M_700_ctau_50mm_TuneCP5_13p6TeV_pythia8_GS-October2023_ToDelete/231026_133209/0000/"), "test_StopToMuD", "STOP")
runSample(pnfs.format(FOLDER = "SMuonToMuGravitino-MSmuon_300_ctau_100mm_TuneCP5_13p6TeV_pythia8/crab_SMuonToMuGravitino-MSmuon_300_ctau_100mm_TuneCP5_13p6TeV_pythia8_GS-October2023_ToDelete/231026_133146/0000/"), "test_SMuon", "SMUON")
runSample(pnfs.format(FOLDER = "HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8/crab_HTo2LongLivedTo2mu2jets_MH-125_MFF-20_CTau-130mm_TuneCP5_13p6TeV_pythia8_GS-October2023_ToDelete/231017_102029/0000/"), "test_2mu2jets", "BENCHMARK")