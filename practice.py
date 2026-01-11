# # 예외처리
# try:
#     num1 = int(input(입력 1 : ))
#     num2 = int(input(입력 2 : ))
#     print("{0} {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError as err:
#     print(err)
# except Exception as err : # 나머지 모든 에러 처리
#     print("알수 없는 오류가 발생하였다.")
#     print(err)


# # 에러 발생시키기.
# try:
#     print("한 자리 숫자 나누기 전용 계산기 만들기")
#     num1 = int(input("첫번째 숫자 입력 : "))
#     num2 = int(input("첫번째 숫자 입력 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError    # 의도적으로 에러를 발생 시켜 에러 처리 예외로 빼 주었다. 
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였다. 한 자리 숫자만 넣어")


# 사용자 정의 예외처리. 
# 예외처리에서 무조건 실행되는 finally 를 해보자. 
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    pass
try:
    print("한 자리 숫자 나누기 전용 계산기 만들기")
    num1 = int(input("첫번째 숫자 입력 : "))
    num2 = int(input("첫번째 숫자 입력 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0},{1}".format(num1,num2))    # 사용자가 정의한 에러로.. 에러 처리 예외로 빼 주었다. 
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print(" ValueError 잘못된 값을 입력하였다. 한 자리 숫자만 넣어")
except BigNumberError as err:
    print(" BignumberError 잘못된 값을 입력하였다. 한 자리 숫자만 넣어주쇼")
    print(err)
# 예외처리에서 무조건 실행되는 finally 를 해보자. 
finally:
    print("계산기를 이용해 주셔서 감사합니다. ")

