### 10 . 결측치
import pandas as pd
import numpy as np # 채우기 할때. 

# data = {
#     '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
#     '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
#     '키' : [197, 184, 168, 187, 188, 202, 188, 190],
#     '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
#     '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
#     '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
#     '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
#     '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
#     'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
# }

#df = pd.DataFrame(data)
#df = pd.read_csv('C:/Python/work/PythonDataworkspace/Pandas/score.csv')
df = pd.read_excel('C:/Python/work/PythonDataworkspace/Pandas/score.xlsx', index_col='지원번호')

## NaN 데이터 채우기 fillna 

#df = df.fillna('없음') # NaN 데이터를 빈 칸으로 채움
# df['학교'] = np.nan   # 학교 데이터를 모두 NaN 으로 바꿈. 
# df = df.fillna('없음' inplace=True) 
# df['SW특기'].fillna('확인 중')

## 데이터 제외하기 dropna

#df = df.dropna()  # nan 을 포함하는 모든 데이터를 삭제한다.
#df = df.dropna(axis='index', how='any') 
# axis 는 index(row) 또는 columns 이 있다. 
# how 는 any(하나라도 있으면) or all(로우 전체가 nan일때 삭제) 이 있다. 
#df = df.dropna(axis='columns') 

#df = df['학교'] = np.nan
#df.dropna(axis='columns', how='all') # 데이터 전체가 Nan 인 경우에만 Column 삭제

### 11. 데이터 정렬

#df = df.sort_values('키')
#df = df.sort_values('키', ascending=False)  # 내림차순

#df = df.sort_values(['수학','영어'], ascending=False) # 내림차순
#df = df.sort_values(['수학','영어'], ascending=True) # 오름차순
#df = df.sort_values(['수학','영어'], ascending=[True,False]) # 수학은 내림차순, 영어는 오름차순

#df = df['키'].sort_values()
#df = df['키'].sort_values(ascending=False)
#df = df.sort_index()  # 지원번호로 인덱스
#df = df.sort_index(ascending=False) 

### 12. 데이터 수정. 

## Cloumn 수정  북산고 -> 상북고
#df = df['학교'].replace({'북산고':'상북고' }, inplace=True)
#df = df['학교'].replace({'북산고':'상북고', '능남고':'무슨고'})

#df = df['SW특기'].str.lower()
#df['SW특기'] = df['SW특기'].str.lower() # 모두 소문자로 바꾼다. ???

#df['학교'] = df['학교'] + '등학교'   # 학교 컬럼끝에 등학교 포함 능남고등학교

## Column 추가
# 없는 부분을 적으면 추가가 된다. 
# df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
# df['결과'] = 'Fail' # 결과 Column 을 추가 하고 전체 데이터는 Fil 로 초기화
# df.loc[df['총합'] > 400, '결과'] = 'Pass' # 총합이 400 보다 큰 데이터에 대해서 결과를 Pass 로 업데이트 


## Column 삭제

#df.drop(columns=['총합'])
#df.drop(columns=['국어','영어','수학'])

# Row 삭제
#df.drop(index='4번')  # 4번 학생 데이터 Row 를 삭제한다. 

# 조건에 해당하는 데이터 삭제

#ft = df['수학'] < 80 # 수학점수 80 점 미만 학생 필터링
#df.drop(index=df[ft].index)  # 위 ft 에 나온 결과를 삭제 한다. 

# Row 추가
# df.loc['9번'] = ['이정환','해남고',188,90,90,90,90,90,'Kotlin',450,'Pass']

# Cell 수정
#df.loc['8번','SW특기'] = 'Python'
#df.loc['1번', ['학교' ,'SW특기']] = ['능남고','Python']

# Column 순서 변경
#cols = list(df.columns)
#print(cols)

# # 맨뒤에 있는 결과 컬럼은 앞으로 가져와서 순서를 변경을 하였다. 
#df = df[[cols[-1]] + cols[0:-1]]
#df = df[['결과','이름','학교']]

## Column 이름 변경
#df = df.columns
#df = df.columns = ['Result','Name','School']

print(df)