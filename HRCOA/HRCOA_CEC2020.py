import os
from copy import deepcopy
import numpy as np
import math
from opfunu.cec_based.cec2020 import *


PopSize = 100
DimSize = 10
LB = [-100] * DimSize
UB = [100] * DimSize

C1 = 0.2
C3 = 3
MU = 25
SIGMA = 3

TrialRuns = 30
MaxFEs = DimSize * 1000
curFEs = 0

MaxIter = int(MaxFEs / PopSize)
curIter = 0

Pop = np.zeros((PopSize, DimSize))
FitPop = np.zeros(PopSize)

FuncNum = 0
SuiteName = "CEC2020"


# initialize the Pop randomly
def Initialization(func):
    global Pop, FitPop, curFEs, DimSize
    Pop = np.zeros((PopSize, DimSize))
    for i in range(PopSize):
        for j in range(DimSize):
            Pop[i][j] = LB[j] + (UB[j] - LB[j]) * np.random.rand()
        FitPop[i] = func.evaluate(Pop[i])

def HRCOA(func):
    global Pop, FitPop, curIter, MaxIter, LB, UB, PopSize, DimSize
    Off = np.zeros((PopSize, DimSize))
    FitOff = np.zeros(PopSize)
    Xbest = Pop[np.argmin(FitPop)]
    T = np.random.rand() * 15 + 20  # Eq. (3)
    C2 = 2 * (1 - curIter / MaxIter)  # Eq. (7)
    for i in range(PopSize):
        if T > 30:
            if np.random.rand() < 0.5:  # summer resort stage
                Off[i] = Pop[i] + C2 * np.random.random(DimSize) * (Xbest - Pop[i])  # Eq. (6)
            else:
                for j in range(DimSize):
                    z = np.random.randint(0, PopSize)  # Eq. (9)
                    Off[i][j] = Xbest[j] + (Pop[i][j] - Pop[z][j])
        else:
            if np.random.rand() < 0.5:
                a = (-2 - curIter / MaxIter) * np.random.random(DimSize) + 1
                Off[i] = (Xbest - Pop[i]) * np.exp(a) * np.cos(2 * np.pi * a) + Pop[i]
            else:
                B = (2 * np.random.rand() - 1) * C2
                Off[i] = Pop[i] + B * (Pop[i] - 0.1 * Xbest)

        Off[i] = np.clip(Off[i], LB, UB)
        FitOff[i] = func.evaluate(Off[i])

    for i in range(PopSize):
        if FitOff[i] < FitPop[i]:
            FitPop[i] = FitOff[i]
            Pop[i] = deepcopy(Off[i])



def RunHRCOA(func):
    global curFEs, curIter, MaxFEs, TrialRuns, Pop, FitPop, DimSize
    All_Trial_Best = []
    for i in range(TrialRuns):
        Best_list = []
        curFEs = 0
        curIter = 0
        Initialization(func)
        Best_list.append(min(FitPop))
        np.random.seed(2020 + 88 * i)
        while curIter <= MaxIter:
            HRCOA(func)
            curIter += 1
            Best_list.append(min(FitPop))
            # print("Iter: ", curIter, "Best: ", Fgbest)
        All_Trial_Best.append(Best_list)
    np.savetxt("./HRCOA_Data/CEC2020/F" + str(FuncNum) + "_" + str(DimSize) + "D.csv", All_Trial_Best, delimiter=",")


def main(dim):
    global FuncNum, DimSize, Pop, MaxFEs, MaxIter, SuiteName, LB, UB
    DimSize = dim
    Pop = np.zeros((PopSize, dim))
    MaxFEs = dim * 1000
    MaxIter = int(MaxFEs / PopSize)
    LB = [-100] * dim
    UB = [100] * dim

    CEC2020 = [F12020(DimSize), F22020(DimSize), F32020(DimSize), F42020(DimSize), F52020(DimSize), F62020(DimSize),
               F72020(DimSize), F82020(DimSize), F92020(DimSize), F102020(DimSize)]

    FuncNum = 0
    for i in range(len(CEC2020)):
        FuncNum = i + 1
        RunHRCOA(CEC2020[i])


if __name__ == "__main__":
    if os.path.exists('./HRCOA_Data/CEC2020') == False:
        os.makedirs('./HRCOA_Data/CEC2020')
    Dims = [50, 100]
    for Dim in Dims:
        main(Dim)
