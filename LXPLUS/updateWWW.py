import os
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-u", "--update", dest="update", default = "", help="updates a given folder in website", required=False)
parser.add_argument("-s", "--keys", dest="keys", action="store_true", help="show registered keys and notes", required=False)
options = parser.parse_args()

def addPlots(key, localFolder, remoteFolder, note = ""):
    '''
    registers a plots folder in the database
    '''
    plotDic = {}
    if len(key) == 0 or len(localFolder) == 0 or len(remoteFolder) == 0:
        print("folder is not properly registered")
        exit()

    plotDic = {"key": key, "localFolder": localFolder, "remoteFolder":remoteFolder, "note": note}
    return plotDic

def updatePlots(key, folders):
    '''
    updates the plots in the website given a foder
    '''
    command = ""
    for folder in folders:
        if folder["key"] == key:
            command = "rsync -rtvu {REMOTE_FOLDER} {LOCAL_FOLDER}".format(REMOTE_FOLDER = folder["remoteFolder"], LOCAL_FOLDER = folder["localFolder"])
            print(command)
            break
    if len(command) == 0:
        print("KEY NOT FOUND")
        exit()
    else:        
        os.system(command)


#Registed plots in website
folders = []
folders.append(addPlots("run3data", "/Users/escalante/cernbox/www/protected/ddm/run3data/Run3/", "alberto.escalante@clip-login-0.cbe.vbc.ac.at:/users/alberto.escalante/plots/Run3/", "Jan22"))

## show database
if (options.keys == True):
    print("Registerd keys \n")
    for index, folder in enumerate(folders):
        print("({INDEX}) KEY: {KEY}".format(INDEX=index+1, KEY=folder["key"]))
        print("REMOTE: {REMOTE}".format(REMOTE = folder["remoteFolder"]))
        print("LOCAL: {LOCAL}".format(LOCAL = folder["localFolder"]))
        print("INFO: {NOTE}".format(NOTE=folder["note"]))
        print("UPDATE: python updateWWW.py --update {KEY}\n".format(KEY=folder["key"]))

#update plots in website
if len(options.update) > 0:
    updatePlots(options.update, folders)
