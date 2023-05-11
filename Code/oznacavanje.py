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
    # Učitavanje podataka sa https://finance.yahoo.com/quote/AAPL/history?p=AAPL
    file = open("AAPL.csv", "r")
    
    podatci = file.readlines()
    ulaz = []
    
    for i in range(1, len(podatci)):
        redak = podatci[i].split(",")
        # Date,Open,High,Low,Close,Adj Close,Volume
        # Uzimamo Open
        ulaz.append(float(redak[1]))

    # Postavljanje parametara za probni primjer
    tau = 0
    n = 10
    
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

    # Postavljanje parametara za traženje najvećeg sharp ratio-a za različite kombinacije 'tau' i 'n'
    n = len(ulaz)
    n_range = list(range(n))[1:n-1]
    print(len(n_range))
    tau_range = [0, 0.05, -0.05, 0.01, -0.01]

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


    

