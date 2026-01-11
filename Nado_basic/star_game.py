
#일반 유닛
# class Unit :
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# #공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self,name, hp, speed)
#         self.damage = damage
#         self.speed = speed
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))
        

#     def damaged(self,damage):
#         print("{0} : {1} 데미지를 입었습니다. ".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다. ".format(self.name))

    


# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 날수 있는 기능이 있는 수송기
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다.  [속도 {2}]"\
#               .format(name, locals, self.flying_speed))
        
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
#         Flyable.__init__(self,flying_speed)

# vulture = AttackUnit("벌쳐", 200, 10, 20)
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)


# ####### 여기서 지상과 공중의 유닛이 움직이건 같은데 분리되어 move, fly 로 되어 이것을 하나로 하는 것이 오버라이딩. 
# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")

# 발키리
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

## 메소드 오바라이딩 4:10

##오버로딩..

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다.  [속도 {2}]"\
#               .format(name, locals, self.flying_speed))
        
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
#         Flyable.__init__(self,flying_speed)

#     def move(self, location):
#         print("공중 유닛 이동")
#         self.fly(self.name, self.location)

# vulture.move("11시")
# battlecruiser.move("3시")

print("----------------------------------------------------")
print("----------------------------------------------------")

#pass

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass    # 코드를 완성하지 않고 일단 넘어간다. 
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

## super

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass    # 코드를 완성하지 않고 일단 넘어간다. 
#         Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)  # super 에서는 super() 괄호를 사용하고 , self 를 적지 않는다. 
#         self.location = location


# class MuteSuper( AttackUnit, Flyable):
#     def __init__(self, name, hp):
#         super().init() # 이렇게 사용하면 3 가지 멀티 상속이 안된다. 처음 Unit 만 값이 찍힌다.
#         # 해결방법        
#         AttackUnit.__init__(self, self.name, self.hp, location)
#         Flyable.__init__(self, self.name, self.hp, location)


### 스타크레프트 전반전 게임처럼 구성해 보기. 

from random import *

#일반 유닛
class Unit :
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다. ".format(name))


    def move(self, location):
        # print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다. ".format(self.name))

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        self.speed = speed
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))
        
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스템팩을 사용합니다. (hp 10 감소)".format(self.name))
        else :
            print("{0} : 체력이 부족하여 스팀팩 사용불가".format(self.name))

class Tank(AttackUnit):
    
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self,"탱크", 150,1,35)    
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다. ".format(self.name))
            self.damage *= 2
            self.seize_developed = True            
        else :
            print("{0} : 시즈모드를 해재합니다.".format(self.name))    
            self.damage /= 2
            self.seize_developed = False

# 공중 공격 유닛 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다.  [속도 {2}]"\
               .format(name, locals, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self,flying_speed)

    def move(self, location):
        # print("공중 유닛 이동")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스",80, 20, 5)
        self.clocked = False
    def clocking(self):
        if self.clocked == False:
            print("{0} : 클록킹 전환합니다. ".format(self.name))            
            self.seize_developed = True            
        else :
            print("{0} : 클록킹를 해재합니다.".format(self.name))                
            self.seize_developed = False


def game_start():
    print("[알림] 새로운 게임을 시작합니다. ")

def game_stop():
    print("[알림] GG 게임을 종료합니다. ")


# 게임 수행

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()
w2 = Wraith()
w3 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료 되었습니다. ")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스: 클로킹)
#지금 만들어진 객체가 어떤 인스턴스의 객체인지 확인 하기 위해 isinstance()

for unit in attack_units:
    # 지금 사용하는 객체가 (현재 유닛이)  unit, Marine 의 객체가 맞는지 확인
    if isinstance(unit, Marine): 
        unit.stimpack()        
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,21)) # 공격은 랜덤으로 받는다. 

# 게임 종료
game_stop()