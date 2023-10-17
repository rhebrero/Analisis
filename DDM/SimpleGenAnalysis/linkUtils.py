from os import system as bash
from os import getcwd

# This is a simple script that links all scripts into the plotter and analyzer folders

analyzerUtils = []
analyzerUtils.append("GenLongLivedUtils.py")
analyzerUtils.append("RecoUtils.py")
analyzerUtils.append("ResolutionUtils.py")
analyzerUtils.append("SamplesDatabase.py")
analyzerUtils.append("SimpleTools.py")
analyzerUtils.append("myMathUtils.py")

plotterUtils = []
plotterUtils.append("GenLongLivedUtils.py")
plotterUtils.append("SimpleTools.py")

currentWorkingDirectory = getcwd()

for analyzerUtil in analyzerUtils:
    command = "ln -s {CWD}/{ANALYZERUTIL} {CWD}/analyzers/utils/.".format(CWD = currentWorkingDirectory, ANALYZERUTIL = analyzerUtil) 
    print(command)
    bash(command)
for plotterUtil in plotterUtils:
    command = "ln -s {CWD}/{PLOTTERUTIL} {CWD}/plotters/utils/.".format(CWD = currentWorkingDirectory, PLOTTERUTIL = plotterUtil) 
    print(command)
    bash(command)
