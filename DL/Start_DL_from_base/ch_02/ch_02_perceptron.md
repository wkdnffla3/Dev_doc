이번 장에서는 퍼셉트론 알고리즘을 설명한다.

퍼셉트론이 신경망(딥러닝)의 기원이 되는 알고리즘이기 때문이다.


---
# 2.1 퍼셉트론이란?

- 퍼셉트론은 다수의 신호를 입력받아 하나로 출력한다.
- 여기서 신호란 전류나 강물처럼 흐름이 있는 것을 상상하면 좋다.

- 다만 실제 전류와는 다르게 흐른다 1 흐르지 안흔다 0이 된다.

![pic2-1](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%202-1.png)

- 위 그림은 입력이 2개인 퍼셉트론이다.
- x1과 x2는 입력신호, y는 출력신호, w1, w2는 가중치를 뜻한다.
- 그림의 원을 뉴런 혹은 노드 라고 부른다. 
- 입력 신호가 뉴런에 보내질 떄는 각각 고유한 가중치가 곱해진다.
- 뉴런에서 보내온 신호의 총합이 정해진 한계를 넘어설 때만 1을 출력한다.(이를 뉴런이 활성화 한다 라고도 표현한다.)
- 그 한계를 임계깞 이라고 하며 세타 라고 표기한다.
- 퍼셉트론의 동작 원리를 식으로 나타내면 다음과 같다.

![e2-1](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/e%202.1.png)