# 2.perceptron (6/5)


    -퍼셉트론은 신경망(딥러닝) 의 기원이 되는 알고리즘이다!

##   2.1 퍼셉트론이란?

    - 퍼셉트론은 "  다수의 신호"를 입력으로 받아 하나의 신호를 출력한다!
    - 신호가 흐른다 1 안흐른다 0 의 값을 가질수 있다!

![perceptron](./img/perceptron.png)

- x<sub>1</sub>, x<sub>2</sub>은 입력신호 w<sub>1</sub>, w<sub>2</sub>은 가중치 y는 출력 신호를 뜻한다
- 위의 그림은 2개의 입력신호를 받는 퍼셉트론의 예시이다!
- 그림의 원을 뉴런 혹은 노드 라고 부른다
- 입력 신호가 뉴런에 보내질 때 고유한 가중치가 곱해진다.
- 뉴런에서는 받은 신호의 총합이 정해진 한계를 넘을때만 1을 출력
- 여기서의 한계를 임계값 Θ(theta)라고 표현

이 내용을  식으로 표현하면 다음과 같이 표현이 가능하다.

--식 2.1--
$$y= \begin{cases}0   (   w_{1}x_{1} +w_{2}x_{2} \leq \theta    ) \\1  (    w_{1}x_{1} +w_{2}x_{2}  >  \theta    ) \end{cases}  $$

***
## 2.2 단순한 논리회로
***
### 2.2.1 AND 게이트

    -AND 게이트는 입력이 2개이고 출력이 하나이다.
    -두 입력이 모두 참이면 출력도 참
    -그 외의 경우는 모두 거짓이다.

![AND_gate_tfTable](./img/equations_and_figures/deep_learning_images/fig%202-2.png)

-   AND 게이트를 퍼셉트론으로 표현을 하면 진리표 대로 작동하는 w<sub>1</sub>, w<sub>2</sub>, Θ를 정하면 된다!
-   조합의 수는 무수히 많지만 예를 들어 (w<sub>1</sub>, w<sub>2</sub>, Θ)= (1.1 , 1.1, 2) 같이 할수가 있다!

### 2.2.2 NAND 게이트와 OR 게이트

    - NAND 게이트는 not AND 게이트를 의미하며 그 동작은 AND 게이트의 정 반대이다.
    - 이것을 퍼셉트론으로 표현하는 순서쌍중 하나는 (w<sub>1</sub>, w<sub>2</sub>, Θ)= (-0.5, -0.5, -0.7)

![NOTAND_gate_TFTABLE](./img/equations_and_figures/deep_learning_images/fig%202-3.png)


    -OR 게이트는 입력 신호눈 하나 이상이 1이면 출력이 1이되는 논리회로 이다!
![OR_gate_TFTABLE](./img/equations_and_figures/deep_learning_images/fig%202-4.png)

    - 여기서 중요한 점은 3가지의 gate 모두 퍼셉트론의 구조가 똑같다는 것이다!
***
## 2.3 퍼셉트론 구현하기

***
### 2.3.1 간단한 구현부터
    - 논리 회로를 파이썬으로 구현

```python
    def AND(x1,x2):
        w1, w2, theta= 0.5, 0.5, 0.7
        tmp = x1*w1 + w2*x2
        if tmp <=theta:
            return 0
        elif    tmp > theta :
            return 1
```
    - 결과값은 AND 의 진리표와 같이 나온다.

### 2.3.2 가중치와 편향 도입

    - 식 2.1의 Θ를 -b로 치환하면 다음과 같은 식이 나온다.
--식 2.1--
$$y= \begin{cases}0   ( b+  w_{1}x_{1} +w_{2}x_{2} \leq 0    ) \\1  (b+    w_{1}x_{1} +w_{2}x_{2}  >  0   ) \end{cases}  $$

    - 식 2.2.와 2.1 은 표기만 다를뿐 같은 식이다!
    - 여기에서 b를 편향(bias) 이라 한다!