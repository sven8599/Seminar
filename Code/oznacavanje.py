import numpy as np

def oznacavanje(ulaz, tau, n):
    #gb - gornja barijera, db -donja barijera
    gb = 0
    db = 0

    oznaceno = []
    povrat = []

    #proces označavanja
    for i in range(len(ulaz) - n):
        r = (ulaz[i + n] - ulaz[i]) / ulaz[i]
        povrat.append(round(r, 2))
        if (r >= tau):
            oznaceno.append(1)
        else:
            oznaceno.append(0)

    return(oznaceno, povrat)


if __name__ == '__main__':

    #ulaz je lista povrata 
    # 1. kako ce biti zapisana
    ulaz = []
    
    #ulaz = [Pt1 Pt2 .. Ptn]
    ulaz = [1, 20, 3, 4 ,5, 6 ,7 ,3, 9, 10]
    print(ulaz)

    tau = 0
    n = 3
    
    oznaceno, povrat = oznacavanje(ulaz, tau, n)
    print(oznaceno)
    print(povrat)

    # BUY / SELL / HOLD
    buysell = []
    for i in range(len(oznaceno) - 1):
        if (oznaceno[i] == 0 and oznaceno[i + 1] == 1):
            buysell.append("BUY")
        elif (oznaceno[i] == 1 and oznaceno[i + 1] == 0):
            buysell.append("SELL")
        else:
            buysell.append("HOLD")
    
    print(buysell)

    n_range = [1, 2, 3]
    tau_range = [0, 0.5, -0.5]

    max_sharp_ratio = float('-inf')
    kombinacija = None

    for n in n_range:
        for tau in tau_range:
            oznaceno, povrat = oznacavanje(ulaz, tau, n)
            sharp_ratio = round(np.mean(povrat) / np.std(povrat), 2)
            print("sharp_ratio: {} for n={} and tau={}".format(sharp_ratio, n, tau))
            if (sharp_ratio > max_sharp_ratio):
                max_sharp_ratio = sharp_ratio
                kombinacija = (n, tau)
    
    print("-------------------")
    print("Max sharp ratio is: {} for n={} and tau={}".format(max_sharp_ratio, kombinacija[0], kombinacija[1]))

