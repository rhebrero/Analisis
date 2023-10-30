## samples dictionary, masses are in GeV and ctau in mm

# benchmark
samples_Benchmark = []
samples_Benchmark.append({"massH": 1000, "massX": 350, "ctauX":[35, 350, 3500], "nevents":30000})
samples_Benchmark.append({"massH": 1000, "massX": 150, "ctauX":[10, 100, 1000], "nevents":30000})
samples_Benchmark.append({"massH": 1000, "massX": 50, "ctauX":[4, 40, 400], "nevents":30000})
samples_Benchmark.append({"massH": 1000, "massX": 20, "ctauX":[2, 20, 200], "nevents":30000})

samples_Benchmark.append({"massH": 400, "massX": 150, "ctauX":[40, 400, 4000], "nevents":50000})
samples_Benchmark.append({"massH": 400, "massX": 50, "ctauX":[8, 80, 800], "nevents":50000})
samples_Benchmark.append({"massH": 400, "massX": 20, "ctauX":[4, 40, 400], "nevents":50000})

samples_Benchmark.append({"massH": 200, "massX": 50, "ctauX":[20, 200, 2000], "nevents":100000})
samples_Benchmark.append({"massH": 200, "massX": 20, "ctauX":[7, 70, 700], "nevents":100000})

samples_Benchmark.append({"massH": 125, "massX": 50, "ctauX":[50, 500, 5000], "nevents":200000})
samples_Benchmark.append({"massH": 125, "massX": 20, "ctauX":[13, 130, 1300], "nevents":200000})

# HAHM
samples_HAHM = []
samples_HAHM.append({"DP": 10, "EPSILON":["1e-06", "5e-07", "1e-07", "3e-08"], "nevents":750000, "BR":["2.055494e-01", "2.050336e-01", "1.538355e-01", "1.538355e-01", "1.528733e-01", "5.171528e-02", "5.171528e-02", "2.543809e-02","1.377642e-06", "1.377642e-06", "1.377642e-06"]})
samples_HAHM.append({"DP": 20, "EPSILON":["5e-07", "2e-07", "5e-08", "1e-08"], "nevents":750000, "BR":["2.001407e-01", "2.001065e-01", "1.476542e-01", "1.476542e-01", "1.475966e-01", "5.256406e-02", "5.256406e-02", "5.148698e-02","7.759277e-05", "7.759277e-05", "7.759277e-05"]})
samples_HAHM.append({"DP": 30, "EPSILON":["3e-07", "1e-07", "3e-08", "7e-09"], "nevents":750000, "BR":["1.995479e-01", "1.995332e-01", "1.437694e-01", "1.437694e-01", "1.437542e-01", "5.621038e-02", "5.621038e-02", "5.590956e-02","4.318735e-04", "4.318735e-04", "4.318735e-04"]})
samples_HAHM.append({"DP": 40, "EPSILON":["2e-07", "8e-08", "2e-08", "5e-09"], "nevents":750000, "BR":["1.657248e-01", "1.653923e-01", "1.462278e-01", "1.462278e-01", "1.460519e-01", "4.874259e-02", "4.874259e-02", "4.515361e-02","2.924555e-02", "2.924555e-02", "2.924555e-02"]})
samples_HAHM.append({"DP": 50, "EPSILON":["2e-07", "6e-08", "1e-08", "4e-09"], "nevents":750000, "BR":["1.946009e-01", "1.945670e-01", "1.257203e-01", "1.257203e-01", "1.257018e-01", "7.345389e-02", "7.345389e-02", "7.306186e-02","4.573330e-03", "4.573330e-03", "4.573330e-03"]})
samples_HAHM.append({"DP": 60, "EPSILON":["1e-07", "4e-08", "7e-09", "2e-09"], "nevents":750000, "BR":["1.862957e-01", "1.862372e-01", "1.069039e-01", "1.069039e-01", "1.068731e-01", "9.093529e-02", "9.093529e-02", "9.028496e-02","1.154356e-02", "1.154356e-02", "1.154356e-02"]})

# RPV
samples_RPV = []
samples_RPV.append({"massSquark": 125, "massChi":  50, "ctauChi":[20, 200, 2000], "nevents":200000})
samples_RPV.append({"massSquark": 125, "massChi": 100, "ctauChi":[35, 350, 3500], "nevents":200000})

samples_RPV.append({"massSquark": 200, "massChi":  50, "ctauChi":[15, 150, 1500], "nevents":100000})
samples_RPV.append({"massSquark": 200, "massChi": 175, "ctauChi":[40, 400, 4000], "nevents":100000})

samples_RPV.append({"massSquark": 350, "massChi":  50, "ctauChi":[8, 80, 800], "nevents":75000})
samples_RPV.append({"massSquark": 350, "massChi": 150, "ctauChi":[25, 250, 2500], "nevents":75000})
samples_RPV.append({"massSquark": 350, "massChi": 325, "ctauChi":[45, 450, 4500], "nevents":75000})

samples_RPV.append({"massSquark": 700, "massChi":  50, "ctauChi":[5, 50, 500], "nevents":50000})
samples_RPV.append({"massSquark": 700, "massChi": 500, "ctauChi":[40, 400, 4000], "nevents":50000})
samples_RPV.append({"massSquark": 700, "massChi": 675, "ctauChi":[50, 500, 5000], "nevents":50000})

samples_RPV.append({"massSquark": 1150, "massChi":   50, "ctauChi":[3,  30, 300], "nevents":50000})
samples_RPV.append({"massSquark": 1150, "massChi":  500, "ctauChi":[30, 300, 3000], "nevents":50000})
samples_RPV.append({"massSquark": 1150, "massChi":  950, "ctauChi":[50, 500, 5000], "nevents":50000})
samples_RPV.append({"massSquark": 1150, "massChi": 1125, "ctauChi":[60, 600, 6000], "nevents":50000})

samples_RPV.append({"massSquark": 1600, "massChi":   50, "ctauChi":[2, 20, 200], "nevents":50000})
samples_RPV.append({"massSquark": 1600, "massChi":  500, "ctauChi":[20, 200, 2000], "nevents":50000})
samples_RPV.append({"massSquark": 1600, "massChi":  950, "ctauChi":[40, 400, 4000], "nevents":50000})
samples_RPV.append({"massSquark": 1600, "massChi": 1400, "ctauChi":[60, 600, 6000], "nevents":50000})
samples_RPV.append({"massSquark": 1600, "massChi": 1575, "ctauChi":[70, 700, 7000], "nevents":50000})

# SMuon
samples_SMUON = []
samples_SMUON.append({"massSMuon": 100, "ctauSMuon": [8000], "nevents": 20000})
samples_SMUON.append({"massSMuon": 200, "ctauSMuon": [6000], "nevents": 20000})
samples_SMUON.append({"massSMuon": 300, "ctauSMuon": [4000], "nevents": 20000})
samples_SMUON.append({"massSMuon": 400, "ctauSMuon": [2000], "nevents": 20000})
samples_SMUON.append({"massSMuon": 500, "ctauSMuon": [1000], "nevents": 20000})
samples_SMUON.append({"massSMuon": 700, "ctauSMuon":  [700], "nevents": 20000})

#DATA
#/store/user/sonawane/Muon/PATFilter_MuonRun2022F-PromptReco-v1_012023-v01/230130_163630/0000/pat_927.root
samples_2022 = []
samples_2022.append({"era": "MuonRun2022F"})
