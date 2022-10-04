"""
Pandas basic functions
"""
import pandas as pd


# data 준비
df1 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})
df2 = pd.DataFrame({"A": [5, 6, 7, 8], "B": [9, 10, 11, 12]})
df3 = pd.DataFrame({"C": [1, 2, 3, 5], "D": [100, 101, 102, 103]})

# merge => column 기준으로 추가 병합 (특정 column을 기준으로)
merged_df = pd.merge(left=df1, right=df3, left_on="A", right_on="C").drop("C", axis=1)
print(merged_df)

# concat => 같은 column을 가지는 경우 axis=0, row 기준으로 추가 병합할 수 있는데 새로운 column을 붙이는 경우 axis=1 로 column 기준 추가 병합
concat_df1 = pd.concat([df1, df2], axis=0)
concat_df2 = pd.concat([df1, df3], axis=1)

print(concat_df1)
print(concat_df2)

# pivot => 조건에 따른 변수들의 통계량을 요약한 테이블 (e.g., 학력, 성별(index, columns)에 따른 소득 평균(value))
data_df = pd.read_csv("../../data/온라인_판매기록.csv", encoding="euc-kr")
print(data_df.head())

# index, columns 는 set of values
# values 는 위 unique combination 이 가진 값들에 대한 그룹 (aggregation function 적용될 대상들)
pivot_table1 = pd.pivot_table(data_df, index=["제품"], columns=["쇼핑몰"], values=["판매금액", "수량"], aggfunc="max")
print(pivot_table1)
print(pivot_table1.unstack())
print(pivot_table1.index)
print(pivot_table1.columns)

# groupby
# df.groupby(분할 기준 column)[적용 기준 column].집계함수
# 예를 들어, 성별 기준으로 분할하고, 소득 금액에 대해 집계함수 적용

# pivot_table 과 groupby 는 내용 측면에선 같지만 pivot_table은 기존 table과 column 자체가 달라지므로 최종 결과물을 만들 때 유리 (plot 도 바로 가능)
# 반대로 groupby는 중간 산출물을 만들고 다른 테이블과 결합 등이 필요할 경우 유리 => as_index=False로 하면 기존 table 형태처럼 나온다.
group_table1 = data_df.groupby(["제품", "쇼핑몰"], as_index=False)[["판매금액", "수량"]].max()
print(group_table1)

# Series 정렬 => sort_values 함수

