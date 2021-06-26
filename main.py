#공부 자료 테크보이 워니(youtuber)

print("Hello World!")

# First Time Variables

a = 1
b = 2
c = 1.2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b) #나머지 값

# 문자열 관련

x = "hello"
y = 'bye'

z= """
안녕하세요
민짱입니다
"""

print (z)

print("안녕" + "잘 지내니?")

print (str(a) + y)

d = "3"

print(b + int(d))

# 불리안: boolean (True or False)

e = True
f = False

print(e)
print(y)

# 조건문

if 2 > 1: 
  print("Hello")

if 1 > 2:
  print("Hello") # 1은 2보다 크지 않으므로 else인 Im not hello 송출
else:
  print("Im not hello")

# not 을 사용한 예시

if not 1 > 2:
  print("YES!!")

# not 과 else

if not 2 > 1:
  print("YES!!")
else:
  print("NO!!")

# and 랑 or

if 1 > 0 and 2 > 1:
  print("둘다 참입니다.") # and 는 둘 중 하나라도 거짓이면 거짓

if 1 > 0 and 1 > 4:
  print("둘다 참 입니다.")
else:
  print("둘다 거짓이거나 둘중 하나가 거짓 입니다.")

#BUT

if 1 > 0 or 1 > 4:
  print("둘다 참이거나 둘중 하나가 참 입니다.")
# or 은 둘 중 하나라도 참이면 참 이다.

#TEST

if 1 > 0 or 1 > 4 and 2 > 0:
  print("해당 부분은 참 입니다.")
else:
  print("해당 부분은 거짓 입니다.")
# 테스트 결과: (1 > 0 or 1 > 4) or 임으로 참이다. 참 and 2 > 0 (참)이므로 결과도 참이다.

g = 3

if g > 2:
  print("Hello")

if g > 5:
  print("참 입니다.")
#else 
elif g == 3:
  print("3 입니다.")
else:
  print("거짓 입니다.")

