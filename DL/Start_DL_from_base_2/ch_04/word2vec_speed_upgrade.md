# 4. word2vec 속도 개선

- 앞의 3장에서 word2vec의 구조를 배우고 cbow 모델을 구현했다.

- cbow 모델은 단순한 2층 신경망이라서 간단하게 구현이 가능했지만 말뭉치에 포함된 어휘 수가 많아 지면 계산량도 커진다는 문제가 있다.

- 그래서 이번장은 word2vec의 속도 개선을 목표로 한다.

- 첫번째 개선으로는 embedding 이라는 새로운 계층을 도입한다

- 두번째 개선으로는 네거티브 샘플링이라는 새로운 손실 함수를 도입한다.

## 4.1 word2vec 개선

- 앞장에서는 그림 4-1 과 같은 cbow 모델을 구현했다.

![그림 4-1](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%204-1.png)

- 그림 4-1 과 같이 앞장의 cbow 모델을 단어 2개를 맥락으로 사용해 이를 바탕으로 하나의 단어를 추측한다.

- CBOW 모델도 작은 말뭉치를 다룰때는 특별히 문제될 것은 없지만 거대한 말뭉치를 다루게 되면 몇가지 문제가 발생한다.

- 따라서 어휘가 100만개 은닉층의 뉴런이 100개인 CBOW 모델을 생각해본다면 그림 4-2처럼 된다.

![그림 4-2](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%204-2.png)

- 그림 4-2에서 보듯 입력층과 출력 층에는 각 100만개의 뉴런이 존재한다

- 이 뉴런들이 계산을 진행하면서 다음의 두계산으로 인해 병목이 발생한다.

    - 입력층의 원핫 표현과 가중치 행렬 W in 의 곱 계산
    - 은닉층과 가중치 행렬 W out 의 곲 및 Softmax 계층의 계산

- 천번쨰는 입력층의 원핫 표현과 관련한 문제이다.

- 원핫벡터로 단어를 표현하기에 어휘가 100만개라면 원핫 벡터도 100만개가되어 메모리를 많이 차지한다. 

- 이러한 원 핫 벡터와 가중치 행렬을 곱해야 하는데 이것 만으로도 상당한 계산력을 사용해서 이문제는 4.1절의 Embedding 계층을 도입하는 것으로 해결을 한다.

- 두번째 문제는 은닉층 이후 계산이다.

- 어휘가 많아짐에 따라 계산량이 증가하는데 이문제는 4.2 절에서 네거티브 샘플링이라는 새로운 손실 함수를 도입해 해결한다.

### 4.1.1 Embedding 계층

- 앞장에서는 단어를 원핫 표현으로 바꿧다 그리고 그것을 matmul 계층에 입력하고 matmul 계층에서 가중치 행렬을 곱했다 그럼 여기서 어휘 수가 100만 개인 경우를 상상 해보면 그림 4-3 과 같이 나온다.\


![그림 4-3](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%204-3.png)


- 그림 4-3에서는 행렬의 특정 행을 추출함으로써 필요없는 계산을 하지 않는다.

- 가중치 매개변수로부터 단어 id에 해당하는 행 을 추출하는 계층을 만들어 보고 이것을 embedding 계층이라고 하겠다.


- embedding 계층의 forward와 backward 처리는 다음 그림과 같다.

![그림 4-4](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%204-4.png)

- backward() 구현에는 문제가 하나 있다 idx의 원소가 중복될 때 발생

![그림 4-5](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%204-5.png)


## 4.2 word2vec 개선

- 남은 병목은 은닉층 처리 이후의 계산이다.

### 4.2.1 은닉층 이후 계산의 문제점

- 어휘가 100만개 은닉층 뉴런이 100개일때 CBOW 모델을 예로 생각해 본다

![그림 4-6](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%204-6.png)

- 계산 부하가 걸리는 곳은 은닉층의 뉴런과 가중치의 곱하는 부분과 softmax 계산이다.

- 첫번째는 거대한 행렬을 곱하는 문제이다 이 행렬곱을 가볍게 만들어야한다

- 두번째 softmax 계산도 가볍게 만들어야 한다.

### 4.2.2 다중분류에서 이진 분류로

- 네거티브 샘플링의 핵심 아이디어는 이진 분류에 있다 정확히는 다중 분류이다.

- 지금까지 우리는 다중 분류로만 문제를 다뤄왔다 하지만 이진 분류로 문제를 다룰수는 없을까?

- 정확히는 다중 분류 문제를 이진 분류로 근사할수는 없을까?

- 이진 분류로 하면 출력층에는 뉴런을 하나만 준비하면 된다

- 이것을 CBOW 모델에 적용시키면 그림 4-7과 같이 나온다.

![그림 4-7](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%204-7.png)

- 그림 4-8은 계산을 자세히 표현한 것이다

![그림 4-8](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%204-8.png)

### 4.2.3 시그모이드 함수와 교차 엔트로피 오차

- 이진 분류 문제를 신경망으로 풀려면 점수에 시그모이드 함수를 적용해 확률로 변환하고 손실을 구할 때는 손실 함수로 교차 엔트로피 오차를 사용한다.

- 시그모이드의 식은 식 4-2와 같다.

![식 4-2](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%204-2.png)

- 입력값은 0과 1 사이의 실수로 변환되며 이는 확률로 해석할수 있다.

- ![그림 4-9](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%204-9.png)

- 시그모이드 함수를 적용해 확률 y를 얻으면 이 확률 y 로 부터 손실을 구한다.

- 손실함수로 교차 엔트로피 오차 를 사용하고 식은 4-3과 같다.

![식 4-3](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%204-3.png)