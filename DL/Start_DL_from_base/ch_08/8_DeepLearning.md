# 8.딥러닝

- 딥러닝은 층을 깁게한 심층 신경망이다.

## 8.1 더 깊게

- 신경망에선 그동안 많은 것들 배웠다.

- 이번 절에서는 그동안 배운 기술을 집약하고 심층 신경망을 만들어 MNIST 데이터 셋의 손글씨 숫자 인식에 도전한다.

### 8.1.1 더 깊은 신경망으로

- 그림 8-1 과 같이 구성된 CNN을 만들고자 한다.

- 이 신경망은 다음절에서 설명하는 VGG 신경망을 참고했다.

 ![(fig8-1)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%208-1.png)

 - 여기서 사용하는 합성곱 계층은 모두 3X3 계층의 필터이다.

 - 층이 깊어지면서 채널 수가 더 늘어난다.

 - 그림과 같이 풀링 계층을 추가하여 중간 데이터의 공간 크기를 줄여 가고 마지막으로 드롭아웃으로 정확도를 높힌다.

 - 가중치 초기값으로 He 초기값을 사용하고 매개변수 갱신에 Adam을 사용한다.

- 특징을 정리하면 다음과 같다

    - 3X3의 작은 필터를 사용한 합성곱 계층
    - 활성화 함수는 ReLu
    - 완전연결 꼐층 뒤에 드롭아웃 계층 사용
    - Adam 을 사용해 최적화
    - 가중치 쵝값은 He 초기값

- 이 신경망의 정확도는 99.38이 된다.

 ![(fig8-2)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%208-2.png)

 - 그림 8-2의사진들은 사람도 판단하기가 어려운 이미지이다.

 - CNN도 이런 이미지를 인식 오류를 일으킨다.

 ### 8.1.2 정확도를 높히려면

 - what is the class of this image? 웹사이트는 다양한 데이터셋을 대상으로 그동안 논문 등에서 발표한 기법들의 정확도 순위를 정리해 두었다.

  ![(fig8-3)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%208-3.png)


- 그림 8-3의 순쉬를 보면 neural network나 deep, convolutional이라는 키워드가 돋보인다.
- 이때 상위권은 대부분 CNN을 기초로 한 기법들이 점령했다.

- 그림 8-3의 상위 기법들을 참고하면 정확도를 더 높일 수 있는 기술이나 힌트를 발견 할 수있다.
- 예를 들어 앙상블 학습 학습률 감소, 데이터 확장 등이 정확도 향상에 공헌하고 있다.
- 데이터 확장은 손쉬운 방법이면서 정확도 개선에 효과적이다.

- 데이터 확장은 입력 이미지를 알고리즘을 동원해 인위적으로 확장한다.
 ![(fig8-4)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%208-4.png)

 - 그림 8-4 같은 변형 외에도 다양한 방법으로 이미지를 확장할수 있다.

 - 이미지 일부를 잘라내는 corp나 좌우를 뒤집는 flip등이 있겠다.

 ### 8.1.3 깊게 하는 이유

 - 층을 깊게 하는 것이 왜 중요한가에 대한 이론적인 근거는 아직 부족한것이 많다.

 - 층을 깊게하는 중요성에 대해서 설명을 한다.

 - 층을 깊게 하는 것의 중요성은 ILSVRC로 대표되는 대규모 이미지 인식 대회의 결과에서 파악할 수 있다.

 - 상위 성과를 낸 기법 대부분은 딥러닝 기반이며 그 경향은 신경망을 더 깊게 만드는 방향을 가고있다.

 ![(fig8-5)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%208-5.png) 

 - 그림 8-5는 5x5 필터로 구성된 합성곱 계층이다.

 ![(fig8-6)](../deep-learning-from-scratch-master/deep-learning-from-scratch-master/equations_and_figures/deep_learning_images/fig%208-6.png)

 - 그림 8-6은 3X3 필터로 구성된 합성곱 계층이다.

 - 3x3 두번 거친 크기와 5x5 한번 거친 크기와 같다.

 - 매개변수는 3x3 을 2번 한게 18개로 25개보다 적다.

 - 3회면 27개가 되지만 같은 크기의 영역 1회의 합성곱 연산으로 보려면 7x7로 49개가 필요하다.

 - 학습의 효율성도 층을 깊게 하는 것의 이점이다.

- 층을 깊게 함으로써 데이터의 양을 줄여 학습을 고속으로 할수 있다.

- 개를 인식한다 했을때 얕은 신경망에서 해결하려면 합성곱 계층은 개의 특징 대부분을 한번에 이해 해야한다.

- 따라서 학습하는데 시간이 오래 걸린다.
