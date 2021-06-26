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
print(a % b) # mod

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
y = False

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
  