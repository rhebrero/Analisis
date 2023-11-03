import os, re
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import numpy as np

parser = ArgumentParser()
parser.add_argument("-m", "--model", dest="model", help="specify model, supported values: Benchmark, HAHM, RPV", required=True)
options = parser.parse_args()

def getEvents(sample):
    """
    count events in million (M) of events
    """
    events = 0.15

    if sample["massSquark"] >= 200: events = 0.075
    if sample["massSquark"] >= 300: events = 0.05
    if sample["massSquark"] >= 500: events = 0.03

    nlifetime = 3
    return events*nlifetime

def drawGrid(samples, tag, label, deltam, fixedChi, draw_others = False):

    massSquark = []
    massChi = []

    massSquark_CMS = []
    massChi_CMS = []

    massSquark_ATLAS = []
    massChi_ATLAS = []

    totalEvents = 0

    print("Sample grid {TAG}".format(TAG=label))
    for sample in samples:
        if sample["tag"] in tag:
            totalEvents = totalEvents + getEvents(sample)
            massSquark.append(sample["massSquark"])
            massChi.append(sample["massChi"])
            print("massSquark: {MASS_SQUARK}, massChi: {MASS_CHI}, nevents: {NEVENTS} M ".format(MASS_SQUARK = sample["massSquark"], MASS_CHI = sample["massChi"], NEVENTS = round(getEvents(sample), 2)))

        if sample["tag"] == "RunI_Grid":
            massSquark_CMS.append(sample["massSquark"])
            massChi_CMS.append(sample["massChi"])

        if sample["tag"] == "RunII_ATLAS":
            massSquark_ATLAS.append(sample["massSquark"])
            massChi_ATLAS.append(sample["massChi"])

    print("------------------".format(NEVENTS = round(totalEvents,2)))
    print("TOTAL {NEVENTS} M".format(NEVENTS = round(totalEvents,2)))

    massSquark_max = 2000
    massChi_max = 1600
    deltaM_max = 800

    plt.xlim([0, massSquark_max])
    plt.ylim([0, massChi_max])

    label_pretty = label.replace("_", " ")

    x = np.linspace(0,massSquark_max,100)
    x_low = np.linspace(fixedChi[0],massSquark_max, 100)
    x_high = np.linspace(fixedChi[1],massSquark_max, 100)

    plt.plot(x, x-deltam[0], 'r', label='$\Delta$ m = {MASS} GeV'.format(MASS=deltam[0]), linestyle='dotted')
    plt.plot(x, x-deltam[1], 'g', label='$\Delta$ m = {MASS} GeV'.format(MASS=deltam[1]), linestyle='dotted')
    plt.plot(x, x-deltam[2], 'k', label='$\Delta$ m = {MASS} GeV'.format(MASS=deltam[2]), linestyle='dotted')

    plt.plot(x, x, 'k', label='$m_\chi = m_{q}$', linestyle='solid')
    plt.plot(x_low,  [fixedChi[0]]*len(x_low) ,'b', label='$m_\chi$ = {MASS} GeV'.format(MASS=fixedChi[0]), linestyle='dashed')
    plt.plot(x_high, [fixedChi[1]]*len(x_high),'b', label='$m_\chi$ = {MASS} GeV'.format(MASS=fixedChi[1]), linestyle='dashdot')


    plt.plot(massSquark, massChi, 'o', label = label_pretty, markersize=6)

    if draw_others == True:
        plt.plot(massSquark_CMS, massChi_CMS, 'o', label = "CMS (Run I)", markersize=4)
        plt.plot(massSquark_ATLAS, massChi_ATLAS, 'o', label = "ATLAS (Run II)", markersize=4)


    plt.ylabel('mass $\chi$ [GeV]')
    plt.xlabel('mass q [GeV]')

    plt.legend(loc="upper left")
    plt.text(x[12], massChi_max+50, 'N(samples) = {NSAMPLES} x 3 = {NSAMPLES3}, N(events) = {NEVENTS} M'.format(NSAMPLES = len(massSquark), NSAMPLES3 = len(massSquark)*3, NEVENTS =round(totalEvents, 2)))

    for format in ["png", "pdf", "eps"]:
        plt.savefig("plots/RPV_scan_tag_{TAG}.{FORMAT}".format(FORMAT=format, TAG=label))

    plt.clf()

    plt.xlim([0, massSquark_max])
    plt.ylim([0, deltaM_max])

    deltaM = [element1 - element2 for (element1, element2) in zip(massSquark, massChi)]

    plt.plot(x, [deltam[0]]*len(x), 'r', label='$\Delta$ m = {MASS} GeV'.format(MASS=deltam[0]), linestyle='dotted')
    plt.plot(x, [deltam[1]]*len(x), 'g', label='$\Delta$ m = {MASS} GeV'.format(MASS=deltam[1]), linestyle='dotted')
    plt.plot(x, [deltam[2]]*len(x), 'k', label='$\Delta$ m = {MASS} GeV'.format(MASS=deltam[2]), linestyle='dotted')
    plt.plot(massSquark, deltaM, 'o', label = label_pretty)

    plt.ylabel('$\Delta$ m [GeV]')
    plt.xlabel('mass q [GeV]')

    plt.legend(loc="best", ncol =2)
    plt.text(x[12], deltaM_max+5, 'N(samples) = {NSAMPLES} x 3 = {NSAMPLES3}, N(events) = {NEVENTS} M'.format(NSAMPLES = len(massSquark), NSAMPLES3 = len(massSquark)*3, NEVENTS =round(totalEvents, 2)))

    for format in ["png", "pdf", "eps"]:
        plt.savefig("plots/deltaM_scan_tag_{TAG}.{FORMAT}".format(FORMAT=format, TAG=label))

    plt.clf()

samples = []
if options.model == "RPV":
    #Run I grid
    tag = "RunI_Grid"
    lifetimeGrid = [1, 100, 10000]  # to be adjunsted
    samples.append({"massSquark": 1500, "massChi": 494, "ctauChi":lifetimeGrid, "tag":tag})
    samples.append({"massSquark": 1000, "massChi": 148, "ctauChi":lifetimeGrid, "tag":tag})
    samples.append({"massSquark":  350, "massChi": 148, "ctauChi":lifetimeGrid, "tag":tag})
    #samples.append({"massSquark":  200, "massChi":  48, "ctauChi":lifetimeGrid, "tag":tag})
    samples.append({"massSquark":  120, "massChi":  48, "ctauChi":lifetimeGrid, "tag":tag})

    tag = "RunII_ATLAS"
    lifetimeGrid = [1, 100, 10000]  # to be adjunsted
    samples.append({"massSquark": 1600, "massChi": 1300, "ctauChi":lifetimeGrid, "tag":tag})
    samples.append({"massSquark": 1600, "massChi":   50, "ctauChi":lifetimeGrid, "tag":tag})
    samples.append({"massSquark":  700, "massChi":  500, "ctauChi":lifetimeGrid, "tag":tag})
    samples.append({"massSquark":  700, "massChi":   50, "ctauChi":lifetimeGrid, "tag":tag})

    #Run III grid (split 1.1: very compressed, 1.3: middle compressed, 2.0: uncompressed)
    #for split in [1.1, 1.3, 2]:
    for split in [1.1, 2]:
        for massChi in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
#            samples.append({"massSquark": int(split*massChi), "massChi":  massChi, "ctauChi":[1, 10, 100, 1000, 10000]})
            samples.append({"massSquark": int(split*massChi), "massChi":  massChi, "ctauChi":lifetimeGrid, "tag":str(split)})


    #run 3 tag
    #for massSquark in [125, 250, 500, 1000, 1500]:
    massSquarks = [125, 200, 350, 700, 1150, 1600]
    ##draw reference lines
    deltam = [25, 200, 650]
    fixedChi = [50, 500]

    for massSquark in massSquarks:

        tag = "deltaM"
        for kdeltam in deltam:
            kmassChi = massSquark - kdeltam
            if kmassChi > 0 and kmassChi not in fixedChi and massSquark > kmassChi:
                samples.append({"massSquark": massSquark, "massChi": kmassChi, "ctauChi":lifetimeGrid, "tag":tag})

        for kmassChi in fixedChi:
            if massSquark > kmassChi:
                samples.append({"massSquark": massSquark, "massChi": kmassChi, "ctauChi":lifetimeGrid, "tag":tag})

#    drawGrid(samples, ["RunI_Grid"], "RunI_Grid", deltam, fixedChi)
#    drawGrid(samples, ["1.1"],  "massSquark_massChi_1p1", deltam, fixedChi)
#    drawGrid(samples, ["2"]  ,  "massSquark_massChi_2p0", deltam, fixedChi)
#    drawGrid(samples, ["1.1", "2"]  ,  "Run_III_Grid_Ratio", deltam, fixedChi)
    drawGrid(samples, ["deltaM", "fixedChi"]  ,  "Run_III_Grid", deltam, fixedChi, draw_others = True)
