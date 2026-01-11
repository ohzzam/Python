


# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())



## 내장 함수  예를 들어 
# input 
# dir : 어떤 객체를 넘겨줬을 때 그 책체가 어떤 변수와 함수를 가지고 있는지 표시

# print(dir())
# import random # 외장함수 추가
# print(dir())  # 추가 확인. 
# import pickle
# print(dir())
#print(dir(random))

# lst = [1,2,3]
# print(dir(lst)) #lst 에서 사용가능한 함수가 출력

# name = "OH"
# print(dir(name))

# google 에서 list of python builtins


## 외장 함수 직접 import 를 해서 사용을 해야 한다. 
# google 에서 list of python builtins
# 외장함수 목록을 볼 수 있다.

## glob : 경로 내의 폴더/파일 목록 조회 (윈도우 dir)

## import glob
# print(glob.glob("*.py"))

# #os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리 표시

## folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더 입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)  #폴더를 생성함. 
#     print(folder, " 폴더를 생성하였습니다.")

# print(os.listdir())

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은 ",today + td)

