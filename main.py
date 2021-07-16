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
#else if 조건문 else if가 참 임으로 3 입니다. 송출 
elif g == 3:
  print("3 입니다.")
else:
  print("거짓 입니다.")

#function

#def functionName (Data를 받을 수 있는 공간)

def chat(name1, name2):

  print("%s 안녕? 넌 몇 살이니?" % name1)
  print("%s 나? 나는 20" % name2)

chat("민", "카논")

#def test

def calc(num1, num2):
  if num1 > 3 and num2 == 1:
    print("맞는 내용 입니다.")
  else:
    print("둘다 혹은 둘중 하나가 틀립니다.")
  
calc(2, 1)

def talk(food1, num):

  print("%s 한 개 주세요." % food1)
  print("합해서" + str(num) + "원 입니다.")

talk("치즈버거", 4500)

# %s는 "%s content" % name 할 때 %s 에 name의 값을 넘겨주는 역할을 하는 것 같다.

def desum(a, b):
  result = a + b
  return result

d = desum(1, 2)
print(d)

def name(msg):

  if msg == 'Kanon':
    return 'daisuki'

  else:
    return 'im solo'

print("반환된 값:" + name('min'))


def other(text):
  #Min 이기에 Daisuki 이다. h는 return된 값을 가지고 있으므로 print(h)는 daisuki가 된다.
  if text == 'Min':
    return 'daisuki'

  else:
    return 'im kanon'

h = other("Min")

print(h)

#복습 나이를 받아라,
#나이가 10살 미만이면 "안녕" 이라고 말해라
#나이가 10살에서 20살 사이면 "안녕하세요" 라고 말해라
#그 외에는 안녕하십니까 라고 말해라

def hello(age):
  if age < 10 :
    return "안녕"
  elif age >= 10 and age <= 20:
    return "안녕하세요"
  else:
    return "안녕하십니까"
a1 = hello(9)
a2 = hello(14)
a3 = hello(23)

print(a1)
print(a2)
print(a3)

#반복문 loof

# for, while

#First For
#몇 번째 반복이 되는지 볼 수 있다. 0부터 시작함.
for i in range(2):
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야 그냥 있어.")

i = 0

while i < 3: #while 이 주로 쓰이는 예시는 무한루프
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야 그냥 있어.")
  i = i + 1 # i가 1씩 증가 즉 i = 0이였으니 1씩 증가해서 i값이 3이되기 전에 끝남으로 0~2 총 3번 루프 된다.

#break and continue
i = 0

while True: #while 이 주로 쓰이는 예시는 무한루프
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야 그냥 있어.")
  i = i + 1

  if i > 2:
    break

for i in range(100):
  print(i) # 0
  print('Hey Johnny its been a while How r u?')
  print("Great, How are you too Ewen?")
  
  if i > 2:
    break
  
for i in range(3):
  print(i) # 0
  print('Hey Johnny its been a while How r u?')
  print("Great, How are you too Ewen?")

  if i == 1:
    continue
  #컨티뉴 밑은 실행이 안되고 컨티뉴를 확인한 순간 다시 처음으로 돌아가 반복함.
  print("MIN! im Kanon")

 #------------------------------------------------------------------------------

  #list, Tuple, Dictionary

  #list
  j = [1,2,3,4]
  #    0,1,2,3
  k = ["Kanon", "MIN"] #list()와 같은 말이다.
  l = ["kanon", 1,2,3]
  print(j)
  print(k)
  print(l)

  print(j + k)
  
  #호출
  print(j[0]) # j 리스트에서 0번째자리 호출 

  #list 내용 변경
  j[2] = 9 # 2번째 자리의 숫자를 9로 변경
  print(j)

  num_elements = len(j)# j의 사이즈 (몇개가 들어가있나를 확인가능)

  print(num_elements)

  # j의 내용을 정렬 sorted

  n = [3,4,1,2]

  Y = sorted(n)#내용을 정렬 시켜줌 sorted

  print(Y)

  Z = sum(n)#리스트의 숫자를 다 합친값 송출

  print(Z)
  
  for q in n:
    print(q) # n안의 있는 리스트 값들이 차례대로 송출 *참고로 좌에서 우 순서로 하나씩 송출 이지 숫자 높은순 낮은순이 아니다.

  word = ["Hello", "Python"]

  for r in word:
    print(r)


  #list 에서 한 엘리멘트가 어디에 위치하고있는지 확인
  print(n.index(1)) # 0부터 시작함으로 012 즉 2번째 자리 위치 하다는것을 표시해줌
  print(word.index("Hello")) #word 리스트 엘리멘트인 Hello 값이 몇번째인지 송출 맨처음이니 0번째가 맞다.

  print("Python" in word)
  #해당 리스트에 엘리멘트가 들어있는지 없는지 송출
  #맞음으로 True

  if "Hello" in n:
    print("Hello 가 있습니다.") # "Hello"가 n리스트 안에 포함이 되있을 경우만 송출
  else:
    print("Hello가 존재하지 않습니다.") #"Hello"가 n리스트 안에 포함이 되어있지 않은 경우 송출

#tuple 튜플

t1 = tuple()
t2 = (1, 2, 3)#tuple()하고 같음
t3 = ('a', 'b', 'c')
t4 = (1, "hello", "there")

print(t2)
print(t3)
print(t4)

print(t2 + t3) #튜플끼리 이으기
print('a' in t3) # list와 마찬가지로 튜플 안에 a가 있는지 확인 True
print(t2.index(1)) # t2에서 1이 몇번째에 위치하는지 확인 * 맨 처음 있음으로. 0번째

#응용

if 'hello' in t2 or 1 in t2 and 1 in t4:
  #hello가 t2에 있거나 1이 t2 t4에 있어야 True
  print("해당 조건문은 True 입니다.")
else:
  print("해당 내용은 False 입니다.")

Tst1 = t2.index(3) # 0 1 2 값은 2 이다.

if Tst1 >= 2 :
  print("True")
else:
  print("False")

#Tuple 과 List 의 차이점 Tuple cannot Assignment (Can't Updating)
#Ex. list는 j[2] = 9 형식으로 j의 2번째 값을 9로 바꾸는 기능이 있으나 튜플은 존재하지 X
# mutable(가변) vs immutable(불변) 엘리먼트의 값을 바꿀 수 있느냐 없느냐.

#중간 정리
#List 와 Tuple은 거의 비슷하지만 List 는 mutable Tuple은 immutable인 것 같다.
#list() = [element], tuple() = ()
#list_Name[1] = 9 리스트 1번째 자리를 9라는 내용으로 새롭게 업데이트 시킬 수 있다. 튜플은 불가
#Ex. tp(1, 2, 3, 4), ls[1, 2, 3, 4]


#Dictionary 딕셔너리 dict() 와 {} 이용
#Dictionary 의 key 값은 가변형이 아닌 불가변형이 와야한다.

x = {
  'age':10,
  'name': "홍길동",
  'job':"백수",
}

print(x["age"]);
print(x["name"]);

#dictionary 또한 값을 바꿀 수 있다.
x["age"] = 23
print(x);

#새로운 값 추가
x["house"] = "서울"
print(x); 

#key랑 key의 값 송출 방법
# for key in x:
#   print("key:"+ str(key));
#   print("value:" + str(x[key]));


  