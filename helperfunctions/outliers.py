import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as scistat
import math

# 정규성 검정과 분포의 주요 속성(평균, 중앙값, 표준편차, 왜도, 첨도) 확인하는 함수
def getdistprops(seriestotest):
    out = {}
    normstat, normpvalue = scistat.shapiro(seriestotest)
    if (not math.isnan(normstat)):
        out['normstat'] = normstat
        if (normpvalue >= 0.05):
            out['normpvalue'] = str(round(normpvalue, 2)) + ": Accept Normal"
        elif (normpvalue < 0.05):
            out['normpvalue'] = str(round(normpvalue, 2)) + ": Reject Normal"
    out['mean'] = seriestotest.mean()
    out['median'] = seriestotest.median()
    out['std'] = seriestotest.std()
    out['kurtosis'] = seriestotest.kurtosis()
    out['skew'] = seriestotest.skew()
    out['count'] = seriestotest.count()
    return out


# IQR로 이상값을 식별하는 함수
def getouliers(dfin, sumvars, othervars):
    dfin = dfin[sumvars + othervars]
    dfout = pd.DataFrame(columns=dfin.columns, data = None)
    
    dfsums = dfin[sumvars]
    for col in dfsums.columns:
        thirdq, firstq = dfsums[col].quantile(0.75), dfsums[col].quantile(0.25)
        interquartilerange = 1.5 * (thirdq - firstq)
        outlierhigh, outlierlow = interquartilerange + thirdq, firstq - interquartilerange
        df = dfin.loc[(dfin[col]> outlierhigh) | (dfin[col] < outlierlow)]
        df = df.assign(varname = col, threshlow = outlierlow, threshhigh = outlierhigh)
        dfout = pd.concat([dfout, df])
    return dfout

# 히스토그램과 박스플롯 생성 함수
def makeplot(seriestoplot, title, xlabel, plottype='hist'):
    if (plottype=='hist'):
        plt.hist(seriestoplot)
        plt.axvline(seriestoplot.mean(), color='red', linestyle='dashed', linewidth=1)
        plt.xlabel(xlabel)
        plt.ylabel('Frequency')
    elif (plottype == 'box'):
        plt.boxplot(seriestoplot.dropna(), labels=[xlabel])
    plt.title(title)
    plt.show()