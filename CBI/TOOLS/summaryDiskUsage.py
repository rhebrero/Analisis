from os import system as bash

"""
Retrieves the disk usage in eos for all DDM users
"""

if __name__ == "__main__":

    differentialInformation = True
    print("[WARNING] Do you have CERN certificate?")
    ddmUsers = ['escalant', 'stempl', 'sonawane']
    for ddmUser in ddmUsers:
        eosFolder = "/eos/vbc/experiments/cms/store/user/{USER}/".format(USER=ddmUser)
        
        #get total information
        command = "du -sh {FOLDER}".format(FOLDER=eosFolder)
        print(command)
        bash(command)
        
        if differentialInformation == True:
            #get differential information
            command = "du -sh {FOLDER}*".format(FOLDER=eosFolder)
            print(command)

    # to be implemented (data operations)
    # gfal-rm -r gsiftp://se.grid.vbc.ac.at:2811/eos/vbc/experiments/cms/store/user/escalant/HTo2ZdTo2mu2x_MZd-10_Epsilon-1e-06_TuneCUETP8M1_13TeV_pythia8/crab_HTo2ZdTo2mu2x_MZd-10_Epsilon-1e-06_TuneCUETP8M1_13TeV_pythia8_ForTest-GS-v2
    # gfal-ls gsiftp://se.grid.vbc.ac.at:2811/eos/vbc/experiments/cms/store/user/escalant/HTo2ZdTo2mu2x_MZd-10_Epsilon-1e-06_TuneCUETP8M1_13TeV_pythia8/
