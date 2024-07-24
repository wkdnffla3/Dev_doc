#  5. 순환 신경망(RNN)

- 지금까지 살펴본 신경망은 피드 포워드 라는 유형의 신경망이다.
- 피드 포워드란 흐름이 단방향인 신경망이다.
- 피드 포워드 신경망은 구성이 단순하여 구조를 이해하기 쉬워 많은 문제에 응용이 가능하다.
- 하지만 시계열 데이터를 잘 학습할수 없다.

- 그래서 순환 신경망이 등장하게 된다.
- 이번 장에서는 피드포워드 신경망의 문제점을 지적하고 RNN이 그 문제를 해결할수 있음을 설명한다.

## 5.1 확률과 언어 모델

- RNN 설명을 위한 준비과정으로 앞장의 word2vec를 복습
- 자연어에 관한 현상을 확률을 사용해 기술
- 언어를 확률로 다루는 언어 모델에 대해 설명한다.

### 5.1.1 word2vec을 확률 관점에서 바라보다

- w1, w2, w3 .... wr라는 단어열로 표현되는 말뭉치를 생각해본다
- 그 전후 단어 t-1 와 t+1을 맥락으로 취급한다.

![그림 5-1](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%205-1.png)

- CBOW 모델은 식 5.1의 사후 확률을 모델링 한다.

- 지금까지는 좌우 대칭으로 맥락을 생각했지만 그림 5-2와 같은 경우도 있다.

![그림 5-2](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%205-2.png)

-  위 그림은 왼쪽 단어 두개만을 맥락으로 생각한다 그러면 CBOW 모델이 출력할 확률은 식 5-2처럼 된다.

![그림 5-2](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%205-2.png)