import os
import DisplacedDimuons.Common.Constants as Constants

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-s", "--selection", dest="selection", default = "", help="creats script file for given selection and set of variables", required=False)
parser.add_argument("-v", "--variable", dest="variable", default = "", help="creats script file for given variables", required=False)
parser.add_argument("-i", "--info", dest="info", action="store_true", help="show all registered selections", required=False)
parser.add_argument("-y", "--year", dest="year", default="2022", help="2016, 2018, 2022(default), all", required=False)
parser.add_argument("-pf","--plotsfolder", dest="plotsFolder", default="/users/alberto.escalante/plots/Run3/", help="base plots folder (selection folders will be created inside)", required=False)
options = parser.parse_args()

def getNtuples(cut, rntuples_dir):
    '''
    retrieves the right set of ntuples given the selection"
    '''
    my_rntuples_dir = rntuples_dir
    variables_patlink = ["DSA11", "DSA3"]

    #getting appropiate rNtuple
    for kvariables_patlink in variables_patlink:
        if kvariables_patlink in cut:
            my_rntuples_dir = my_rntuples_dir.replace("_REP_", "_DSAPATLINK_")
            my_rntuples_dir = my_rntuples_dir.replace("TSTAT_ISTM_", "")

    #getting appropiate skim rNtuple
    if "LXYS " not in cut:
        my_rntuples_dir = my_rntuples_dir.replace("LxySig6.0", "LxySig0.0")
    if "ILXYS " in cut:
        my_rntuples_dir = my_rntuples_dir.replace("LxySig6.0", "LxySig0.0")
    if "LXYS3 " in cut:
        my_rntuples_dir = my_rntuples_dir.replace("LxySig6.0", "LxySig3.0")

#    for kvariables_patlink in variables_patlink:
#        if kvariables_patlink in cut:
#            my_rntuples_dir = my_rntuples_dir.replace("_REP_", "_DSAPATLINK_")
#            my_rntuples_dir = my_rntuples_dir.replace("TSTAT_ISTM_", "")

    return my_rntuples_dir
    
def makePlot(plotsFolder, script = "", year = "2022", cut = "", variable = "", dim_type = "dsa", flags = "--nomcbg --nosig --noratio", options = "", run = False):
    '''
    creates a python scripts to produce plots (to be submitted in batch system)
    '''
    
    #creates output folder (if it does not exist)
    os.system("mkdir -p {OUTPUTFOLDER}".format(OUTPUTFOLDER = plotsFolder))

    #example to make plot
    #python3 plotstack.py --year 2022 -c BASE SS -x deltaphi -t dsa --nomcbg --nosig --noratio

    samplepath = getNtuples(cut, Constants.RNTUPLES_DIRS[int(year)])

    nvariables = variable.split(",")
    ncuts = cut.split(",")

    if len(nvariables) == 1 and len(ncuts) == 1:
        script = "plotstack.py"
        varx = variable
        command = "python3 {SCRIPT} -d {OUTPUTFOLDER} --samplepath {SAMPLEPATH} --year {YEAR} -c {CUTS} -x {VARX} -t {DIM_TYPE} {FLAGS}".format(SCRIPT = script, OUTPUTFOLDER = plotsFolder, SAMPLEPATH = samplepath, YEAR = year, CUTS = cut, VARX = varx, DIM_TYPE = dim_type, FLAGS = flags)

    elif len(nvariables) == 1 and len(ncuts)==2:
        #python plotoverlaidcuts.py -x mass --year 2022 --dir /users/alberto.escalante/plots/Run3/debug -c REP LXYE IMASS CHI2 COSA LXYS DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF --dcuts OS SS --nomcbg --nosig -t dsa -x1 0 -x2 10
        script = "plotoverlaidcuts.py"
        varx = variable
        cutbase  = ncuts[0]
        cutextra = ncuts[1]
        command = "python3 {SCRIPT} -d {OUTPUTFOLDER} --samplepath {SAMPLEPATH} --year {YEAR} -c {CUTS} -x {VARX} -t {DIM_TYPE} --dcuts {CUTEXTRA} {FLAGS}".format(SCRIPT = script, OUTPUTFOLDER = plotsFolder, SAMPLEPATH = samplepath, YEAR = year, CUTS = cutbase, VARX = varx, CUTEXTRA = cutextra, DIM_TYPE = dim_type, FLAGS = flags + "--legpos bl")
        #at the moment --noratio option is supported
        command = command.replace("--noratio", "")
    elif len(nvariables) == 2 and len(ncuts) == 1:
        script = "plot2d.py"
        varx = nvariables[0]
        vary = nvariables[1]
        command = "python3 {SCRIPT} -d {OUTPUTFOLDER} --samplepath {SAMPLEPATH} --year {YEAR} -c {CUTS} -x {VARX} -y {VARY} -t {DIM_TYPE} {FLAGS}".format(SCRIPT = script, OUTPUTFOLDER = plotsFolder, SAMPLEPATH = samplepath, YEAR = year, CUTS = cut, VARX = varx, VARY = vary, DIM_TYPE = dim_type, FLAGS = flags.replace("--noratio", ""))
    else:
        print("ERROR: number of variables or script cannot be identified")
        print("  nvariables: ", nvariables)
        print("  ncuts: ", ncuts)
        exit()

    if len(options) >0:
        #options are specified in variable, added to the command
        command = command + " {OPTIONS}".format(OPTIONS = options)

    print(command)
    if run == True:
        os.system(command)

    return command

def addVariable(variables, newvariable, options = "", group_type = []):
    '''
    registers a new variable with plotting options (by default no extra options are assumed). --cutexpr no yet supported.
    2D variables can be provided if they are separated by a comma
    '''
    suffix = ""

    variables[newvariable] = options
    
    if len(options)>0 and "-x1" in options or "-x2" in options or "-y1" in options or "-y2" in options or "-xe" in options and "--suffix" not in options:
        ## create suffix for the filename if not specified
        suffix = options.strip()
        suffix = suffix.replace(" ", "_")
        suffix = suffix.replace("-", "")
        suffix = "_extra-" + suffix
        variables[newvariable] = variables[newvariable] + " --suffix {SUFFIX}".format(SUFFIX = suffix)
        #print(variables[newvariable])

    if len(group_type) > 0:
        group_type = group_type.append(newvariable)
    
    return variables

def clearVersion(variable):
    import re
    variable = re.sub('_v\d', '', variable)
    return variable

def showSelections(selections):
    for index, selection in enumerate(selections.keys()):
        print("({INDEX}) {SELECTION_KEY} : {SELECTION}".format(INDEX = index, SELECTION_KEY = selection, SELECTION = selections[selection]))
        print("   Example: plotter_2022.py -s {SELECTION_KEY} \n".format(SELECTION_KEY = selection))
    print(" rNtuple version (2022): {RNTUPLEDIR}".format(RNTUPLEDIR = Constants.RNTUPLES_DIRS[int(2022)]))
    print(" rNtuple version (2018): {RNTUPLEDIR}".format(RNTUPLEDIR = Constants.RNTUPLES_DIRS[int(2018)]))
    print(" rNtuple version (2016): {RNTUPLEDIR}".format(RNTUPLEDIR = Constants.RNTUPLES_DIRS[int(2016)]))
def skipVariable(cutstring, variable, condition_required):
    '''
    skips a variable if it does not make sense to produce. This function matches cutstrings and conditions.
    '''
    skipVariable = False
    #dsapatlinked sample required
    for kcondition in condition_required[0].split(" "):
        if kcondition in cutstring:
            if variable in condition_required:
                skipVariable = True

    if len(variable.split(",")) == 2 and len(cutstring.split(",")) == 2:
        #to be implemented 2d plots with incremental cuts
        skipVariable = True
        
    return skipVariable
    
print("Registering selections... \n")

# add sections
selections = {}

#measurement regions
selections['base_selection_dy_cr_patpat']  = 'DSA3  LXYE MASS CHI2 COSA DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF OS DYTFPATCUTS LXYS '
selections['base_selection_dy_cr_patpat_match']  = 'DSA3  LXYE MASS CHI2 COSA DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF OS DYTFPATCUTS LXYS PATMATCH'
selections['base_selection_dy_cr_hyb']     = 'DSA11 LXYE MASS CHI2 COSA DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF OS DYTFHYBCUTS LXYS '
selections['base_selection_qcd_cr_patpat'] = 'DSA3  LXYE MASS CHI2 COSA DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF OS NONISOPATDIM0p1 LXYS '
selections['base_selection_qcd_cr_hyb']    = 'DSA11 LXYE MASS CHI2 COSA DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF OS NONISOHYBDIM0p1 LXYS '

#BASE: 'REP', 'LXYE', 'MASS', 'CHI2', 'COSA', 'LXYS', 'DCA', 'DETANDT', 'DETASEG', 'SEG', 'DSATIME', 'DIR', 'BBDSATIMEDIFF'

#control regions
selections['base_selection_dy']      = 'BASE OS IDPHI'
selections['base_selection_qcd']     = 'BASE SS DPHI'
selections['base_selection_qcd_all'] = 'BASE SS DPHI'

#validation regions
selections['base_selection_qcd_IDETANDTIDETASEG'] = 'REP LXYE MASS CHI2 COSA LXYS DCA IDETANDTIDETASEG DSATIME DIR BBDSATIMEDIFF'
selections['base_selection_qcd_IMASS']            = 'REP LXYE IMASS CHI2 COSA LXYS DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF'
selections['base_selection_dy_ILXYS']             = 'REP LXYE MASS CHI2 COSA ILXYS DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF'

#cosmic ray selection
selections['base_selection_cosmic'] = 'REP LXYE MASS CHI2 ICOSA LXYS DCA DETANDT DETASEG SEG IDSATIME IDPHI'

#validation regions (overlays)
selections['base_overlay_qcd_IDETANDTIDETASEG_OS_SS'] = 'REP LXYE MASS CHI2 COSA LXYS DCA IDETANDTIDETASEG DSATIME DIR BBDSATIMEDIFF, OS SS'
selections['base_overlay_qcd_IMASS_OS_SS']            = 'REP LXYE IMASS CHI2 COSA LXYS DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF, OS SS'
selections['base_overlay_dy_ILXYS_DPHI_IDPHI3']        = 'REP LXYE MASS CHI2 COSA ILXYS DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF, DPHI IDPHI3'
selections['base_overlay_dy_ILXYS_DPHI1_IDPHI2']        = 'REP LXYE MASS CHI2 COSA ILXYS DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF, DPHI1 IDPHI2'

selections['base_overlay_qcd_IDETANDTIDETASEG_DSAISO0P1_IDSAISO0P1'] = 'REP LXYE MASS CHI2 COSA LXYS DCA IDETANDTIDETASEG DSATIME DIR BBDSATIMEDIFF, DSAISO0P1 IDSAISO0P1'
selections['base_overlay_qcd_IMASS_DSAISO0P1_IDSAISO0P1']            = 'REP LXYE IMASS CHI2 COSA LXYS DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF, DSAISO0P1 IDSAISO0P1'

selections['base_overlay_qcd_IDETANDTIDETASEG_SS_DSAISO0P1_IDSAISO0P1'] = 'REP LXYE MASS CHI2 COSA LXYS DCA IDETANDTIDETASEG DSATIME DIR BBDSATIMEDIFF SS, DSAISO0P1 IDSAISO0P1'
selections['base_overlay_qcd_IMASS_SS_DSAISO0P1_IDSAISO0P1']            = 'REP LXYE IMASS CHI2 COSA LXYS DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF SS, DSAISO0P1 IDSAISO0P1'
selections['base_overlay_qcd_BASE_SS_DSAISO0P1_IDSAISO0P1']             = 'REP LXYE MASS CHI2 COSA LXYS DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF SS, DSAISO0P1 IDSAISO0P1'

selections['base_overlay_qcd_IDETANDTIDETASEG_OS_DSAISO0P1_IDSAISO0P1'] = 'REP LXYE MASS CHI2 COSA LXYS DCA IDETANDTIDETASEG DSATIME DIR BBDSATIMEDIFF OS, DSAISO0P1 IDSAISO0P1'
selections['base_overlay_qcd_IMASS_OS_DSAISO0P1_IDSAISO0P1']            = 'REP LXYE IMASS CHI2 COSA LXYS DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF OS, DSAISO0P1 IDSAISO0P1'

if options.info == True:
    showSelections(selections)
    exit()

print("Registering variables... \n")

#add variables
variables = {}

addVariable(variables, "lxypv")
addVariable(variables, "lxypv_v1", "-x1 0 -x2 60")
addVariable(variables, "lxypv_v2", "-x1 0 -x2 300")
addVariable(variables, "lxypv_v3", "-x1 0 -x2 600")
addVariable(variables, "lxysigpv")
addVariable(variables, "lxysigpv_v1", "-x1 0 -x2 200")
addVariable(variables, "mass")
addVariable(variables, "mass_v1", "-x1 0 -x2 300")
addVariable(variables, "mass_v2", "-x1 0 -x2 10 -nx 10")
addVariable(variables, "mass_v3", "-x1 6 -x2 10 -nx 4")
addVariable(variables, "mass_v4", "-xe 0 10 30 60 80")
addVariable(variables, "qsum")
addVariable(variables, "dca")
addVariable(variables, "dca_v1", "-x1 0 -x2 100")
addVariable(variables, "deltaphi")
addVariable(variables, "dimdeltaeta")
addVariable(variables, "minpt")
addVariable(variables, "minpt_v1", "-x1 0 -x2 300")
addVariable(variables, "vtxnormchi2")
addVariable(variables, "muon_iso")
addVariable(variables, "muon_iso", "-x1 0 -x2 5")
addVariable(variables, "maxmuon_iso")
addVariable(variables, "minmuon_iso")
addVariable(variables, "dim_isoPmumu")
addVariable(variables, "dim_isoLxy")
addVariable(variables, "deltar")
addVariable(variables, "timediff")
addVariable(variables, "maxabstime")
addVariable(variables, "minbbdsatimediff")

## special variables
#Need DSAPAT-LINK
dsapatlink_required = ["REP BASE"] #do not plot if those cuts are included
addVariable(variables, "ass_eta", "-x1 0 -x2 0.5", group_type = dsapatlink_required)
addVariable(variables, "ass_phi", "-x1 0 -x2 0.5", group_type = dsapatlink_required)
addVariable(variables, "PATmass", group_type = dsapatlink_required)
addVariable(variables, "PATmass_v1", "-x1 50 -x2 110", group_type = dsapatlink_required)
addVariable(variables, "PATmass_v2", "-x1 0 -x2 300", group_type = dsapatlink_required)
addVariable(variables, "corr_muon_iso", group_type = dsapatlink_required)
addVariable(variables, "corr_muon_iso_v1", "-x1 -0.2 -x2 0.2", group_type = dsapatlink_required)
addVariable(variables, "mincorr_muon_iso", group_type = dsapatlink_required)
addVariable(variables, "maxcorr_muon_iso", group_type = dsapatlink_required)

#2d variables (comma separated)
addVariable(variables, "dim_isoPmumu,dim_isoLxy"    )
addVariable(variables, "muon_iso,muon_iso"          )
addVariable(variables, "corr_muon_iso,corr_muon_iso")
addVariable(variables, "maxcorr_muon_iso,PATmass"   )

plotsFolder = options.plotsFolder
if plotsFolder[-1] != "/": plotsFolder = plotsFolder + "/"

jobs_file = "run_plotter_2022.sh"

print("Creating submission script {JOB_FILE}... \n".format(JOB_FILE = jobs_file))
jobs = open(jobs_file, "w")
nselections = 0
nvariables = 0
njobs = 0
years = []
if options.year=="all":
    years.append("2016")
    years.append("2018")
    years.append("2022")
else:
    years.append(options.year)

for selection in selections.keys():
    if len(options.selection) > 0 and options.selection not in selection:
        continue
    nselections = nselections + 1
    for variable in variables.keys():
        if len(options.variable) > 0 and options.variable not in variable:
            continue
        if skipVariable(selections[selection], variable, dsapatlink_required) == True:
            #removes pairs selection - variable that do not make sense
            continue
        if nselections == 1:
            nvariables = nvariables + 1
        #print(selection, variable)
        for year in years:
            command = makePlot(plotsFolder = plotsFolder + selection, year = year, cut = selections[selection], variable = clearVersion(variable), dim_type = "dsa", options = variables[variable], run = False)
            njobs = njobs +1
            jobs.write(command +"\n")
        
#summary
jobs.close()
print("\n =============")
print("above list of jobs contains Nselections = {NSELECTIONS}, Nvariables = {NVARIABLES}, Year = {YEAR}, Njobs = {NJOBS} and can be submitted as ".format(NSELECTIONS = nselections, NVARIABLES = nvariables, YEAR = options.year, NJOBS = njobs))
print("python lxplusCondorSubmit.py --clip --inputFile run_plotter_2022.sh")
print(" =============\n")


##TODO: Implement overlaid
#python plotoverlaidcuts.py -x mass --year 2022 --dir /users/alberto.escalante/plots/Run3/debug -c REP LXYE IMASS CHI2 COSA LXYS DCA DETANDT DETASEG SEG DSATIME DIR BBDSATIMEDIFF --dcuts OS SS --nomcbg --nosig -t dsa -x1 0 -x2 10
