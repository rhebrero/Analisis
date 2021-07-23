import os, commands
#configuration
inputFile = '/users/alberto.escalante/private/CleanUp_Eos/23_June_2021.txt' #the format is a list of folder directories that you want to scan. 
eosFolter = '/eos/vbc/experiments/cms/store/user/escalant/'

#You need a crab certificate
f = open(inputFile, "r")
fout_pub= open(inputFile.replace(".txt", "_Published.txt"), "w")
fout_unp = open(inputFile.replace(".txt", "_Unpublished.txt"), "w")
for line in f:
    line = line.strip()
    dataset = eosFolter+str(line).strip()
    productions = os.listdir(dataset)
    for kproduction in productions:
        #I have found a production
        #print dataset+"/"+kproduction
        dasgoclient_command = 'dasgoclient --query "dataset =/'+line+'/*escalant*'+kproduction+'-*/USER instance=prod/phys03"'
        status, dasgoclient_command_output = commands.getstatusoutput(dasgoclient_command)
        print dataset+"/"+kproduction
        if len(dasgoclient_command_output) > 0 and status ==0:
            dasgoclient_command_output = dasgoclient_command_output.split("\n")
        #    print dasgoclient_command_output
            print "   ^^ DAS: "+ dasgoclient_command_output[0]
            fout_pub.write(dataset+"/"+kproduction+" , "+dasgoclient_command_output[0]+"\n")
            if len(dasgoclient_command_output) > 1:
                for related_sample in dasgoclient_command_output[0:]:
                    print "       ^^ related samples: ", related_sample
                    fout_pub.write("       ^^ related samples: "+ related_sample+"\n")
        else:
            print "   ^^ NOT PUBLISHED "
            fout_unp.write(dataset+"/"+kproduction+'\n')
