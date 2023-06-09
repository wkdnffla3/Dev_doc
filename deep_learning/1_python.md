1.hello python (5/31)
===============================

    1.1 파이썬??
        - 간단하고 배우기 쉬운 프로그래밍 언어
        - numpy, Scipy와 같은 데이터 처리 라이브러리가 존재
        - Caffe, TensorFlow, Chainer, Theano 같은 유명 딥러닝 프레임 워크들이 존재

***

1.2 파이썬 설치하기

        - 파이썬은 2가지 버전이 존재 2 버전 3버전
        - 3에서 짠코드는 2에서 실행이 되지 않음
        - 책에서는 3을 사용
        - 이책의 목표는 외부 라이브러리를 최소한으로 사용하고자 하지만 numpy, matplotlib 이 두가지는 예외로 한다.
        - 아나콘다를 사용해서 파이썬을 설치한다.

***

1.3 파이썬 인터프리터

        - 파이썬 인터프리터는 '대화 모드'하 하여 개발자와 파이썬이 대화하듯이 프로그래밍이 가능
        - 즉 질문하는데로 대답하는 형식
        
```python
>>1+2 #3
>>2+3 #5
```
        - 산술 연산은 다음과 같이 가능
```python
>>> 1-1 #-1
>>> 4*5 #20
>>> 7/5 #1.4
>>> 3**2 # 9
```
    - *은 곱셈, /는 나눗셈, **는 거듭제곱을 의미
    - 파이썬에서 정수를 나눈 결과는 실수가 된다!

1.3.2 자료형

    - 프로그래밍 언어에는 자요형이 존재
    - python은 type()함수로 자료형을 조회 가능

```python
>>> type(10) #<class 'int'>
>>> type(2.718) #<class 'float'>
>>> type("hello") #<class 'str'>
```

1.3.3 변수

    - x나 y등의 알파벳을 사용해 변수를 정의 가능하고 계산도 가능하다.

```python
>>> x=10
>>> print(x)
10
>>> x=100
>>> print(x)
100
>>> y=3.14
>>> x+y
314.0
>>> type(x*y)
<class 'float'>
```
    - 파이썬은 변수에 자료형을 자동으로 부여해주는 동적언어이다

1.3.4 리스트

    - 여러 데이터를 List로도 정리가 가능하다
    - 원소에 접근시 []를 사용한다
    - []를 인덱스 라 하며 0부터 시작한다
    - 파이썬에는 슬라이싱이라는 기법이 존재, 이를 이용하여 범위를 지정해 원하는 부분 리스트를 반환 가능
```python
>>> a=[1,2,3,4,5] #리스트 생성
>>> print(a) #리스트의 내용 출력
[1,2,3,4,5]
>>> len(a) #리스트의 길이 출력
5
>>> a[0] #첫번째 원소에 접근
1
>>> a[4] #다섯번째 원소에 접근
5
>>> a[4] = 99 #값 대입
>>> print(a)
[1,2,3,4,99]

>>> a[0:2] # 인덱스 0부터 2까지의 값을 반환
[1,2]
>>> a[1:] # 인덱스 1부터 끝까지 얻기
[2,3,4,99]
>>> a[:3] # 인덱스 처음부터 2까지 값 얻기
[1,2,3]
>>> a[:-1]# 처음부터 마지막-1 까지의 원소 값 얻기
[1,2,3,4]
>>>a[:-2] # 처음부터 마지막-2 까지의 원소 값 얻기
[1,2,3]
```

1.3.6 딕셔너리

    - 리스트는 인덱스 번호로 0,1,2,3.... 의 순서로 값을 가진다
    - 딕셔너리는 키(key)와 값(value)를 한쌍으로 가진다

```python
>>> me = {height : 180}
>>> me['height']
180
>>> me['weight'] = 70
>>> print(me)
{'weight' : 70, 'height' : 180}
```

1.3.6 bool

    - 파이썬에는 bool이라는 true, false 값을 가지는 데이터 형이 있다
    - and, or, not 연산자를 사용이 가능

```python
>>> hungry = true # 배가 고프다
>>> sleepy = false #졸립지 않다

>>> type(hungry)
<class 'bool'>

>>> not hungry
flase
>>> hungry and sleepy
flase
>>> hungry or sleepy
true
```

1.3.7 if문

    - 조건에 따라서 달리 처리하려면 if/else 를 사용한다
    - 아래와 같이 파이썬에서 공백(들여쓰기)은 매우 중요하다 
    - 들여쓰기는 코드를 묶어 단으로 쓸때 사용한다

```python
>>> hungry = true
>>> if hungry:
        print("i'm hungry")

i'm hungry
>>> hungry = false
>>> if hungry:
        print("I'm hungry")
    else:
        print("Im not hungry")
        print("im sleepy")

i'm not hungry
i'm sleepy
```

1.3.8 for 문

    - 반복 문인 for문이 존재
```python
>>> for i in[1,2,3]:
        print(i)

1
2
3
```
    - [1,2,3] 이라는 리스트 안의 원소를 하나씩 출력하는 예를 보여준다

1.3.9 함수

    - 특정 기능을 수행하는 일련의 명령들을 묶어 하나의 함수(function)으로 정의 할 수 있다

```python
>>> def hello():
        print("hello world")

>>> hello()
hello world!
```

    - 함수는 인수(매개변수)를 가질수 있다, + 연산자를 이용해서 문자열을 붙힐수도 있다

```python
>>> def hello(obj):
        print("heelo" + obj+ "!")
>>> hello("cat")
hello cat!
```
***
1.4 파이썬 스크립트 파일

    - 매번 코드를 입력하는 방법보다 저장해서 불러오는 방법이 더 간편하다!!

1.4.1 파일로 저장하기

    - 편집기를 열고 파이썬 파일을 작성

``` python 
#test.py
print("i'm hungry!")
```

    - 터미널에서 test.py를 실행하면 프로그램이 실행될 것이다!!


1.4.2 클래스

    - 개발자가 직접 클래스를 정의해서 독자적인 자료형을 만들 수 있다!
    - 클래스만의 전용 함수(메서드)를 만들 수 있다!

```python
    class 클래스이름:
        def __init__(self,인수,인수,....) 
        #생성자 기본적으로 한번 클래스를 생성하면 자동으로 1회 호출

        def 메서드 이름1(self,인수,인수,.....)
        def 메서드 이름2(self,인수,인수.....)
```

```python
    #simple class ex
    #self는 자기 자신을 뜻함!
    class Man:
        def __init__(self,name):
            self.name = name
            print('init')

        def hello(self):
            print("hello" + self.name+"!")

        def goodbye(self):
            print("bye"+self.name+"!")

    m = Man("david")

    m.hello()
    m.goodbye()

```

***

1.5 넘파이

    - 딥러닝 구현시 배열이나 행렬 계산을 도와주는 라이브러리

1.5.1 넘파이 가져오기

```python
>>> import numpy as np

#numpy를 가져오고 그것을 np라 부른다.

```

1.5.3 넘파이의 산술 연산

    - 산술 연산을 행할때는 배열의 크기가 서로 동일해야 에러가 나지 않는다
    - 배열이 아닌 스칼라값의 경우 연산이 가능하다 이 기능을 브로드 캐스트 라고 한다!

```python
>>> x = np.array([1.0,2.0,3.0])
>>> y = np.array([2.0,4.0,6.0])

>>> x+y #원소별 덧샘
array([3. , 6. , 9. ])
>>>x - y #원소별 뺄샘
array([-1. , -2. , -3. ])
>>>x*y  #원소별 곱샘
array([2. , 8. , 18. ])
>>> x/y #원소별 나눗샘
array([0.5 , 0.5 , 0.5 ])

>>> x = np.array([1.0, 2.0, 3.0])
>>> x / 2.0 #broad cast
array([0.5, 1. , 1.5])

```

1.5.4 넘파이의 N차원 배열
    
    - 넘파이는 1차원 배열 뿐만 아니라 다차원 배열도 사용이 가능하다!

```python
>>> A = np.array([[1,2],[3,4]])
>>> print(A)
[
    [1 2]
    [3 4]
]
>>> A.shape
(2,2)

>>> A.dtype
dtype('int64')

>>> B = np.array([[3,0],[0,6]])

>>> A+B

array([[4,2],[3,10]])

>>> A*B
array([[3,0],[0,24]])
```

1.5.5 브로드캐스트

    - 넘파이에서는 형상이 다른 배열끼리도 계산 자체는 가능 하다!
    - 브로드캐스트는 알아서 형태를 맞춰준다!

```python
>>> A = np.array([1,2],[3,4])
>>> B = np.array([10,20])

>>> A*B
array(  [10,40],
        [30,80]
    )
```

1.5.6 원소 접근

    - 원소의 인덱스는 np도 0부터 시작한다

```python
>>> X = np.array([[51,55],[14,19],[0,4]])
>>> print(x)
[[51 55]
[14 19]
[0 4]
]
>>> X[0]
array([51, 55])
>>> X[0][1]
55

#for 문으로도 각 원소에 접근이 가능하다

>>> for i in X:
        print(i)

        
[51 55]
[14 19]
[0 4]

#다차원 배열을 1차원 배열로 변환 가능
>>> X = X.flatten()
>>> print(x)
[51 55 14 19 0 4]

>>> X[np.array([0,2,4])]    #인덱스가 0,2,4인 원소 얻기
array([51, 14, 0])

#특정 조건을 만족하는 원소만 얻을수도 있다.
>>> X>15
array([true,true,False,true,False,False],dtype = bool) #처음 나온 값은 BOOL형 배열 이다.

>>> X[X>15]
aray([51,55,19])

```

***

1.6 matplotlib

    - matplotlib은 그래프를 그려주는 라이브러리다!
    - 데이터의 시각화가 쉬워진다!

1.6.1 단순한 그래프 그리기

    - 그래프를 그리려면 matplotlib의 pyplot 모듈을 이용합니다.

```python
import numpy as np
import matplotlib.pyplot as plt

#데이터 준비
x = np.arange(0,6,0.1) # 0에서 6까지가 0.1 간격으로 생성
y = np.sin(x)

#그래프 그리기
plt.plot(x,y)
plt.show()
```

1.6.2 pyplot의 기능

```python
import numpy as np
import matplotlib.pyplot as plt

#데이터 준비
x = np.arrange(0, 6, 0.1) #0에서 6까지 0.1 간격으로 생성!
y1 = np.sin(x)
y2 = np.cos(x)

#그래프 그리기
plt.plot(x, y1, label="sin")
plt.plot(x,y2, linestyle="--",label="cos") #cos 함수는 점선으로 설정

plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')

plt.legend()
plt.show()
```

1.6.3 이미지 표시하기

    - pyplot에는 이미지를 표시해주는 메서드인 imshow()가 존재
    - 이미지를 읽어들일 때는 matplotlib, image 모듈의 imread() 메서드를 사용

```python
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('cactus.png') # 이미지 읽어오기

plt.imsohw(img)
plt.show()
```