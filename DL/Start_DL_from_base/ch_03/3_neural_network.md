#   3.신경망

    - 퍼셉트론 으로는 복잡한 함수를 표현 가능하다!
    - 가중치 설정은 사람이 수동으로 해야한다.
    - 신경망은 사람이 수동으로 가중치를 설정하는 것을 처리해 준다.


***

##  3.1 퍼셉트론에서 신경망으로

    - 신경망은 앞 장에서 설명한 퍼셉트론과 공통점이 많다!
    - 여기서는 퍼셉트론과 다른 점을 중심으로 신경망의 구조를 설명한다.

### 3.1.1

    - 신경망을 그림으로 나타내면 다음과 같이 나타난다.


![neural_network](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%203-1.png)

    -   은닉층은 사람의 눈에 보이지 않기 때문에 은닉층이다.
    -   입력층에서 출력층 방향으로 0,1,2 층 이라고 한다.

### 3.1.2 퍼셉트론 복습

    - 앞에서 우리는 퍼셉트론에서 bias 부분을 배웠다. 

    - bias 부분의 퍼셉트론은 그림 3-3과 같다

!그림 3-3

    -위의 그림에서는 가중치가 b 이고 입력이 1인 뉴런이 추가되었다.
    - 이 퍼셉트론에서의 동작은 x x 1 이라는 3개의 신호가 뉴런에 입력되어 각 신호에 가중치를 곱한 후 다음 뉴런에 전달.
    - 이 퍼셉트론을 식으로 표현하면 식 3-2 식 3-3과 같다.

    - x 가 0보다 크면 1을 x가 0보다 작으면 0을 출력하는 함수가 나온다

### 3.1.3 활성화 함수의 등장

    - 위에서 함수 h 처럼 입력 신호의 총합을 출력하는 함수를 활성화 함수(activation function)이라고 한다.
    - 활성화 함수는 신호의 총합이 활성화를 일으키는지를 정하는 역할을 한다.
    - 식3.2를 다시 써보면 가중치가 곱해진 입력 신호의 총합을 계산하고 그 합을 활성화 함수에 입력해 결과를 내는 2단계로 처리된다.
    - 따라서 식은 식 3.4 식3.5로 나눌수 있다.
    - 이를 그림 3-4로 나타낼수 있다.
!그림 3-4

    그림 3-4에서는 기존 뉴런의 원을 키우고 그 안에 활성화 함수의 처리 과정을 명시적으로 그렸다.
    - 즉 가중치 신호를 조합한 결과가 a 노드가 되고 활성화 함수 h()를 통하여 y라는 노드로 변환 되는 과정이 나타나 있다.
    - 뉴런을 그릴 때 하나의 원을 뉴런으로 나타낸다.


***

##  3.2 활성화 함수

    - 식3.3과 같은 활성화 함수는 임계값을 경계로 출력이 바뀌는데 이를 계단함수 라고 한다.
    - 퍼셉트론에서 계단함수 말고 다른 함수를 활성화 함수로 변경이 가능하다

### 3.2.1 시그모이드 함수

    - 식 3.6을 시그모이드 함수 라고 한다.
    - 신경 망에서는 활성화 함수로 시그모이드 함수를 이용하여 신호를 변환하고 그 변환된 신호를 다음 뉴런에 전달한다.

### 3.2.2 계단 함수 구현하기

    -  이번 절에서는 파이썬으로 계단 함수를 그려본다.
    - 

```python
    def step_function(x):
        if x>0:
            return 1
        else:
            return 0
```
    -  이 구현은 쉽지만 매개변수 x는 실수 하나 밖에 넣지 못한다.
    -  따라서 우리는 넘파이 배열도 넣어서 바꿀수가 있다!
```python
    def step_function(x):
        y =x>0
        return y.astype(np.int)
```   
    
```python
import numpy as np
x = np.array([-1.0, 1.0, 2.0])
x       #array([-1. , 1., 2.])
y=x>0
y       #array([false, true, true],dtype = bool)

```
    - 넘파이 배열에 부등호 연산을 수행하면 배열의 원소 각각에 부등호 연산을 수행한 bool 배열이 생성된다.
    - 이 예에서는 x의 원소가 각각0 보다 크면 true로 작으면 false 로 리턴하는 배열이 생성된다.
    - 우리가 원하는건 0 이나 1을 출력하는 int 형 리스트 이기 때문에 y의 원소를 bool에서 int 형으로 바꾼다

```python
y = y.astype(np.int)
y       #array([0, 1, 1])
```
    - 이처럼 넘파이 배열의 자료형을 변환할 때는 astype() 메서드를 이용한다.

### 3.2.3 계단 함수의 그래프

    - 앞에서 정의한 계단 함수를 그래프로 그려보면 다음과 같다.

```python
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype = np.int)

x= np.arange(-5.0, 5.0, 0.1)
y= step_function(x)

plt.plot(x,y)
plt.ylim(-0.1, 1.1) #y축 출력 범위 지정
plt.show()
```

    - 0을 경계로 출력 값이 변한다!


### 3.2.4 시그모이드 함수 구현하기

    - 식 3.6의 시그모이드 함수는 파이썬으로 다음과 같이 구현이 가능하다

```python
    def sigmoid(x):
        return 1/(1+np.exp(-x))
```

    - 실제로 잘 동작하는지 시험해본다

```python
x=np.array([-1.0,1.0, 2.0])
sigmoid(x) #array([0.26894142, 0.73105858, 0.88079708])


```
    - 넘파이의 브로드 캐스팅 연산으로 연산이 가능하다!


### 3.2.5 시그모이드 함수와 계단 함수 비교

    - 시그모이드 함수와 계단 함수를 비교하면 직선과 곡선 차이
    - 계단은 0 또는 1이지만 시그모이드는 연속된 실수로 표현이 된다.
    - 큰 시야로 보면 두 함수는 비슷하다.


### 3.2.6 비선형 함수

    - 계단함수와 시그모이드함수 둘다 비선형 함수이다. 
    - 신경망에서 활성화 함수로는 비선형 함수를 사용해야한다.
    - 선형 함수를 사용하면 신경망의 층을 깊게 하는 의미가 없기 때문이다.
    - 선형 함수를 사용하게 되면 결과적으로 1차원 함수로 귀결되기 때문에 사용을 하면 의미가 없게된다.

### 3.2.7 Relu 함수

    - relu 함수는 입력이 0을 넘으면 그 입력을 그대로 출력하고 0 이하이면 0을 출력하는 함수이다.
    - 식으로는 3.7로 쓸수 있다.
![pic3-7](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/e%203.7.png)
```python

    def relu(x):
        return np.maximum(0,x)
```

## 3.3 다차원 배열의 계산

    - 넘파이의 다차원 배열을 사용한 계산법을 숙달하면 신경망을 효율적으로 구현이 가능하다.

### 3.3.1 다차원 배열

    - 다차원 배열도 그 기본은 '숫자의 집합이다'
    - 이러한 숫자의 배열을 N차원으로 나눈 것이 다차원 배열이다.
    - 배열의 차원의 수는 np.ndim()으로 확인이 가능하다
    - 배열의 형상은 인스턴스 변수인 shape로 확인이 가능하다!
    - 2차원 배열은 가로를 행 세로를 열 이라고 한다.

### 3.3.2 행렬의 곱

    - 2x2의 행렬의 곲은 그림 3-11 처럼 계산한다
![pic3-11](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%203-11.png)

    - 행렬 곱에는 np.dot()로 계산한다
    - np.dot()은 입력이 1차원 배열이면 백터를 2차원 배열이면 행렬 곱을 계산한다
    - 백터도 행렬곱 성질을 따른다!(선형 대수학)
    - 행렬 AB 와 BA는 값이 다를수 있다!
    - 행렬간 곲은 그 형태가 같아야 한다 

### 3.3.3 신경망에서의 행렬곱

    - 넘파이 행렬을 써서 신경망을 구현이 가능하다
    - 그림 3-14의 간단한 신경망을 예로 든다
![pic3-14](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%203-14.png)
    - 이 신경망은 편향과 활성화 함수를생략하고 가중치만 같는다.
    - 2    2X3      =       3 의 형태로 곱셈이 가능하다!

## 3.4 3층 신경망 구현하기
![pic3-15](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%203-15.png)
    - 그림 3-15 의 3층 신경망에서 수행되는 입력부터 출력까지의 처리를 구현한다.
    - 앞서 설명한 넘파이를 이용한다.
    - 넘파이를 이용하면 아주 적은 코드만으로 신경망의 순방향 처리가 가능ㅎ다.

### 3.4.1 표기법 설명
![pic3-16](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%203-16.png)
    - 이번 절에서는 신경망에서의 처리를 설명하며 w와a 같은 표기법을 선보인다.
    - 그림 3-16을 보면 입력층의 뉴런 x와 가중치 w가 보인다.
    - 오른쪽 위의 숫자는 몇층인지를 나타낸다
    - 오른쪽 아래의 숫자는 뉴런의 인덱스 번호이다
    
### 3.4.2 각층의 신호 전달 구현하기

    - 그림 3-17을 보면 그다음층으로 입력층의 값들이 각각의 가중치에 곱해서 전달이 된다.
    - 이를 다차원 배열을 사용해서 표현 할수 있으며 식 3.8 - 3.9로 표현이 된다.
    - 나중에 사진을 첨부해 추가 설명을 적는다.


![pic3-17](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%203-17.png)
![pic3-18](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%203-18.png)
![pic3-19](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%203-19.png)
![pic3-20](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%203-20.png)

## 3.5 출력층 설계하기

    - 신경망은 분류와 회귀 모두에 사용이 가능하다
    - 분류는 데이터가 어느 클래스에 속한지
    - 회귀는 연속적인 데이터의 수치를 나타낸다.
    - 일반적으로 회귀에는 항등 함수를 분류에는 소프트 맥스 함수를 사용한다.

### 3.5.1 항등 함수와 소프트 맥스 함수 구현하기

    - 항등 함수는 입력을 그대로 출력한다 입력과 출력이 항상 같다는 뜻의 항등이다.
    - 분류에 사용되는 소프트 맥스 함수의 식은 식3-10이 된다.
![식3.10](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/e%203.10.png)

    - 이 소프트 맥스 함수를 그림으로 나타내면 그림 [3-22] 처럼 된다.

![pic3-22](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%203-22.png)

### 3.5.2 소프트 맥스 함수 구현시 주의점

    - 구현한 함수는 지수를 사용하기 때문에 오버 플로우의 위험이 있다.
    - 이 문제를 해결할 수식으로 식 3.11 이 있다.

![식 3.11](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/e%203.11.png)

### 3.5.3 소프트 맥스 함수의 특징
    - 소프트 맥스 함수의 특징은 0과 1.0 사이의 실수이며 출력의 총합은 1이다.
    - 소프트 맥스 함수로 가장 큰 결과의 위치는 변하지 않는다.
    - 따라서 출력층으 소프트 맥스 함수를 계산하지 않아도 된다.

### 3.5.4 출력층의 뉴런 수 정하기

    - 출력층의 뉴런 수는 분류에서는 분류하고자 하는 클래스의 수로 정하는 것이 일반적이다.

## 3.6 손글씨 인식

    - 이번 절에서는 손글씨 인식을 할 것이다.
    - 미리 설정해둔 파라메터 값을 이용하여 학습과정은 생략하고 추론 과정만 구현할 것이다.

### 3.6.1 MNIST 데이터 셋

    - mnist 데이터 셋은 손글씨 데이터로 유명하다.

### 3.6.2 신경망의 추론 처리

    - 사용하는 신경망은 입력층 뉴런 784개 출력층 뉴런을 10개로 구성한다.
    - 입력 이미지의 크기가 28 * 28 이기 때문에 784 10가지로 구분을 해서 출력이 10개이다.
    - 사진의 픽셀값 인 0~ 255를 0~1 까지의 실수로 바꾸는 것을 정규화 신경망에 입력 데이터에 특정 변환을 하는 것을 전처리 라고 한다.

### 3.6.3 배치 처리

    - 이미지 여러장을 한꺼번에 넣는것
    - 데이터를 적절하게 넣어서 학습을 진행 시킬수 있다!
    - 배치의 크기가 크면 작은것들을 돌리는것보다 더 빠르게 학습이 가능하지만 메모리의 한계가 존재 한다.