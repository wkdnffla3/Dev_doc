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