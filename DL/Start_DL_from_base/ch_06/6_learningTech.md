# 6. 학습 관련 기술들

- 신경망 학습의 핵심 개념을 알아본다
- 가중치 매개변수 최적값을 탐색하는 최적화 방법, 가중치 매개변수 초깃값, 하이퍼파라미터 설정방법 등
- 오버피팅 대응책인 가중치 감소와 드롭아웃 등의 정규화 방법도 설명 및 구현
- 배치 정규화도 알아본다.

## 6.1 매개변수 갱신

- 신경망 학습의 목적은 손실 함수의 값을 가능한 한 낮추는 매개변수를 찾는것.
- 매개변수의 최적값을 찾음 이 문제를 최적화 라고 한다.
- 매개변수 공간은 매우 넓기 때문에 찾기에 쉽지 않다.
- 지금까지 최적의 매개변수 값을 찾는 단서로 매개변수의 기울기를 이용했다.
- 기울기 값을 갱신해 가면서 최적의 값을 찾는 것을 확률적 경사 하강법 이란 방법이다.
- sgd 보다 똑똑한 방법도 있다.

### 6.1.1 모험가 이야기

- 지도를 보지않고 눈가리개를 쓴 모험가가 가장 깊은 골짜기를 찾는 방법
- 모험가는 땅의 기울기를 이용해서 깊은곳을 찾아야한다.
- 이것이 sgd의 전략이다.

### 6.1.2 확률적 경사 하강법(SGD)

- SGD의 수식은 다음과 같이 쓸수 있다.

![(e6-1)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/e%206.1.png)

- 여기서 W는 갱신할 가중치 매개변수고 그 옆의 분수는 W에 대한 손실 함수의 기울기 이다.
- 감마? 는 학습률을 의미 미리 0.01 이나 0.001로 값을 정해서 사용한다.
- SGD는 기울어진 방향으로 일정 거리만 가겠다는 단순한 방법이다.

```python
class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr

    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]


```

- 초기화떄 받는 인수인 lr 은 학습률을 뜻한다
- 이 학습률을 인스턴스 변수로 유지한다.
- 인수인 params 와 grads 는 딕셔너리 변수이다.

- SGD 클래스를 사용하면 신경망 매개변수의 진행을 다음과 같이 수행할 수 있다.
``` python
network = TwoLayerNet()

optimizer = SGD()

for i in range(10000):
    ...
    x_batch, t_batch = get_mini_batch()
    grads = network.gradient(x_batch, t_batch)
    params= network.params
    optimizer.update(params, grads)


```


- optimizer는 최적화를 행하는 자 라는 뜻의 단어이다. 여기서는 SGD가 그 역할을 한다.
- 매개변수 갱신은 optimizer 가 진행하니 optimizer에 매개변수와 기울기 정보만 넘겨주면 된다

- 이처럼 최적화를 담당하는 클래스를 분리해 구현하면 기능을 모듈화 하기 좋다.

### 6.1.3 SGD의 단점

 - SGD는 단순하고 구현도 쉽지만 문제에 따라서 비효율적일 때가 있다.

 ![(e6-2)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/e%206.2.png)

 - 위 식은 아래의 그림과 같다.

 ![(fig6-1)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%206-1.png)

 - 함수의 기울기를 보면 다음과 같이 된다.

  ![(fig6-2)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%206-2.png)

  -여기서 기울기 대부분은 (0,0)을 가르키지 않는다.

  - 그림 6-1 함수에 시작점이 (-7.0, 2.0) SGD를 적용하면 결과는 다음과 같이 나온다.
  
  ![(fig6-3)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%206-3.png)
