import os

from argparse import ArgumentParser

parser = ArgumentParser()
#at the moment only GEN-SIM are supported
parser.add_argument("-f", "--fragmentsFolder", dest="fragmentsFolder", help="specify a folder containing the fragments to be submitted to crab", required=True)
parser.add_argument("-v", "--version",         dest="version", help="specify the version of the production (e.g  GS-March2022_v1)", required=True)
parser.add_argument("-p", "--publish",         dest="publish", help="specify if the sample needs to be published", required=False, action="store_true")
parser.add_argument("-s", "--unitsPerJob",     dest="unitsPerJob", help="units per job (split)", required=False,default=1000, type=int)
parser.add_argument("-n", "--totalUnits",      dest="totalUnits", help="total number of events", required=False,default=10000, type=int)
parser.add_argument("-c", "--crabTemplate",    dest="crabTemplate", help="specify the crab3 temoplate file", required=False, default="crab3_PrivateProd.py", type=str)
parser.add_argument("-d", "--debug",           dest="debug", help="only process first fragment and do not submit", required=False, action="store_true")
options = parser.parse_args()

fragments = os.listdir(options.fragmentsFolder)
if len(fragments) == 0:
    print("ERROR: No files found in ", options.fragmentsFolder)
    exit()

## loop over files in folder
for fragment in fragments:
    #basic cleanup
    fragment = fragment.strip()
    if len(fragment) == 0: continue
    if ".py" not in fragment:
        print("ERROR: ", fragment, "is not a valid fragment")
        exit()
    if "_cfg_" not in fragment and "_cff_" not in fragment:
        print("ERROR: ", fragment, "does not look like a valid fragment. Is the name sound?")
        exit()
    if "ythia" not in fragment:
        print("ERROR: ", fragment, "only tested with pythia fragments")
        exit()

    #configure arguments
    primaryDataset = fragment.split("ythia8")[0] + "ythia8" #this should remove the typical suffix after *ythia8 in the fragment name (e.g _1_cfg_GS.py)
    workArea = "crab_Private_"+options.version
    version = options.version
    crabTemplate = options.crabTemplate
    requestName = primaryDataset + "_" + version
    if len(requestName) > 100:
        requestName = requestName[:100]
        print("WARNING: requestName had to be shortened to", requestName)
        
    outputPrimaryDataset = primaryDataset 
    unitsPerJob = options.unitsPerJob
    totalUnits = options.totalUnits

    #format fragment filename
    fragment = options.fragmentsFolder +"/"+fragment
    fragment = fragment.replace("//", "/")

    command = "crab submit -c {CRABTEMPLATE} General.requestName={REQUESTNAME} General.workArea={WORKAREA} JobType.psetName={FRAGMENT} Data.outputPrimaryDataset={OUTPUTPRIMARYDATASET} Data.unitsPerJob={UNITSPERJOB} Data.totalUnits={TOTALUNITS}".format(
        CRABTEMPLATE = crabTemplate,
        REQUESTNAME = requestName,
        WORKAREA = workArea,
        FRAGMENT = fragment,
        OUTPUTPRIMARYDATASET = outputPrimaryDataset,
        UNITSPERJOB = unitsPerJob,
        TOTALUNITS = totalUnits         
    )

    if options.publish == True:
        command = command + "Data.publication=True Data.outputDatasetTag={VERSION}".format(VERSION=version)

    print (command)
    if options.debug == True:
        print("\n")
        print("DEBUG: only process the first fragment, no jobs have been submited")
        print("DEBUG: as a reminder, at clip submission only workds in login node")
        print("DEBUG: double check outputPrimaryDataset?", outputPrimaryDataset)
        print("DEBUG: double check requestName", requestName)
    else:
        os.system(command)

