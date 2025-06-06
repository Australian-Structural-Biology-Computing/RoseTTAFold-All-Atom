import json, os

script_dir = os.path.dirname(os.path.realpath(__file__))+'/'

##
## lk and lk term
#(LJ_RADIUS LJ_WDEPTH LK_DGFREE LK_LAMBDA LK_VOLUME)
type2ljlk = {
    "CNH2":(1.968297,0.094638,3.077030,3.5000,13.500000),
    "COO":(1.916661,0.141799,-3.332648,3.5000,14.653000),
    "CH0":(2.011760,0.062642,1.409284,3.5000,8.998000),
    "CH1":(2.011760,0.062642,-3.538387,3.5000,10.686000),
    "CH2":(2.011760,0.062642,-1.854658,3.5000,18.331000),
    "CH3":(2.011760,0.062642,7.292929,3.5000,25.855000),
    "aroC":(2.016441,0.068775,1.797950,3.5000,16.704000),
    "Ntrp":(1.802452,0.161725,-8.413116,3.5000,9.522100),
    "Nhis":(1.802452,0.161725,-9.739606,3.5000,9.317700),
    "NtrR":(1.802452,0.161725,-5.158080,3.5000,9.779200),
    "NH2O":(1.802452,0.161725,-8.101638,3.5000,15.689000),
    "Nlys":(1.802452,0.161725,-20.864641,3.5000,16.514000),
    "Narg":(1.802452,0.161725,-8.968351,3.5000,15.717000),
    "Npro":(1.802452,0.161725,-0.984585,3.5000,3.718100),
    "OH":(1.542743,0.161947,-8.133520,3.5000,10.722000),
    "OHY":(1.542743,0.161947,-8.133520,3.5000,10.722000),
    "ONH2":(1.548662,0.182924,-6.591644,3.5000,10.102000),
    "OOC":(1.492871,0.099873,-9.239832,3.5000,9.995600),
    "S":(1.975967,0.455970,-1.707229,3.5000,17.640000),
    "SH1":(1.975967,0.455970,3.291643,3.5000,23.240000),
    "Nbb":(1.802452,0.161725,-9.969494,3.5000,15.992000),
    "CAbb":(2.011760,0.062642,2.533791,3.5000,12.137000),
    "CObb":(1.916661,0.141799,3.104248,3.5000,13.221000),
    "OCbb":(1.540580,0.142417,-8.006829,3.5000,12.196000),
    "Phos":(2.1500,0.5850,-4.1000,3.5000,14.7000),  # phil
    "Oet2":(1.5500,0.1591,-5.8500,3.5000,10.8000),
    "Oet3":(1.5500,0.1591,-6.7000,3.5000,10.8000),
    "HNbb":(0.901681,0.005000,0.0000,3.5000,0.0000),
    "Hapo":(1.421272,0.021808,0.0000,3.5000,0.0000),
    "Haro":(1.374914,0.015909,0.0000,3.5000,0.0000),
    "Hpol":(0.901681,0.005000,0.0000,3.5000,0.0000),
    "HS":(0.363887,0.050836,0.0000,3.5000,0.0000),
    "genAl":(1,0.1, 0.0000, 0.0000, 0.0000),
    "genAs":(1, 0.1, 0.0000, 0.0000, 0.0000),
    "genAu":(1, 0.1, 0.0000, 0.0000, 0.0000),
    "genB": (1,0.1, 0.0000, 0.0000, 0.0000),
    "genBe": (1,0.1, 0.0000, 0.0000, 0.0000),
    "genBr": (2.1971, 0.1090, 2.7951, 3.5000, 19.6876),
    "genC": (2.0067, 0.0689, 2.2256, 3.5000, 10.6860), # params from CT
    "genCa": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genCl": (2.0496, 0.1070, 2.3668, 3.5000, 17.5849),
    "genCo": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genCr": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genCu": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genF": (1.6941, 0.0750, 1.6442, 3.5000, 12.2163),
    "genFe": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genHg": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genI": (2.3600, 0.1110, 3.1361, 3.5000, 22.0891),
    "genIr": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genK": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genLi": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genMg": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genMn": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genMo": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genN": (1.7854, 0.1497, -6.3760, 3.5000, 9.5221), # params from NG2
    "genNi": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genO": (1.5492, 0.1576, -3.5363, 3.5000, 10.7220), # params for OG3
    "genOs": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genP": (2.1290, 0.5838, -9.6272, 3.5000, 34.8000), # params for PG5
    "genPb": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genPd": (1, 0.1, 0.0000, 0.0000,0.0000),
    "genPr": (1, 0.1, 0.0000, 0.0000,0.0000),
    "genPt": (1, 0.1, 0.0000, 0.0000,0.0000),
    "genRe": (1, 0.1, 0.0000, 0.0000,0.0000),
    "genRh": (1, 0.1, 0.0000, 0.0000,0.0000),
    "genRu": (1, 0.1, 0.0000, 0.0000,0.0000),
    "genS": (1.9893, 0.3634, -2.3560, 3.5000, 17.6400), # params for SG3
    "genSb": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genSe": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genSi": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genSn": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genTb": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genTe": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genU": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genW": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genV": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genY": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genZn": (1, 0.1, 0.0000, 0.0000, 0.0000),
    "genATM": (1, 0.0, 0.0000, 0.0000, 0.0000), # masked
}

# cartbonded
with open(script_dir+'cartbonded.json', 'r') as j:
    cartbonded_data_raw = json.loads(j.read())

# hbond donor/acceptors
class HbAtom:
    NO = 0
    DO = 1 # donor
    AC = 2 # acceptor
    DA = 3 # donor & acceptor
    HP = 4 # polar H

type2hb = {
    "CNH2":HbAtom.NO, "COO":HbAtom.NO,  "CH0":HbAtom.NO,  "CH1":HbAtom.NO,
    "CH2":HbAtom.NO,  "CH3":HbAtom.NO,  "aroC":HbAtom.NO, "Ntrp":HbAtom.DO,
    "Nhis":HbAtom.AC, "NtrR":HbAtom.DO, "NH2O":HbAtom.DO, "Nlys":HbAtom.DO,
    "Narg":HbAtom.DO, "Npro":HbAtom.NO, "OH":HbAtom.DA,   "OHY":HbAtom.DA,
    "ONH2":HbAtom.AC, "OOC":HbAtom.AC,  "S":HbAtom.NO,    "SH1":HbAtom.NO,
    "Nbb":HbAtom.DO,  "CAbb":HbAtom.NO, "CObb":HbAtom.NO, "OCbb":HbAtom.AC,
    "HNbb":HbAtom.HP, "Hapo":HbAtom.NO, "Haro":HbAtom.NO, "Hpol":HbAtom.HP,
    "HS":HbAtom.HP, # HP in rosetta(?)
    "Phos":HbAtom.NO, "Oet2":HbAtom.AC, "Oet3":HbAtom.AC,
    "genAl":HbAtom.NO, "genAs":HbAtom.NO, "genAu":HbAtom.NO, "genB": HbAtom.NO,
    "genBe": HbAtom.NO, "genBr": HbAtom.NO, "genC": HbAtom.NO, "genCa": HbAtom.NO,
    "genCl": HbAtom.NO, "genCo": HbAtom.NO, "genCr": HbAtom.NO, "genCu": HbAtom.NO,
    "genF": HbAtom.DA, "genFe": HbAtom.NO, "genHg": HbAtom.NO, "genI": HbAtom.NO,
    "genIr": HbAtom.NO, "genK": HbAtom.NO, "genLi": HbAtom.NO, "genMg": HbAtom.NO,
    "genMn": HbAtom.NO, "genMo": HbAtom.NO, "genN": HbAtom.DA,  "genNi": HbAtom.NO,
    "genO": HbAtom.DA, "genOs": HbAtom.NO, "genP": HbAtom.NO,  "genPb": HbAtom.NO,
    "genPd": HbAtom.NO, "genPr": HbAtom.NO, "genPt": HbAtom.NO, "genRe": HbAtom.NO,
    "genRh": HbAtom.NO, "genRu": HbAtom.NO, "genS": HbAtom.DA, "genSb": HbAtom.NO,
    "genSe": HbAtom.NO, "genSi": HbAtom.NO,"genSn": HbAtom.NO,"genTb": HbAtom.NO,
    "genTe": HbAtom.NO, "genU": HbAtom.NO, "genW": HbAtom.NO, "genV": HbAtom.NO,
    "genY": HbAtom.NO, "genZn": HbAtom.NO, "genATM": HbAtom.NO, # masked
}

##
## hbond term
## TO DO: ADD DNA
class HbDonType:
    PBA = 0
    IND = 1
    IME = 2
    GDE = 3
    CXA = 4
    AMO = 5
    HXL = 6
    AHX = 7
    NTYPES = 8

class HbAccType:
    PBA = 0
    CXA = 1
    CXL = 2
    HXL = 3
    AHX = 4
    IME = 5
    NTYPES = 6

class HbHybType:
    SP2 = 0
    SP3 = 1
    RING = 2
    NTYPES = 3

type2dontype = {
    "Nbb": HbDonType.PBA,
    "Ntrp": HbDonType.IND,
    "NtrR": HbDonType.GDE,
    "Narg": HbDonType.GDE,
    "NH2O": HbDonType.CXA,
    "Nlys": HbDonType.AMO,
    "OH": HbDonType.HXL,
    "OHY": HbDonType.AHX,
}

type2acctype = {
    "OCbb": HbAccType.PBA,
    "ONH2": HbAccType.CXA,
    "OOC": HbAccType.CXL,
    "OH": HbAccType.HXL,
    "OHY": HbAccType.AHX,
    "Nhis": HbAccType.IME,
}

type2hybtype = {
    "OCbb": HbHybType.SP2,
    "ONH2": HbHybType.SP2,
    "OOC": HbHybType.SP2,
    "OHY": HbHybType.SP3,
    "OH": HbHybType.SP3,
    "Nhis": HbHybType.RING,
}

dontype2wt = {
    HbDonType.PBA: 1.45,
    HbDonType.IND: 1.15,
    HbDonType.IME: 1.42,
    HbDonType.GDE: 1.11,
    HbDonType.CXA: 1.29,
    HbDonType.AMO: 1.17,
    HbDonType.HXL: 0.99,
    HbDonType.AHX: 1.00,
}

acctype2wt = {
    HbAccType.PBA: 1.19,
    HbAccType.CXA: 1.21,
    HbAccType.CXL: 1.10,
    HbAccType.HXL: 1.15,
    HbAccType.AHX: 1.15,
    HbAccType.IME: 1.17,
}

class HbPolyType:
    ahdist_aASN_dARG = 0
    ahdist_aASN_dASN = 1
    ahdist_aASN_dGLY = 2
    ahdist_aASN_dHIS = 3
    ahdist_aASN_dLYS = 4
    ahdist_aASN_dSER = 5
    ahdist_aASN_dTRP = 6
    ahdist_aASN_dTYR = 7
    ahdist_aASP_dARG = 8
    ahdist_aASP_dASN = 9
    ahdist_aASP_dGLY = 10
    ahdist_aASP_dHIS = 11
    ahdist_aASP_dLYS = 12
    ahdist_aASP_dSER = 13
    ahdist_aASP_dTRP = 14
    ahdist_aASP_dTYR = 15
    ahdist_aGLY_dARG = 16
    ahdist_aGLY_dASN = 17
    ahdist_aGLY_dGLY = 18
    ahdist_aGLY_dHIS = 19
    ahdist_aGLY_dLYS = 20
    ahdist_aGLY_dSER = 21
    ahdist_aGLY_dTRP = 22
    ahdist_aGLY_dTYR = 23
    ahdist_aHIS_dARG = 24
    ahdist_aHIS_dASN = 25
    ahdist_aHIS_dGLY = 26
    ahdist_aHIS_dHIS = 27
    ahdist_aHIS_dLYS = 28
    ahdist_aHIS_dSER = 29
    ahdist_aHIS_dTRP = 30
    ahdist_aHIS_dTYR = 31
    ahdist_aSER_dARG = 32
    ahdist_aSER_dASN = 33
    ahdist_aSER_dGLY = 34
    ahdist_aSER_dHIS = 35
    ahdist_aSER_dLYS = 36
    ahdist_aSER_dSER = 37
    ahdist_aSER_dTRP = 38
    ahdist_aSER_dTYR = 39
    ahdist_aTYR_dARG = 40
    ahdist_aTYR_dASN = 41
    ahdist_aTYR_dGLY = 42
    ahdist_aTYR_dHIS = 43
    ahdist_aTYR_dLYS = 44
    ahdist_aTYR_dSER = 45
    ahdist_aTYR_dTRP = 46
    ahdist_aTYR_dTYR = 47
    cosBAH_off = 48
    cosBAH_7 = 49
    cosBAH_6i = 50
    AHD_1h = 51
    AHD_1i = 52
    AHD_1j = 53
    AHD_1k = 54

# map donor:acceptor pairs to polynomials
hbtypepair2poly = {
  (HbDonType.PBA,HbAccType.PBA): (HbPolyType.ahdist_aGLY_dGLY,HbPolyType.cosBAH_off,HbPolyType.AHD_1j),
  (HbDonType.CXA,HbAccType.PBA): (HbPolyType.ahdist_aGLY_dASN,HbPolyType.cosBAH_off,HbPolyType.AHD_1j),
  (HbDonType.IME,HbAccType.PBA): (HbPolyType.ahdist_aGLY_dHIS,HbPolyType.cosBAH_off,HbPolyType.AHD_1j),
  (HbDonType.IND,HbAccType.PBA): (HbPolyType.ahdist_aGLY_dTRP,HbPolyType.cosBAH_off,HbPolyType.AHD_1j),
  (HbDonType.AMO,HbAccType.PBA): (HbPolyType.ahdist_aGLY_dLYS,HbPolyType.cosBAH_off,HbPolyType.AHD_1h),
  (HbDonType.GDE,HbAccType.PBA): (HbPolyType.ahdist_aGLY_dARG,HbPolyType.cosBAH_off,HbPolyType.AHD_1j),
  (HbDonType.AHX,HbAccType.PBA): (HbPolyType.ahdist_aGLY_dTYR,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.HXL,HbAccType.PBA): (HbPolyType.ahdist_aGLY_dSER,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.PBA,HbAccType.CXA): (HbPolyType.ahdist_aASN_dGLY,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.CXA,HbAccType.CXA): (HbPolyType.ahdist_aASN_dASN,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.IME,HbAccType.CXA): (HbPolyType.ahdist_aASN_dHIS,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.IND,HbAccType.CXA): (HbPolyType.ahdist_aASN_dTRP,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.AMO,HbAccType.CXA): (HbPolyType.ahdist_aASN_dLYS,HbPolyType.cosBAH_off,HbPolyType.AHD_1h),
  (HbDonType.GDE,HbAccType.CXA): (HbPolyType.ahdist_aASN_dARG,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.AHX,HbAccType.CXA): (HbPolyType.ahdist_aASN_dTYR,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.HXL,HbAccType.CXA): (HbPolyType.ahdist_aASN_dSER,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.PBA,HbAccType.CXL): (HbPolyType.ahdist_aASP_dGLY,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.CXA,HbAccType.CXL): (HbPolyType.ahdist_aASP_dASN,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.IME,HbAccType.CXL): (HbPolyType.ahdist_aASP_dHIS,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.IND,HbAccType.CXL): (HbPolyType.ahdist_aASP_dTRP,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.AMO,HbAccType.CXL): (HbPolyType.ahdist_aASP_dLYS,HbPolyType.cosBAH_off,HbPolyType.AHD_1h),
  (HbDonType.GDE,HbAccType.CXL): (HbPolyType.ahdist_aASP_dARG,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.AHX,HbAccType.CXL): (HbPolyType.ahdist_aASP_dTYR,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.HXL,HbAccType.CXL): (HbPolyType.ahdist_aASP_dSER,HbPolyType.cosBAH_off,HbPolyType.AHD_1k),
  (HbDonType.PBA,HbAccType.IME): (HbPolyType.ahdist_aHIS_dGLY,HbPolyType.cosBAH_7,HbPolyType.AHD_1i),
  (HbDonType.CXA,HbAccType.IME): (HbPolyType.ahdist_aHIS_dASN,HbPolyType.cosBAH_7,HbPolyType.AHD_1i),
  (HbDonType.IME,HbAccType.IME): (HbPolyType.ahdist_aHIS_dHIS,HbPolyType.cosBAH_7,HbPolyType.AHD_1h),
  (HbDonType.IND,HbAccType.IME): (HbPolyType.ahdist_aHIS_dTRP,HbPolyType.cosBAH_7,HbPolyType.AHD_1h),
  (HbDonType.AMO,HbAccType.IME): (HbPolyType.ahdist_aHIS_dLYS,HbPolyType.cosBAH_7,HbPolyType.AHD_1i),
  (HbDonType.GDE,HbAccType.IME): (HbPolyType.ahdist_aHIS_dARG,HbPolyType.cosBAH_7,HbPolyType.AHD_1h),
  (HbDonType.AHX,HbAccType.IME): (HbPolyType.ahdist_aHIS_dTYR,HbPolyType.cosBAH_7,HbPolyType.AHD_1i),
  (HbDonType.HXL,HbAccType.IME): (HbPolyType.ahdist_aHIS_dSER,HbPolyType.cosBAH_7,HbPolyType.AHD_1i),
  (HbDonType.PBA,HbAccType.AHX): (HbPolyType.ahdist_aTYR_dGLY,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.CXA,HbAccType.AHX): (HbPolyType.ahdist_aTYR_dASN,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.IME,HbAccType.AHX): (HbPolyType.ahdist_aTYR_dHIS,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.IND,HbAccType.AHX): (HbPolyType.ahdist_aTYR_dTRP,HbPolyType.cosBAH_6i,HbPolyType.AHD_1h),
  (HbDonType.AMO,HbAccType.AHX): (HbPolyType.ahdist_aTYR_dLYS,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.GDE,HbAccType.AHX): (HbPolyType.ahdist_aTYR_dARG,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.AHX,HbAccType.AHX): (HbPolyType.ahdist_aTYR_dTYR,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.HXL,HbAccType.AHX): (HbPolyType.ahdist_aTYR_dSER,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.PBA,HbAccType.HXL): (HbPolyType.ahdist_aSER_dGLY,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.CXA,HbAccType.HXL): (HbPolyType.ahdist_aSER_dASN,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.IME,HbAccType.HXL): (HbPolyType.ahdist_aSER_dHIS,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.IND,HbAccType.HXL): (HbPolyType.ahdist_aSER_dTRP,HbPolyType.cosBAH_6i,HbPolyType.AHD_1h),
  (HbDonType.AMO,HbAccType.HXL): (HbPolyType.ahdist_aSER_dLYS,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.GDE,HbAccType.HXL): (HbPolyType.ahdist_aSER_dARG,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.AHX,HbAccType.HXL): (HbPolyType.ahdist_aSER_dTYR,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
  (HbDonType.HXL,HbAccType.HXL): (HbPolyType.ahdist_aSER_dSER,HbPolyType.cosBAH_6i,HbPolyType.AHD_1i),
}


# polynomials are triplets, (x_min, x_max), (y[x<x_min],y[x>x_max]), (c_9,...,c_0)
hbpolytype2coeffs = { # Parameters imported from rosetta sp2_elec_params @v2017.48-dev59886
    HbPolyType.ahdist_aASN_dARG: ((0.7019094761929999, 2.86820307153,),(1.1, 1.1,),( 0.58376113, -9.29345473, 64.86270904, -260.3946711, 661.43138077, -1098.01378958, 1183.58371466, -790.82929582, 291.33125475, -43.01629727,)),
    HbPolyType.ahdist_aASN_dASN: ((0.625841094801, 2.75107708444,),(1.1, 1.1,),( -1.31243015, 18.6745072, -112.63858313, 373.32878091, -734.99145504, 861.38324861, -556.21026097, 143.5626977, 20.03238394, -11.52167705,)),
    HbPolyType.ahdist_aASN_dGLY: ((0.7477341047139999, 2.6796350782799996,),(1.1, 1.1,),( -1.61294554, 23.3150793, -144.11313069, 496.13575, -1037.83809166, 1348.76826073, -1065.14368678, 473.89008925, -100.41142701, 7.44453515,)),
    HbPolyType.ahdist_aASN_dHIS: ((0.344789524346, 2.8303582266000005,),(1.1, 1.1,),( -0.2657122, 4.1073775, -26.9099632, 97.10486507, -209.96002602, 277.33057268, -218.74766996, 97.42852213, -24.07382402, 3.73962807,)),
    HbPolyType.ahdist_aASN_dLYS: ((0.542905671869, 2.45259389314,),(1.1, 1.1,),( 1.38531754, -18.48733797, 106.14444613, -344.70585054, 698.91577956, -917.0879402, 775.32787908, -403.09588787, 113.65054778, -11.66516403,)),
    HbPolyType.ahdist_aASN_dSER: ((1.0812774602500002, 2.6832123582599996,),(1.1, 1.1,),( -3.51524353, 47.54032873, -254.40168577, 617.84606386, -255.49935027, -2361.56230539, 6426.85797934, -7760.4403891, 4694.08106855, -1149.83549068,)),
    HbPolyType.ahdist_aASN_dTRP: ((0.6689984999999999, 3.0704254,),(1.1, 1.1,),( -0.5284840422, 8.3510150838, -56.4100479414, 212.4884326254, -488.3178610608, 703.7762350506, -628.9936994633999, 331.4294356146, -93.265817571, 11.9691623698,)),
    HbPolyType.ahdist_aASN_dTYR: ((1.08950268805, 2.6887046709400004,),(1.1, 1.1,),( -4.4488705, 63.27696281, -371.44187037, 1121.71921621, -1638.11394306, 142.99988401, 3436.65879147, -5496.07011787, 3709.30505237, -962.79669688,)),
    HbPolyType.ahdist_aASP_dARG: ((0.8100404642229999, 2.9851230124799994,),(1.1, 1.1,),( -0.66430344, 10.41343145, -70.12656205, 265.12578414, -617.05849171, 911.39378582, -847.25013928, 472.09090981, -141.71513167, 18.57721132,)),
    HbPolyType.ahdist_aASP_dASN: ((1.05401125073, 3.11129675908,),(1.1, 1.1,),( 0.02090728, -0.24144928, -0.19578075, 16.80904547, -117.70216251, 407.18551288, -809.95195924, 939.83137947, -593.94527692, 159.57610528,)),
    HbPolyType.ahdist_aASP_dGLY: ((0.886260952629, 2.66843608743,),(1.1, 1.1,),( -7.00699267, 107.33021779, -713.45752385, 2694.43092298, -6353.05100287, 9667.94098394, -9461.9261027, 5721.0086877, -1933.97818198, 279.47763789,)),
    HbPolyType.ahdist_aASP_dHIS: ((1.03597611139, 2.78208509117,),(1.1, 1.1,),( -1.34823406, 17.08925926, -78.75087193, 106.32795459, 400.18459698, -2041.04320193, 4033.83557387, -4239.60530204, 2324.00877252, -519.38410941,)),
    HbPolyType.ahdist_aASP_dLYS: ((0.97789485082, 2.50496946108,),(1.1, 1.1,),( -0.41300315, 6.59243438, -44.44525308, 163.11796012, -351.2307798, 443.2463146, -297.84582856, 62.38600547, 33.77496227, -14.11652182,)),
    HbPolyType.ahdist_aASP_dSER: ((0.542905671869, 2.45259389314,),(1.1, 1.1,),( 1.38531754, -18.48733797, 106.14444613, -344.70585054, 698.91577956, -917.0879402, 775.32787908, -403.09588787, 113.65054778, -11.66516403,)),
    HbPolyType.ahdist_aASP_dTRP: ((0.419155746414, 3.0486938610500003,),(1.1, 1.1,),( -0.24563471, 3.85598551, -25.75176874, 95.36525025, -214.13175785, 299.76133553, -259.0691378, 132.06975835, -37.15612683, 5.60445773,)),
    HbPolyType.ahdist_aASP_dTYR: ((1.01057521468, 2.7207545786900003,),(1.1, 1.1,),( -0.15808672, -10.21398871, 178.80080949, -1238.0583801, 4736.25248274, -11071.96777725, 16239.07550047, -14593.21092621, 7335.66765017, -1575.08145078,)),
    HbPolyType.ahdist_aGLY_dARG: ((0.499016667857, 2.9377031027599996,),(1.1, 1.1,),( -0.15923533, 2.5526639, -17.38788803, 65.71046957, -151.13491186, 218.78048387, -199.15882919, 110.56568974, -35.95143745, 6.47580213,)),
    HbPolyType.ahdist_aGLY_dASN: ((0.7194388032060001, 2.9303772333599998,),(1.1, 1.1,),( -1.40718342, 23.65929694, -172.97144348, 720.64417348, -1882.85420815, 3194.87197776, -3515.52467458, 2415.75238278, -941.47705161, 159.84784277,)),
    HbPolyType.ahdist_aGLY_dGLY: ((1.38403812683, 2.9981039433,),(1.1, 1.1,),( -0.5307601, 6.47949946, -22.39522814, -55.14303544, 708.30945242, -2619.49318162, 5227.8805795, -6043.31211632, 3806.04676175, -1007.66024144,)),
    HbPolyType.ahdist_aGLY_dHIS: ((0.47406840932899996, 2.9234200830400003,),(1.1, 1.1,),( -0.12881679, 1.933838, -12.03134888, 39.92691227, -75.41519959, 78.87968016, -37.82769801, -0.13178679, 4.50193019, 0.45408359,)),
    HbPolyType.ahdist_aGLY_dLYS: ((0.545347533475, 2.42624380351,),(1.1, 1.1,),( -0.22921901, 2.07015714, -6.2947417, 0.66645697, 45.21805416, -130.26668981, 176.32401031, -126.68226346, 43.96744431, -4.40105281,)),
    HbPolyType.ahdist_aGLY_dSER: ((1.2803349239700001, 2.2465996077400003,),(1.1, 1.1,),( 6.72508613, -86.98495585, 454.18518444, -1119.89141452, 715.624663, 3172.36852982, -9455.49113097, 11797.38766934, -7363.28302948, 1885.50119665,)),
    HbPolyType.ahdist_aGLY_dTRP: ((0.686512740494, 3.02901351815,),(1.1, 1.1,),( -0.1051487, 1.41597708, -7.42149173, 17.31830704, -6.98293652, -54.76605063, 130.95272289, -132.77575305, 62.75460448, -9.89110842,)),
    HbPolyType.ahdist_aGLY_dTYR: ((1.28894687639, 2.26335316892,),(1.1, 1.1,),( 13.84536925, -169.40579865, 893.79467505, -2670.60617561, 5016.46234701, -6293.79378818, 5585.1049063, -3683.50722701, 1709.48661405, -399.5712153,)),
    HbPolyType.ahdist_aHIS_dARG: ((0.8967400957230001, 2.96809434226,),(1.1, 1.1,),( 0.43460495, -10.52727665, 103.16979807, -551.42887412, 1793.25378923, -3701.08304991, 4861.05155388, -3922.4285529, 1763.82137881, -335.43441944,)),
    HbPolyType.ahdist_aHIS_dASN: ((0.887120931718, 2.59166903153,),(1.1, 1.1,),( -3.50289894, 54.42813924, -368.14395507, 1418.90186454, -3425.60485859, 5360.92334837, -5428.54462336, 3424.68800187, -1221.49631986, 189.27122436,)),
    HbPolyType.ahdist_aHIS_dGLY: ((1.01629363411, 2.58523052904,),(1.1, 1.1,),( -1.68095217, 21.31894078, -107.72203494, 251.81021758, -134.07465831, -707.64527046, 1894.6282743, -2156.85951846, 1216.83585872, -275.48078944,)),
    HbPolyType.ahdist_aHIS_dHIS: ((0.9773010778919999, 2.72533796329,),(1.1, 1.1,),( -2.33350626, 35.66072412, -233.98966111, 859.13714961, -1925.30958567, 2685.35293578, -2257.48067507, 1021.49796136, -169.36082523, -12.1348055,)),
    HbPolyType.ahdist_aHIS_dLYS: ((0.7080936539849999, 2.47191718632,),(1.1, 1.1,),( -1.88479369, 28.38084382, -185.74039957, 690.81875917, -1605.11404391, 2414.83545623, -2355.9723201, 1442.24496229, -506.45880637, 79.47512505,)),
    HbPolyType.ahdist_aHIS_dSER: ((0.90846809159, 2.5477956147,),(1.1, 1.1,),( -0.92004641, 15.91841533, -117.83979251, 488.22211296, -1244.13047376, 2017.43704053, -2076.04468019, 1302.42621488, -451.29138643, 67.15812575,)),
    HbPolyType.ahdist_aHIS_dTRP: ((0.991999676806, 2.81296584506,),(1.1, 1.1,),( -1.29358587, 19.97152857, -131.89796017, 485.29199356, -1084.0466445, 1497.3352889, -1234.58042682, 535.8048197, -75.58951691, -9.91148332,)),
    HbPolyType.ahdist_aHIS_dTYR: ((0.882661836357, 2.5469016429900004,),(1.1, 1.1,),( -6.94700143, 109.07997256, -747.64035726, 2929.83959536, -7220.15788571, 11583.34170519, -12078.443492, 7881.85479715, -2918.19482068, 468.23988622,)),
    HbPolyType.ahdist_aSER_dARG: ((1.0204658147399999, 2.8899566041900004,),(1.1, 1.1,),( 0.33887327, -7.54511361, 70.87316645, -371.88263665, 1206.67454443, -2516.82084076, 3379.45432693, -2819.73384601, 1325.33307517, -265.54533008,)),
    HbPolyType.ahdist_aSER_dASN: ((1.01393052233, 3.0024434159299997,),(1.1, 1.1,),( 0.37012361, -7.46486204, 64.85775924, -318.6047209, 974.66322243, -1924.37334018, 2451.63840629, -1943.1915675, 867.07870559, -163.83771761,)),
    HbPolyType.ahdist_aSER_dGLY: ((1.3856562156299999, 2.74160605537,),(1.1, 1.1,),( -1.32847415, 22.67528654, -172.53450064, 770.79034865, -2233.48829652, 4354.38807288, -5697.35144236, 4803.38686157, -2361.48028857, 518.28202382,)),
    HbPolyType.ahdist_aSER_dHIS: ((0.550992321207, 2.68549261999,),(1.1, 1.1,),( -1.98041793, 29.59668639, -190.36751773, 688.43324385, -1534.68894765, 2175.66568976, -1952.07622113, 1066.28943929, -324.23381388, 43.41006168,)),
    HbPolyType.ahdist_aSER_dLYS: ((0.8603189393170001, 2.77729502744,),(1.1, 1.1,),( 0.90884741, -17.24690746, 141.78469099, -661.85989315, 1929.7674992, -3636.43392779, 4419.00727923, -3332.43482061, 1410.78913266, -253.53829424,)),
    HbPolyType.ahdist_aSER_dSER: ((1.10866545921, 2.61727781204,),(1.1, 1.1,),( -0.38264308, 4.41779675, -10.7016645, -81.91314845, 668.91174735, -2187.50684758, 3983.56103269, -4213.32320546, 2418.41531442, -580.28918569,)),
    HbPolyType.ahdist_aSER_dTRP: ((1.4092077245899999, 2.8066121197099996,),(1.1, 1.1,),( 0.73762477, -11.70741276, 73.05154232, -205.00144794, 89.58794368, 1082.94541375, -3343.98293188, 4601.70815729, -3178.53568678, 896.59487831,)),
    HbPolyType.ahdist_aSER_dTYR: ((1.10773547919, 2.60403567341,),(1.1, 1.1,),( -1.13249925, 14.66643161, -69.01708791, 93.96846742, 380.56063898, -1984.56675689, 4074.08891127, -4492.76927139, 2613.13168054, -627.71933508,)),
    HbPolyType.ahdist_aTYR_dARG: ((1.05581400627, 2.85499888099,),(1.1, 1.1,),( -0.30396592, 5.30288548, -39.75788579, 167.5416547, -435.15958911, 716.52357586, -735.95195083, 439.76284677, -130.00400085, 13.23827556,)),
    HbPolyType.ahdist_aTYR_dASN: ((1.0994919065200002, 2.8400869077900004,),(1.1, 1.1,),( 0.33548259, -3.5890451, 8.97769025, 48.1492734, -400.5983616, 1269.89613211, -2238.03101675, 2298.33009115, -1290.42961162, 308.43185147,)),
    HbPolyType.ahdist_aTYR_dGLY: ((1.36546155066, 2.7303075916400004,),(1.1, 1.1,),( -1.55312915, 18.62092487, -70.91365499, -41.83066505, 1248.88835245, -4719.81948329, 9186.09528168, -10266.11434548, 6266.21959533, -1622.19652457,)),
    HbPolyType.ahdist_aTYR_dHIS: ((0.5955982461899999, 2.6643551317500003,),(1.1, 1.1,),( -0.47442788, 7.16629863, -46.71287553, 171.46128947, -388.17484011, 558.45202337, -506.35587481, 276.46237273, -83.52554392, 12.05709329,)),
    HbPolyType.ahdist_aTYR_dLYS: ((0.7978598238760001, 2.7620933782,),(1.1, 1.1,),( -0.20201464, 1.69684984, 0.27677515, -55.05786347, 286.29918332, -725.92372531, 1054.771746, -889.33602341, 401.11342256, -73.02221189,)),
    HbPolyType.ahdist_aTYR_dSER: ((0.7083554962559999, 2.7032011990599996,),(1.1, 1.1,),( -0.70764192, 11.67978065, -82.80447482, 329.83401367, -810.58976486, 1269.57613941, -1261.04047117, 761.72890446, -254.37526011, 37.24301861,)),
    HbPolyType.ahdist_aTYR_dTRP: ((1.10934023051, 2.8819112108,),(1.1, 1.1,),( -11.58453967, 204.88308091, -1589.77384548, 7100.84791905, -20113.61354433, 37457.83646055, -45850.02969172, 35559.8805122, -15854.78726237, 3098.04931146,)),
    HbPolyType.ahdist_aTYR_dTYR: ((1.1105954899400001, 2.60081798685,),(1.1, 1.1,),( -1.63120628, 19.48493187, -81.0332905, 56.80517706, 687.42717782, -2842.77799908, 5385.52231471, -5656.74159307, 3178.83470588, -744.70042777,)),
    HbPolyType.AHD_1h: ((1.76555274367, 3.1416,),(1.1, 1.1,),( 0.62725838, -9.98558225, 59.39060071, -120.82930213, -333.26536028, 2603.13082592, -6895.51207142, 9651.25238056, -7127.13394872, 2194.77244026,)),
    HbPolyType.AHD_1i: ((1.59914724347, 3.1416,),(1.1, 1.1,),( -0.18888801, 3.48241679, -25.65508662, 89.57085435, -95.91708218, -367.93452341, 1589.6904702, -2662.3582135, 2184.40194483, -723.28383545,)),
    HbPolyType.AHD_1j: ((1.1435646388, 3.1416,),(1.1, 1.1,),( 0.47683259, -9.54524724, 83.62557693, -420.55867774, 1337.19354878, -2786.26265686, 3803.178227, -3278.62879901, 1619.04116204, -347.50157909,)),
    HbPolyType.AHD_1k: ((1.15651981164, 3.1416,),(1.1, 1.1,),( -0.10757999, 2.0276542, -16.51949978, 75.83866839, -214.18025678, 380.55117567, -415.47847283, 255.66998474, -69.94662165, 3.21313428,)),
    HbPolyType.cosBAH_off: ((-1234.0, 1.1,),(1.1, 1.1,),( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,)),
    HbPolyType.cosBAH_6i: ((-0.23538144897100002, 1.1,),(1.1, 1.1,),( -0.822093, -3.75364636, 46.88852157, -129.5440564, 146.69151428, -67.60598792, 2.91683129, 9.26673173, -3.84488178, 0.05706659,)),
    HbPolyType.cosBAH_7: ((-0.019373850666900002, 1.1,),(1.1, 1.1,),( 0.0, -27.942923450028, 136.039920253368, -268.06959056747, 275.400462507919, -153.502076215949, 39.741591385461, 0.693861510121, -3.885952320499, 1.024765090788892)),
}
