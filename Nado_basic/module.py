# 모듈  예를 들어 필요한 부품끼리 이어진 파일  , 필요한것만 변경해서 사용
# 같은 경로에 있거나 lib 경로에 있어야 theater_module.py 사용 가능

# import theater_module
# theater_module.price(3) # 일반 가격
# theater_module.price_morning(4) # 조조 가격
# theater_module.price_soldier(5) # 군인 가격

# import theater_module as mv   # 별명을 줘서 줄여준다.
# mv.price(3) # 일반 가격
# mv.price_morning(4) # 조조 가격
# mv.price_soldier(5) # 군인 가격

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)

# from theater_module import price_soldier as priso
# priso(5)

print("======================================")
## packege 모듈을 모아둔것을 pkg travel folder
# import 에서 .tailand 의 직접 연결 부분은 module, PKG 만 가능하고 class 는 불가능
# from travel.thailand import ThailnadPackage 와 같이 from 에서는 가능

# import travel.thailand
# trip_to = travel.thailand.ThailnadPackage()
# trip_to.detail()


# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

##__all__
# 아래는 오류 발생 travel 의 모든것을 가져 왔지만 에러가 발생한다. 
# pkg 안에 포함된것 중에서 import 만 공개하고 나머지는 비공개로 하겠다는 뜻
# 이럴때는 __init__.py 안에 __all__ = ["vietnam"] 을 넣어줘본다.
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailnadPackage()
trip_to.detail()

## 모듈 직접 실행. 
# thailand.py 안에 if __name__ == "__main__": 를 등록 모듈 직접수행.

## 패키지, 모듈 위치
# 지금까지는 동일한 폴더나 파이썬 lib 에 있었지만.

import inspect
import random
print(inspect.getfile(random))  # 해당 위치에서 가지고 모듈을 가져옴.
print(inspect.getfile(thailand)) # lib 에 옮겨 놓으면 자동으로 됨.

# 이미 잘 만들어진 pkg 를 가져다가 사용하면 좋다. 
# 예를 들어 난수 생성 pkg 같은거를 찾아보고 
# google -> pypi



