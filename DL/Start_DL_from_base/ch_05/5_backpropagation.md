#   오차 역 전파법

    앞장에서는 신경망 학습에 대해서 설명했다.
    그때 가중치 매개변수에 대한 손실 함수의 기울기를 수치 미분을 사용해 구했다.
    이번 장에서는 가중치 매개변수의 기울기는 효율적으로 계산하는 오차역전파법 을 배워본다.

    오차역 전파법을 제대로 이해하는 방법은 두가지가 있다
    하나는 수식을 통한것
    다른 하나는 계산 그래프를 이용한것
    다른 기계 학습을 다루는 책 대부분은 수식을 중심으로 이야기 한다.
    하지만 이책은 수식보다 계산 그래프를 이용해 설명한다.

    오차역 전파법을 계산 그래프로 설명하는 생각은 아드레 카패시의 블로그 또 그와 페이페이 리 교수가 진행한 스탠퍼드 대학교의 딥러닝 수업을 참고했다.


##  5.1 계산 그래프

    - 계산 그래프는 계산 과정을 그래프로 나타낸 것이다.
    - 복수의 노드와 엣지 로 표현된다.

### 5.1.1 계산 그래프로 풀다

    - 계산 그래프는 계산 과정을 노드와 화살표로 표현한다.
    - 노드는 원 으로 표기하고 원 안에 연산 내용을 적는다
    - 계산 결과를 화살표 위에 적어 각 노드의 계산 결과가 왼쪽에서 오른쪽으로 전해지게 한다.

![pic5-1](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%205-1.png)

    - 위의 그림에서는 갯수까지 같이 연산에 들어가 있지만 아래 그림처럼 따로 뺄수도 있다.
![pic5-2](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%205-2.png)

    - 문제 2: 현빈 군은 슈퍼에서 사과를 2개 귤을 3개 샀습니다 사과는 1개에 100원 귤은 1개에 150원 이다 소비세가 10%일 때 지불 금액을 구하시오.
    - 다른 문제 2도 그림처럼 표기할 수 있다.

![pic5-3](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%205-3.png)

    - 계산 그래프를 이용한 문제들은 다음 흐름으로 진행된다
    1. 계산 그래프를 구성한다.
    2. 그래프에서 계산을 왼쪽에서 오른쪽으로 진행한다.
    - 여기서 2번째 단계를 순전파 forwward propagation 이라고 한다.
    - 순전파의 반대 말은 역전파 이다.

### 5.1.2 국소적 계산

    - 계산 그래프의 특징은 국소적 계산을 전파함으로써 최종 결과를 얻는다는 점이다.
    - 그림 5-4에서 국소적의 특징을 알려준다.

![pic5-4](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%205-4.png)

    - 여기에서 계산 하나하나가 국소적 계산 이라고 할수 있다.
    - 계산 그래프는 국소적 계산에 집중한다.

### 5.1.3 왜 계산 그래프로 푸는가?

    - 계산 그래프의 이점은 국소적 계산이다. 
    - 중간 계산 결과를 모두 보관할수 있다.
    - 역전파를 통해 미분을 효율적으로 계산이 가능하다.
    - 그림 5-5처럼 계산 그래프 상에서 역전파가 가능

![pic5-5](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%205-5.png)

    - 이 전파는 국소적 미분을 전달하고 그 미분 값은 아래에 적힌다.
    - 사과 값이 1개 오르면 최종 값은 2.2배 오르는걸 뜻한다.

## 5.2 연쇄 법칙

    - 역전파는 국소적 미분을 순방향과는 반대인 오른쪽에서 왼쪽으로 전파한다.
    - 국소적 미분을 전달하는 원리는 연쇄법칙에 따른다.

### 5.2.1 계산 그래프의 역전파

![pic5-6](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%205-6.png)
     
     - 계산 그래프를 사용한 역전파는 위의 그림과 같다. 
     - 역전파의 계산 절차는 신호 E에 노드의 국소적 미분을 곱한 후 다음 노드로 전달하는 것이다.


### 5.2.2 연쇄 법칙이란?

    - 연쇄법칙을 설명하기 전에 합성 함수부터 이야기 해야된다.
    - 합성 함수는 여러 함수로 구성된 함수이다.
    - 연쇄법칙은 합성 함수의 미분에 대한 성질이며 다음과 같이 정의 될수 있다. "합성 함수의 미분은 합성 함수를 구성하는 각 함수의 미분의 곱으로 나타낼수 있다."


### 5.2.3 연쇄법칙과 계산 그래프

    - 연쇄 법칙 계산을 계산 그래프로 나타내면 다음과 같이 나타낼 수 있다.
![pic5-7](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%205-7.png)

