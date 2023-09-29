# Examples of running simple plots in using fast tools

Examples of running 2022 code with `plotter_2022.py`, in a python2 release,  `CMSSW_10_2_5`, inside `DisplacedDimuons/Analysis/fast`

pre-requisites:

```bash
#add simpolic links to useful toos in fast directory
ln -s ~/private/Github/work/DDM/fast/plotter_2022.py DisplacedDimuons/Analysis/fast/.
ln -s ~/private/Github/computing/LXPLUS/lxplusCondorSubmit.py DisplacedDimuons/Analysis/fast/.
# optional: .gitignore symbolic linls in DisplacedDimuons/Analysis/fast/
cd DisplacedDimuons/Analysis/fast/
find . -type l | sed -e s'/^\.\///g' >> .gitignore
#check that you are pointing at the right slimmed ntuples in DisplacedDimuons/Common/python/Constants.py
```

```bash
# after you do cmsenv and make sure you are using python20
#run 2022 TMS-TMS
python plotter_2022.py -s base_patpat -v mass,eta,mind0sigpv,deltaphi,lxysigpv,minpt,deltar,lxypv_v1,lxypv_v4,mass_v1 -pf /users/alberto.escalante/plots/Run3_TMS-TMS/
#check content of run_plotter_2022.sh and if correct, submit jobs.
python lxplusCondorSubmit.py --clip --inputFile run_plotter_2022.sh
#tip: to monitor the jobs you can use
slurm q alberto.escalante
#tip: you can add as many variables as registered in plotter.py and parse it in argument -v
```

At the end of the production you can sync the plots and update the website, for this you need to go to the webiste folder

```bash
# e.g update plots
python updateWWW.py --update run3data_tms-tms #for TMS-TMS
python updateWWW.py --update run3data #for STA-STA
```