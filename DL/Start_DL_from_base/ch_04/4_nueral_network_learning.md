#   4 신경망 학습

    -  이번 장의 주제는 신경망 학습이다
    - '학습' 이란 훈련 데이터로부터 가중치 매개변수의 최적값을 자동으로 획득하는 것을 뜻한다.
    - 신경망이 학습할 수 있도록 해주는 지표인 손실 함수를 소개한다.
    - 손실함수를 가장 작게 만드는 가중치 매개변수를 찾는 것이 학습의 목표이다.
    - 손실함수를 작게 만드는 기법으로 함수의 기울기를 활용하는 경사법을 소개한다

## 4.1 데이터에서 학습한다.

    - 신경망의 특징은 데이터를 보고 가중치 매개변수를 학습 할수 있다.
    - 가중치 매개변수의 수는 매우 많기 때문에 수작업으로 하는것이 거의 불가능하다.

### 4.1.1 데이터 주도 학습

    - 기계학습의 중심에는 데이터가 존재한다.
    - 이로인해 사람 중심의 접근 방식에서 벗어날수 있다.
    - 사람은 경험을 바탕으로 패턴을 찾는것에 반해 기계는 수집한 데이터로 부터 패턴을 찾으려 한다.
    - 이미지에서 특징을 추출하고 그 특징의 패턴을 기계학습 기술로 학습하는 방법이 있다.
    - 여기서의 특징은 입력 데이터에서 본질적인 데이터(중요한 데이터)를 정확하게 추출할 수 있도록 설계된 변환기를 뜻한다.
    - 이미지의 특징은 보통 벡터로 많이 나타낸다.
    - 컴퓨터 비전 분야에서는 sift surf hog 등의 특징을 많이 사용한다.
    - 이런 이미지 데이터 벡터들을 가지고 대표적인 분류 기법인 svm, knn등으로 학습한다.
    - 데이터에서 규칙을 찾아내는 것은 기계가 하지만 이미지를 벡터로 바꿀때 사용하는 특징은 사람이 설계해야된다.
    - 이 내용들을 그림으로 정리하면 아래와 같다.

![그림 4-2](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%204-2.png)

    - 신경망은 이미지를 있는 그대로 학습한다.
    - 두번째 접근 방식(특징과 기계학습 방식)에서는 특징을 사람이 설계했지만 신경망(3번째)은 이미지에 표함된 중요한 특징까지도 기계가 학습한다.
    - 신경망의 이점은 모든 문제를 같은 맥락에서 풀 수 있다는 점이다.

### 4.1.2 훈련 데이터와 시험 데이터

    - 기계학습 문제는 데이터를 훈련 데이터와 시험 데이터로 나눠서 학습이 가능하다.
    - 훈련데이터만을 학습하고 그것을 가지고 시험데이터로 테스트한다.
    - 범용 능력을 기르기 위해 시험데이터를 분리하는 것이다.
    - 학습을 오래 하게 되면 데이터 셋에만 최적화된 오버피팅 상태가 일어난다.

## 4.2 손실함수

    - 신경망 에서는 현재의 상태를 하나의 지표로 표현해 그 지표를 가장 좋게 만드는 매개변수를 탐색한다.
    - 신경망 함수에서 사용하는 지표를 손실함수 loss function 이라고 한다.
    - 임의의 함수를 사용할수 있지만 오차제곱합과 교차 엔트로피 오차를 사용한다.

### 4.2.1 오차제곱합

    - 가장 많이 사용하는 손실함수는 오차제곱합 sum of squares for error 이다.
    - 정답레이블과 추정한 레이블의 차의 곱을 합으로 나타낸 것이다.
    - 한 원소만 1로하고 나머지 원소를 0으로 나타내는 표기법을 원핫 인코딩 이라고 한다,.

### 4.2.2 교차 엔트로피 오차

    - 다른 손실함수로써 교차 엔트로피 오차 cross entropy error도 있다.
    - 정답일때의 추정의 자연로그를 계산하는 식이다.
    - 정답일때 추정은 0에 가까워진다.

![그림 4-3](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%204-3.png)

### 4.2.3 미니배치 학습

    - 기계 학습은 여러 훈련 데이터를 이용해 학습하므로 이 여러 데이터의 손실함수의 값을 찾는다.
    - 손실함수의 값들의 평균으로 나타낼수 있다.
    - 하지만 거대한 데이터 셋 전체를 손실합수로 표현하는것은 비효율 적이다.
    - 따라서 데이터중 일부를 뽑아서 학습을 수행한다 이를 미니 배치 라고 한다.

### 4.2.4 배치용 교차 엔트로피 오차 구현하기

    - 조금 전에 구현한 교차 엔트로피 오차( 데이터를 하나씩 처리하는 구현)를 조금만 바꿔주면 된다.
    - 데이터가 하나인 경우와 데이터가 배치로 묶여 입력될 경우 모두를 처리할수 있도록 구현한다.

``` python
def cross_entropy_error(y,t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t*np.log(y+ 1e-7)) / batch_size


```

    - 이 코드에서 y는 신경망의 출력 t는 정답 레이블 입다.
    - y가 1차원 이라면 데이터 하나당 교차 엔트로피 오차를 구하는 경우는 reshape 함수로 데이터의 횽상을 바꿔 계산한다.

    -정답 레이블이 원 핫 인코딩이 아니라 2나 7등의 숫자 레이블로 주어졌을 떄의 교차 엔트로피 오차는 다음과 같이 구현할수 있다.

``` python
    def cross_entropy_error(y,t):
        if y.ndim == 1:
            t = t.reshape(1,t.size)
            y = y.reshape(1, y.size)

        batch_size = y.shape[0]

        return -np.sum(np.log(y[np.arane(batch_size),t]+1e-7))/batch_size
```

### 4.2.5 왜 손실함수를 설정하는가?

    - 왜 우리는 정확도라는 지표를 놔두고 손실 함수의 값 이라는 우회적인 방법을 택하는 이유가 뭘까
    - 손실 함수의 값을 가장 작게하는 매개변수의 값을 찾아야 하는데 매개변수의 미분값을 계산하고 그 값을 단서로 매개변수의 값을 서서히 변화 시킨다. 
    - 미분값이 0이면 매개변수의 변화가 없어진다.
    - 정확도를 지표로 삼게되면 매개변수의 미분값이 0으로 되버리는 양이 많아 정확한 탐색이 어렵기 때문이다.
    - 정확도는 매개변수의 조그만 변화에는 거의 변화를 보이지 않고 반응이있더라도 그 값이 불연속 적으로 갑자기 변한다.
    - 이는 계단 함수를 활성화 함수로 사용하지 않는 이유와도 똑같다.(계단 함수의 미분값은 대부분이 0이다.)

## 4.3 수치 미분

    - 경사법에서는 기울기 값을 기준으로 나아갈 방향을 정한다.

### 4.3.1 미분

    - 미분은 좌표 간에 기울기를 구하는 것이다 
    - 진짜 미분은 거의 점위치에서 기울기를 구하지만 프로그램에서는 오차가 발생한다.
    - 컴퓨터에서는 0과 가깝게 구현이 불가능 하기 때문..?
    - 따라서 x 축의 값 2개의 중심을 이용해서 중심 차분 혹은 중앙 차분을 구한다.

### 4.3.2 수치 미분의 예

    - 앞 절의 수치 미분을 사용하여 간단한 함수를 미분해 본다.

### 4.3.3 편미분

    - 변수가 여렷인 함수에 대한 미분을 편미분 이라고 한다.
    - 이 문제들을 변수가 하나인 문제로 만들고 그 변수를 미분한다.

## 4.4 기울기

    - 모든 변수에 대해 편미분 한것을 벡터로 정리한 것을 기울기 라고 한다.
    - 기울기가 가리키는 쪽은 각 장소에서 함수의 출력 값을 가장 크게 줄이는 방향이다.

### 4.4.1 경사법(경사 하강법)

    - 기계학습에서 최적의 매개변수란 손실 함수가 최솟값이 될때의 매개변수 값이다.
    - 최솟값을 찾으려고 하는것이 경사법이다.
    - 함수의 값을 낮추는 방법을 제시하는 지표가 기울기다.
    - 하지만 복잡한 함수에서는 기울기가 가리키는 방향에 최솟값이 없는 경우가 대부분이다.
    - 기울어진 방향이 꼭 최솟값을 가리키는것은 아니나 그방향으로 가야 함수의 값을 줄일수 있다.
    - 경사법은 현 위치에서 기울어진 방향으로 일정 거리만큼 이동하는 방법이다.
    - 일정 거리만큼 이동하는 크기를 학습률 이라고 한다

### 4.4.2 신경망에서의 기울기

    - 신경망 학습에서도 기울기를 구해야 한다.
    - 여기서의 기울기는 가중치 매개변수에 대한 손실 함수의 기울기 이다.
    - 파이썬의 람다 기법을 이용하면 더 편하다.

## 4.5 학습 알고리즘 구현하기

    - 전제 : 신경망에서는 적응 가능한 가중치와 편향이 있고 이 가중치와 편향을 훈련 데이터에 적응하도록 조정하는 과정을 학습 이라 합니다 신경망 학습은 다음과 같이 4단계로 수행한다.
    - 1단계 - 미니배치 : 훈련 데이터 중 일부를 무작위로 가져온다. 이렇게 선별한 데이터를 미니배치라 하며, 그 미니배치의 손실 함수 값을 줄이는 것이 목표이다.
    - 2단계 - 기울기 산출 : 미니배치의 손실 함수 값을 줄이기 위해 각 가중치 매개변수의 기울기를 구한다. 기울기는 손실 함수의 값을 가장 작게 하는 방향을 제시한다.
    - 3단계 - 매개변수 갱신 : 가중치 매개변수를 기울기 방향으로 아주 조금 갱신한다.
    - 4단계 -반복 : 1~3단계를 반복한다.

    - 이것은 경사 하강법으로 매개변수를 갱신하는 방법이며 이때 데이터를 미니배치로 무작위로 선정하기 때문에 확률적 경사 하강법 stochastic gradient desscent : SGD 라고 한다.

### 4.5.1 2층 신경망 클래스 구현하기

    - 처음에는 2층 신경망을 하나의 클래스로 구현하는 것부터 시작한다
    - 나머지는 코드의 설명 주석에 존재한다

### 4.5.2 미니배치 학습 구현하기

    - 신경망 학습 구현에는 앞에서 설명한 미니배치 학습을 활용한다.
    - 미니배치 학습이란 훈련 데이터 중 일부를 무작위로 꺼내고(미니배치), 그 미니배치에 대해서 경사법으로 매개변수를 갱산한다.

### 4.5.3 시험 데이터로 평가하기

    - 학습을 반복함으로써 손실 함수의 값이 서서히 내려가는 것을 확인했다.
    - 이때 손실 함수의 값이란 정확히는 훈련 데이터의 미니배치에 대한 손실 함수의 값이다.
    - 이때 훈련데이터의 손실 함수 값이 작아지는 것은 신경망이 잘 학습하고 있다는 증거이지만 이것만으로 다른 데이터셋에도 비슷한 성능을 발휘하는지 확실치 않다.
    - 따라서 시험 데이터로 평가를 해야한다.
    
asd


