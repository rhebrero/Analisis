# simple script that copies the DDM ntuples from our /eos/ space at CERN (/eos/cms/store/group/phys_exotica/displacedMuons) and copies them to pnfs (/pnfs/ciemat.es/data/cms/store/user/escalant/displacedMuons)

# import needed packages
from os import system as bash

# input path in eos
source_path = '/eos/cms/store/group/phys_exotica/displacedMuons/'

# target path in pnfs
target_path = '/pnfs/ciemat.es/data/cms/store/user/escalant/displacedMuons/'

# directoies to copy
directories = ['NTuples', 'rNTuples']

# template commands
command_template = "rsync {OPTIONS} escalant@lxplus.cern.ch:{SOURCE_PATH}/{SAMPLE} {TARGET_PATH}/{SAMPLE}"

rsync_options = ""
# -r 
# getting rNtuples and hadding them
for directory in directories:
    if samples[key]["nfiles"] > 1:
        for index in range(1, samples[key]["nfiles"]+1 ):
            if "{INDEX}" in key: sample = key.format(INDEX=index)
            command = command_template.format(SAMPLE = sample, SOURCE_PATH = source_path, TARGET_PATH = target_path)
            print(command)
            if do_scp : bash(command)
        if  index == samples[key]["nfiles"]:
            #hadd samples
            hadd = hadd_template.format(OUTPUTFILE = key.replace("_{INDEX}", ""), INPUTFILES = key.replace("_{INDEX}", "_*"),
            TARGET_PATH = target_path)
            print(hadd)
            if do_hadd: bash(hadd)
    else:
        command = command_template.format(SOURCE_PATH = source_path, SAMPLE = key, TARGET_PATH = target_path)
        print(command)
        if do_scp: bash(command)
