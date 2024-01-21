import pandas as pd

# 데이터프레임에 대한 요약 정보를 딕셔너리로 반환
def getfirstlook(df, nrows=5, uniqueids=None):
    out = {}
    out['head'] = df.head(nrows)
    out['dtypes'] = df.dtypes
    out['nrows'] = df.shape[0]
    out['ncols'] = df.shape[1]
    out['index'] = df.index
    
    if (uniqueids is not None):
        out['uniqueids'] = df[uniqueids].nunique()
    return out

# 딕셔너리를 보기 좋게 출력하는 함수
def displaydict(dicttodisplay):
    print(*(': '.join(map(str, x)) for x in dicttodisplay.items()), sep='\n\n')