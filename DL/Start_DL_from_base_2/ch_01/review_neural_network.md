# 1. 신경망 복습
- 이 책은 밑시딥의 속편으로 딥러닝의 가능성을 한층 더 깊게 탐험할 것이다.
- 이번 장에서는 신경망을 복습할 것이다.
- 효율을 높히고자 전편에서의 구현 규칙을 일부 변경하겠다

## 1.1 수학과 파이썬 복습

- 수학적 지식으로는 벡터 나 행렬 등을 알아야한다.
- 신경망을 원활하게 구현하기  위한 파이썬 코드 특히 넘파이를 사용한 코드도 리뷰한다.


### 1.1.1 벡터와 행렬

- 신경망에서는 벡터와 행렬 또는 텐서가 도처에서 등장한다.
- 벡터는 크기와 방향을 가진 양이다.
- 벡터는 숫자가 일렬로 늘어선 집합으로 표현할 수 있고 파이썬에서는 1차원 배열로 취급이 가능하다.
- 행렬은 숫자가 2차원 형태로 늘어선 것이다.

![그림 1-1](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-1.png)
- 이것은 행렬이다.

![그림 1-2](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-2.png)
- 이건 벡터다.

- 수학과 딥러닝등 많은 분야에서 열벡터 방식을 선호하지만 여기서 구현 편의를 위해 행벡터로 다루겟다.

- 수식에서의 벡터나 행렬은 X와 W 처럼 굵게 표기하여 단일 원소로 이루어진 스칼라 값과 구별한다.

- 코드에서 보듯이 벡터와 행렬은 np.array() 메서드로 생성할수 있다. 

- 이 메서드는 넘파이의 다차원 배열 클래스인 np.ndarray 클래스를 생성한다.

- np.ndarray 클래스에는 다양한 편의 메서드와 인스턴스 변수가 준비되어 있다.

- 위 코드에서는 shape 와 ndim을 이용했다.

### 1.1.2 행렬의 원소별 연산

- 이번에는 표현한 벡터와 행렬을 사용해 간단한 계산을 할것이다.


### 1.1.3 브로드 캐스트

- 넘파이의 다차원 배열에서는 형상이 다른 배열 끼리도 연산이 가능하다.

- 10이 앞의 크기에 맞춰 증식 하는것이 브로드 캐스트 이다.

![그림 1-3](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-3.png)


- 브로드 캐스트의 또 다른 예는 다음과 같다.

![그림 1-4](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-4.png)


### 1.1.4 벡터의 내적과 행렬의 곱

- 벡터의 내 수식은 다음과 같다.

![식 1-1](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%201-1.png)

- 여기서 2개의 벡터 x와 y가 있다고 가정한다. 그리고 식 1.1에서 보듯 벡터의 내적은 두 벡터에서 대응하는 원소들의 곱을 모두 더한것이다.

- 행렬의 곱은 다음과 같다.

![그림 1-5](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-5.png)

- 벡터의 내적과 행렬의 곱을 파이썬으로 구현하면 다음과 같은 코드가 나온다.
- 넘파이의 np.dot() 과 np.matmul() 메서드를 이용하면 쉽게 구현이 된다.