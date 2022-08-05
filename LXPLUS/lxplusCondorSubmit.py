#~ /usr/bin/env python

import subprocess
import os 
import argparse

parser = argparse.ArgumentParser(description="Handle to submit lxplus condor jobs, it request a plain file with all the scripts to run.")

#modes                                                                                                                                                                                                                                                                                                                                                                                                                      
parser.add_argument('--flavour'    , dest='FLAVOUR'   , default='longlunch'     , help='which condor job flavour to use')
parser.add_argument('--inputFile'  , dest='INPUTFILE' , default='master_jobs.sh',  help='input file (with scripts to run on)')
parser.add_argument('--use-proxy'  , dest='PROXY'     , action='store_true'     , help='whether to ship the GRID certificate with the jobs')

args = parser.parse_args()
print ("running on jobs in {INPUTFILE}".format(INPUTFILE=args.INPUTFILE) )

# set some global variables needed for submission scripts
CMSSW_BASE   = os.environ['CMSSW_BASE']
SCRAM_ARCH   = os.environ['SCRAM_ARCH']
USER         = os.environ['USER']
HOME         = os.environ['HOME']
PWD          = os.environ['PWD']

# Various literal submission scripts with formatting placeholders for use in submission loops below
# Some format specifiers are global; otherwise ARGS will be set during the loop + format
condorExecutable = '''
#!/bin/bash
export SCRAM_ARCH={SCRAM_ARCH}
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd {CMSSW_BASE}/src/
eval `scramv1 runtime -sh`
cd {PWD}
$@
'''

condorSubmit = '''
universe               = vanilla
executable             = condorExecutable.sh
getenv                 = True
'''

condorSubmitAdd = '''
output                 = logs/run{runNum}/{logname}_{index}.out
log                    = logs/run{runNum}/{logname}_{index}.log
error                  = logs/run{runNum}/{logname}_{index}.err
arguments              = {ARGS}
{proxy_literal}
should_transfer_files  = NO
+JobFlavour            = "{flavour}"
queue 1
'''

# get rid of empty lines in the condor scripts
# if condorExecutable starts with a blank line, it won't run at all!!
# the other blank lines are just for sanity, at this point
def stripEmptyLines(string):
    if string[0] == '\n':
        string = string[1:]
    return string
condorExecutable = stripEmptyLines(condorExecutable)
condorSubmit     = stripEmptyLines(condorSubmit    )
condorSubmitAdd  = stripEmptyLines(condorSubmitAdd )


if args.PROXY == True:
    # prepare the grid certificate
    proxy = '{HOME}/private/.proxy'.format(**locals())
    if not os.path.isfile(proxy) or int(subprocess.check_output('echo $(expr $(date +%s) - $(date +%s -r {}))'.format(
           proxy), shell=True)) > 6*3600:
        print('GRID certificate not found or older than 6 hours. You will need a new one.')
        subprocess.call('voms-proxy-init --voms cms --valid 168:00 -out {}'.format(proxy), shell=True)
        
    # export the environment variable related to the certificate
    os.environ['X509_USER_PROXY'] = proxy
    
    PROXY_LITERAL = 'x509userproxy = $ENV(X509_USER_PROXY)\nuse_x509userproxy = true'
else: 
     PROXY_LITERAL = '#'

# make the logs directory if it doesn't exist
subprocess.call('mkdir -p logs', shell=True)
executableName = 'condorExecutable.sh'
open(executableName, 'w').write(condorExecutable.format(**locals()))

# get the number of run* directories, and make the next one
try:
    numberOfExistingRuns = int(subprocess.check_output('ls -d logs/run* 2>/dev/null | wc -l', shell=True).strip('\n'))
except subprocess.CalledProcessError:
    numberOfExistingRuns = 0
runNum = numberOfExistingRuns+1
subprocess.call('mkdir logs/run{}'.format(runNum), shell=True)

# make the submit file
#work is needed
    
submitName = 'condorSubmit'
f = open(args.INPUTFILE, 'r')
lines = f.readlines()
for index, line in enumerate(lines):
    line = line.strip()
    print (line)
    condorSubmit += condorSubmitAdd.format(
        runNum        = runNum,
        #logname       = line.split(".")[-1] if line != '' else 'dummy',
        logname       = "dummy_job",
        index         = index,
        ARGS          = line,
        flavour       = args.FLAVOUR,
        proxy_literal = PROXY_LITERAL
    )

print ("logs in logs/run{runNum}".format(runNum=runNum))

#runNum        = runNum,
#logname       = SCRIPT.replace('.py', '') if SCRIPT != '' else 'dummy',
#index         = index,
#ARGS          = SCRIPT + ' ' + ARGS,

#write file and submit.
open(submitName, 'w').write(condorSubmit)
subprocess.call('chmod +x '+executableName                                 , shell=True)
subprocess.call('condor_submit '+submitName                                , shell=True)
subprocess.call('cp '+executableName+' '+submitName+' logs/run'+str(runNum), shell=True)
#subprocess.call('rm '+submitName                                           , shell=True)
