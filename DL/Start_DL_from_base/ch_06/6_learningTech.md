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

 - 위 그림은 심하게 굽이진 움직임을 보여준다 , 비효율적
 - 즉 sgd의 단점은 비등방성 함수 에서는 탐색 경로가 비효율적 이라는 것이다.
 - 따라서 이러한 SGD의 단점을 개선해주는 모멘텀, ADAGRAD, ADAM 이라는 세 방법을 소개할 것이다.

 ### 6.1.4 모멘텀

 - 모멘텀은 운동량이란 뜻으로 수식으로 다음과 같다.

![(e6-3)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/e%206.3.png)

![(e6-4)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/e%206.4.png)

- SGD 처럼 여기에서도 W는 갱신할 가중치 매개변수, 분수는 W에 대한 손실함수의 기울기, 나머지는 학습률이다.
- V는 물리에서 말하는 벡터 즉 속도에 해당한다.

- 식 6-3은 기울기 방향으로 힘을 받아 물체가 가속된다는 물리 법칙을 나타낸다.
- 모멘텀은 그림 6-4와 같이 공이 그릇의 바닥을 구르는 듯한 움직임을 보여준다.

![(fig6-4)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%206-4.png)

- 식 6-3의 av 항은 물체가 아무런 힘을 받지 않을 때 서서히 하강시키는 역할을 한다 a는 0.9등의 값으로 설정한다.
- 소스코드는 common/optimizer.py에 있다.


``` python
class Momentum:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr=lr
        self.momentum = momentum
        self.v = None

    def update(self,params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key]=np.zeros_lisk(val)

            for key in params.keys():
                self.vp[key] = self.momentum*self.v[key] - self.lr*grads[key]
                params[key] += self.v[key]


```

- 변수 v가 물체의 속도이다 초기화때는 아무 값도 담지 않다가 update 구문이 시작되면 처음 호출될 때 매개변수와 같은 구조의 데이터를 딕셔너리 변수로 저장

- 모멘텀은 사용하여 식 6-2의 최적화 문제를 풀어보면 다음과 같은 그림이 나온다.

  ![(fig6-5)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%206-5.png)

- 공이 바닥을 구르는것 처럼 나온다.

### 6.1.5 AdaGrad

- 신경망 학습에서는 학습룰 (수식에서는 감마? 파이?)값이 중요하다 값이 너무 작으면 학습 시간이 길어지고 크면 발산하여 학습이 제대로 이루어 지지 않는다.

- 이 학습률을 정하는 효과적 기술로 학습률 감소가 있다.
- 학습을 진행하면서 학습률을 줄여가는 방법이고 실제로도 자주 쓰인다.

- 학습률을 서서히 낮추는 가장 간단한 방법은 매개변수 '전체'의 학습률 값을 일괄적으로 낮추는 것이다.

- 이를 더욱 발전 시킨것이 AdaGrad 이다.
- AdaGrad는 각각의 매개변수에 맞춤형 값을 만들어 낸다.

- 식으로는 다음과 같다.

![(e6-5)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/e%206.5.png)


![(e6-6)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/e%206.6.png)

- 같은 변수는 위에서 설명한 봐와 같으나 h 라는 새로운 변수가 등장한다.
- h는 기존 기울기 값을 제곱하여 계속 더해준다 그리고 매개변수를 갱신할때 루트를 씌운것을 나눠 학습률을 조정한다.
- 매개변수의 원소 중에서 많이 움직인(크게 갱신된) 원소는 학습률이 낮아진다는 뜻이다.

- AdaGrad의 구현을 살펴본다. 소스 코드는 common/optimizer.py에 있다.

```python
class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h={}
        for key, val in params.items():
            self.h[key] = np.zeros_like(val)

        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)

```
- 여기에서 주의할 것은 마지막 줄에서 1e-7이라는 아주 작은 값을 더하는 부분이다.

- 이 작은 값은 self.h[key]에 0이 있다 해도 0으로 나누는 사태를 방지한다.

- 식 6-2의 최적화 문제를 풀면 그림 6-6과 같이 나온다.

 
  ![(fig6-6)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%206-6.png)


- 그림 6-6을 보면 최솟값을 향해 효율적으로 움직이는 것을 알 수 있다.

### 6.1.6 Adam

- 모멘텀은 공이 그릇 바닥을 구르는 듯한 움직임을 보였다.

- AdaGrad는 매개변수의 원소 마다 적응적으로 갱신 정도를 조정했다.         

- 이 두 기법을 조합한 것이 Adam 이다.

- 두 방법의 이점을 조합했다면 매개변수 공간을 효율적으로 탐색해줄것으로 기대

- 하이퍼 파라미터의 편향 보정이 이 진행

- 결과는 그림 6-7과 같다.

  ![(fig6-7)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%206-7.png)



 ### 6.1.7 어느 갱신 방법을 이용할 것인가?

  ![(fig6-8)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%206-8.png)

  - 4개의 방법이다.

  - 기법에 따라 생신 경로가 다르다. 문제에 따라 푸는 방법이 달라져야 하므로 주의해야한다.

  - 많은 연구에서 SGD를 사용하고있지만 다른 방법도 많이 있다.

  ### 6.1.8 MNIST 데이터셋으로 본 갱신 방법 비교

 - 손글씨 숫자 인식을 대상을 ㅗ지금껏 설명한 네 기법을 비교해보자

   ![(fig6-9)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%206-9.png)

 - 이 실험은 각 층이 100개의 뉴런으로 구성된 5층 신경망에서 ReLU를 활성화 함수로 사용해 측정.


 ## 6.2 가중치의 초기값

 - 신경망 학습에서 중요한 것이 가중치의 초기값이다.

 - 이번 절에서는 권장 초깃값에 대해서 설명하고 실험을 통해 실제로 신경망 학습이 이뤄지는지를 확인한다.

 ### 6.2.1 초기값을 0으로 하면?

 - 오버피팅을 억제해 범용 성능을 높이는 테크닉인 가중치 감소 기법을 소개하려 한다.

 - 가중치 감소는 가중치 매개변수의 값이 작아지도록 학습하는 방법이다.

 - 가중치 값을 작게 하여 오버 피팅이 일어나지 않는다.

 - 가중치를 작게 만들고 싶으면 초기값도 최대한 작은 값에서 시작하는것이 정공법이다.

 - 하지만 0 으로 설정하면 안된다. 학습이 올바르게 이루어지지않는다.

 - 정확히는 가중치를 균일한 값으로 설정 해서는 안된다.

 - 그 이유는 오차 역 전파법에서 모든 가중치의 값이 똑같이 갱신되기 떄문이다.

 - 그럼 순전파때 입력층의 가중치가 0이기 떄문에 두번째 층의 뉴런에서 모두 같은 값이 전달 된다.

 - 따라서 모든 층에 가중치가 똑같아 진다.

 ### 6.2.2 은닉층의 활성화값 분포

 - 은닉층의 활성화 값의 분포를 관찰하면 중요한 정보를 얻을 수 있다.

 - 이번 절에서는 가중치의 초깃값에 따라 은닉층 활성화 값들이 어떻게 변하는지 간단한 실험을 한다.

 - 활성화 함수로 시그모이드 함수를 사용하는 5층 신경망에 무작위로 생성한 입력 데이터를 흘리며 각 층의 활성화 값 분포를 히스토 그램으로 그려 보겠다.

 - 이 실험을 위한 소스 코드는 ch06/weight_init_activation_histogram.py 에 있으니 참고 하면 된다.

```python
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):

    return 1 / (1+ np.ecp(-x))

x = np.rando.randn(1000,100)    # 1000개의 데이터
node_num = 100                  # 각 은닉층의 노드(뉴런 수)
hidden_layer_size = 5           # 은닉층이 5개

activations = {}                # 이곳에 활성화 결과를 저장

for i in range(hiddent_layer_size):

    if i !=0 :
        x = activations[i-1]

    w=np.random.randn(node_num, node_num)*1

    a = np.dot(x,w)
    z = sigmoid(a)
    activations[i] = z

```
- 층이 5개가 있으며 각 층의 뉴런은 100개씩이다. 입력 데이터로써 1000개의 데이터를 정규분포롤 무작위로 생성하여 이 5층 신경망에 흘리고 확성화 함수는 시그모이드를 각 층의 활성화 결과를 activations 변수에 저장한다.


- 가중치의 분포에 주의를 해야한다 표준 편차가 1인 정규 분포를 이용했는데 이 분포된 정도를 바꿔가며 활성화 값들의 분포가 어떻게 변환하는지 관찰하는 것이 이 실험의 목적이다.

``` python
for i, a in activations.items():
    plt.subplot(1,len(activations), i+1)
    plt.title(str(i+1) + "-layer")
    plt.hist(a.flatten(), 30 , range=(0,1))
plt.show()
```

- 이를 실행하면 그림 6-10 의 히스토 그램을 얻을수 있다.

  ![(fig6-10)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%206-10.png)

- 각 층의 활성화 값들이 0과 1에 치우쳐 분포가 되어있다.

- 따라서 역전파의 기울기 값이 점점 작아지다가 사라지게 된다 이것은 기울기 소실 문제이다.

- 가중치의 표준편차를 0.01로 바꿔 같은 실험을 반복해보자

```python
# w = np.random.randn(node_num , node_num) * 1
w = np.random.randn(node_num , node_num) * 0.01
```

- 결과를 보면 그림 6-11과 같이 나온다.

  ![(fig6-11)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%206-11.png)

- 이번엔 0.5 부근에 집중 되어있다. 기울기 소실 문제는 발생하지 않지만 활성화 값들이 치우쳤다는 것은 표현력 관점에서 문제가 있는 것이다.

- 그래서 활성화 값들이 치우치면 표현력을 제한한다는 관점에서 문제가 된다.
