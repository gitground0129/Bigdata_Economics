import pandas as pd

# 시계열(time series)로 분석하기 위해 기존 csv wide 형태를 long 형태로 변환
def wide_to_long(df, value_name):
    # csv 파일 내 날짜 컬럼은 무조건 YYYY/MM 형태 - (변동 값)
    date_cols = [col for col in df.columns if "/" in col]

    #  날짜가 아닌 모든 컬럼 = id_vars (list형태) - (고정 값)
    id_vars = [col for col in df.columns if col not in date_cols]

    # wide -> long 변환 핵심 로직.
    df_long = df.melt(
        id_vars=id_vars,
        value_vars=date_cols,
        var_name="date",
        value_name=value_name
    )

    # 날짜 변환 (str -> date)
    df_long["date"] = pd.to_datetime(df_long["date"], format="%Y/%m")

    # 값 데이터 변환 (str -> int)
    # Step 1) 숫자 변환 하기 전 str 형변환 후 쉼표와 공백 제거
    df_long[value_name] = (
        df_long[value_name].astype(str).str.replace(",", "", regex=False)
    )
    # Step 2) 쉼표와 공백이 제거된 str -> int 변환
    df_long[value_name] = pd.to_numeric(df_long[value_name])

    return df_long[["date", value_name]].dropna()

# Oil 전처리
def preprocess_oil(df):
    # (필터링) 계정항목에서 유가 : 원유 WTI 데이터만 가져오기
    df = df[df["계정항목"].str.contains("원유- WTI", na=False)]
    return wide_to_long(df, "oil")


def preprocess_cpi(df):
    # (필터링) 계정항목에서 총지수열 선택
    df = df[df["계정항목"].str.contains("총지수", na=False)]
    return wide_to_long(df, "cpi")


def preprocess_rate(df):
    # (필터링) 계정항목에서 한국은행열 선택
    df = df[df["계정항목"].str.contains("한국은행", na=False)]
    return wide_to_long(df, "rate")


def preprocess_unemployment(df):
    # ** 모든 문자열 컬럼 strip 처리 (공백 문제 방지) **
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

    # 3) 실업률 + 계절조정만 필터링
    df = df[df["계정항목"].str.contains("실업률", na=False)]
    df = df[df["구분코드"].str.contains("계절조정", na=False)]

    return wide_to_long(df, "unemployment")
