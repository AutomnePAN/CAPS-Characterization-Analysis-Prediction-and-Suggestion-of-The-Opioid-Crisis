import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt

def readWash(YY):
    lostItems=[]
    dF=pd.read_csv('ACS_'+str(YY)+'_5YR_DP02_with_ann.csv')
    for col in list(dF.columns):
        if dF[col].iloc[1]=='(X)' or 'Error;' in str(dF[col].iloc[0]).split() or 'Percent;' in str(dF[col].iloc[0]).split():
            dF.pop(col)
    for i in range(1,dF.shape[0]):
        for j in range(3,dF.shape[1]):
            try:
                float(dF.iloc[i][j])
            except:
                dF.iloc[i][j]=np.nan
                lostItems.append([dF.iloc[i][j],i,j])
    dF=dF.dropna()
    return(dF)

metaSetCommon=set(readWash(10).columns)
for YY in range(11,17):
    metaSetCommon=metaSetCommon.intersection(set(readWash(YY).columns))
countySetCommon=set(readWash(10)['GEO.id2'])
for YY in range(11,17):
    countySetCommon=countySetCommon.intersection(set(readWash(YY)['GEO.id2']))

dF_Group={}
for YY in range(10,17):
    dropList=[]
    dF_tmp=readWash(YY)
    for col in dF_tmp.columns:
        if col not in metaSetCommon:
            try:
                dF_tmp.pop(col)
            except:
                pass
    for index in range(dF_tmp.shape[0]):
        if dF_tmp.iloc[index]['GEO.id2'] not in countySetCommon:
            dropList.append(index)
    dF_tmp=dF_tmp.drop(dropList)
    dF_Group[YY]=dF_tmp
    print(dF_tmp.shape)

columnsDict={}
for i in range(3,dF_Group[10].shape[1]):
    columnsDict[i-3]=dF_Group[10].columns[i]

def plotCorr(dF_corr):
    fig, ax = plt.subplots()

    image = np.array(dF_corr)
    ax.imshow(image, cmap='viridis', interpolation='nearest')
    ax.set_title('Corr')

    # Move left and bottom spines outward by 10 points
    ax.spines['left'].set_position(('outward', 10))
    ax.spines['bottom'].set_position(('outward', 10))
    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    scale_ls = range(6)
    index_ls = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    plt.rcParams['savefig.dpi'] = 300
    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['figure.figsize']=[16,9]
    plt.savefig('figure.pdf')
    plt.show()

corrList=[]
for YY in range(10,17):
    dF_Data=dF_Group[10].iloc[1:,3:]
    corrList.append(list(dF_Data.astype(float).corr().mean()))
plotCorr(corrList)
corrList=pd.DataFrame(corrList)
corrMean=dict(corrList.mean())
for i in range(corrList.shape[1]):
    if (corrMean[i]>0.7):
        corrList.pop(i)
corrList.columns=[columnsDict[corrList.columns[i]] for i in range(0,corrList.shape[1])]
columnList=['GEO.id2']+list(corrList.columns)
for YY in range(10,17):
    dF_tmp=dF_Group[YY].copy()
    for col in dF_tmp.columns:
        if col not in columnList:
            dF_tmp.pop(col)
    dF_tmp=dF_tmp.drop(0).reset_index()
    dF_tmp.pop('index')
    dF_tmp.columns=['FIPS']+list(dF_tmp.columns[1:])
    print(dF_tmp.shape)
    dF_tmp.to_csv('ACS_'+str(YY)+'_COOKED.csv')
