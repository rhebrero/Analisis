from CRABClient.UserUtilities import config 
config = config()

config.section_("General")
config.General.requestName = 'GEN_SIM_931' #Modified - Anything
config.General.workArea = 'crab_Private_CMSSW_12_0_2_patch1' 

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'WprimeToMuNu_M_3000_TuneCUETP8M1_13TeV_pythia8_cfi_all_step.py' #Modified - Anything

config.section_("Data")
config.Data.outputPrimaryDataset = 'WprimeToMuNu_M_3000_TuneCUETP8M1_13TeV_pythia8' #Modified - Anything
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
#config.Data.unitsPerJob = 25

#config.Data.totalUnits = 200
config.Data.totalUnits = 10000
config.Data.publication = False
if config.Data.publication == True:     
    config.Data.outputDatasetTag = 'dataset_tag_name' #please follow naming conventions when publishing (if existing).

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
#config.Site.whitelist = ['T2_AT_Vienna'] (only for debugging purposes)
