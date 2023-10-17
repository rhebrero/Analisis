# simple script that copies the DDM ntuples from our /eos/ space at CERN (/eos/cms/store/group/phys_exotica/displacedMuons) and copies them to pnfs (/pnfs/ciemat.es/data/cms/store/user/escalant/displacedMuons)

# import needed packages
from os import system as bash
from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument("-d", "--debug", dest="debug", default = False, action = 'store_true', help="does a dry-run (with verbose logs)", required=False)
parser.add_argument("-f", "--folder", dest="folder", default = "", help="name of the folder you wish to sync (e.g 'NTuples', 'rNTuples')", required=False)
options = parser.parse_args()

# input path in eos
source_path = '/eos/cms/store/group/phys_exotica/displacedMuons/'

# target path in pnfs
target_path = '/pnfs/ciemat.es/data/cms/store/user/escalant/displacedMuons/'

# directoies to copy
directories = ['NTuples', 'rNTuples']

# template commands
command_template = "rsync {OPTIONS} escalant@lxplus.cern.ch:{SOURCE_PATH}{DIRECTORY} {TARGET_PATH}"

# common rsync options
# -r recursive 
# -a 'archive', it preserves symlinks, permisions etc...
# -z compresses the file while transferinbg
# -P allows you to resume the transfer and it shows a status bar
# -nv means verbose and debug, useful to check that rsync is doing the right stuff
# --delete removes directories from the destination folder if they do not match the original folder

if options.debug == True:
    rsync_options = "-azPnv"
else:
    rsync_options = "-azP"

# getting the directories and rsyncing them
for directory in directories:
    if len(options.folder) > 0 and options.folder != directory:
        # only rsync the selected folder
        continue
    command = command_template.format(OPTIONS = rsync_options, 
                                        SOURCE_PATH = source_path,
                                        DIRECTORY = directory,   
                                        TARGET_PATH = target_path)
    print(command)
    bash(command)
